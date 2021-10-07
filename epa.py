#!/usr/bin/env python3

import sys

stats_i_dont_need = ['broadcast_network', 'temperature', 'condition', 'humidity', 'wind_speed', 'wind_direction', 'attendance']

if __name__ == '__main__':
    filename = "./2021_PBP_DATA/Week_1.csv"
    firstline = True
    allgames = list()
    cur_week = ""
    cur_home = ""
    cur_away = ""
    this_game = ""

    with open(filename) as f:
        for line in f:
            
            if firstline:
                stat_names = line.split(',')
                firstline = False
                continue

            stats = line.split(',')
            this_line = dict()
            for stat,stat_name in zip(stats,stat_names):
                if stat_name in stats_i_dont_need:
                    continue
                this_line[stat_name] = stat
            if cur_home != this_line['home_market'] or cur_away != this_line['away_market'] or cur_week != this_line['week']:
                if this_game != "":
                    allgames.append(this_game)
                cur_home = this_line['home_market']
                cur_away = this_line['away_market']
                cur_week = this_line['week']
                this_game = list()
            
            this_game.append(this_line)
            print(allgames)








