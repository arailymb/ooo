#task_1
def get_keys_with_value_true(input_dict):
    return [key for key, value in input_dict.items() if value is True]

input_dict = {"a": True, "b": False, "c": True}
output = get_keys_with_value_true(input_dict)
print(output)

#task_2
def get_unique_elements(input_list):
    return [element for element in input_list if input_list.count(element) <= 1]

input_list = [1, 2, 3, 1, 2, 4]
output = get_unique_elements(input_list)
print(output)

#task_3
from datetime import datetime

def get_date_in_format(input_date):
    date_object = datetime.strptime(input_date, '%Y.%m.%d')
    
    formatted_date = date_object.strftime('%d.%m.%Y')
    
    return formatted_date

input_date = "2023.10.23"
output = get_date_in_format(input_date)
print(output)

#task_4
def get_elements_with_no_more_than_two_occurrences(input_list):
    return [element for element in set(input_list) if input_list.count(element) <= 2]

input_list = [1, 2, 3, 1, 2, 4]
output = get_elements_with_no_more_than_two_occurrences(input_list)
print(output)

#task_5
def get_words_from_string(input_string):
    words_list = input_string.split()
    return words_list

input_string = "This is a string with several words."
output = get_words_from_string(input_string)
print(output)

#task_6 
def get_unique_elements_with_count(input_list):
    count_dict = {}
    
    for element in input_list:
        count_dict[element] = count_dict.get(element, 0) + 1
    
    return count_dict

input_list = [1, 2, 3, 1, 2, 4, 1, 2]
output = get_unique_elements_with_count(input_list)
print(output)

#task_7
def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers

n = 100
output = get_prime_numbers(n)
print(output)

#task_8
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_prime_numbers_in_list(input_list):
    return [num for num in input_list if is_prime(num)]

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 27, 36, 48, 54, 67, 71, 73, 75, 83, 89, 99]
output = get_prime_numbers_in_list(input_list)
print(output)

#task_9
from datetime import datetime

def get_difference_between_dates(date1, date2):
    date1_obj = datetime.strptime(date1, "%Y.%m.%d")
    date2_obj = datetime.strptime(date2, "%Y.%m.%d")
    
    difference = (date2_obj - date1_obj).days
    
    return difference

date1 = "2023.10.23"
date2 = "2023.10.24"
output = get_difference_between_dates(date1, date2)
print(output)

#task_10
def get_decimal_number_from_binary_string(binary_string):
    decimal_number = int(binary_string, 2)
    return decimal_number

binary_string = "10110011"
output = get_decimal_number_from_binary_string(binary_string)
print(output)

#task_11
def get_perfect_squares(numbers):
    return [num for num in numbers if (num**0.5).is_integer()]

numbers = [4, 25, 81]
output = get_perfect_squares(numbers)
print(output)

#task_12
def get_price(shopping_list):
    return shopping_list.get('price')

shopping_list = [
    {"name": "Apple", "price": 100},
    {"name": "Banana", "price": 50},
    {"name": "Orange", "price": 20}
]

shopping_list.sort(key=get_price)
print(shopping_list, end='\n\n')

#task_13
def get_words_starting_with_vowel(words):
    vowels = set("aeiouAEIOU")
    return [word for word in words if word[0] in vowels]

word_list = ["apple", "banana", "orange", "bear", "cat"]
output = get_words_starting_with_vowel(word_list)
print(output)

