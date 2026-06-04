# List
cities=["Hyderabad","Mumbai","Delhi"]
print(cities[0])
print(cities[1])
print(cities[2])

# Negative Indexing
print(cities[-1])
print(cities[-2])

# Update an Element
cities[1]="Bangalore"
print(cities)

# Append
cities.append("Chennai")
print(cities)

# Insert
cities.insert(1,"Pune")
print(cities)

# Multiple Values
cities.extend(["Kochi","Pondi"])
print(cities)

# Remove
cities.remove("Bangalore")
print(cities)

# Pop
cities.pop(1)
print(cities)

# Delete
del cities[0]
print(cities)

# Length
print(len(cities))

# Check Membership
print("Mumbai" in cities)
print("Pune" in cities)

# Index
print(cities.index("Delhi"))

# Sort
cities.sort()
print(cities)

# Clear
cities.clear()
print(cities)
