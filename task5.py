#

#A population can be modeled by the following:
#future population = (current population)*(1+r)^(time in years) 
#Have the user enter the current population, the rate of growth as a decimal and the number of DAYS.
#Calculate the expected future population

#Enter the population: 25000000
#Enter the rate of growth in percent: 2.1
#Enter the number of days: 12
#There will be 25017087 people after 12 days

currentpopulation = input("Enter the population: ")
r = input("Enter the rate of growth in percent: ")
day = input("Enter the number of days: ")

import math

futurepopulation = (currentpopulation)*(1+r)^(day)

print(f"There will be {futurepopulation} people after {day} days.")