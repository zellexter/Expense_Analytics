from openpyxl import Workbook
from Data_Formatter_Module import *
from openpyxl.chart import (
    PieChart,
    Reference
)
from openpyxl.chart.series import DataPoint
from openpyxl.worksheet.worksheet import Worksheet

def draw_piechart(title: str, worksheet: Worksheet, header:list, dict_df:dict, start_row:int, start_col:int, add_to: str):
    """
    Draws a piechart after formatting data from a given dataframe.
    Only handles two columns of data currently.

    Args:
        ws_title (str): Used to title the chart.
        worksheet (Worksheet): Used to append data onto and add chart.
        header (list): Used to add headers to data.
        dict_df (dict): Used to extract data.
        start_row (int): First row where data will be appended in worksheet.
        start_col (int): First column where data will be appended in worksheet.
    """

    # format data and store in reusable variable
    formatted_data = format_piechart(header=header, dict_df=dict_df)

    # goes through each row in index, formatted_data and appends to cells in columns C and D
    for i, row in enumerate(formatted_data, start=start_row):
        worksheet.cell(row=i, column=start_col, value=row[0]) # writes 'Expense Category' to column C row 1
        worksheet.cell(row=i, column=start_col+1, value=row[1]) # writes 'Amount' to column D row 1
    
    pie = PieChart()

    # extracting data from formatted_data
    labels = Reference(worksheet, min_col=start_col, min_row=2, max_col=start_col, max_row=len(formatted_data))
    data = Reference(worksheet, min_col=start_col+1, min_row=1, max_col=start_col+1, max_row=len(formatted_data))

    # creating references for piechart
    pie.add_data(data, titles_from_data=True)
    pie.set_categories(labels)
    pie.title = title


    worksheet.add_chart(pie, add_to)

    ### ughhhhhh lesson learned, openpyxl's add_data() REQUIRES a reference() object. no way around it.
    ### ALSO: labels reference only references the actual labels, while in data reference you can include the header (min row 1)
    #   if you want the header to be used as a series label in the chart
    

