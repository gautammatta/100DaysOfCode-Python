# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 22:34:58 2018

@author: G-Machine
"""

us_state_abbrev = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ',
                   'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
                   'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL',
                   'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
                   'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
                   'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
                   'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA',
                   'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
                   'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE',
                   'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
                   'New Mexico': 'NM', 'New York': 'NY',
                   'North Carolina': 'NC', 'North Dakota': 'ND',
                   'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR',
                   'Pennsylvania': 'PA', 'Rhode Island': 'RI',
                   'South Carolina': 'SC', 'South Dakota': 'SD',
                   'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT',
                   'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
                   'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'}

states = ['Oklahoma', 'Kansas', 'North Carolina', 'Georgia', 'Oregon',
          'Mississippi', 'Minnesota', 'Colorado', 'Alabama',
          'Massachusetts', 'Arizona', 'Connecticut', 'Montana',
          'West Virginia', 'Nebraska', 'New York', 'Nevada', 'Idaho',
          'New Jersey', 'Missouri', 'South Carolina', 'Pennsylvania',
          'Rhode Island', 'New Mexico', 'Alaska', 'New Hampshire',
          'Tennessee', 'Washington', 'Indiana', 'Hawaii', 'Kentucky',
          'Virginia', 'Ohio', 'Wisconsin', 'Maryland', 'Florida',
          'Utah', 'Maine', 'California', 'Vermont', 'Arkansas', 'Wyoming',
          'Louisiana', 'North Dakota', 'South Dakota', 'Texas',
          'Illinois', 'Iowa', 'Michigan', 'Delaware']

NOT_FOUND = 'N/A'


def get_every_nth_state(n=10):
    """Return a list with every nth item (default 10th item)
       of states (takeaway: lists keep order)"""
   # nstates = []
    #for i in range(n-1,len(states),n):
     #   nstates.append(states[i])
        
    return [states[i] for i in range(n-1,len(states),n) ]    
    #return nstates


def get_state_abbrev(abbrev):
    """Look up a state abbreviation by full name in
       us_state_abbrev, if not found return the string stored in the
       NOT_FOUND constant (takeaway: dicts are great for lookups)"""
    if abbrev in us_state_abbrev.keys():
        return us_state_abbrev[abbrev]
    else : 
        return NOT_FOUND
    


def get_longest_state(data):
    """Takes dict or list and determines the longest state name
       (takeaways: use a dict method to get all keys, use sorted)"""
    return sorted(data,key=len,reverse = True)[0]
    

def combine_state_names_and_abbreviations():
    """Return a new list with the first 10 abbreviations from the
       us_state_abbrev dict ordered values and the last 10 states from
       the states list (takeaways: use another dict method to get all
       values and use sorted, list slicing and list concatenation)"""
    
    pass













############################## TESTS ############################## 


from states import (get_every_nth_state, get_state_abbrev,
                    get_longest_state, combine_state_names_and_abbreviations,
                    states, us_state_abbrev, NOT_FOUND)


def test_get_every_nth_state():
    states = get_every_nth_state()
    assert states == ['Massachusetts', 'Missouri', 'Hawaii',
                      'Vermont', 'Delaware']
    assert get_every_nth_state(20) == ['Missouri', 'Vermont']


def test_get_state_abbrev():
    abbrev = 'Illinois'
    assert get_state_abbrev('Illinois') == 'IL'
    assert get_state_abbrev('North Dakota') == 'ND'
    assert get_state_abbrev('bogus') == NOT_FOUND


def test_get_longest_state():
    # depending the direction of the sort (reversed or not)
    # both North and South Carolina are correct
    correct_answers = ('North Carolina', 'South Carolina')
    assert get_longest_state(us_state_abbrev) in correct_answers
    assert get_longest_state(states) in correct_answers


def test_combine_state_names_and_abbreviations():
    expected = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
                'South Dakota', 'Tennessee', 'Texas', 'Utah',
                'Vermont', 'Virginia', 'Washington', 'West Virginia',
                'Wisconsin', 'Wyoming']
    assert combine_state_names_and_abbreviations() == expected