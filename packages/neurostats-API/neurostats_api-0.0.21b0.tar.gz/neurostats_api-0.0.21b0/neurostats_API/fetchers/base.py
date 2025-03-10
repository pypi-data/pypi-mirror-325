import abc
from typing import Union
from pymongo import MongoClient
import pandas as pd
import json
import pytz
from datetime import datetime, timedelta, date
from ..utils import StatsDateTime, StatsProcessor, YoY_Calculator
import yaml


class StatsFetcher:

    def __init__(self, ticker, db_client):
        self.ticker = ticker
        self.db = db_client["company"]    # Replace with your database name
        self.collection = self.db["twse_stats"]

        self.timezone = pytz.timezone("Asia/Taipei")

        self.target_metric_dict = {
            'value': ['value'],
            'value_and_percentage': ['value', 'percentage'],
            'percentage': ['percentage'],
            'grand_total': ['grand_total'],
            'grand_total_values': ['grand_total', 'grand_total_percentage'],
            'grand_total_percentage': ['grand_total_percentage'],
            'growth': [f'YoY_{i}' for i in [1, 3, 5, 10]],
            'grand_total_growth': [f"YoY_{i}" for i in [1, 3, 5, 10]]
        }

    def prepare_query(self):
        return [
            {
                "$match": {
                    "ticker": self.ticker,
                }
            },
        ]

    def collect_data(self, start_date, end_date):
        pipeline = self.prepare_query()

        fetched_data = list(self.collection.aggregate(pipeline))

        return fetched_data[0]

    def str_to_datetime(self, date_str):
        year, month, day = [int(num) for num in date_str.split("-")]

        date = datetime.strptime(date_str, "%Y-%m-%d")
        date = self.timezone.localize(date)

        season = (month - 1) // 3 + 1

        return StatsDateTime(date, year, month, day, season)

    def has_required_columns(self, df: pd.DataFrame, required_cols=None):
        """
        Check if the required columns are present in the DataFrame.

        Args:
            df (pd.DataFrame): The DataFrame to check.
            required_cols (list, optional): List of required column names. 
                                            Defaults to ['date', 'open', 'high', 'low', 'close', 'volume'].

        Returns:
            bool: True if all required columns are present, False otherwise.
        """
        if required_cols is None:
            required_cols = ['date', 'open', 'high', 'low', 'close', 'volume']

        return all(col in df.columns for col in required_cols)


class BaseTEJFetcher(abc.ABC):

    @abc.abstractmethod
    def get(self):
        pass

    def get_latest_data_time(self, ticker):
        latest_data = self.collection.find_one(
            {
                "ticker": ticker
            }, 
            {
                "last_update": 1,
                "_id": 0
            }
        )

        try:
            latest_date = latest_data['last_update']["latest_data_date"]
        except Exception as e:
            latest_date = None

        return latest_date

    def process_value(self, value):
        if isinstance(value, str) and "%" in value:
            value = value.replace("%", "")
        try:
            return float(value)
        except (ValueError, TypeError):
            return None

    def calculate_growth(self, this_value, last_value, delta):
        try:
            return YoY_Calculator.cal_growth(this_value, last_value, delta) * 100
        except Exception:
            return None

    def cal_YoY(self, data_dict: dict, start_year: int, end_year: int, season: int):
        year_shifts = [1, 3, 5, 10]
        return_dict = {}
        
        for year in range(start_year, end_year + 1):
            year_data = data_dict.get(f"{year}Q{season}", {}).copy()
            if not year_data:
                continue
            
            for key in list(year_data.keys()):
                if key == "season":
                    continue
                
                this_value = self.process_value(year_data[key])
                if this_value is None:
                    year_data.pop(key)
                    continue
                
                temp_dict = {"value": year_data[key]}
                for shift in year_shifts:
                    past_year = year - shift
                    last_value = data_dict.get(f"{past_year}Q{season}", {}).get(key)
                    last_value = self.process_value(last_value)
                    growth = self.calculate_growth(this_value, last_value, shift) if last_value is not None else None

                    temp_dict[f"YoY_{shift}"] = (f"{growth:.2f}%" if growth else None)
                year_data[key] = temp_dict
            
            return_dict[f"{year}Q{season}"] = year_data
        
        return return_dict

    def cal_QoQ(self, data_dict):
        return_dict = {}
        
        for time_index, this_data in data_dict.items():
            year, season = map(int, time_index.split("Q"))
            last_year, last_season = (year - 1, 4) if season == 1 else (year, season - 1)
            
            for key in list(this_data.keys()):
                if key == "season":
                    continue
                
                this_value = self.process_value(this_data[key])
                if this_value is None:
                    this_data.pop(key)
                    continue
                
                temp_dict = {"value": this_data[key]}
                last_value = data_dict.get(f"{last_year}Q{last_season}", {}).get(key, {}).get('value')
                last_value = self.process_value(last_value)
                growth = self.calculate_growth(this_value, last_value, 1) if last_value is not None else None
                temp_dict['growth'] = (f"{growth:.2f}%" if growth else None)
                
                this_data[key] = temp_dict
            
            return_dict[time_index] = this_data
        
        return return_dict

    def get_dict_of_df(self, data_dict):
        """
        dict[dict] -> dict[df]
        """
        for key in data_dict.keys():
            data_dict[key] = pd.DataFrame.from_dict(data_dict[key])
        return data_dict

    def set_time_shift(self, date: Union[str, datetime], period: str):
        if isinstance(date, str):
            date = datetime.strptime(date, "%Y-%m-%d")

        period_mapping = {
            "1d": timedelta(days=1),
            "7d": timedelta(days=7),
            "1m": timedelta(days=30),
            "3m": timedelta(days=90),
            "1y": timedelta(days=365),
            "3y": timedelta(days=365 * 3),
            "5y": timedelta(days=365 * 5),
            "10y": timedelta(days=365 * 10),
        }

        if period == "all":
            return datetime.strptime("1991-01-01", "%Y-%m-%d")

        return date - period_mapping.get(period, timedelta(days=0))  # 預設為不變"
