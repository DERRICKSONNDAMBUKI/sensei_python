import random

country = input('Enter your country: ')
city = input('Enter your city: ')

country = country[:2]
random = random.randint(1, 100)
print(country, ',', city, random)
