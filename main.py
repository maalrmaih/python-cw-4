def my_name():
    name = input('what are your nam')
    print(f"my nsme is {name}")

my_name()

def my_meal():  
    food = input('what u like to eat')
    drink = input('what u like to drink')
    print(f"i like to eat {food} and i like drinking {drink}")

my_meal()
def cube(number):
    return number**3
cube(6)

def by_three(number):
    if number % 3 == 0:
      return cube(number)
        
    else:
        False
by_three(12)