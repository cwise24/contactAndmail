#!/usr/bin/env python3

import os, json


def location(l):
    return{
        '1' : 'lv',
        '2' : 'az',
        '3' : 'nm'
    }.get(l)

def look_up(city, comp):
    with open('../Contacts/'+city+'_contacts.json') as j_file:
        payload = json.load(j_file)
        for e in payload:
            try:
                if (e['company'].upper() == comp.upper()):
                    print(e['name'], "\t"+e['email'], "\t"+e['phone'])
            except:
                print("I could not find a match")

# Search by Company
c = location(input('Enter location to search by: \r\n'+
             '\t 1 => LV \r\n'+
             '\t 2 => AZ \r\n'+
             '\t 3 => NM \r\n'))
company = input('Enter company name you want to search by: ')
look_up(c, company)
