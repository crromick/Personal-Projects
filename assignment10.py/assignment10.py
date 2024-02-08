import doctest
from race_time import RaceTime
from race_result import RaceResult

# represents a racer as (name, country)
# where name and country != ''
RacerNameCountry = tuple[str, str]

# columns of values in input file row and positions in RacerNameCountry
NAME = 0
COUNTRY = 1
TIME_MS = 2

# indexing the race_time tuple
MS = 0
SECONDS = 1
MINUTES = 2

# initizaling the get_fastest_time loop
FIRST_RACER = 0

def read_file(filename: str) -> list[RaceResult]:
    """ returns a list of RaceResults populated with data from filename
    Precondition: the file exists, is not empty, has the following
      information on each row separated by commas:
      racer's name, racer's country, race time in milliseconds>=0
      and contains a header row with the column titles.
      The header row is ignored.

    >>> read_file('0lines_data.csv')
    []
    >>> read_file('9lines_data.csv') # doctest: +NORMALIZE_WHITESPACE
    [RaceResult('Evan Jager', 'United States', RaceTime(450, 0, 8)), \
     RaceResult('Brimin Kipruto', 'Kenya', RaceTime(640, 53, 7)), \
     RaceResult('Saif Saaeed Shaheen', 'Qatar', RaceTime(630, 53, 7)), \
     RaceResult('Wander Moura', 'Brazil', RaceTime(410, 14, 8)), \
     RaceResult('Mahiedine Mekhissi-Benabbad', 'France', RaceTime(90, 0, 8)), \
     RaceResult('Peter Renner', 'New Zealand', RaceTime(50, 14, 8))]
    """
    # TODO: complete this function
    
    lo_raceresult = []
    
    fhandle = open(filename, 'r')
    
    fhandle.readline()
    
    for line in fhandle:
        line_data = line.strip()
        line_data = line_data.split(',')
        
        rt = int(line_data[TIME_MS])
        race_time = race_time_calc(rt)
        race_time = RaceTime(race_time[MS], race_time[SECONDS],\
                             race_time[MINUTES])
                
        rr = RaceResult(line_data[NAME], line_data[COUNTRY], race_time)
        lo_raceresult.append(rr)
        
    return lo_raceresult
        

        
def race_time_calc(ms: int) -> list[int]:
    '''
    This function takes an interger that represents a race time in ms and
    converts it into ms, seconds, and minutes 
    
    Precondtion: ms >= 0 
    
    >>> race_time_calc(480450)
    (450, 0, 8)
    
    >>> race_time_calc(473640)
    (640, 53, 7)
    '''
    
    (ms // 1000) > 0
    seconds = (ms // 1000)
    ms_r = ms - (seconds * 1000)
    (seconds // 60) > 0
    minutes = (seconds // 60)
    sec_r = seconds - (minutes * 60)
        
    time_tuple = (ms_r, sec_r, minutes)
    
    return time_tuple

        
    


def find_athlete(loresults: list[RaceResult], name: str) -> int:
    """ returns the position of RaceResult with given athlete name in loresults
    Returns -1 if name not found
    Returns the position of the first if there >1 RaceResult with given name
    Precondition: case sensitive (ie. 'Brad' != 'brad')

    >>> find_athlete([], 'Brimin Kipruto')
    -1
    >>> find_athlete(\
        [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 22, 20)), \
         RaceResult('Brimin Kipruto', 'Kenya', RaceTime(640, 53, 7))],\
        'brimin kipruto')
    -1
    >>> find_athlete(\
        [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 22, 20)), \
         RaceResult('Brimin Kipruto', 'Kenya', RaceTime(640, 53, 7))], \
        'Brimin Kipruto')
    1
    >>> find_athlete(\
        [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 22, 20)), \
         RaceResult('Brimin Kipruto', 'Kenya', RaceTime(640, 53, 7))], \
        'Peter Renner')
    -1
    >>> find_athlete(\
        [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 22, 20)), \
         RaceResult('Usain Bolt', 'Canada', RaceTime(1, 2, 2019))], \
        'Usain Bolt')
    0
    
    >>> find_athlete(\
        [RaceResult('Jianping Scriven', 'Spain', RaceTime(476, 41, 3))],\
        'Jianping Scrive')
    -1
    """
    # TODO: complete this function
    position = 0
    
    if loresults == []:
        return -1
    else:
        
        for athlete in loresults:
            rr = athlete
            if name == athlete.get_name():
                return position 
            position += 1
        return -1
        
    
    
    
    
    

def get_all_from_country(loresults: list[RaceResult], country: str
                         ) -> list[RaceResult]:
    """ returns a list of all results of the given country
    Precondition: case sensitive (ie. 'Canada' != 'canada')

    >>> results = \
    [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 31, 4)), \
     RaceResult('Zhou', 'China', RaceTime(9, 15, 12)), \
     RaceResult('Perrier', 'France', RaceTime(1, 23, 18)), \
     RaceResult('Perrieruels', 'Canada', RaceTime(3, 29, 0)), \
     RaceResult('Bailey', 'Jamaica', RaceTime(2, 8, 3)), \
     RaceResult('Allen', 'Jamaica', RaceTime(9, 15, 5))]

    >>> get_all_from_country([], 'Jamaica')
    []

    >>> get_all_from_country(results, 'jamaica')
    []

    >>> get_all_from_country(results, 'Jamaica') # doctest: +NORMALIZE_WHITESPACE
    [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 31, 4)), \
     RaceResult('Bailey', 'Jamaica', RaceTime(2, 8, 3)), \
     RaceResult('Allen', 'Jamaica', RaceTime(9, 15, 5))]

    >>> get_all_from_country(results, 'Japan')
    []
    
    >>> get_all_from_country(\
       [RaceResult('Mwayi Garfield', 'China', RaceTime(529, 17, 4))],\
       'Chin')
    []
    """
    # TODO: complete this function
    lo_country = []
    
    if loresults == []:
        return lo_country
    else:
        
        for athlete in loresults:
            rr = athlete
            if country == athlete.get_country():
                lo_country.append(athlete)
                
    return lo_country 
    
    


def get_fastest_time(loresults: list[RaceResult]) -> RaceTime:
    """ returns the fastest RaceTime of all finish_times of 
    RaceResult instances in loresults
    Precondition: loresults is not empty

    >>> one_result = [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 31, 9))]
    >>> results = \
    [RaceResult('Allen', 'Jamaica', RaceTime(12, 31, 10)), \
     RaceResult('Zhou', 'China', RaceTime(9, 16, 17)), \
     RaceResult('Barnes', 'Canada', RaceTime(3, 43, 9)), \
     RaceResult('Perrier', 'France', RaceTime(3, 29, 9)), \
     RaceResult('Bailey', 'Jamaica', RaceTime(2, 48, 9)), \
     RaceResult('Davis', 'Jamaica', RaceTime(9, 15, 17))]

    >>> get_fastest_time(one_result)
    RaceTime(12, 31, 9)
    >>> get_fastest_time(results)
    RaceTime(3, 29, 9)
    """
    # TODO: complete this function
    
    other = loresults[FIRST_RACER].get_finish_time()
    ms_sum = 0
    for athlete in loresults:
        rr = athlete
        rr = rr.get_finish_time()
        if rr.is_faster(other) == True:
                other = rr
        
    return other
        
    
   


def get_with_fastest_time(loresults: list[RaceResult]
                          ) -> list[RacerNameCountry]:
    """ returns a list tuples of fastest RaceResults in loresults

    >>> results = \
    [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 31, 10)), \
     RaceResult('Zhou', 'China', RaceTime(9, 15, 6)), \
     RaceResult('Barnes', 'Canada', RaceTime(1, 23, 9)), \
     RaceResult('Perrier', 'France', RaceTime(3, 10, 7)), \
     RaceResult('Bailey', 'Jamaica', RaceTime(2, 15, 9)), \
     RaceResult('Davis', 'Jamaica', RaceTime(9, 15, 6))]
     
    >>> get_with_fastest_time([])
    []
    >>> get_with_fastest_time(results)
    [('Zhou', 'China'), ('Davis', 'Jamaica')]
    """
    # TODO: complete this function
    
    lo_fastest = []
    
    if loresults == []:
        return lo_fastest
    
    fastest_time = get_fastest_time(loresults)
   
       
    for athlete in loresults:
        name = athlete.get_name()
        country = athlete.get_country()
        RacerNameCountry = (name, country)
        if athlete.get_finish_time() == fastest_time:
            lo_fastest.append(RacerNameCountry)
            
    return lo_fastest
            
        

