#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 14:18:59 2018

@author: gmatta
"""



#### exercise 

import csv
from collections import defaultdict, namedtuple



MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie','title year score')

def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    directors = defaultdict(list)
    with open(MOVIE_DATA, newline = '\n') as csvfile : 
        movieData = csv.DictReader(csvfile)
        for mov in movieData:
            try: 
                director = mov['director_name']
                movie = mov['movie_title'].replace('\xa0','')
                year = int(mov['title_year'])
                score = float(mov['imdb_score'])
            except ValueError :
                continue
            m = Movie(title = movie, year = year, score = score)
            directors[director].append(m)
          #  dir_mov_dict{row['director_name']} = 
    return directors

def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    filtered_directors = defaultdict(list)
    final_directors = defaultdict(list)
    #[filtered_directors[k].append(v) for k,v in directors.items() for l in range(len(v)) if v[l][2] >= MIN_YEAR]
    #for k,v in directors.items() : 
#        for l in range(len(v)):
#            if v[l][1] >= MIN_YEAR : 
#                filtered_directors[k].append(v)
#    for k, v in filtered_directors.items():
#        if len(v) >= MIN_MOVIES:
#            scores = 0.0
#            for l in range(len(v)):
#                scores = float(v[l][2])
#                if l == (len(v) - 1): 
#                    final_directors[k].append(scores/len(v))
#                
#    final_directors 
#                
#                
#            
#    return filtered_directors
    
dir =  get_average_scores(directors)  
directors = get_movies_by_director()

for k,v in dir.items():
    print(v[len(v)-1]['2])

