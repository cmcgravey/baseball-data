import pandas as pd
import openpyxl

def main():
    ## read csv file
    hitting_data = pd.read_csv('archive/batting.csv')

    ## Filtering for players who played in the modern era, who played in more than 50 games in a season, and had more than 100 ABs
    hitting_data = hitting_data[hitting_data['yearID'] >= 1960]
    hitting_data = hitting_data[hitting_data['G'] >= 50]
    hitting_data = hitting_data[hitting_data['AB'] >= 100]

    ## Creating columns for AVG, OBP, SLG, and OPS
    hitting_data['AVG'] = hitting_data['H'] / hitting_data['AB']
    hitting_data['PA'] = hitting_data['AB'] + hitting_data['BB'] + hitting_data['SH'] + hitting_data['SF']
    hitting_data['OBP'] = (hitting_data['H'] + hitting_data['BB']) / hitting_data['PA']
    hitting_data['1B'] = hitting_data['H'] - (hitting_data['2B'] + hitting_data['3B'] + hitting_data['HR'])
    hitting_data['TB'] = hitting_data['1B'] + (2 * hitting_data['2B']) + (3 * hitting_data['3B']) + (4 * hitting_data['HR'])
    hitting_data['SLG'] = hitting_data['TB'] / hitting_data['AB']
    hitting_data['OPS'] = hitting_data['OBP'] + hitting_data['SLG']

    ## Grouping by playerID and yearID decreasing
    hitting_data = hitting_data.sort_values(['playerID', 'yearID'])

    ## Print one player's data by indexing by ID
    stats = hitting_data[hitting_data['playerID'] == "aaronha01"]

    ## Dump data to spreadsheet
    excel_file = 'hitting_data.xlsx'
    hitting_data.to_excel(excel_file)


if __name__ == "__main__":
    main()
