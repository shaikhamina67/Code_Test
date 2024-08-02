#1. Write a Python program to read a CSV file and display its contents.

import csv

def read_csv(file_path):
    try:
        # Open the CSV file for reading with UTF-8 encoding
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            # Create a CSV reader object to read
            csv_reader = csv.reader(file)
            # Iterate over each row in the CSV file
            for row in csv_reader:
                # Print each row
                print(row)
    except FileNotFoundError:
        # handle exceptions
        print(f"The file at path {file_path} was not found.")
    except Exception as e:
        # exception handling
        print(f"An error occurred: {e}")

# Specify the path to the CSV file
file_path ='C:/Users/shaik/Downloads/test_file - Sheet1.csv'  
# Call the function
read_csv(file_path)

"""
Output:
['Product', 'Region', 'Sales Amount', 'Date']
['Product A', 'North', '1200', '2024-01-01']
['Product B', 'South', '1500', '2024-01-02']
['Product C', 'East', '800', '2024-01-03']
['Product D', 'West', '700', '2024-01-04']
['Product A', 'North', '1100', '2024-01-05']
['Product B', 'South', '1400', '2024-01-06']
['Product C', 'East', '900', '2024-01-07']
['Product D', 'West', '850', '2024-01-08']
['Product A', 'North', '1300', '2024-01-09']
['Product B', 'South', '1600', '2024-01-10']"""
