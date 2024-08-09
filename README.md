# Finofo Take Home Assignment

## Installation and Setup

- Python Version - 3.12.*
- Clone this repository
- Create a virtual environment: `python3 -m venv venv`
- Activate the virtual environment: macOS: `source venv/bin/activate` / Windows: `.\venv\Scripts\activate`
- Install Dependencies: `pip install -r requirements.txt`
- Run the application: `python3 app.py`

## Constraints

1. This PR already includes the `financial_projections.xlsx` file.
2. The file has two sheets, `Sheet1` and `Sheet2`.
3. `Sheet1` contains data that is pre-populated from the start.
4. `Sheet2` only includes historical data, which is July 2024.
5. The reason for `Sheet2` is to prove that if we change the sheet when we read the file, it will calculate accordingly.
6. The format should be the same as the original file provided by the interviewer (i.e., `financial_projections.xlsx`).

## Analysis

After careful analysis, the following are the relationships between the data in the `financial_projections.xlsx` file:

1. `Product Sales` increase by 4% every month in the first year.
2. `Service Sales` will increase by 5% every month in the first year.
3. `Total Sales` is the sum of `Product Sales` and `Service Sales`.
4. `Cost of Goods Sold` is 75% of `Product Sales`.
5. `Marketing` remains the same for the first 6 months and then doubles in the next 6 months.
6. `Staff Salaries` are 20% of `Total Sales`.
7. `Total Operating Expenses` is the sum of `Cost of Goods Sold`, `Marketing`, and `Staff Salaries`.
8. `Net Income` is the difference between `Total Sales` and `Total Operating Expenses`.

## Approach

1. Adding all the code together in the same file will make it difficult to maintain and read.
2. For that reason, I have decided to split the code into two classes: `File` and `Projections`.
3. The `File` class will be responsible for reading the file based on the file name and sheet name.
4. After the file is read, the file object is passed into the `Projections` class, which will do the calculations and return one year of formatted projection data.

## Sample Output

```
July 2024

Product Sales:   $83,200.00
Service Sales:   $21,000.00
-------------------------------
Total Sales:   $21,000.00

Cost of Good Sold:   $62,400.00
Marketing:  $5,000.00
Staff Salaries:  $20,840.00
-------------------------------
Total Operating Expenses:  $88,240.00

Net Income:  $15,960.00
=================================

August 2024

Product Sales:   $86,528.00
Service Sales:   $22,050.00
-------------------------------
Total Sales:   $22,050.00

Cost of Good Sold:   $64,896.00
Marketing:  $5,000.00
Staff Salaries:  $21,715.60
-------------------------------
Total Operating Expenses:  $91,611.60

Net Income:  $16,966.40
=================================

September 2024

Product Sales:   $89,989.12
Service Sales:   $23,152.50
-------------------------------
Total Sales:   $23,152.50

Cost of Good Sold:   $67,491.84
Marketing:  $5,000.00
Staff Salaries:  $22,628.32
-------------------------------
Total Operating Expenses:  $95,120.16

Net Income:  $18,021.46
=================================
```

