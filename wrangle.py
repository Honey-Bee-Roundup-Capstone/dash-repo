#standard imports
import pandas as pd
import numpy as np


def prep_bees():
    '''This function loads the bee_colony_loss.csv into a dataframe, cleans and sorts it, and returns a dataframe.'''
    # read the csv into a pandas dataframe
    df = pd.read_csv('bee_colony_loss.csv')
    # drop the unnamed column
    df = df.drop(columns='Unnamed: 0')
    # sort by descending year and ascending state
    df = df.sort_values(['year','state'], ascending=[False,True])
    # drop nulls
    df = df.dropna()
    # lowercase all strings in state and replace spaces with underscores
    df.state = df.state.str.lower().str.replace(' ','_')
    # lowercase all strings in the season column
    df.season = df.season.str.lower()
    # remove observations that have 10 or less beekeepers
    df = df[df.beekeepers > 10]
    # drop duplicate rows
    df = df.drop_duplicates()
    # change total_loss column to float
    df.total_loss = df.total_loss.astype(float)
    # change average_loss column to float
    df.average_loss = df.average_loss.astype(float)
    # change ending_colonies column to int
    df.ending_colonies = df.ending_colonies.astype(int)
    # change colonies_lost column to int
    df.colonies_lost = df.colonies_lost.astype(int)
    # pull only annual season data
    df = df[df.season == "annual"]
    #pull non multistates and non continental usa data
    df = df[(df.state != "multistates")& (df.state != "non_continental_usa")]
    # create column net gain / loss for each state
    df['colonies_net_gain'] = df.ending_colonies - df.starting_colonies
    # create a column for beekeeper to colony ratio
    df['beekeeper_colony_ratio'] = df.ending_colonies / df.beekeepers
    # look at only beekeepers exclusive to state
    df = df[df.beekeepers_exclusive_to_state == 100]
    # return the cleaned and sorted dataframe
    return df


def state_ansi():
    ''' This function will load state ansi from csv and turn state with its corresponding ansi'''
    #read the csv
    df = pd.read_csv("state_ansi.txt",sep = "|")
    #lower case column names 
    df.columns = df.columns.str.lower()
    #lower case string values on the column and replace wmpty spaces with underscore
    df.state_name = df.state_name.str.lower().str.replace(' ','_')
    #rename column names and drop unnecessary columns
    df = df.rename(columns = {"state":"ansi", "state_name":"state"}).drop(columns = ["stusab", "statens"])
    
    #return back dataframe
    return df

def geo_data():
    ''' This function will load state ansi from csv and turn state with its corresponding ansi'''
    #read csv
    df = pd.read_csv("state_geocords.csv", index_col = [0] )
    #rename column
    df= df.rename(columns = {"name":"state"})
    # lowercase values of column and replace spaces with underscore
    df.state = df.state.str.lower().str.replace(' ','_')
    #pull only useful column
    df = df[["state","latitude","longitude"]]
    
    #return back dataframe
    return df

def bee_merged():
    """This function will call in three different function and merge them all"""
    #call in prep bees function
    df = prep_bees()
    #call in function for state  ansi data
    df1 = state_ansi()
    #call in function for geo data
    df2 = geo_data()
    #left join prep_bees dataset with state_ansi
    df = df.merge(df1, on = 'state', how = 'left')
    #left join prep_bees dataster with geo_state
    df = df.merge(df2, on="state", how = "left")
    
    #return back dataframe
    return df

def ts_bee_prep():
    '''This function loads the bee colony loss csv into a pandas dataframe. It cleans the data and prepares it for time
        series analysis. The function returns the cleaned dataframe with the year converted to datetime.'''
    # pull in the csv and save to a variable
    df2 = pd.read_csv('bee_colony_loss.csv')
    # drop the unnamed index column
    df2 = df2.drop(columns='Unnamed: 0')
    # make the season column all lowercase
    df2.season = df2.season.str.lower()
    # make the state column lowercase and replace spaces with underscores
    df2.state = df2.state.str.lower().str.replace(' ','_')
    # remove observations with 10 or less beekeepers (info in these columns is null due to privacy protections)
    df2 = df2[df2.beekeepers > 10]
    # get dummy variables for the season column and save to a dataframe
    dummy_df = pd.get_dummies(df2.season)
    # concatenate the dummy_df with the original df2
    df2 = pd.concat([df2, dummy_df], axis=1)
    # isolate beekeepers exclusive to state and resave 
    df2 = df2[df2.beekeepers_exclusive_to_state == 100]
    # change average_loss to a float
    df2.average_loss = df2.average_loss.astype(float)
    # change total_loss to a float
    df2.total_loss = df2.total_loss.astype(float)
    # change colonies_lost to an integer
    df2.colonies_lost = df2.colonies_lost.astype(int)
    # change ending_colonies to an integer
    df2.ending_colonies = df2.ending_colonies.astype(int)
    # remove multstate and non_continental data
    df2 = df2[(df2.state != "multistates") & (df2.state != "non_continental_usa")]
    # create column net gain / loss for each state
    df['colonies_net_gain'] = df.ending_colonies - df.starting_colonies
    # create a column for beekeeper to colony ratio
    df['beekeeper_colony_ratio'] = df.ending_colonies / df.beekeepers
    # add the month of October to winter observations (prep for datetime conversion)
    df2.year[df2.season=='winter'] = df2.year.astype(str) + '-10-01'
    # add the month of April to summer observations (prep for datetime conversions)
    df2.year[df2.season=='summer'] = df2.year.astype(str) + '-04-01'
    # add the month of January to annual observations (prep for datetime conversion)
    df2.year[df2.season=='annual'] = df2.year.astype(str) + '-01-01'
    # convert year column to datetime
    df2.year = pd.to_datetime(df2.year)
    return df2

def ts_split(df2):
    '''This function takes in the dataframe from the ts_bee_prep function and splits it into train, validate, and test
        by year. Train is data up to and including 2017, validate is from 2018-2020, and test is 2021-2022. The function
        returns three dataframes: train, validate, test.'''
    # split dataframe at the end of 2017 and save into train    
    train = df2[df2['year'].dt.year <= 2017]
    # create a variable to hold data after 2017 that will be split again
    val = df2[df2['year'].dt.year > 2017]
    # split val dataframe at the end of 2020 and save into validate
    validate = val[val['year'].dt.year <= 2020]
    # split val dataframe and save 2021-2022 data into test
    test = val[val['year'].dt.year > 2020]
    # return three dataframes for exploration and modeling
    return train, validate, test