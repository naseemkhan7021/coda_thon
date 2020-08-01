from csv import DictWriter, DictReader
import pandas as pd

def append_dict_as_row(file_name, dict_of_elem, field_names):       #to creat the .csv file
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
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


def searchrecord():
    empName = input('Enter employee name => ')
    with open('eployeeDetails.csv', 'r',) as rf:
        with open('eployeeDetails2.csv', 'a+', newline='') as wf:
            rfile = DictReader(rf)
            wfile = DictWriter(wf, fieldnames=['nEmployeeName','nEmployeeNo','nStreet','nCity','nState','nCode'])
            wfile.writeheader()
            for row in rfile:
                if empName == row['EmployeeName'] :
                    value = wfile.writerow({
                        'nEmployeeName': row['EmployeeName'],
                        'nEmployeeNo': row['EmployeeNo'],
                        'nStreet': row['Street'],
                        'nCity' : row['City'],
                        'nstate': row['State'],
                        'nCode' : row['Code']

                    })
            return value

                
# EmployeeName,EmployeeNo,Street, City,State,Code
#  empName = input('Enter employee name => ')
#     data=pd.read_csv('eployeeDetails.csv')
#     oneData =  data.iloc[0][empName]
#     if oneData:
#         return oneData
#     else:
#         return ('Data not found')