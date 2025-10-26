# Some logic adapted from PhoneInfoga by sundowndev
# Source: https://github.com/sundowndev/phoneinfoga
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
import phonenumbers
import requests
import phonenumbers
from phonenumbers import geocoder, carrier

parser = argparse.ArgumentParser(description='Phone number intelligence, powered by open source data\nhttps://github.com/T-Devs0/numINT.git', prog='numINT features', usage='%(prog)s -n <number>')
parser.add_argument('--n', metavar ='number', type=str, help='Enter number to scan here')
args = parser.parse_args()

if len(sys.argv) == 1:
    print('\033[36m')
    print(parser.description)
    parser.print_usage()
    print('\033[0m')

#  function for number scan to call API here 
#  def num_scan():


