from datetime import datetime

def calculate_age(birth_year):
    current_year = datetime.now().year
    return current_year - birth_year

year = int(input("أدخل سنة ميلادك: "))
age = calculate_age(year)
print(f"عمرك هو: {age} سنة")
