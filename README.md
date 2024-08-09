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
August 2024

Product Sales:   $83,200.00
Service Sales:   $21,000.00
-------------------------------
Total Sales:   $104,200.00

Cost of Good Sold:   $62,400.00
Marketing:  $5,000.00
Staff Salaries:  $20,840.00
-------------------------------
Total Operating Expenses:  $88,240.00

Net Income:  $15,960.00
=================================

September 2024

Product Sales:   $86,528.00
Service Sales:   $22,050.00
-------------------------------
Total Sales:   $108,578.00

Cost of Good Sold:   $64,896.00
Marketing:  $5,000.00
Staff Salaries:  $21,715.60
-------------------------------
Total Operating Expenses:  $91,611.60

Net Income:  $16,966.40
=================================

October 2024

Product Sales:   $89,989.12
Service Sales:   $23,152.50
-------------------------------
Total Sales:   $113,141.62

Cost of Good Sold:   $67,491.84
Marketing:  $5,000.00
Staff Salaries:  $22,628.32
-------------------------------
Total Operating Expenses:  $95,120.16

Net Income:  $18,021.46
=================================

November 2024

Product Sales:   $93,588.68
Service Sales:   $24,310.12
-------------------------------
Total Sales:   $117,898.80

Cost of Good Sold:   $70,191.51
Marketing:  $5,000.00
Staff Salaries:  $23,579.76
-------------------------------
Total Operating Expenses:  $98,771.27

Net Income:  $19,127.53
=================================

December 2024

Product Sales:   $97,332.23
Service Sales:   $25,525.63
-------------------------------
Total Sales:   $122,857.86

Cost of Good Sold:   $72,999.17
Marketing:  $5,000.00
Staff Salaries:  $24,571.57
-------------------------------
Total Operating Expenses:  $102,570.74

Net Income:  $20,287.12
=================================

January 2025

Product Sales:   $101,225.52
Service Sales:   $26,801.91
-------------------------------
Total Sales:   $128,027.43

Cost of Good Sold:   $75,919.14
Marketing:  $5,000.00
Staff Salaries:  $25,605.49
-------------------------------
Total Operating Expenses:  $106,524.63

Net Income:  $21,502.80
=================================

February 2025

Product Sales:   $105,274.54
Service Sales:   $28,142.01
-------------------------------
Total Sales:   $133,416.55

Cost of Good Sold:   $78,955.90
Marketing:  $10,000.00
Staff Salaries:  $26,683.31
-------------------------------
Total Operating Expenses:  $115,639.21

Net Income:  $17,777.33
=================================

March 2025

Product Sales:   $109,485.52
Service Sales:   $29,549.11
-------------------------------
Total Sales:   $139,034.63

Cost of Good Sold:   $82,114.14
Marketing:  $10,000.00
Staff Salaries:  $27,806.93
-------------------------------
Total Operating Expenses:  $119,921.07

Net Income:  $19,113.56
=================================

April 2025

Product Sales:   $113,864.94
Service Sales:   $31,026.56
-------------------------------
Total Sales:   $144,891.50

Cost of Good Sold:   $85,398.71
Marketing:  $10,000.00
Staff Salaries:  $28,978.30
-------------------------------
Total Operating Expenses:  $124,377.01

Net Income:  $20,514.49
=================================

May 2025

Product Sales:   $118,419.54
Service Sales:   $32,577.89
-------------------------------
Total Sales:   $150,997.43

Cost of Good Sold:   $88,814.65
Marketing:  $10,000.00
Staff Salaries:  $30,199.49
-------------------------------
Total Operating Expenses:  $129,014.14

Net Income:  $21,983.29
=================================

June 2025

Product Sales:   $123,156.32
Service Sales:   $34,206.79
-------------------------------
Total Sales:   $157,363.11

Cost of Good Sold:   $92,367.24
Marketing:  $10,000.00
Staff Salaries:  $31,472.62
-------------------------------
Total Operating Expenses:  $133,839.86

Net Income:  $23,523.25
=================================

July 2025

Product Sales:   $128,082.58
Service Sales:   $35,917.13
-------------------------------
Total Sales:   $163,999.71

Cost of Good Sold:   $96,061.93
Marketing:  $10,000.00
Staff Salaries:  $32,799.94
-------------------------------
Total Operating Expenses:  $138,861.88

Net Income:  $25,137.83
=================================
```

