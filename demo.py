

def list():
    courses = ['history', 'maths', 'compsec']
    courses.insert(0,'arts')
    print(courses)
    courses2 = ['medicine', 'science']
    courses.extend(courses2)
    print(courses)
    courses.remove('history')
    print(courses)
    poped = courses.pop()
    print(courses)
    print(poped)
    courses.reverse()
    print(courses)
    courses.sort()
    print(courses)
    for index, course in enumerate(courses):
        print(index,course)
    count_str = '-'.join(courses)
    print(count_str)
    count_str = ','.join(courses)
    print(count_str)
    new_list = count_str.split('-')
    print(new_list)


def sets():
    courses = {'history', 'maths', 'compsec', 'physics', 'maths'}
    print(courses)
    print('maths' in courses)
    cs1_courses = {'history', 'maths', 'compsec', 'physics'}
    cs_courses = {'history', 'compsec', 'art', 'design'}
    print(cs1_courses.intersection(cs_courses))
    print(cs1_courses.difference(cs_courses))
    print(cs1_courses.union(cs_courses))

def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
def is_leap(year):
    return year % 4 ==0 and (year % 100 !=0 or year % 400 ==0)

def list_comp():
    nums = [1,2,4,5,6,3,7,8,9]
    mylist = [n for n in nums]
    print(mylist)
    mylist1 = [n*n for n in nums]
    print(mylist1)
    mylist2 = [n for n in nums if n % 2 == 0]
    print(mylist2)
    mylist3 = [(letter , num) for letter in 'abcd' for num in range(4)]
    print(mylist3)

def dict_comp():
    names = ['bruce', 'clark', 'peter', 'logan', 'wade']
    heros = ['batman', 'superman', 'spiderman', 'wolvoreine', 'deadpool']
    my_dict = {name: hero for name, hero in zip(names, heros) if name != 'peter'}
    print(my_dict)

def set_comp():
    nums = [1,1,2,2,3,3,3,4,5,6,6,5,4,6,7,4,4,4,6,5,4,7,7,4,0,3,]
    my_set = {n for n in nums}
    print(my_set)

def days_in_month(year,month):
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if not 1 <= month <= 12:
        return 'invalid match'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

def pattern_prog():
    for x in range(3, 6):
        for z in range(5, x, -1):
            print(" ", end="")
        for y in range(x):
            print(y+1, end=" ")
        print()
    for x in range(4, 2, -1):
        for z in range(x, 5):
            print(" ",end="")
        for y in range(x):
            print(y+1,end=" ")
        print()

list()
sets()
student_info()
print(is_leap(2019))
print(days_in_month(2017, 2))
list_comp()
dict_comp()
set_comp()
