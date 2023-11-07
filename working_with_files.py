import json
from pprint import pprint


# `with` -> Context Manager -> takes care of clean up(closing of opened files)
# safer way to handle files
with open("cities.json") as cities_file:
    cities_data = json.load(cities_file)
    # pprint(cities_data)
    
    
    # print("\n")
    # print(cities_data[0])
    # print(cities_data[2]['name'])
    
new_city = {
    "name": "New City",
    "country": "New Country",
    "population": 1000000
}  
# you can access this outside of the context manager - i didn't realize this right away 
cities_data.append(new_city)
print(cities_data)



# --- appending ---
with open("cities.json", "w") as cities_file:
    json.dump(cities_data, cities_file)
   