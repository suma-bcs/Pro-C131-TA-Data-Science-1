# -*- coding: utf-8 -*-
"""Pro C131 TA Data Science 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mAKSSGfNvgrAqSNskENJbIPtH-Gx4M9d

# Exploring Solar Systems with Statistics

In today's class, we will plot a few graphs and apply statistics to the data we have! We will also try to find some interesting insights about different solar systems.

\
Before we do that, let us recall the fields that are left in the CSV -

*   ***name*** - name of the planet
*   ***light_years_from_earth*** - Distance of the exo-planet from earth in light years
*   ***planet_mass*** - Mass of the planet
*   ***stellar_magnitude*** - This is the brightness of the host star of the planet when observed from Earth (just as the sun is our host star)
*   ***discovery_date*** - This is the year of discovery for the exo-planet
*   ***planet_type*** - This is the type of the planet (Gas Giant, Super Earth, etc.)
*   ***planet_radius*** - This is the radius of the exo-planet with respect to Earth or Jupiter.
*   ***orbital_radius*** - This is the average distance of this exo-planet from its sun. Just like our solar system has 1 sun, there are multiple solar systems that contain many planets and sun(s)
*   ***orbital_period*** - This is the time it takes to complete one orbit of it’s sun
*   ***eccentricity*** - This denotes how circular the orbit is. It might be oval in shape too. The lower the eccentricity, the more circular is the orbit
*   ***solar_system_name*** - The name of the host solar system
*   ***planet_discovery_method*** - This is the discovery method which was used to find this exo-planet
*   ***planet_orbital_inclination*** - This is the orbital inclination, which means that it is the tilt of the exo-planet’s orbit when it revolves around its sun
*   ***planet_density*** - This is the density of the planet
*   ***right_ascension*** - This is the right ascension of the planetary system, which is the east-west coordinate by which the position of this planet is measured
*   ***declination*** - This is the north-south coordinate by which the position of the planet is measured
*   ***host_temperature*** - This is the temperature of the host star in Kelvin
*   ***host_mass*** - This is the amount of mass contained in the host star
*   ***host_radius*** - This is the radius of the host star

\
Great! Now since we already know that we have 8 planets in our solar system, let's see if we can find out if there are any similar solar systems like us in the universe by seeing how many planets are there in the other solar systems.

\
For this, we have a column known as ***solar_system_name*** in our CSV. Using this, we can create a dictionary to maintain the count of planets each solar system has!

\
Before we write any code for this, let's just upload the CSV to our Colab first!
"""

from google.colab import files
uploaded = files.upload()

"""Now let's just write the code to read the CSV"""

import csv

rows = []

with open("main.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

headers = rows[0]
planet_data_rows = rows[1:]
print(headers)
print(planet_data_rows[0])

"""Here, we can see that there is an extra field added into the CSV, denoting the row count but the first header is an empty string. Let's fix that and then proceed with finding the number of planets in each of the solar system!"""

headers[0] = "row_num"

solar_system_planet_count = {}
for planet_data in planet_data_rows:
  if solar_system_planet_count.get(planet_data[11]):
    solar_system_planet_count[planet_data[11]] += 1
  else:
    solar_system_planet_count[planet_data[11]] = 1

max_solar_system = max(solar_system_planet_count, key=solar_system_planet_count.get)
print("Solar system {} has maximum planets {} out of all the solar systems we have discovered so far!".format(max_solar_system, solar_system_planet_count[max_solar_system]))

"""Great! Solar system **HD 10180** has **6** planets! Could this be our next home? Let's create a list of all the planets in this solar system so we can take a deeper look at it!"""

temp_planet_data_rows = list(planet_data_rows)
for planet_data in temp_planet_data_rows:
  planet_mass = planet_data[3]
  if planet_mass.lower() == "unknown":
    planet_data_rows.remove(planet_data)
    continue
  else:
    planet_mass_value = planet_mass.split(" ")[0]
    planet_mass_ref = planet_mass.split(" ")[1]
    if planet_mass_ref == "Jupiters":
      planet_mass_value = float(planet_mass_value) * 317.8
    planet_data[3] = planet_mass_value

  planet_radius = planet_data[7]
  if planet_radius.lower() == "unknown":
    planet_data_rows.remove(planet_data)
    continue
  else:
    planet_radius_value = planet_radius.split(" ")[0]
    planet_radius_ref = planet_radius.split(" ")[2]
    if planet_radius_ref == "Jupiter":
      planet_radius_value = float(planet_radius_value) * 11.2
    planet_data[7] = planet_radius_value

print(len(planet_data_rows))

hd_10180_planets = []
for planet_data in planet_data_rows:
  if max_solar_system == planet_data[11]:
    hd_10180_planets.append(planet_data)

print(len(hd_10180_planets))
print(hd_10180_planets)

"""Great, now let's plot a bar chart on the planet_mass column with these 6 planet data -"""

import plotly.express as px

hd_10180_planet_masses = []
hd_10180_planet_names = []
for planet_data in hd_10180_planets:
  hd_10180_planet_masses.append(planet_data[3])
  hd_10180_planet_names.append(planet_data[1])

hd_10180_planet_masses.append(1)
hd_10180_planet_names.append("Earth")

fig = px.bar(x=hd_10180_planet_names, y=hd_10180_planet_masses)
fig.show()

"""Now before we proceed, let's learn a fun fact -

Great Scientist Albert Einstein gave us a formula with which we can calculate the gravity of any planet.
The formula is this -

![Screenshot 2020-10-06 at 05.32.49.png](data:image/png;base64,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)

Here, G is a gravitational constant, which means that it will always be the same.

M(earth) is the mass of Earth (or any other planet if we are calculating it for another planet)

d is the radius of the planet!

Here, we can see an inverse relation between the the radius of the planet and the gravity. The more the radius (and bigger the planet), the lesser would be Gravity.

But then, we also see a direct relation between The mass of the planet and the gravity. The more the mass of the planet, the more will be the gravity.

Our **Earth’s gravity is 9.8 m/s**, and we as humans are accustomed to it.

In order for us to exist on any other planet, the gravity should be close to what we have here.

**Mars** has a gravity of **3.711 m/s** and **Moon** has a gravity of **1.62 m/s**.

Given what we have just learnt, let’s try to plot a scatter plot for all the planets, where we will keep the mass of the planet as the Y-Coordinate, The Radius of the Planet as X-Coordinate, and the size of the blob as the gravity of it. Let’s see if we can find anything interesting!

**The Value of G (Gravitational Constant) is *6.674e-11***

**Mass of Earth = 5.972e+24**

**Radius of Earth = 6371000**

Note - Since we have the planet_mass and planet_radius with Reference to Earth, don’t forget to multiple the mass of the earth and the radius of the earth with these values -
"""

temp_planet_data_rows = list(planet_data_rows)
for planet_data in temp_planet_data_rows:
  if planet_data[1].lower() == "hd 100546 b":
    planet_data_rows.remove(planet_data)

planet_masses = []
planet_radiuses = []
planet_names = []
for planet_data in planet_data_rows:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])
  planet_names.append(planet_data[1])
planet_gravity = []
for index, name in enumerate(planet_names):
  gravity = (float(planet_masses[index])*5.972e+24) / (float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*6371000) * 6.674e-11
  planet_gravity.append(gravity)

fig = px.scatter(x=planet_radiuses, y=planet_masses, size=planet_gravity, hover_data=[planet_names])
fig.show()

"""**Fun Fact - Our standing human bodies can withstand a gravitational force 90 times stronger than earth!**

Although that is going to be a bit extreme, we can still survive at 10 times the gravity we have at Earth. Let’s list down all the names of the planets that have Gravity of 100 or less!

"""

low_gravity_planets = []
for index, gravity in enumerate(planet_gravity):
  if gravity < 10:
    low_gravity_planets.append(planet_data_rows[index])

print(len(low_gravity_planets))

