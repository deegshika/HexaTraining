# Set
cities={"Hyderabad","Mumbai","Delhi"}
print(cities)

# Duplicate Values Not Allowed
cities={"Hyderabad","Mumbai","Delhi","Mumbai"}
print(cities)

# # Remove Duplicates from List
# cities=["Hyderabad","Mumbai","Mumbai","Delhi"]
# unique_cities=set(cities)
# print(unique_cities)

# Add
cities.add("Chennai")
print(cities)

# Update Multiple Values
cities.update(["Delhi","Pune"])
print(cities)

# Remove
cities.remove("Mumbai")
print(cities)

# Discard
cities.discard("Pune")
print(cities)

set1 = {"Python", "SQL"}
set2 = {"MongoDB", "Python"}

result = set1.union(set2)
print(result)

result = set1.intersection(set2)
print(result)

result = set1.difference (set2)
print(result)

result = set1.symmetric_difference (set2) #Non-Common Values
print(result)
