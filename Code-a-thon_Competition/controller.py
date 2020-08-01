from csv import DictWriter, DictReader
import pandas as pd
import os

# adding the data in csv file
def append_dict_as_row(file_name, dict_of_elem, field_names):       #to creat the .csv file
    # chacke for the file pracent or not 
    file_ext = os.path.isfile(file_name)
    
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        if file_ext == False:
            dict_writer.writeheader()
        
        # Add dictionary as wor in the csv
        dict_writer.writerow(dict_of_elem)



def dataSoter(name,number,street,city,state,code):
    field_names=['EmployeeName','EmployeeNo','Street',
                        'City','State','Code'
                    ]

    # dict for store the data
    dic1={'EmployeeName':   name,
            'EmployeeNo':   number,
            'Street':       street,
            'City':         city,
            'State':        state,
            'Code':         code
            }

    return append_dict_as_row('eployeeDetails.csv',dic1,field_names)

# To show the all eployees 

def toShowallDetail():
    data=pd.read_csv('eployeeDetails.csv')
    return data

'''
This way is long
def searchrecord():
    empName = input('Enter employee no => ')
    with open('eployeeDetails.csv', 'r',) as rf:
        rfile = DictReader(rf)
        for row in rfile:
            if int(empName) == int(row['EmployeeNo']):
                value = {
                    'nEmployeeName': row['EmployeeName'],
                    'nEmployeeNo': row['EmployeeNo'],
                    'nStreet': row['Street'],
                    'nCity' : row['City'],
                    'nState': row['State'],
                    'nCode': row['Code']
                }
        return value
 '''
# using pandas   (sort fuction)
def searchrecord():
    data=pd.read_csv('eployeeDetails.csv')
    data = data.set_index('EmployeeNo')
    empName = int(input('Enter employee no => '))
    return data.loc[empName]
