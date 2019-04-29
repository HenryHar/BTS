import pandas as pd


def hit_checker(df,year,month,day, players):
    results =[]
    hit_flags = [20, 21, 22, 23]   #20 = single, 21 = double, 22 = triple, 23 = homerun
    df = df[df['year']==year]
    df = df[df['month'] == month]
    df = df[df['day_'] == day]
    for player in players:
        new_df = df[df.res_batter==player]
        if sum(new_df.ab_flag)> 0:
            results.append(int(sum(new_df.event_type.isin(hit_flags))>=1))

    if len(results) ==0:     #all the players either did not play or got charged 0 at bats so the streak should continue
        return 'continue_streak'

    if sum(results) < len(results):   
        return 'lose_streak'

    if sum(results) == len(results): 
        return sum(results)
    
    # Same function as below except returns 'continue_streak', 'lose_streak' or the number your stream should extend by
    
#pass df to avoid re-loading it, year, month, date, list of players and current streak lenght

def streak_counter(df,year,month,day, players, streak):
    
    #STILL need to look at BTS rules for double_headers and rules with that
    
    results =[]
    hit_flags = [20, 21, 22, 23]   #20 = single, 21 = double, 22 = triple, 23 = homerun
    df = df[df['year']==year]
    df = df[df['month'] == month]
    df = df[df['day_'] == day]
    for player in players:
        new_df = df[df.res_batter==player]
        if sum(new_df.ab_flag)> 0:
            results.append(int(sum(new_df.event_type.isin(hit_flags))>=1))

    if len(results) ==0:     #all the players either did not play or got charged 0 at bats so the streak should continue
        #return 'continue_streak'
        return streak
        
    if sum(results) < len(results):
        #return 'lose_streak'
        streak = 0
        return streak
        
    if sum(results) == len(results): 
        streak = streak + sum(results)
        return streak
    
# The way it works: results gets 1 or 0 depending on if the player got a hit. 
# results is a list, it only expands if the player got an official at-bat, this is tracked by retrosheet in a column ab_flag

#results can only contain 1 for True ( >=1 hit ) or 0 for 0 hits, the sum of results needs to be equal to the lenght of results
#if not that means that at least 1 of the batters did not get a hit so the streak should reset 
#(remember results only expands if the player got an AB)

#since results is 1 or 0 in the last case the sum equals the lenght so it should return the new streak counter



# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 14:44:27 2019

@author: henry
"""

