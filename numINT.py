# Some logic adapted from PhoneInfoga by sundowndev
# Source: https://github.com/FOGSEC/PhoneInfoga
# License: GPL 3.0
import pyfiglet
import datetime
import colorama 
from colorama import Fore, Style

def display():
    ascii_art = pyfiglet.figlet_format("NumINT", font="slant")
    print('\033[1;96m')
    print(ascii_art)
    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print('\033[0m')            

import argparse
from tqdm import tqdm
import time
import json
import sys
import requests
import phonenumbers
import re
from phonenumbers import geocoder, carrier, timezone

parser = argparse.ArgumentParser(description='Phonenumber intelligence, gathered from open source data\nhttps://github.com/T-Devs0/numINT.git',
prog='numINT features', usage='%(prog)s --n <number to enter>, --h [display help and additional options]')

parser.add_argument('--n', metavar ='number', type=str, help='Enter number to scan/verify here')
parser.add_argument('--s', action='store_true', help='Gather info from number entered')
parser.add_argument('--osint', action='store_true', help='Use OSINT to retrieve additional information')
parser.add_argument('--output', metavar ='output',help="Save info into PDF",)
args = parser.parse_args()

#Display general info upon running py file
if len(sys.argv) == 1:
   print('\033[1;96m')
   print(parser.description)
   parser.print_usage()
   print('\33[0m')
   sys.exit()

def numformat(NumInput: str) -> str:
     return re.sub((r"[^0-9]"), " ", NumInput)

def numsearch(NumInput: str):
    try:
        print('\033[1;96m')
        
        for t in tqdm(range(100), desc="Checking if phonenumber is valid..",leave=False):
            time.sleep(0.007)
       
        formatted = numformat(NumInput)
        nums = phonenumbers.parse(formatted, "US")
        if phonenumbers.is_valid_number(nums):
            number = phonenumbers.format_number(nums, phonenumbers.PhoneNumberFormat.E164), phonenumbers.geocoder.description_for_number(nums, "US")
            print(f"Phone number is valid: {number}")
            print('\033[0m')
            return number
        else:
            print("Invalid Number")
    except phonenumbers.NumberParseException as e:
        print("Error parsing please try again", e)
        return None


def numscan(Number: str):
    
    API_KEY: str = ' '
    r = requests.get('https://phoneintelligence.abstractapi.com/v1/?api_key='+ API_KEY +'&phone='+ Number)
    numinfo = json.loads(r.content)
  
    if r.content == "Unauthorized" or r.status_code != 200:
        print("Unexpected error to API call, please retry")
        return -1

    carrier_info = numinfo.get("phone_carrier", {})
    location_info = numinfo.get("phone_location", {})
    messaging_info = numinfo.get("phone_messaging", {})
    validation_info = numinfo.get("phone_validation", {})
    registration_info = numinfo.get("phone_registration", {})
    risk_info = numinfo.get("phone_risk", {})
    breach_info = numinfo.get("phone_breaches", {})

    print('\033[1;96m')
    for t in tqdm(range(100), desc="Running scan..", leave=False):
        time.sleep(0.007)

    print(f"status code: {r.status_code}")
    print("Phone carrier:", carrier_info.get("name", "N/A"))
    print("Line type:", carrier_info.get("line_type", "N/A"))
    print("Phone location, region:", location_info.get("city", "N/A"))
    print("Phone location, city:", location_info.get("region", "N/A"))
    print("Timezone:", location_info.get("timezone", "N/A"))
    print("Messaging info, sms email:", messaging_info.get("sms_email", "N/A"))
    print("Phone validation, status:", validation_info.get("line_status", "N/A"))
    print("Voip?:", validation_info.get("is_voip", "N/A"))
    print("Minimum age:", validation_info.get("minimum_age", "N/A"))
    print("Phone registration, name:", registration_info.get("name", "N/A"))
    print("Phone registration, type:", registration_info.get("type", "N/A"))
    print("Phone risk:", risk_info.get("risk_level", "N/A"))
    print("Is disposable?:", risk_info.get("is_disposable", "N/A"))
    print("Phone breaches:", breach_info.get("total_breaches", "N/A"))
    print("Date first breached:", breach_info.get("date_first_breached", "N/A"))
    print("Date last breached", breach_info.get("date_last_breached", "N/A"))
    print("Breached domains:", breach_info.get("domain", "N/A"))
    print("Breach domain date:", breach_info.get("breach_date", "N/A"))
    print('\033[0m')


if args.n:
    numsearch(args.n)

if args.s == True:
    numscan(args.n)

#def osintscan():
