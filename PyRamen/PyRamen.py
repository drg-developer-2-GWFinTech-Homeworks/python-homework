# -*- coding: UTF-8 -*-
"""
PyRamen

Name: David Gayman <davidrgayman@gmail.com>

Description: This script analyzes sales data for the PyRamen company.
"""


# Import libraries
import csv
from pathlib import Path
import os 


# Get script directory
script_filepath = os.path.dirname(os.path.realpath(__file__))


# Set file paths for menu_data.csv and sales_data.csv
menu_filepath = os.path.join(script_filepath, Path("Resources/menu_data.csv"))
sales_filepath = os.path.join(script_filepath, Path("Resources/sales_data.csv"))
report_filepath = os.path.join(script_filepath, Path("PyRamenReport.txt"))


# Initialize list objects to hold our menu and sales data
menu = []
sales = []


# Read in the menu data into the menu list
with open(menu_filepath, "r") as menu_file:

    
    # Open menu file with a CSV reader and ingest the header row
    menu_file_reader = csv.reader(menu_file, delimiter=",")
    menu_file_header = next(menu_file_reader)
    
    
    # Read each row and ingest into a list
    for row in menu_file_reader:
        menu.append(row)


# Read in the sales data into the sales list
with open(sales_filepath, "r") as sales_file:
    
    
    # Open sales file with a CSV reader and ingest the header row
    sales_file_reader = csv.reader(sales_file, delimiter=",")
    sales_file_header = next(sales_file_reader)
    
    
    # Read each row and ingest into a list
    for row in sales_file_reader:
        sales.append(row)


# Initialize dict object to hold our key-value pairs of items and metrics
report = {}


# Initialize a row counter variable
row_count = 0


# Loop over every row in the sales list object
for sales_row in sales:
    
    
    # Extract sales data variables from row
    #line_item_id,date,Credit_Card_Number,Quantity,Menu_Item
    quantity = int(sales_row[3])
    sales_item = sales_row[4]
    
    
    # If the item value not in the report, add it as a new entry with initialized metrics
    if sales_item not in report:
        report[sales_item] = {
            "01-count": 0,
            "02-revenue": 0,
            "03-cogs": 0,
            "04-profit": 0
        }
        
        
    # For every row in our sales data, loop over the menu records to determine a match
    profit = 0
    for menu_row in menu:
        
        
        # Extract variables from row
        # Item,Category,Description,Price,Cost
        # Initialize menu data variables
        menu_item = menu_row[0]
        category = menu_row[1]
        description = menu_row[2]
        price = float(menu_row[3])
        cost = float(menu_row[4])
        
        
        # Calculate profit of each item in the menu data
        profit = price - cost
        
        
        # If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if menu_item == sales_item:
            
            
            # Print out matching menu data
            #print(f"Menu data:  Item={menu_item}  Category={category}  Description={description}  Price=${price}  Cost=${cost}")
            
            # Cumulatively add up the metrics for each item key
            report[sales_item]["01-count"] += quantity
            report[sales_item]["02-revenue"] += price * quantity
            report[sales_item]["03-cogs"] += cost * quantity
            report[sales_item]["04-profit"] += profit * quantity
            
            
        #else:
            
            
            # Else, the sales item does not equal any of the items in the menu data, therefore no match
            #print(f"{sales_item} does not equal {menu_item}! NO MATCH!")



    # Increment the row counter by 1
    row_count += 1


# Print total number of records in sales data
print(f"Total number of sales records: {row_count}")


# Write out report to a text file
report_file = open(report_filepath, "w")
report_file.write(str(report))
report_file.close()
