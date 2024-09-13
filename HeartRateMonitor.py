# the formula for calculating your maximum heart rate in beats per minute is (220 minus your age in years)
# Your target heart rate is 50–85% of your maximum heart rate.
# Write a script that prompts for and inputs the user’s age
# and calculates and displays the user’s maximum heart rate
# and the range of the user’s target heart rate.
"""
script: HeartRateMonitor
action: calculates maxHeart rate and range
author: Amaris Rojo
date: 08/30/2024
"""
#declare variables
maxTargetRate = 0
maxHeartRate = 0
minTargetRate = 0
#ask for patients age as an integer
age = int(input('Please enter patients age in years: '))

#calculate max heart rate (maxHeartRate)
maxHeartRate = 220 - age

#range of users target heart rate
minTargetRate = maxHeartRate * .50
maxTargetRate = maxHeartRate * .85

#display results of Max heart rate and target range
print("The patient's maximum heart rate is: ", maxHeartRate, "bpm. ")
print("The range for the patient's target heart rate is:",minTargetRate,"-",maxTargetRate,"bpm.")
 