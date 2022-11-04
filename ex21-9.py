import csv

def get_col_sum(filename, col):
    try:
        with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            running_sum = sum((int(row[col]) for row in csv_reader))
            csv_file.close()
            print(f'Sum = {str(running_sum)}')
    except:
        pass