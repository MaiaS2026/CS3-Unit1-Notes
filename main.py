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