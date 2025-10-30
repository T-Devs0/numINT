# Some logic adapted from PhoneInfoga by sundowndev
# Source: https://github.com/FOGSEC/PhoneInfoga
# License: GPL 3.0
import pyfiglet
import datetime
import colorama 
from colorama import Fore, Style

def display():
    ascii_art = pyfiglet.figlet_format("NumINT", font="slant")
    print('\033[36m')
    print(ascii_art)
    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print('\033[0m')            


if __name__ == "__main__":
    display()


import argparse
import json
import sys
import requests
import phonenumbers
import re
from phonenumbers import geocoder, carrier, timezone

parser = argparse.ArgumentParser(description='Phone number intelligence, gathered from open source data\nhttps://github.com/T-Devs0/numINT.git',
prog='numINT features', usage='%(prog)s --n <number to enter>, --h [display help and additional options]')

parser.add_argument('--n', metavar ='number', type=str, help='Enter number to scan here')
parser.add_argument('--s', metavar = 'numscan', type=str, help='Scanning function for number entered')
parser.add_argument('--osint', action='store_true', help='Use OSINT to retrieve additional information')
parser.add_argument('--output', )
args = parser.parse_args()

#Display general info upon running py file
if len(sys.argv) == 1:
   print('\033[36m')
   print(parser.description)
   parser.print_usage()
   print('\33[0m')
   sys.exit()


number: str = " "

def numformat(NumInput: str) -> str:
     return re.sub((r"[^0-9]"), " ", NumInput)


def numscan(NumInput: str):
    try:
        formatted = numformat(NumInput)
        nums = phonenumbers.parse(formatted, "US")
        if phonenumbers.is_valid_number(nums):
            number = phonenumbers.format_number(nums, phonenumbers.PhoneNumberFormat.E164)
            print(f"Phone number is valid: {number}")
            return number
        else:
            print("Invalid Phone number")
            return None
    except phonenumbers.NumberParseException as e:
        print("Error parsing number:", e)
        return None
    
if args.n:
    numscan(args.n)

#def websearch():
#def osintscan():
