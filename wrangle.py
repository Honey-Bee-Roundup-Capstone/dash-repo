import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns

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
    # return the cleaned and sorted dataframe
    return df

