print("Hello world")

# Variables store data
lucky_num = 26 #int
my_name = "Maia" #str
cash = 5.50 #float
is_raining = True
is_Sunny = False

# CONCATENATE a string literal + string variable
greeting = "Howdy, " + my_name
print(greeting)
# You can use single quotes instead
greeting = 'Python is cool, it\'s better than Java'
print(greeting)
# You can use triple double quotes for long strings
long_greeting = """
                we were both young
                when i first saw you
                i close my eyes
                """
print(long_greeting)
# f-strings are FORMATTED strings (like templates)
f_string = f"My name is {my_name} and my lucky number is {lucky_num}."
print(f_string)

def helloworld():
    print("hello world I am a function")

helloworld()

# define a func with arguments
def multiply(x, y):
    result = x * y 
    return result

# call a nonvoid func
five_times_three = multiply (5, 3)
print(five_times_three)
print(multiply(20,6))

# *** LISTS ***
empty_list = list()
another_empty_list = []

class_roster = ["Bryce", "Finny", "Jackson", "Kevin", "Maia", "Natalie", "Paige"]
print(class_roster)
print(len(class_roster))

# Indexes start at 0
first_item = class_roster[0]
print(first_item)

# Update an item in a list, access by index
class_roster[2] = "Jack"
print(class_roster)

# Sorting lists
lottery_nums = [13, 7, 89, 99, 44, 23, 4]
print(sorted(lottery_nums))
print(sorted(lottery_nums, reverse=True))
print(lottery_nums) # sorted () does not modify OG list
# Sort IN PLACE -> modifies OG list
lottery_nums.sort()
print(lottery_nums)
class_roster.sort(reverse=True)
print(class_roster)

# List operations
class_roster.append("Alex")
class_roster.insert(0, "Zoie")
class_roster.remove("Zoie")
class_roster.pop() # Should remove last item
print(class_roster)

# Check if item exists in a list
print(13 in lottery_nums)
print(26 in lottery_nums)

# ** TUPLES **
# ordered and immutable (can't change items)
# useful for "snapshot" of a row of data
student = ('Maia', 17, 'AP Stats', 4.0)
print(student)
# student[3] = 2.6

# ** SETS **
# unsorted, and stores other immutable types
# NO DUPLICATES allowed! 
songs = {'Stranger', '3005', '7', '3', 'Mutt', 'Freeze', '3005'}
print(songs)
# sets can be used to de-duplicate list items
colors = ['blue', 'pink', 'purple', 'blue', 'pink']
print(set(colors))
songs.add('Gypsy')
songs.add('Stranger') # duplicate value
print(songs)

# ** DICTIONARIES **
# mutable, but the KEYS can only be immutable types
# { key: value } pairs. Keys must be UNIQUE!
# unordered (no order, can't sort in place)
characters = { 'Aelin': 'assasin queen',
               'Karate Kid': 'pupil',
               'Phil Dunphy': 'dad',
               'Wall-E': 'trash robot',
               'Princess Peach': 'damsel in distress',
               'Dexter': 'serial killer (justified?)',
               'Lara Jean': 'letter writer'
               }
print(len(characters))
# dictionary with numerical keys, list values
grade_requirements = { 9: ['Bio', 'Math', 'English'],
                      10: ['Chem', 'Math', 'English'],
                      11: ['Physics', 'Math', 'English'],
                      12: ['Math', 'English', 'PE']
                      }