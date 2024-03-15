import random
import time

# ANSI escape codes for text formatting
class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

GAS_LEVELS = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
GAS_STATIONS = ["Shell", "Speedway", "Marathon", "Circle K", "Mobil", "Costco", "Meijer", "7Eleven"]

def get_gas_level():
    return random.choice(GAS_LEVELS)

def get_gas_station():
    return random.choice(GAS_STATIONS)

def display_warning(message, color):
    print(f"{color}{message}{Color.ENDC}")
    time.sleep(1.75)

def check_gas_level():
    gas_level = get_gas_level()
    if gas_level == "Empty":
        display_warning("*** WARNING - YOU ARE ON EMPTY ***\nCalling Triple AAA", Color.FAIL)
    elif gas_level == "Low":
        gas_station = get_gas_station()
        distance = round(random.uniform(1, 25), 1)
        display_warning(f"Your gas tank is extremely low.\nThe closest gas station ({gas_station}) is {distance} miles away.", Color.WARNING)
    elif gas_level == "Quarter Tank":
        gas_station = get_gas_station()
        distance = round(random.uniform(25.1, 50), 1)
        display_warning(f"Your gas tank is on a quarter tank.\nThe closest gas station ({gas_station}) is {distance} miles away.", Color.WARNING)
    elif gas_level == "Half Tank":
        print(f"{Color.OKGREEN}Your gas tank is half full which is plenty to get to your destination.{Color.ENDC}")
    elif gas_level == "Three Quarter Tank":
        print(f"{Color.OKBLUE}Your gas tank is three quarters full.{Color.ENDC}")
    else:
        print(f"{Color.OKGREEN}Your gas tank is full.{Color.ENDC}")

if __name__ == "__main__":
    print("***********************************")
    print("Gasoline Branch\n\n")
    check_gas_level()
