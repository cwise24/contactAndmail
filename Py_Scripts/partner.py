#!/usr/bin/python3
 
import os, json

'''
Find partner contacts
'''

def partner_contact():
    locations = ["lv", "az", "nm"]
    cat = "PARTNER"
    for l in locations:
        with open('../Contacts/'+l+'_contacts.json') as j_file:
            payload = json.load(j_file)
            print("\r\n====================================")
            print("For "+l.upper())
            for e in payload:
                try:
                    if (e['category'].upper() == cat):
                        print(e['name'], "\t"+e['email'], "\t"+e['phone'])
                except:
                    print("I could not find a match")

partner_contact()