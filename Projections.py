import File
import pandas as pd
from typing import List, Dict
from datetime import  timedelta


class Projections:
    def __init__(self, file: File) -> None:
        self._file: File = file

    def generate_sales_projections(self, initial_sales: float, growth_rate: float) -> List[Dict[str, str]]:
        historical_date = self._file.historical_date()
        start_date = pd.to_datetime(historical_date)

        projections = []
        current_sales = initial_sales

        for i in range(1, 13):
            date = start_date + timedelta(days=30 * i)
            current_sales *= (1 + growth_rate)
            projections.append({
                'date': date.strftime('%Y-%m-%d %H:%M:%S'),
                'sales': f'{current_sales:.2f}'
            })

        return projections

    def generate_product_sales_projections(self) -> List[Dict[str, str]]:
        initial_product_sales = self._file.get_product_sales_value()
        return self.generate_sales_projections(initial_product_sales, 0.04)

    def generate_service_sales_projections(self) -> List[Dict[str, str]]:
        initial_service_sales = self._file.get_service_sales_value()
        return self.generate_sales_projections(initial_service_sales, 0.05)

    def generate_combined_projections(self) -> pd.DataFrame:
        product_sales_projections = self.generate_product_sales_projections()
        service_sales_projections = self.generate_service_sales_projections()

        combined_projections = []
        for product, service in zip(product_sales_projections, service_sales_projections):
            total_sales = float(product['sales']) + float(service['sales'])
            combined_projections.append({
                'Date': product['date'],
                'Product Sales': product['sales'],
                'Service Sales': service['sales'],
                'Total Sales': f'{total_sales:.2f}',
                'Cost of Good Sold': f'{total_sales * 0.3:.2f}'
            })

        return pd.DataFrame(combined_projections)

    def get_projections(self) -> pd.DataFrame:
        return self.generate_combined_projections()
