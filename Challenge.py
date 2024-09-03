
# Challenge 1
def add_numbers(num1, num2):

    return num1 + num2

# Challenge 2
def is_even(number):
    
    return number % 2 == 0

# Challenge 3

def reverse_string(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

 #Challenge 4: Function to count vowels in a string  
def vowel_count(input_text):  
    """Returns the count of vowels in the input text."""  
    vowel_set = {'a', 'e', 'i', 'o', 'u'}  
    return sum(1 for character in input_text.lower() if character in vowel_set)  

# Challenge 5: Function to calculate factorial of a non-negative integer  
def factorial_of(n):  
    """conditional statement to catch error for negative integers."""
    if n < 0:  
        raise ValueError("Input must be a non-negative integer.")  
    result = 1  
    for number in range(1, n + 1):  
        result *= number  
    return result  

# Challenge 6: Function to apply a decorator  
def decorator_func(func):  
    """Decorator that prints a message before calling the function."""  
    def wrapper(*args, **kwargs):  
        print("Decorator Applied")  
        return func(*args, **kwargs)  
    return wrapper  

def apply_decorator(func):  
    """Applies the decorator to a given function."""  
    decorated_function = decorator_func(func)  
    return decorated_function  

# Challenge 7: Function to sort a list of tuples by age  
def sort_people_by_age(people):  
    """Sorts a list of tuples (name, age) by age in ascending order."""  
    return sorted(people, key=lambda person: person[1])  

# Challenge 8: Function to merge two dictionaries  
def combine_dictionaries(dict1, dict2):  
    """Merges two dictionaries and sums values of common keys."""  
    combined = dict1.copy()  
    for key, value in dict2.items():  
        if key in combined:  
            combined[key] += value  
        else:  
            combined[key] = value  
    return combined  

# Challenge 9: Class to represent a Car and display its information  
class Vehicle:  
    """Class representing a car."""  
    
    def __init__(self, make, model, year):   
        self.make = make  
        self.model = model  
        self.year = year  

    def display_info(self):  
        """Prints the information of the car."""  
        print(f"{self.year} {self.make} {self.model}")  

