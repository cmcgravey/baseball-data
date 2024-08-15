import pandas as pd
import openpyxl
import click
from utils.config import load_config, connect

@click.command()
@click.option("--debug", "debug", default=False)
def main(debug):
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
    hitting_data = hitting_data.reset_index(drop=True)
    hitting_data.index.name = 'ID'

    ## Print one player's data by indexing by ID
    if debug==True:
        stats = hitting_data[hitting_data['playerID'] == "aaronha01"]
        print(stats)

    ## Dump data to spreadsheet or CSV
    if debug == True:
        excel_file = 'hitting_data.xlsx'
        hitting_data.to_excel(excel_file)
    else:
        csv_file = "hitting_data.csv"
        hitting_data.to_csv(csv_file)
    
    ## Insert data to postgres database
    if debug == False:
        config = load_config()
        print(config)
        print("here")
        conn = connect(config)



if __name__ == "__main__":
    main()
