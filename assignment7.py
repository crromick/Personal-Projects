import doctest

# represents the (year, month, day)
Date = tuple[int,int,int]
YEAR = 0
MONTH = 1
DAY = 2

Netflix = tuple[str,str,str,str,Date]
TYPE = 0
TITLE = 1
DIRECTORS = 2
ACTORS = 3
DATE = 4


def raise_to_power(list_1: list[int], list_2:list[int]) -> None:
    '''
    This function takes the value in list 1 and raises it the power of 
    
    >>> list_1= [1, 2, 3]
    >>> list_2= [2, 4, 0]
    >>> raise_to_power(list_1,list_2)
    >>> list_1
    [1, 16, 1]
    
    
    >>> lst1= [1, 2, 3]
    >>> lst2= [2, 4]
    >>> raise_to_power(lst1,lst2)
    >>> lst1
    [1, 16, 3]
    
    >>> lst1= [1, 2]
    >>> lst2= [2, 4, 0]
    >>> raise_to_power(lst1,lst2)
    >>> lst1
    [1, 16]
    
    >>> lst1= []
    >>> lst2= [2, 4, 0]
    >>> raise_to_power(lst1,lst2)
    >>> lst1
    []
    
    >>> lst1= [1, 2]
    >>> lst2= []
    >>> raise_to_power(lst1,lst2)
    >>> lst1
    [1, 2]
    
    >>> lst1= []
    >>> lst2= []
    >>> raise_to_power(lst1,lst2)
    >>> lst1
    []
    
    
    '''
    len_1 = len(list_1)
    len_2 = len(list_2)
    num = 0
    
    while num < len_1 and num < len_2:
        new_entry =list_1[num] ** list_2[num]
        list_1[num] = new_entry
        
        num += 1
    
        
        
    
    
def create_date(date: str) -> tuple:
    '''
    This function takes a str in the form 'day-month-year'
    and returns the date as a tuple 
    
    Precondition: "day" is a two digit integer, "month" is a three letter
    combination, "year" is a 2 digit integer after 1999
    
    >>> create_date('10-Jan-18')
    (2018, 1, 10)
    
    >>> create_date('22-Feb-00')
    (2000, 2, 22)
    
    >>> create_date('03-Mar-19')
    (2019, 3, 3)
    '''
    s = date
    date_list = s.split('-')
    DAY = (int(date_list[0]))
    MONTH = month_calculater(date_list[1])
    YEAR = int(date_list[2])
    YEAR = YEAR + 2000
    
    Date = (YEAR,MONTH,DAY)
    
    
    
    return Date
    
    
def month_calculater(month: str) -> int:
    '''
    This function when given a three letter combination will
    give you the eqivalent month number
    
    Precondition: month's first letter must be captialized 
    >>> month_calculater('Jan')
    1
    >>> month_calculater('Feb')
    2
    >>> month_calculater('Mar')
    3
    >>> month_calculater('Apr')
    4
    >>> month_calculater('May')
    5
    >>> month_calculater('Jun')
    6
    >>> month_calculater('Jul')
    7
    >>> month_calculater('Aug')
    8
    >>> month_calculater('Sep')
    9
    >>> month_calculater('Oct')
    10
    >>> month_calculater('Nov')
    11
    >>> month_calculater('Dec')
    12
    >>> month_calculater('jan')
    'spelling error'
    >>> month_calculater('xcx')
    'spelling error'
    >>> month_calculater('January')
    'spelling error'
    '''
    month_int = 0
    if month == 'Jan':
        month_int = 1
    elif month == 'Feb':
        month_int = 2
    elif month == 'Mar':
        month_int = 3
    elif month == 'Apr':
        month_int = 4
    elif month == 'May':
        month_int = 5
    elif month == 'Jun':
        month_int = 6
    elif month == 'Jul':
        month_int = 7
    elif month == 'Aug':
        month_int = 8
    elif month == 'Sep':
        month_int = 9
    elif month == 'Oct':
        month_int = 10
    elif month == 'Nov':
        month_int = 11
    elif month == 'Dec':
        month_int = 12
    else: 
        month_int = 'spelling error'
        
    return month_int


def create_show(TYPE, TITLE, DIRECTORS, ACTORS, Date) -> tuple:
    ''' 
    This function takes the type of show, title, directors, actors,
    and date, to create tuple of information in that order
    
    
    >>> create_show('Movie', 'Audrey & Daisy', 'Bonni Cohen:Jon Shenk', \
    '', '23-Sep-16') # doctest: +NORMALIZE_WHITESPACE
    ('Movie', 'Audrey & Daisy', ['Bonni Cohen', 'Jon Shenk'], [], (2016, 9, 23))

    
    >>> create_show('Movie', 'Room on the Broom', 'Max Lang:Jani Lachauer', \
    'Simon Pegg:Gillian Anderson:Rob Brydon:Martin Clunes:Sally Hawkins:David Walliams:Timothy Spall', \
    '1-Jul-19') # doctest: +NORMALIZE_WHITESPACE
    ('Movie', 'Room on the Broom', ['Max Lang', 'Jani Lachauer'], \
    ['Simon Pegg', 'Gillian Anderson', 'Rob Brydon', 'Martin Clunes', \
    'Sally Hawkins', 'David Walliams', 'Timothy Spall'], \
    (2019, 7, 1))
    
    >>> create_show('TV Show',\
    'Harry Potter and the Chamber of Secrets', '', '', '15-Jul-16')
    ('TV Show', 'Harry Potter and the Chamber of Secrets', [], [], (2016, 7, 15))
    '''
    Date = create_date(Date)
    d = str(DIRECTORS)
    if d == '':
        directors_act = []
    else:
        directors_act = d.split(':')    
    a = (ACTORS)
    if a == '':
        actors_act = []
    else:
        actors_act = a.split(':')
    show = (TYPE, TITLE, directors_act, actors_act, Date)
    return show

def get_titles(collection_of_shows: list[Netflix]) -> list:
    '''
    This function creates a list of the titles of the shows
    
    >>> collection_of_shows = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',\
    'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',\
    'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
    (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
    'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], \
    ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
    'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
    (2019, 12, 31))]

    >>> get_titles(collection_of_shows)
    ["Viceroy's House", 'Superbad', 'Maniac', 'Road to Sangam']

    '''
    
    show_len = len(collection_of_shows)
    num = 0
    new_list = []
    
    while num < show_len:
        
        titles = collection_of_shows[num][TITLE]
        new_list.append(titles)
        
        num += 1
    return new_list
    
    

def is_actor_in_show(Netflix, actor: str) -> bool:
    '''
    This function takes an actor's name and finds 
    out if they are in the given film/show
    
    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    'Justin Bieber')
    False
    
    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    'Michael Cera')
    True
    
    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    'MichaEL cerA')
    True
    
    
    
    '''
    
    in_show = Netflix[ACTORS]
    in_show = str(in_show)
    in_show = in_show.lower()
    
    
    actor = (actor.lower())
    
    if actor in in_show:
        return True
    else:
        return False
    
    
def count_shows_before_date(collection_of_shows: list[Netflix], Date) -> int:
    '''
    This function takes a list of shows according to the Netflix type
    alias and returns how many of them where created before the given date
    
    For collection_of_shows=
    
    >>> collection_of_shows= [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',\
    'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',\
    'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
    (2017, 2, 6)),\
    ('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
    'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], \
    ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
    'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
    (2017, 4, 18))]
    
    >>> count_shows_before_date(collection_of_shows, (2015, 1, 1))
    0

    >>> count_shows_before_date(collection_of_shows, (2018, 10, 20))
    3
    
    >>> count_shows_before_date(collection_of_shows, (2024, 10, 20))
    4
    
    >>> count_shows_before_date(collection_of_shows, (2017, 4, 18))
    1
    '''
    show_len = len(collection_of_shows)
    num = 0
    count = 0
    
    while num < show_len:
        release_date = collection_of_shows[num][DATE]
        
        if release_date < Date:
            count += 1
            
        num += 1
        
    return count



def get_shows_with_actor(collection_of_shows: list[Netflix], actor_name: str) -> list:
    '''
    This function takes a list of shows and checks if the contain
    the given actor, and returns a list of all the matches
    
    >>> collection_of_shows = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'], \
    ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
    'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
    'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
    (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
    'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], \
    ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
    'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
    (2019, 12, 31))]

    >>> get_shows_with_actor(collection_of_shows, 'Jonah Hill')  # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
    'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], \
    (2018, 9, 21))]

    >>> get_shows_with_actor(collection_of_shows, 'jonaH hiLL')  # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
    'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], \
    (2018, 9, 21))]

    >>> get_shows_with_actor(collection_of_shows, 'Justin Bieber')
    []

    
    '''
    
    num = 0 
    new_list = []
    show_list = len(collection_of_shows)
    
    while num < show_list:
        wanted_actor = is_actor_in_show(collection_of_shows[num], actor_name)
        if wanted_actor == True:
            new_list.append(collection_of_shows[num])
        
        num += 1
        
    return new_list