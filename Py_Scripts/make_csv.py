#!/usr/bin/env python3

import csv, json

'''
Make CSV Python Program for entire Desert Region
All account types (N/T) and All categories (customer/partner)
'''

def csv_file(email_list):
    with open('../email.csv', 'w') as myfile:
        wr = csv.writer(myfile, dialect='excel')
        wr.writerow(email_list)
    
def m_csv():
    locations = ["lv", "az", "nm"]
    e_csv = open('../email.csv', 'w+')
    countr = 0
    for l in locations:
        with open('../Contacts/'+l+'_contacts.json') as j_file:
            payload = json.load(j_file)
            myfile = csv.writer(e_csv)
            for e in payload:
                if countr == 0:
                    header = ['name', 'fname', 'email', 'company', 'title', 'data1', 'data2', 'phone', 'category', 'type']
                    myfile.writerow(header)
                    countr+=1
                if len(e['email']) >1 and countr != 0:
                    first = e['name'].split(" ")
                    row = [e['name'], first[0], e['email'], e['company'], e['title'], e['data1'], e['data2'], e['phone'], e['category'], e['type']]
                    myfile.writerow(row)
                
m_csv()
