planets = ["Mercury",
           "Venus",
           "Earth",
           "Mars",
           "Jupyter",
           "Saturn",
           "Uranus",
           "Neptune"]
"""
planets[2] = "India"

print(planets)
"""

# lists are mutable like pen drive (Ayush's analogy)

# keep round bracket instead of square bracket

# tuples are like read only CDs
planets = ("Mercury",
           "Venus",
           "Earth",
           "Mars",
           "Jupyter",
           "Saturn",
           "Uranus",
           "Neptune")
print(planets)
print(type(planets))

print(planets[2])
# planets[2] = "India"

print(planets[0:4])

for idx, planet in enumerate(planets):
    print(f'Planet {idx + 1} is: {planet}')

# planets.append('Pluto')
# planets.pop()
# planets.remove('Earth')
