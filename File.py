import os
import pandas as pd
from typing import Optional


class File:
    def __init__(self, file_name: str, sheet: str) -> None:
        self._file_name: str = file_name
        self._sheet: str = sheet
        self.data: Optional[pd.DataFrame] = None

    def read_file(self) -> None:
        # This read_excel setting is only compatable with `Financial Projections (Assignment).xlsx`
        self.data = pd.read_excel(self._file_name, sheet_name=self._sheet, usecols='A,B', index_col=0, skiprows=1)
        self.data.fillna('', inplace=True)
        # print(self.data)

    def get_product_sales_value(self) -> float:
        return self.data.at['Product Sales', 'Historical']

    def get_service_sales_value(self) -> float:
        return self.data.at['Service Sales', 'Historical']

    def get_total_sales_value(self) -> float:
        return self.data.at['Total Sales', 'Historical']

    def get_cost_of_goods_sold_value(self) -> float:
        return self.data.at['Cost of Goods Sold', 'Historical']

    def get_marketing_value(self) -> float:
        return self.data.at['Marketing', 'Historical']

    def get_staff_salaries_value(self) -> float:
        return self.data.at['Staff Salaries', 'Historical']

    def get_total_operating_expenses(self) -> float:
        return self.data.at['Total Operating Expenses', 'Historical']

    def get_net_income(self) -> float:
        return self.data.at['Net Income', 'Historical']

    def historical_date(self) -> str:
        return self.data.loc[self.data.index.isna(), 'Historical'].values[0]
