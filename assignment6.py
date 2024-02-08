import doctest

def get_powers(power_list: list[int], power: int) -> list:
    '''
    This function will rasie every item in a given list
    to the power of the second argument
    
    >>> get_powers([6,2,3,1,5], 2)
    [36, 4, 9, 1, 25]
    
    >>> get_powers([6,2,3,1,5], 0)
    [1, 1, 1, 1, 1]
    
    >>> get_powers([6,2,3,1,5], 1)
    [6, 2, 3, 1, 5]
    
    >>> get_powers([6,2,3,1,5], -1)
    [0.16666666666666666, 0.5, 0.3333333333333333, 1.0, 0.2]
    
    '''
    new_list = []
    powered = 0
    
    for index in (power_list):
        powered = index ** power
        new_list.append(powered)
    return new_list



def concatenate(strings: list[str]) -> str:
    '''
    This function takes a list made up of strings and
    returns a single string containing all the other strings in order
    
    
    >>> concatenate(['abc', 'de'])
    'abc de'
    
    >>> concatenate(['abc'])
    'abc'
    '''
    prompt = ''
    count = 0
    for word in strings:
        prompt += word
        count += 1
        if count != len(strings):
            prompt += ' '
        
    
    return prompt




def contains_multiple(integers: list[int], multiple: int) -> bool:
    '''
    This function will take an argument and check
    if any of the numbers in the list are a mutiple of the given argument
    
    >>> contains_multiple([6,2,3,1,5], 2)
    True
    
    >>> contains_multiple([3,2,3,1,5], 7)
    False
    
    >>> contains_multiple([22, 15, 25, 29, 16, 0, 23, 8, 36, 12, 38],0)
    True
    
    >>> contains_multiple([3,2,3,1,5], 0)
    True
    
    >>> contains_multiple([12,2,3,1,5], 3)
    True
    
    >>> contains_multiple([3,2,3,5], 9)
    False
    
    >>> contains_multiple([92, 34, 19, 7, 29],23)
    True
    '''
    
    is_multiple = 1
    index = 0
    num_elements = len(integers)
    if multiple == 0:
        return True
    while index < num_elements and (is_multiple % multiple != 0):
        is_multiple = integers[index]
        index += 1
    return (is_multiple % multiple) == 0

def get_long_enough(strings: list[str], threshold: int) -> list:
    '''
    This function will return a list of strings
    that were longer than the threshold argument
    
    
    >>> get_long_enough(['dance', 'toast', 'no', 'yes'] ,2)
    ['dance', 'toast', 'no', 'yes']
    
    >>> get_long_enough(['dance', 'toast', 'no', 'yes'] ,3)
    ['dance', 'toast', 'yes']
    
    >>> get_long_enough(['dance', 'toast', 'no', 'yes'] ,8)
    []
    
    >>> get_long_enough([] ,2)
    []
    '''
    new_list = []
    
    for index in strings:
        if len(index) >= threshold:
            new_list.append(index)
    return new_list


def all_multiples(integers: list[int], multiple: int) -> bool:
    '''
    This function will take an argument and check
    if any of the numbers in the list are a mutiple of the given argument
    
    >>> all_multiples([6,2,3,1,5], 2)
    False
    
    >>> all_multiples([3,2,3,1,5], 7)
    False
    
    >>> all_multiples([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0)
    True
    
    >>> all_multiples([19, 63, 27, -63, -81, 153, -54, 72, 90, -153, 162],9)
    False
    
    >>> all_multiples([3,2,3,1,5], 0)
    True
    
    >>> all_multiples([3,2,3,1,5], 1)
    True
    
    >>> all_multiples([12,18,24,30,36], 6)
    True
    
    >>> all_multiples([12,18,24,30,35], 6)
    False
    '''
    
    is_multiple = 0
    index = 0
    num_elements = len(integers)
    if multiple == 0:
        return True
    while index < num_elements and ((is_multiple % multiple) == 0):
        is_multiple = integers[index]
        index += 1
    return ((is_multiple % multiple) == 0)    
        
        
        
def getting_shorter(shortening: list[str]) -> bool:
    '''
    This function returns true if the length of
    the given string are less than the previous
    
    >>> getting_shorter(['tiny', 'same', 'are', 'at'])
    False
    
    >>> getting_shorter(['tiny', 'sam', 'ar', 'a'])
    True
    
    >>> getting_shorter(['tiny', 'are', 'at'])
    True
    
    >>> getting_shorter(['tiny', 'same', 'alligator' 'are', 'at'])
    False
    
    >>> getting_shorter([])
    True
    
    >>> getting_shorter(['ti', 'a'])
    True
    
    >>> getting_shorter(['always'])
    True
    
    >>> getting_shorter(['auqlfymdeu', 'dlzpsobcc','ew', 'ews', 'ahabypkqhj'])
    False
    '''
    
    if shortening == [] or len(shortening) == 1:
        return True
    previous = len(shortening[0])
    num_elements = len(shortening)
    index = 0
    while (index + 1) < num_elements and previous > len(shortening[index + 1]):
        previous = len(shortening[index])
        index += 1
            
    return(previous > len(shortening[index]))