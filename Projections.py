import File
import pandas as pd
from typing import List, Dict
from datetime import timedelta


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
                'date': date.strftime('%B %Y'),
                'sales': f'{current_sales:,.2f}'
            })

        return projections

    def generate_product_sales_projections(self) -> List[Dict[str, str]]:
        initial_product_sales = self._file.get_product_sales_value()
        return self.generate_sales_projections(initial_product_sales, 0.04)

    def generate_service_sales_projections(self) -> List[Dict[str, str]]:
        initial_service_sales = self._file.get_service_sales_value()
        return self.generate_sales_projections(initial_service_sales, 0.05)

    def get_marketing_value(self, month: int) -> float:
        base_marketing_value = self._file.get_marketing_value()
        if month > 6:
            return base_marketing_value * 2
        return base_marketing_value

    def generate_combined_projections(self) -> pd.DataFrame:
        product_sales_projections = self.generate_product_sales_projections()
        service_sales_projections = self.generate_service_sales_projections()

        combined_projections = []
        for month, (product, service) in enumerate(zip(product_sales_projections, service_sales_projections), start=1):
            total_sales = float(product['sales'].replace(',', '')) + float(service['sales'].replace(',', ''))
            cost_of_goods_sold = float(product['sales'].replace(',', '')) * 0.75
            staff_salaries = total_sales * 0.20
            marketing = self.get_marketing_value(month)
            total_operation_expense = cost_of_goods_sold + marketing + staff_salaries

            combined_projections.append({
                'Date': product['date'],
                'Product Sales': product['sales'],
                'Service Sales': service['sales'],
                'Total Sales': f'{total_sales:,.2f}',
                'Cost of Good Sold': f'{cost_of_goods_sold:,.2f}',
                'Marketing': f'{marketing:,.2f}',
                'Staff Salaries': f'{staff_salaries:,.2f}',
                'Total Operating Expenses': f'{total_operation_expense:,.2f}',
                'Net Income': f'{total_sales - total_operation_expense:,.2f}',
            })

        return pd.DataFrame(combined_projections)

    @staticmethod
    def format_projections(df: pd.DataFrame) -> str:
        formatted_output = ""
        for _, row in df.iterrows():
            formatted_output += f"\n{row['Date']}\n\n"
            formatted_output += f"Product Sales:   ${row['Product Sales']}\n"
            formatted_output += f"Service Sales:   ${row['Service Sales']}\n"
            formatted_output += "-------------------------------\n"
            formatted_output += f"Total Sales:   ${row['Service Sales']}\n"

            formatted_output += "\n"
            formatted_output += f"Cost of Good Sold:   ${row['Cost of Good Sold']}\n"
            formatted_output += f"Marketing:  ${row['Marketing']}\n"
            formatted_output += f"Staff Salaries:  ${row['Staff Salaries']}\n"
            formatted_output += "-------------------------------\n"
            formatted_output += f"Total Operating Expenses:  ${row['Total Operating Expenses']}\n"

            formatted_output += "\n"
            formatted_output += f"Net Income:  ${row['Net Income']}\n"
            formatted_output += "=================================\n"

        return formatted_output

    def get_projections(self) -> str:
        df = self.generate_combined_projections()
        df = df.reset_index(drop=True)
        return self.format_projections(df)
