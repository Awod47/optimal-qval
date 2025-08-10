import pandas as pd
import os

base_dir = os.path.dirname(__file__) 

def write_to_excel(df):
    print('finishing up..')
    save_file_path = os.path.join(base_dir, '..', 'results', 'quant_value_stocks.xlsx')
    writer = pd.ExcelWriter(save_file_path, engine = 'xlsxwriter')
    df.to_excel(writer, sheet_name = 'Value Strategy', index = False)

    background_color = '#0a0a23'
    font_color = '#ffffff'

    string_template = writer.book.add_format(
            {
                'font_color': font_color,
                'bg_color': background_color,
                'border': 1
            }
        )

    dollar_template = writer.book.add_format(
            {
                'num_format':'$0.00',
                'font_color': font_color,
                'bg_color': background_color,
                'border': 1
            }
        )

    integer_template = writer.book.add_format(
            {
                'num_format':'0',
                'font_color': font_color,
                'bg_color': background_color,
                'border': 1
            }
        )

    float_template = writer.book.add_format(
            {
                'num_format':'0.00',
                'font_color': font_color,
                'bg_color': background_color,
                'border': 1
            }
        )

    percent_template = writer.book.add_format(
            {
                'num_format':'0.0%',
                'font_color': font_color,
                'bg_color': background_color,
                'border': 1
            }
        )

    column_formats = {
        'A': ['Ticker', string_template],
        'B': ['Price', dollar_template],
        'C': ['Number of Shares to Buy', integer_template],
        'D': ['Price to Earnings Ratio', float_template],
        'E': ['PE Percentile', percent_template],
        'F': ['Price to Book Ratio', float_template],
        'G': ['PB Percentile',percent_template],
        'H': ['Price to Sales Ratio', float_template],
        'I': ['PS Percentile', percent_template],
        'J': ['EV / EBITDA', float_template],
        'K': ['EV / EBITDA Percentile', percent_template],
        'L': ['EV / GP', float_template],
        'M': ['EV / GP Percentile', percent_template],
        'N': ['RV Score', percent_template]
    }

    for column in column_formats.keys():
        writer.sheets['Value Strategy'].set_column(f'{column}:{column}', 25, column_formats[column][1])

    print('your value stock portfolio is saved in the results directory :)')
    writer.close()