# charts needed:
#   bar chart: [x_axis, values]
#       summary of annual monthly total exp
#       monthly dining to groceries exp
#   pie chart: [pie slice, value]
#   line chart: [month, category, cateogry, category...]

from openpyxl import Workbook
from openpyxl.chart import (
    LineChart,
    Reference,
)
import pandas as pd
from pandas import DataFrame

def format_piechart(header:list, dict_df:dict) -> list:
    '''Formats data and appends to ws to be ready for draw chart function.
        header is a list containing [pie slice, value]
        dict_df is where the data is extracted from.
        '''
    data = [header] + [[row.Category, row.Amount] for row in dict_df.itertuples(index=False)]

    return data


### NOTE attempt this summary line chart later
# for worksheet, dataframe in dict_df.items():
# format_linechart(header=['Month','Groceries','Dining','Shopping','Pet','Car','Misc','Event','Snacks'])

# def format_linechart(header:list, df:DataFrame):
#     # [ [Month, Groceries, Dining, sHopping, pet, car, misc, event, snakcs]
#     #   [SEP23, total groc, total din, ...]
#     data = [
#         *header,
#         []


#     ]
