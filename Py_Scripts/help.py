#!/usr/bin/env python3
 
import os, json

def help_contact(name):
    locations = ["lv", "az", "nm"]
    for l in locations:
        with open('../Contacts/'+l+'_contacts.json') as j_file:
            payload = json.load(j_file)
            print("\r\n==========================================================")
            print("For "+l.upper())
            #print(" Name"+"\t Company"+"\t Title"+"\t Email"+"\t Phone")
            for e in payload:
                sch_name = e['name'].upper()
                try:
                    if (sch_name[:3] == name[:3].upper()):
                        print(e['name'], "\t"+e['company'], "\t"+e['title'], "\t"+e['email'], "\t"+e['phone'])
                except:
                    print("I could not find a match")

n = input("Enter at least first 3 characters of name: ")
help_contact(n)