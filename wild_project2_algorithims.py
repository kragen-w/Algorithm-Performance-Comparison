from time import time
from random import randint

"""
    This program creates three fucntions that all use different algorithms to find if a list contains both a negative and positive
    version of the same integer. Alg 1 checks every integer against every ineger to find this, and this is very slow. Alg 2 uses a 
    binary search algorithm, and it is much faster. Alg 3 uses another algorithm, which is 10 times faster than Alg 2. Then, the program 
    outputs how long each function takes to completly search a list with increasing input sizes, and displays the data to the console.
    Filename: wild_project2_algorithims.py
    Author: Kragen Wild
    Date: 4-18-23
    Course: Programming II
    Assignment: Project 2 - Algorithm Analysis
    Collaborators: nada
    Internet Source: nada
"""


def alg1(list)->bool:
    """
        this function tries to find a negative match to an existing number in the input list by iterating through
        every value in the list, and checking the entire list for a negative match. Its complexity is O(n^2).
        perameters: list: list[int]
        return: bool
        """
    for i in range(len(list)):
        current_element = list[i]
        for j in range(len(list)):
            possible_match = list[j]
            if possible_match == current_element * -1:
                return True
    return False

def alg2(list)->bool:
    """
        this function tries to find a negative match to an existing number in the input list by iterating through the list
        and finding the middle value of that list. If the middle is higher than the target number's negaive match, then the code repaeats
        but only for the first half of the code, and the same thing happenens with the last half if the middle is smaller.
        This contunues until the number is found, or until the area of the list the code looks at closes.
        perameters: list: list[int]
        return: bool
        """
    for i in range(len(list)):
        target = list[i] * -1
        start_index = 0
        end_index = len(list) - 1
        while True:
            if start_index  > end_index:
                return False
            else:
                middle = (start_index  + end_index)//2
                if target < list[middle]:
                    end_index = middle-1
                elif target > list[middle]:
                    start_index = middle+1
                elif target == list[middle]:
                    return True

def alg3(list)->bool:
    """
        this function tries to find a negative match to an existing number in the input list by keeping track of two variables,
        one for the beginning index of the list and one for the ending index. If the some of the list values at these indexes 
        are 0, then a match is found, if the sum is less than 0, the begining variable moves up one indes, and if the sum is
        more than 0, the ending variable moves back one index. The code returns false if the beginning and end index are the same
        perameters: list: list[int]
        return: bool
        """
    i = 0
    j = len(list)-1
    while True:
        if list[i] + list[j] == 0:
            return True
        elif list[i] + list[j] < 0:
            i += 1
        elif list[i] + list[j] > 0:
            j -= 1
        if i == j:
            return False

def get_random_list(n)->list:
    """
        this function creates a random list of integers that allows for the "worst case scenario," which is if there is no
        negative matches in the list. This is done by only assinging positive integers to the list. Then, the list is sorted.
        perameters: n: int
        return: list[int]
        """
    l = []
    for i in range(n):
        l.append(randint(1,100))
        l.sort()
    return l

#each one of these code chunks follow the same structure, so I will only explain one.

#the toops of each column are printed
print(f"n\t\telapsed_time\t\t\truntime\t\tAlgorithm 1")
#the number of trials are set
num_trial = 1
#n will take on these in a loop
for n in (5000, 10000, 20000, 40000, 80000):
    #a random list is created with n integers in it
    l = get_random_list(n)
    #the timer is started
    start = time()
    #for however many trials there are...
    for j in range(num_trial):
        #the algorithm is ran
        (alg1(l))
    #the time is stopped
    stop = time()
    #the times are printed
    print(f"{n}\t\t{stop - start}\t\t{(stop - start)/num_trial}")


print(f"n\t\telapsed_time\t\t\truntime\t\tAlgorithm 2")
num_trial = 120
for n in (5000, 10000, 20000, 40000, 80000):
    l = get_random_list(n)
    start = time()
    for j in range(num_trial):
        (alg2(l))
    stop = time()
    print(f"{n}\t\t{stop - start}\t\t{(stop - start)/num_trial}")


print(f"n\t\telapsed_time\t\t\truntime\t\tAlgorithm 3")
num_trial = 1000
for n in (5000, 10000, 20000, 40000, 80000):
    l = get_random_list(n)
    start = time()
    for j in range(num_trial):
        (alg3(l))
    stop = time()
    print(f"{n}\t\t{stop - start}\t\t{(stop - start)/num_trial}")



    


