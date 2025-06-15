import datetime

# Get birthdays from user input
my_bday_str = input("Enter your birthday (YYYY-MM-DD): ")
other_bday_str = input("Enter the other person's birthday (YYYY-MM-DD): ")

# Parse the input strings into date objects
my_bday = datetime.datetime.strptime(my_bday_str, "%Y-%m-%d").date()
other_bday = datetime.datetime.strptime(other_bday_str, "%Y-%m-%d").date()

# Compute current date
today = datetime.date.today()

# Helper function to compute age

def calculate_age(birthdate):
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age

my_age = calculate_age(my_bday)
other_age = calculate_age(other_bday)

print(f"Your current age: {my_age}")
print(f"Other person's current age: {other_age}")
print(f"Age difference: {abs(my_age - other_age)}")
