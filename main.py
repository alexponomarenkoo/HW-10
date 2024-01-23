####Task-1
# Створіть клас "Місто".
# Необхідно зберігати в полях класу: назву міста, назву регіону, назву країни, кількість жителів міста,
# поштовий індекс міста, телефонний код міста.
# Реалізуйте доступ до окремих полів (Інкапсуляція).class City:

# class City:
#     def __init__(self, name, region, country, population, postal_code, phone_code):
#         self.name = name
#         self.region = region
#         self.country = country
#         self.population = population
#         self.postal_code = postal_code
#         self.phone_code = phone_code
#
# city1 = City("Kharkiv", "Kharkiv region", "Ukraine", "1419000", "61122", "+380")
#
# print("Інформація про місто:")
# print(f"Назва: {city1.name}")
# print(f"Регіон: {city1.region}")
# print(f"Країна: {city1.country}")
# print(f"Населення: {city1.population}")
# print(f"Поштовий індекс: {city1.postal_code}")
# print(f"Телефонний код: {city1.phone_code}")

####Task-2
# Створіть клас "Країна".
# Необхідно зберігати в полях класу: назву країни, назву континенту, кількість жителів країни,
# телефонний код країни, назву столиці, назву міст країни.
# Реалізуйте доступ до окремих полів (Інкапсуляція).

# class Country:
#     def __init__(self, name, continent, population, phone_code, capital, cities):
#         self.name = name
#         self.continent = continent
#         self.population = population
#         self.phone_code = phone_code
#         self.capital = capital
#         self.cities = cities
#
# cities_of_ukraine = ("Kyiv", "Odessa", "Kharkiv", "Lviv", "Donetsk")
# ukraine = Country("Country", "Europe", "43227825", "+380", "Kyiv", cities_of_ukraine)
#
# print("Інформація про країну:")
# print(f"Назва: {ukraine.name}")
# print(f"Континент: {ukraine.continent}")
# print(f"Населення: {ukraine.population}")
# print(f"Телефонний код: {ukraine.phone_code}")
# print(f"Столиця: {ukraine.capital}")
# print(f"Міста: {', '.join(ukraine.cities)}")
