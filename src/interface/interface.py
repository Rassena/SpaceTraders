import matplotlib.pyplot as plt

data = [{'systemSymbol': 'X1-ZA40', 'symbol': 'X1-ZA40-15970B', 'type': 'PLANET', 'x': 10, 'y': 0,
         'orbitals': [{'symbol': 'X1-ZA40-69371X'}, {'symbol': 'X1-ZA40-97262C'}, {'symbol': 'X1-ZA40-11513D'}],
         'traits': [{'symbol': 'OVERCROWDED', 'name': 'Overcrowded',
                     'description': 'A waypoint teeming with inhabitants, leading to cramped living conditions and a high demand for resources.'},
                    {'symbol': 'HIGH_TECH', 'name': 'High-Tech',
                     'description': 'A center of innovation and cutting-edge technology, driving progress and attracting skilled individuals from around the galaxy.'},
                    {'symbol': 'BUREAUCRATIC', 'name': 'Bureaucratic',
                     'description': 'A waypoint governed by complex regulations, red tape, and layers of administration, often leading to inefficiencies and frustration.'},
                    {'symbol': 'TEMPERATE', 'name': 'Temperate',
                     'description': 'A world with a mild climate and balanced ecosystem, providing a comfortable environment for a variety of life forms and supporting diverse industries.'},
                    {'symbol': 'MARKETPLACE', 'name': 'Marketplace',
                     'description': 'A thriving center of commerce where traders from across the galaxy gather to buy, sell, and exchange goods.'}],
         'chart': {'submittedBy': 'COSMIC', 'submittedOn': '2023-05-13T17:48:46.579Z'},
         'faction': {'symbol': 'COSMIC'}},
        {'systemSymbol': 'X1-ZA40', 'symbol': 'X1-ZA40-69371X', 'type': 'MOON', 'x': 10, 'y': 0, 'orbitals': [],
         'traits': [{'symbol': 'BARREN', 'name': 'Barren',
                     'description': 'A desolate world with little to no vegetation or water, presenting unique challenges for habitation and resource extraction.'},
                    {'symbol': 'TRADING_HUB', 'name': 'Trading Hub',
                     'description': "A critical junction in the galaxy's trade network, with countless goods and services flowing through daily."},
                    {'symbol': 'MARKETPLACE', 'name': 'Marketplace',
                     'description': 'A thriving center of commerce where traders from across the galaxy gather to buy, sell, and exchange goods.'}],
         'chart': {'submittedBy': 'COSMIC', 'submittedOn': '2023-05-13T17:48:46.632Z'},
         'faction': {'symbol': 'COSMIC'}},
        {'systemSymbol': 'X1-ZA40', 'symbol': 'X1-ZA40-97262C', 'type': 'MOON', 'x': 10, 'y': 0, 'orbitals': [],
         'traits': [{'symbol': 'VOLCANIC', 'name': 'Volcanic',
                     'description': 'A volatile world marked by intense volcanic activity, creating a hazardous environment with the potential for valuable resource extraction, such as rare metals and geothermal energy.'},
                    {'symbol': 'TRADING_HUB', 'name': 'Trading Hub',
                     'description': "A critical junction in the galaxy's trade network, with countless goods and services flowing through daily."},
                    {'symbol': 'MARKETPLACE', 'name': 'Marketplace',
                     'description': 'A thriving center of commerce where traders from across the galaxy gather to buy, sell, and exchange goods.'}],
         'chart': {'submittedBy': 'COSMIC', 'submittedOn': '2023-05-13T17:48:46.653Z'},
         'faction': {'symbol': 'COSMIC'}},
        {'systemSymbol': 'X1-ZA40', 'symbol': 'X1-ZA40-11513D', 'type': 'MOON', 'x': 10, 'y': 0, 'orbitals': [],
         'traits': [{'symbol': 'FROZEN', 'name': 'Frozen',
                     'description': 'An ice-covered world with frigid temperatures, providing unique research opportunities and resources such as ice water, ammonia ice, and other frozen compounds.'},
                    {'symbol': 'TRADING_HUB', 'name': 'Trading Hub',
                     'description': "A critical junction in the galaxy's trade network, with countless goods and services flowing through daily."},
                    {'symbol': 'MARKETPLACE', 'name': 'Marketplace',
                     'description': 'A thriving center of commerce where traders from across the galaxy gather to buy, sell, and exchange goods.'}],
         'chart': {'submittedBy': 'COSMIC', 'submittedOn': '2023-05-13T17:48:46.671Z'},
         'faction': {'symbol': 'COSMIC'}},
        {'systemSymbol': 'X1-ZA40', 'symbol': 'X1-ZA40-34964E', 'type': 'PLANET', 'x': 5, 'y': 0, 'orbitals': [],
         'traits': [{'symbol': 'TOXIC_ATMOSPHERE', 'name': 'Toxic Atmosphere',
                     'description': 'A waypoint with a poisonous atmosphere, necessitating the use of specialized equipment and technology to protect inhabitants and visitors from harmful substances.'},
                    {'symbol': 'VOLCANIC', 'name': 'Volcanic',
                     'description': 'A volatile world marked by intense volcanic activity, creating a hazardous environment with the potential for valuable resource extraction, such as rare metals and geothermal energy.'},
                    {'symbol': 'WEAK_GRAVITY', 'name': 'Weak Gravity',
                     'description': 'A waypoint with a low gravitational pull, providing unique opportunities for research and industry while also challenging the adaptation of life forms and technology.'}],
         'chart': {'submittedBy': 'COSMIC', 'submittedOn': '2023-05-13T17:48:46.689Z'},
         'faction': {'symbol': 'COSMIC'}},
        {'systemSymbol': 'X1-ZA40', 'symbol': 'X1-ZA40-99095A', 'type': 'ASTEROID_FIELD', 'x': -9, 'y': 29,
         'orbitals': [], 'traits': [{'symbol': 'MINERAL_DEPOSITS', 'name': 'Mineral Deposits',
                                     'description': 'Abundant mineral resources, attracting mining operations and providing valuable materials such as iron ore, copper ore, aluminum ore, and quartz sand for various industries.'},
                                    {'symbol': 'COMMON_METAL_DEPOSITS', 'name': 'Common Metal Deposits',
                                     'description': 'A waypoint rich in common metals like iron, copper, and aluminum, as well as their ores, essential for construction and manufacturing.'},
                                    {'symbol': 'PRECIOUS_METAL_DEPOSITS', 'name': 'Precious Metal Deposits',
                                     'description': 'A source of valuable metals like gold, silver, and platinum, as well as their ores, prized for their rarity, beauty, and various applications.'},
                                    {'symbol': 'STRIPPED', 'name': 'Stripped',
                                     'description': 'A waypoint that has been heavily exploited for its resources, leaving a scarred and depleted landscape with diminished opportunities for future development.'},
                                    {'symbol': 'MARKETPLACE', 'name': 'Marketplace',
                                     'description': 'A thriving center of commerce where traders from across the galaxy gather to buy, sell, and exchange goods.'}],
         'chart': {'submittedBy': 'COSMIC', 'submittedOn': '2023-05-13T17:48:46.701Z'},
         'faction': {'symbol': 'COSMIC'}},
        {'systemSymbol': 'X1-ZA40', 'symbol': 'X1-ZA40-23636D', 'type': 'GAS_GIANT', 'x': -44, 'y': -22,
         'orbitals': [{'symbol': 'X1-ZA40-68707C'}], 'traits': [{'symbol': 'VIBRANT_AURORAS', 'name': 'Vibrant Auroras',
                                                                 'description': "A celestial light show caused by the interaction of charged particles with the waypoint's atmosphere, creating a mesmerizing spectacle and attracting tourists from across the galaxy."},
                                                                {'symbol': 'STRONG_MAGNETOSPHERE',
                                                                 'name': 'Strong Magnetosphere',
                                                                 'description': 'A waypoint enveloped in a powerful magnetic field, potentially affecting spacecraft systems, and creating unique phenomena such as the concentration of exotic matter and graviton emitters.'}],
         'chart': {'submittedBy': 'COSMIC', 'submittedOn': '2023-05-13T17:48:46.719Z'},
         'faction': {'symbol': 'COSMIC'}},
        {'systemSymbol': 'X1-ZA40', 'symbol': 'X1-ZA40-68707C', 'type': 'ORBITAL_STATION', 'x': -44, 'y': -22,
         'orbitals': [], 'traits': [{'symbol': 'MILITARY_BASE', 'name': 'Military Base',
                                     'description': 'A fortified stronghold housing armed forces, advanced weaponry, and strategic assets for defense or offense.'},
                                    {'symbol': 'TRADING_HUB', 'name': 'Trading Hub',
                                     'description': "A critical junction in the galaxy's trade network, with countless goods and services flowing through daily."},
                                    {'symbol': 'MARKETPLACE', 'name': 'Marketplace',
                                     'description': 'A thriving center of commerce where traders from across the galaxy gather to buy, sell, and exchange goods.'},
                                    {'symbol': 'SHIPYARD', 'name': 'Shipyard',
                                     'description': 'A bustling hub for the construction, repair, and sale of various spacecraft, from humble shuttles to mighty warships.'}],
         'chart': {'submittedBy': 'COSMIC', 'submittedOn': '2023-05-13T17:48:46.733Z'},
         'faction': {'symbol': 'COSMIC'}},
        {'systemSymbol': 'X1-ZA40', 'symbol': 'X1-ZA40-41138D', 'type': 'PLANET', 'x': 0, 'y': 70, 'orbitals': [],
         'traits': [{'symbol': 'DRY_SEABEDS', 'name': 'Dry Seabeds',
                     'description': 'Vast, desolate landscapes that once held oceans, now exposing the remnants of ancient marine life and providing opportunities for the discovery of valuable resources.'},
                    {'symbol': 'TRADING_HUB', 'name': 'Trading Hub',
                     'description': "A critical junction in the galaxy's trade network, with countless goods and services flowing through daily."},
                    {'symbol': 'WEAK_GRAVITY', 'name': 'Weak Gravity',
                     'description': 'A waypoint with a low gravitational pull, providing unique opportunities for research and industry while also challenging the adaptation of life forms and technology.'},
                    {'symbol': 'MARKETPLACE', 'name': 'Marketplace',
                     'description': 'A thriving center of commerce where traders from across the galaxy gather to buy, sell, and exchange goods.'}],
         'chart': {'submittedBy': 'COSMIC', 'submittedOn': '2023-05-13T17:48:46.764Z'},
         'faction': {'symbol': 'COSMIC'}},
        {'systemSymbol': 'X1-ZA40', 'symbol': 'X1-ZA40-28549E', 'type': 'JUMP_GATE', 'x': 2, 'y': 75, 'orbitals': [],
         'traits': [], 'chart': {'submittedBy': 'COSMIC', 'submittedOn': '2023-05-13T17:48:46.782Z'},
         'faction': {'symbol': 'COSMIC'}}]

# Extract x and y coordinates from the data
x_values = [item['x'] for item in data]
y_values = [item['y'] for item in data]

# Plot the data points
plt.scatter(x_values, y_values)

# Add labels to the data points
for i in range(len(data)):
    plt.annotate(data[i]['symbol'], (x_values[i], y_values[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Set the axes labels
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')

# Set the plot title
plt.title('Data on X-Y Coordinates')

# Display the plot
plt.show()





