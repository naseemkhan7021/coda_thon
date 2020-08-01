from controller import dataSoter, toShowallDetail,searchrecord

# All user to add employee datials


class EmpDetails:
    def __init__(self):
        self.__empName = input('Enter Employee name => ')
        self.__empNo = int(input('Enter Employee number => '))
        self.__street = input('Enter Street name =>')
        self.__city =   input('Enter City name =>  ')
        self.__state = input('Enter State name => ')
        self.__code = input('Enter Code name => ')

    def toStoreDatials(self):
        try:
            dataSoter(self.__empName, self.__empNo, self.__street,
                      self.__city, self.__state, self.__code)
            print('Data Store succefully')
        except Exception as erro:
            print('Oops!!', erro)
    
    def toShowcaruntEmp(self):
        return (f'''\t \t Name: {self.__empName},
                    EmpNumber: {self.__empNo},
                    Street: {self.__street},
                    City: {self.__city},
                    State: {self.__state},
                    Code: {self.__code}''')


# To display the emp details
class MallingList(EmpDetails):
    def __init__(self):
        super().__init__()

    def display(self):
        return toShowallDetail()

    def searchRecord(self):
        return searchrecord()

    

def main():

    x = "y"
    while(x == "y"):
        mal = MallingList()
        # eml=EmpDetails()
        mal.toStoreDatials()
        print(mal.toShowcaruntEmp())

        x = input("add another records y/n => ")

    ans = input("Show all records from table y/n => ")
    if(ans == "y"):
        print(mal.display())
    else:
        print("OK")

    ans = input("search particular employee record y/n => ")
    if(ans == "y"):
        print(mal.searchRecord())
    else:
        print("ok")
        
if __name__ == "__main__":
    main()
