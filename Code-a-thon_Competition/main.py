from controller import dataSoter, toShowallDetail,searchrecord

# All user to add employee datials


class EmpDetails:
    def __init__(self,name,number,street,city,state,code):
        self.__empName = name
        self.__empNo = number
        self.__street = street
        self.__city = city
        self.__state = state
        self.__code = code

    def toStoreDatials(self):
        try:
            dataSoter(self.__empName, self.__empNo, self.__street,
                      self.__city, self.__state, self.__code)
            print('Data Store succefully')
        except Exception as erro:
            print('Oops!!', erro)


# To display the emp details
class MallingList(EmpDetails):
    def __init(self,name,number,street,city,state,code):
        super().__init__(name,number,street,city,state,code)
    def toShowcaruntEmp(self):
        return (f'''Name: {self._EmpDetails__empName},
                    EmpNumber: {self._EmpDetails__empNo},
                    Street: {self._EmpDetails__street},
                    City: {self._EmpDetails__city},
                    State: {self._EmpDetails__state},
                    Code: {self._EmpDetails__code}''')

    def display(self):
        return toShowallDetail()

    def searchRecord(self):
        return searchrecord()

    

def main():
    empName = input('Enter Employee name => ')
    empNo = int(input('Enter Employee number => '))
    street = input('Enter Street name =>')
    city = input('Enter City name =>  ')
    state = input('Enter State name => ')
    code = input('Enter Code name => ')
    mal = MallingList(empName,empNo,street,city,state,code)
    x = "y"
    while(x == "y"):
        eml=EmpDetails(empName,empNo,street,city,state,code)
        eml.toStoreDatials()
        print(mal.toShowcaruntEmp())

        x = input("add another records y/n")

    ans = input("Show all records from table y/n")
    if(ans == "y"):
        print(mal.display())
    else:
        print("OK")

    ans = input("search particular employee record y/n")
    if(ans == "y"):
        print(mal.searchRecord())
    else:
        print("ok")


    # ans = input("delete  particular employee record y/n")
    # if(ans == "y"):
    #     empno = int(input("enter empno to be deleted"))
    #     e1.deleterecord(empno)
    # else:
    #     print("ok")
    # ans = input("update particular employee record y/n")
    # if(ans == "y"):
    #     empno = int(input("enter empno to be update"))
    #     new_desig = input("enter new designation")
    #     e1.updaterecord(empno, new_desig)
    # else:
    #     print("ok")
    # del e1


if __name__ == "__main__":
    main()
