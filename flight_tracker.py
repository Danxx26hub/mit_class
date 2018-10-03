#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 11:22:31 2018

@author: danielgalvan
"""

import requests
import progress
from bs4 import BeautifulSoup



def main():
    print_banner()
    flight_num = get_flight_number()
    html = req_data(flight_num)
    parse_data(html)
    # print(url)
    # flight_data = parse_data(html)
    display_data()


def print_banner():
    print('-' * 40)
    print('|                    Flight tracker     |')
    print('-' * 40)


def get_flight_number():
    print('please input your flight number\n')
    flight = input()
    return flight


def req_data(flight_num):
    progress.display_spinner()
    url =   'https://flightaware.com/live/flight/{}'.format(flight_num)
    response = requests.get(url)
    print(response.text)
    html = response.text
    return html


def parse_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    disp = soup.find_all('div#flightPageSummaryBlock  flightPageSummaryAirports')
    print(disp)
    


def display_data():
    pass


if __name__ == "__main__":
    main()
