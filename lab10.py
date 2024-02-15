import doctest
from student import Student
""" Student with unique id (sid) and current grade (grade)"""


#for indexing the student_info list
SID = 0
GRADE = 1

def get_students(filename: str) -> list[tuple]:
    '''
    this funciton will open a file and create a list of Student objects
    
    >>> get_students('student_data.csv')
    [Student('V00123456', 89), Student('V00123457', 99), Student('V00123458', 30), Student('V00123459', 78)]
    
    >>> get_students('empty_file.txt')
    []

    '''
    lo_students = []
    
    fhandle = open(filename, 'r')
    
    for line in fhandle:
        student_info = line.strip()
        sid,grade = student_info.split(',')
        student = Student(student_info[SID],int(student_info[GRADE]))
        lo_students.append(student)
        

        
    fhandle.close()
    
    #return lo_students
    
    
    

def get_classlist(classlist: list[Student]) -> list[str]:
    '''
    this function takes a list of Student objects and creates a new list
    of just the student ids
    
    >>> get_classlist([Student('V00123456', 89), Student('V00123457', 99), Student('V00123458', 30), Student('V00123459', 78)])
    ['V00123456', 'V00123457', 'V00123458', 'V00123459']
    
    >>> get_classlist([])
    []
    '''
    new_list = []
    
    
    for student in classlist:
        new_list.append(student.get_sid())
    return new_list

def count_above(classlist: list[Student], threshold: int) -> int:
    '''
    this funciton takes a class list and returns the number of students who
    passed the course
    
    Precondition: 0 < threshold < 100
    
    >>> count_above([Student('V00123456', 89), Student('V00123457', 99), Student('V00123458', 30), Student('V00123459', 78)], 79)
    2
    
    >>> count_above([Student('V00123456', 89), Student('V00123457', 99), Student('V00123458', 30), Student('V00123459', 78)], 78)
    2
    
    >>> count_above([Student('V00123456', 89), Student('V00123457', 99), Student('V00123458', 30), Student('V00123459', 78)], 1)
    4
    
    >>> count_above([Student('V00123456', 89), Student('V00123457', 99), Student('V00123458', 30), Student('V00123459', 78)], 100)
    0
    
    >>> count_above([], 100)
    0
    
    '''
    count = 0
    
    for student in classlist:
        student_grade = student.get_grade()
        
        if student_grade > threshold:
            count += 1
            
    return count


def get_average_grade(classlist: list[Student]) -> float:
    '''
    this function takes a classlist and calculates the average grade
    
    >>> get_average_grade([Student('V00123456', 89), Student('V00123457', 99), Student('V00123458', 30), Student('V00123459', 78)])
    74.0
    
    >>> get_average_grade([Student('V00123456', 99), Student('V00123457', 19), Student('V00123458', 32), Student('V00123459', 79)])
    57.25
    
    >>> get_average_grade([Student('V00123456', 0), Student('V00123457', 0), Student('V00123458', 0), Student('V00123459', 0)])
    0.0
    
    '''
    total_sum = 0
    
    
    for student in classlist:
        divisor = len(classlist)
        student_grade = student.get_grade()
        total_sum += student_grade
    avg = total_sum / divisor
    
    return avg
        