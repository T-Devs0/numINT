# Some logic adapted from PhoneInfoga by sundowndev
# Source: https://github.com/FOGSEC/PhoneInfoga
# License: GPL 3.0
import pyfiglet
import datetime
import colorama 
from colorama import Fore, Style

def display():
    ascii_art = pyfiglet.figlet_format("NumINT", font="slant")
    print('\033[1;36m')
    print(ascii_art)
    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print('\033[0m')            


if __name__ == "__main__":
    display()


import argparse
import time
import json
import sys
import requests
import phonenumbers
import re
from phonenumbers import geocoder, carrier, timezone

parser = argparse.ArgumentParser(description='Phone number intelligence, gathered from open source data\nhttps://github.com/T-Devs0/numINT.git',
prog='numINT features', usage='%(prog)s --n <number to enter>, --h [display help and additional options]')

parser.add_argument('--n', metavar ='number', type=str, help='Enter number to scan/verify here')
parser.add_argument('--s', metavar = 'scan', type=str, help='Gather info from number entered')
parser.add_argument('--osint', action='store_true', help='Use OSINT to retrieve additional information')
parser.add_argument('--output', metavar ='output',help="Save info into PDF",)
args = parser.parse_args()

#Display general info upon running py file
if len(sys.argv) == 1:
   print('\033[1;36m')
   print(parser.description)
   parser.print_usage()
   print('\33[0m')
   sys.exit()

def numformat(NumInput: str) -> str:
     return re.sub((r"[^0-9]"), " ", NumInput)

def numsearch(NumInput: str):
    try:
        print("Checking if Phone Number is valid ... \n")
        time.sleep(1)
        formatted = numformat(NumInput)
        nums = phonenumbers.parse(formatted, "US")
        if phonenumbers.is_valid_number(nums):
            number = phonenumbers.format_number(nums, phonenumbers.PhoneNumberFormat.E164), phonenumbers.geocoder.description_for_number(nums, "US")
            print(f"Phone number is valid: {number}")
            return number
        else:
            print("Invalid Number")
    except phonenumbers.NumberParseException as e:
        print("Error parsing please try again", e)
        return None
    
if args.n:
    numsearch(args.n)

def numscan():
#def osintscan():

