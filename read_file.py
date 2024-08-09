from File import File
from Projections import Projections

file = File('financial_projections.xlsx', 'Sheet1')
file.read_file()

projections = Projections(file)

combined_projections = projections.generate_combined_projections()

for projection in combined_projections:
    print(projection)
