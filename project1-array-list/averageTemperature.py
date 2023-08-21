# This script calculates the average temperature of a series of of user inputs
# and then determines how many of these days were above the average temperature

# Written by JAM
# 19-08-2023

# User inputs: n for number days on which to average
#              n subsequent temperature values (values with the same units)

# Import libraries
import logging
import array

# Logging settings
logging.basicConfig(filename='averageTemperature.log',
                    format='%(asctime)s-%(levelname)s-%(message)s',
                    encoding='utf-8',
                    level=logging.INFO)

# Script
def main():

    # Logging
    logging.info(f"Starting averageTemperature...")

    # Input for the number of days to average over
    days = 0
    days = int(input("How many day's was the temperature measured? "))

    logging.info(f"Parsing number of days to average over...")

    # Take an input for each day with a temperature value
    i = 0
    temperature = array.array('i',[])
    while i <= days - 1:

        x = int(input(f"Temperature value for day {i + 1}: "))
        temperature.append(x)
        i += 1

    # logging
    logging.info(f" {days} temperature values captured...")

    # Average temperature
    averageTemperature = float(sum(temperature) / days)
    print(f"The average temperature from the user inputs is " \
        f"{averageTemperature}")
    logging.info(f"The average temperature from the user inputs is " \
                f"{averageTemperature}")

    # Number of days above average temperature
    daysAboveAverage = [i for i in temperature if i > averageTemperature]
    print(f"There were {len(daysAboveAverage)} days above the average " \
        f"temperature of {averageTemperature}")
    logging.info(f"There were {len(daysAboveAverage)} days above the " \
                f"average temperature of {averageTemperature}")

# Script execution
if __name__ == "__main__":
    main()