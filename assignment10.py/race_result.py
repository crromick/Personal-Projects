import doctest
from race_time import RaceTime

class RaceResult:
    """ RaceResult: represents a racer's result with 
    name, country and race finish time
    """

    def __init__(self, name: str, country: str, finish_time: RaceTime) -> None:
        """ initializes attributes of RaceResult instance
        >>> rt = RaceTime(12, 19, 9)
        >>> racer = RaceResult('Usain Bolt', 'Jamaica', rt)
        """
        self.__name = name
        self.__country = country
        self.__finish_time = finish_time

    def get_name(self) -> str:
        """ returns name of self RaceResult instance
        >>> rt = RaceTime(12, 19, 9)
        >>> racer = RaceResult('Usain Bolt', 'Jamaica', rt)
        >>> racer.get_name()
        'Usain Bolt'
        """
        return self.__name

    def get_country(self) -> str:
        """ returns country of self RaceResult instance
        >>> rt = RaceTime(12, 19, 9)
        >>> racer = RaceResult('Usain Bolt', 'Jamaica', rt)
        >>> racer.get_country()
        'Jamaica'
        """
        return self.__country

    def get_finish_time(self) -> RaceTime:
        """ returns RaceTime of self RaceResult instance
        >>> rt = RaceTime(12, 19, 9)
        >>> racer = RaceResult('Usain Bolt', 'Jamaica', rt)
        >>> racer.get_finish_time()
        RaceTime(12, 19, 9)
        """
        return self.__finish_time

    def __str__(self) -> str:
        """ returns a readable string with name, country, finish_time 
        of RaceResult
        >>> rt = RaceTime(12, 19, 9)
        >>> racer = RaceResult('Usain Bolt', 'Jamaica', rt)
        >>> str(racer)
        'Usain Bolt is from Jamaica. Finish Time: 9:19:12'
        """
        result_str = f'{self.__name} is from {self.__country}. ' \
            + f'Finish Time: {self.__finish_time}'
        return result_str

    def __repr__(self) -> str:
        """ returns a string representation of self RaceResult
        >>> rt = RaceTime(12, 19, 9)
        >>> racer = RaceResult('Usain Bolt', 'Jamaica', rt)
        >>> repr(racer)
        "RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 19, 9))"
        """
        result_str = f'RaceResult({repr(self.__name)}, ' \
            f'{repr(self.__country)}, {repr(self.__finish_time)})'
        return result_str
    
    def __eq__(self, other: 'RaceResult') -> bool:
        '''
        This function will return True if the country name and finish time 
        between self and other are equal, and will return False otherwise 
        
        
        >>> rt = RaceTime(12, 19, 9)
        >>> racer = RaceResult('Usain Bolt', 'Jamaica', rt)
        
        >>> rt2 = RaceTime(12, 18, 9)
        >>> racer2 = RaceResult('Usain Bolt', 'Jamaica', rt2)
        
        >>> rt3 = RaceTime(12, 19, 9)
        >>> racer3 = RaceResult('Usain Bolt', 'Jamaica', rt3)
        
        >>> rt4 = RaceTime(12, 19, 9)
        >>> racer4 = RaceResult('usain bolt', 'Jamaica', rt4)
        
        
        >>> racer == racer2
        False
        
        >>> racer == racer3
        True
        
        >>> racer == racer4
        False
        
        '''
        
        others = repr(other)
        
        return repr(self) == others
