# 1) Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(list):
    for x in range(len(list)):
        if list[x] > 0:
            list[x] = "big"
    return list

big_list = print(biggie_size([-2,3,-5,7,10]))

# 2) Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. 
# (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(list):
    count = 0
    for x in range(len(list)):
        if(list[x] > 0):
            count += 1
    list[len(list)-1] = count
    return list

postive_count = print(count_positives([-4,3,-2,1,25,1]))

# 3) Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(list):
    sum = 0
    for x in range(len(list)):
        sum += list[x]
    return sum

my_sum_total = print(sum_total([5,8,2,1,-4,0]))

# 4) Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5

def average(list):
    sum = 0
    for x in range(len(list)):
        sum += list[x]
    average = sum / len(list)
    return average

my_average = print(average([-2,8,0,-3]))

# 5) Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def list_length(list):
    return len(list)

my_list_length = print(list_length([2,4,6,-12,-99]))
my_list_length1 = print(list_length([]))

# 6) Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum_number(list):
    if len(list) == 0:
        return False
    min_number = list[0]
    for x in range(len(list)):
        if min_number > list[x]:
            min_number = list[x]
    return min_number

my_min_number = print(minimum_number([1,5,9,2,3,-2]))
my_min_number1 = print(minimum_number([]))

# 7) Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maximum_number(list):
    if len(list) == 0:
        return False
    max_number = list[0]
    for x in range(len(list)):
        if max_number < list[x]:
            max_number = list[x]
    return max_number

my_max_number = print(maximum_number([12,10,-13,2,0]))
my_max_number1 = print(maximum_number([]))

# 8) Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(list):
    sum_total = 0
    min_number = list[0]
    max_number = list[0]
    for x in range(len(list)):
        sum_total += list[x]
        if max_number < list[x]:
            max_number = list[x]
        elif min_number > list[x]:
            min_number = list[x]
    average = sum_total / len(list)
    return {'sumTotal': sum_total, 'average': average, 'minimum': min_number, 'maximum': max_number, 'length': len(list)}

my_ultimate_stats = print(ultimate_analysis([-1,10,3,-4,0,9]))

# 9) Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. 
# (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(list):
    list.reverse()
    return list

my_reverse_list = print(reverse_list([9,0,3,5,7,6,8]))