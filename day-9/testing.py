travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


# for item in travel_log:
#     # print(item) = {'country': 'France', 'visits': 12, 'cities': ['Paris', 'Lille', 'Dijon']}
#     # print(item['country'] ) = France


def add_new_country(country, add_visit, add_cities):
    print()




#🚨 Do not change the code below
def add_new_country(country_value, visits_value, cities_value):
    new_country = {"country": country_value, "visits": visits_value, "cities": cities_value}
    travel_log.append(new_country)



print(travel_log)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



