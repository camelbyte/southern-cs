import re
import pydoc as pydoc
path = 'data/city_states.txt'


cs_dict = {}


with open(path, "r") as file:

    for line in file:

        city_states = line.strip().split(", ")
        city, state = city_states
        cs_dict[city] = state

print(city_states)

pydoc.writedoc('city_states')

