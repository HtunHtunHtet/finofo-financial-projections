from File import File
from Projections import Projections

file = File('financial_projections.xlsx', 'Sheet1')
file.read_file()

projections = Projections(file)
formatted_projections = projections.get_projections()

print(formatted_projections)