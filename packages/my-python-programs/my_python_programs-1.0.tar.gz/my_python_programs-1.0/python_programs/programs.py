import math
import re
import pprint

# 1. Swap Two Numbers
def swap_numbers():
    code = """\
# Program to Swap Two Variables
print("Program to swap two variables")
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("Before swapping A =", a, "B =", b)

# Method 1: Using a temporary variable
temp = a
a = b
b = temp

# Alternate Method: Without a temp variable
a = a + b
b = a - b
a = a - b

print("After swapping A =", a, "B =", b)
"""
    print(code)


# 2. Area of Triangle
def area_of_triangle():
    code = """\
# Program to Calculate Area of a Triangle
b = float(input("Enter the base of the triangle: "))
h = float(input("Enter the height of the triangle: "))

area = 0.5 * b * h
print("Area of the triangle =", area)
"""
    print(code)


# 3. Temperature Conversion
def fahrenheit_to_celsius():
    code = """\
# Program for Temperature Conversion (Fahrenheit to Celsius)
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) / 1.8

print(f"{fahrenheit}° Fahrenheit is equal to {celsius}° Celsius")
"""
    print(code)


# 4. Circle Properties
def circle():
    code = """\
# Program to Calculate Area and Circumference of a Circle
import math
radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print("Area =", area)
print("Circumference =", circumference)
"""
    print(code)


# 5. Leap Year Check
def leap_year_check():
    code = """\
# Program to Check Leap Year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"The year {year} is a leap year")
else:
    print("The year is not a leap year")
"""
    print(code)


# 6. Palindrome Check
def palindrome_check():
    code = """\
# Program to Check if a Number is Palindrome
num = int(input("Enter a number: "))
temp = num
reverse = 0

while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10

print("Reversed number:", reverse)

if num == reverse:
    print("The given number is a palindrome")
else:
    print("The given number is not a palindrome")
"""
    print(code)


# 7. Season Finder
def find_season():
    code = """\
# Program to Determine Season from Month Number
def check_season(month):
    if month in [2, 3]:
        return "Spring"
    elif month in [4, 5, 6]:
        return "Summer"
    elif month in [7, 8, 9, 10]:
        return "Autumn"
    elif month in [11, 12]:
        return "Winter"
    else:
        return "Invalid month"

month = int(input("Enter a month (1-12): "))
print("Season:", check_season(month))
"""
    print(code)


# 8. Star Pattern
def star_pattern():
    code = """\
# Program to Print Star Pattern
n = int(input("Enter the number of rows: "))
m = 40

for i in range(1, n + 1):
    print(" " * m + " *" * i)
    m -= 1
"""
    print(code)


# 9. Prime Number Check
def prime_number_check():
    code = """\
# Program to Check if a Number is Prime
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("The number is not prime")
            break
    else:
        print("The number is prime")
else:
    print("The number is not prime")
"""
    print(code)


# 10. List Operations
def list_operations():
    code = """\
# List Operations (Sorting, Min, Max, Sum, Median, Range)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()

print("Sorted Ages:", ages)
print("Minimum Age:", ages[0])
print("Maximum Age:", ages[-1])

sum_min_max = ages[0] + ages[-1]
print("Sum of Min & Max Ages:", sum_min_max)

median = ages[len(ages) // 2]
print("Median Age:", median)

average = sum(ages) / len(ages)
print("Average Age:", average)

age_range = ages[-1] - ages[0]
print("Age Range:", age_range)
"""
    print(code)


# 11. IT Company List Operations
def it_company_list():
    code = """\
# List Methods on IT Companies
IT_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
IT_companies.sort()
print("Sorted List:", IT_companies)

IT_companies.reverse()
print("Reversed List:", IT_companies)
"""
    print(code)


# 12. Dictionary Operations
def dictionary_operations():
    code = """\
# Dictionary Operations
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 25,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
}

print("Dictionary Length:", len(person))
print("Skills:", person['skills'])
print("Skills Data Type:", type(person['skills']))
"""
    print(code)


# 13. Dictionary Sum
def dictionary_sum():
    code = """\
# Program to Find Sum of All Items in a Dictionary
def return_sum(my_dict):
    return sum(my_dict.values())

dict_nums = {'a': 100, 'b': 200, 'c': 300}
print("Sum:", return_sum(dict_nums))
"""
    print(code)


# 14. Reverse Words in String
def reverse_words():
    code = """\
# String Reversal Program
s = input("Enter a sentence: ")

# Split, Reverse Each Word, and Join Back
words = s.split()
reversed_words = [word[::-1] for word in words]

res = " ".join(reversed_words)
print(res)
"""
    print(code)

# 15. String and Pretty Print
def string_and_pprint():
    code = """\
# Pretty Print that Counts the Occurrences of Each Letter in a String
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
"""
    print(code)


# 16. File Handling
def file_handling():
    code = """\
# File Handling Example
try:
    infile = open("input.txt", 'r')
except:
    print('Failed to open the file for reading .... Quitting')
    quit()

valid = {}
words_file = open('output.txt', 'r')

for i in words_file:
    i = i.lower().rstrip()
    valid[i] = 0
words_file.close()

misspelled = []
for i in infile:
    if i.strip().lower() not in valid and i not in misspelled:
        misspelled.append(i)

infile.close()

if len(misspelled) == 0:
    print('No words were misspelled')
else:
    print('Following words are misspelled:')
    for word in misspelled:
        print(' ', word)
"""
    print(code)


# 17. Regular Expression (Extract Year, Month, Date from URL)
def extract_date_from_url():
    code = """\
# Program to Extract Year, Month, and Date from URL using Regular Expression
import re
def extract_date(url):
    return re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url)

url1 = "https://www.washingtonpost.com/news/footballinsider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-balljosh-norman-tells-author/"
print(extract_date(url1))
"""
    print(code)


# 18. Regular Expression for Various Cases
def regex_cases():
    code = """\
# Program to Handle Various Regular Expression Cases
import re

# Case 1: Retrieve lines starting with "This"
file = open('test.txt', 'r')
text = file.readlines()
file.close()
kw = re.compile(r'^This')
for line in text:
    if kw.search(line):
        print(line)

# Case 2: Retrieve lines starting with "this" (case-insensitive)
file = open('test.txt', 'r')
text = file.readlines()
file.close()
kw = re.compile('this', re.IGNORECASE)
for line in text:
    if kw.search(line):
        print(line)

# Case 3: Retrieve lines that contain consecutive "te"
file = open('test.txt', 'r')
text = file.readlines()
file.close()
kw = re.compile(r'te')
for line in text:
    if kw.search(line):
        print(line)

# Case 4: Retrieve lines containing words starting with 's' and ending with 'e'
file = open('test.txt', 'r')
text = file.readlines()
file.close()
kw = re.compile(r'\\bs\\S*e\\b')
for line in text:
    if kw.search(line):
        print(line)

# Case 5: Retrieve lines with date format: dd.dd.dd
file = open('test.txt', 'r')
text = file.readlines()
file.close()
kw = re.compile(r'\\d\\d?\\.\\d\\d?\\.\\d\\d')
for line in text:
    if kw.search(line):
        print(line)
"""
    print(code)

