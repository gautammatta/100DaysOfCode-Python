#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:19:27 2018

@author: gmatta

Given the provided cars dictionary:

Get all Jeeps
Get the first car of every manufacturer.
Get all vehicles containing the string Trail in their names (should work for other grep too)
Sort the models (values) alphabetically
See the docstrings and tests for more details. Have fun!
"""
    import operator
    cars = {
        'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
        'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
        'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
        'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
        'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
    }
    
    
    def get_all_jeeps():
        """return a comma separated string of jeep models (original order)"""
        return (", " .join(cars['Jeep']))
        
    
    
    def get_first_model_each_manufacturer():
        """return a list of matching models (original ordering)"""
        model= [] 
        [model.append(c[0]) for c in cars.values()]
        return model
    
    
    def get_all_matching_models(grep='trail'):
        """return a list of all models containing the case insensitive
           'grep' string which defaults to 'trail' for this exercise,
           sort the resulting sequence alphabetically"""
        match = []
        for c in cars.values():
            for item in c : 
                if grep.lower() in item.lower() : 
                    match.append(item)
        match.sort()
        return match
    
    def sort_car_models():
        """sort the car models (values) and return the resulting cars dict"""
        cars_sorted = {}
        for k,v in cars.items():
            v_sort = sorted(v)
            cars_sorted[k] = v_sort
#        cars_sorted = sorted(cars.values(), key=operator.itemgetter(1))
#        cars_sorted1 = sorted(cars.items(), key=lambda x: x[1])
#        key=lambda x: x[1]
        return cars_sorted
    
    
    
    
###################### Tests.py #############################
    
    
from cars import (get_all_jeeps, get_first_model_each_manufacturer,
                  get_all_matching_models, sort_car_models)


def test_get_all_jeeps():
    expected = 'Grand Cherokee, Cherokee, Trailhawk, Trackhawk'
    actual = get_all_jeeps()
    assert type(actual) == str
    assert actual == expected


def test_get_first_model_each_manufacturer():
    actual = get_first_model_each_manufacturer()
    expected = ['Falcon', 'Commodore', 'Maxima', 'Civic', 'Grand Cherokee']
    assert actual == expected


def test_get_all_matching_models():
    expected = ['Trailblazer', 'Trailhawk']
    assert get_all_matching_models() == expected
    expected = ['Accord', 'Commodore', 'Falcon']
    assert get_all_matching_models(grep='CO') == expected


def test_sort_dict_alphabetically():
    actual = sort_car_models()
    # Order of keys should not matter, two dicts are equal if they have the
    # same keys and the same values.
    # The car models (values) need to be sorted here though
    expected = {
        'Ford': ['Fairlane', 'Falcon', 'Festiva', 'Focus'],
        'Holden': ['Barina', 'Captiva', 'Commodore', 'Trailblazer'],
        'Honda': ['Accord', 'Civic', 'Jazz', 'Odyssey'],
        'Jeep': ['Cherokee', 'Grand Cherokee', 'Trackhawk', 'Trailhawk'],
        'Nissan': ['350Z', 'Maxima', 'Navara', 'Pulsar'],
    }
    assert actual == expected
    
    
    
    
    
    
    
    
    
    
######################## Solution.py ########################## 
    
cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    """return a comma separated string of jeep models (original order)"""
    return ', '.join(cars['Jeep'])


def get_first_model_each_manufacturer():
    """return a list of matching models (original ordering)"""
    return [models[0] for models in cars.values()]


def get_all_matching_models(grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    grep = grep.lower()
    models = sum(cars.values(), [])  # flatten list of lists
    matching_models = [model for model in models
                       if grep in model.lower()]
    return sorted(matching_models)


def sort_car_models():
    """sort the car models (values) and return the resulting cars dict"""
    return {manufacturer: sorted(models) for
            manufacturer, models in cars.items()}