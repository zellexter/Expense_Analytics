# EXPENSES PROJECT
# Goal: create in depth visualization for expenses data
#       include:
#           monthly data
#           expenditure by category (yearly and monthly)
#           high low categories by month
# Skills to practice:
#       xlsx file read in
#       data extraction on xlsx files
#       pandas df manipulation
#       creating and importing modules
#       visualization with charts (by calling external functions created previously)
#           line chart for monthly totals, by month category totals
#           pie chart for monthly category expenditure
# Data Format:
#       WHERE: EXPENSES_CHROMA.xlsx is kept within Expenses_Data Folder in CodingWDad\Expense Analytics
#       FILE AND DATA: EXPENSES_CHROMA.xlsx contains worksheets with each month's data
#       DATA DESCRIPTION: Within each worksheet, data is stored starting from row20 (header inclusive)
#                         across columns A:C where:
#                                               A: Expenditure (name)
#                                               B: Category (data validation rules)
#                                               C: Amount (in dollars)
#       NOTE*** first work on expense based data in described columns. don't worry about subscriptions/monthly expenses yet.

# BREAKDOWN:

### READ IN FILE
### IMPORT DATA FROM WS TO DF
# for ws in wb:
#   store data into df using min/max row/col
### CLEAN DATA USING PANDAS
# create a module to clean data using pandas (this would be a seperate .py file)
### FORMAT DATA FOR CHARTS
# find what data format is needed for each type of chart
# create functions for each type of chart that will format df data
### DRAW/SAVE CHARTS
### EXPORT NEW FILE WITH VISUALIZATIONS

# NOTE*** LATER IMPROVEMENTS
# currently the plan is to store data from file into pandas df (to practice pandas).
#   future improvement may be to read and extract data directly from file into clean/format functions
# BANK STATEMENTS---
#   pass in pdfs of bank statements and read expense data from there
#   need to learn:
#       converting pdf into txt files or something readable
#       finding right data within the txt files and assigning correct dollar amounts to the expense name
#       categorize expenses by name and send unknown expenses to manual input box, and then learn from there
#   workbook:
#       ws1: yearly overview
#       ws2+: monthly expense data with visualizations on same ws

# MODULES
import pandas as pd
import os

class Expense_Visualization():

    def __init__(self, import_file, export_file) -> None:
        '''Initializes import and export file, sets original workbook to None'''
        self.import_file = import_file
        self.export_file = export_file
        self.wb = None 

    def main():
        '''Main function:
            Reads in file
            Imports data from worksheet to dataframe
            Cleans data using DataCleaner Module
            Format data for charts
            Draw and save chart in new file
            Export new file with visualizations'''
        
        
        
    def file_import(self, data_type='all'):
        '''
        Imports all worksheets to dataframes.
        Dataframes stored in dictionary {worksheet:dataframe}.
        data_type parameter defaulted to import all data in worksheet(s),
        however can import only 'fixed' and only 'expense' data as well.
        '''
        # TODO do not import template ws
        # TODO fix fixed expenses, set amount of rows
        # DONE simplify!!! no need for all the if statements, can store type:parameters in a dictionary
        #   initialize dict for import_parameters
        #   initialize variable parameters to get() parameters by data_type
        #   return read_excel function with parameters unpacked

        import_parameters = {
            'all': {},
            'fixed': {
                'header': None,
                'names': ['Fixed Expense','Type','Amount'],
                'usecols': 'A:C',
                'skiprows': 5,
                'skipfooter': 18
            },
            'expenses': {
                'header': None,
                'names': ['Expenditure','Category','Amount'],
                'usecols': 'A:C',
                'skiprows': 20
            }
        }

        parameters = import_parameters.get(data_type, {})

        return pd.read_excel(io=self.import_file, sheet_name=None, **parameters)
    
        # if data_type == 'all':
        #     all_df = pd.read_excel(io=self.import_file,
        #                         sheet_name=None,
        #                         )
        #     return all_df
        
        # if data_type == 'fixed':
        #     fixed_df = pd.read_excel(io=self.import_file,
        #                         sheet_name=None,
        #                         header=None,
        #                         names=['Fixed Expense','Type','Amount'],
        #                         usecols='A:C',
        #                         skiprows=5,
        #                         skipfooter=18, # ERROR HERE
        #                         )
        #     return fixed_df
        
        # if data_type == 'expense':
        #     expense_df = pd.read_excel(io=self.import_file,
        #                         sheet_name=None,
        #                         header=None,
        #                         names=['Expenditure','Category','Amount'],
        #                         usecols='A:C',
        #                         skiprows=20,
        #                         )
        #     return expense_df

        



# if Expense_Visuatlization is run on original py file, use specified filepath and save_file
if __name__ == '__main__':
    filepath = os.path.join('C:','Users','miche','OneDrive','Documents','CodingwDad','Expense Analytics','Expenses_Data','EXPENSES_CHROMA.xlsx')
    save_file = os.path.join('Expense Analytics', 'Expense_Summary.xlsx')
    Expense_Visualization(filepath, save_file).main()

