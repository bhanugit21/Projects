class CMS:
    def __init__(self):
        self.Name = None
        self.RollNo = None
        self.Email = None
        self.Password = None
        self.dic = {}

    def DisplayDetails(self, Rollno):
        if Rollno in self.dic.keys():
            print("Roll Number is: ", Rollno)
            print("Name is: ", self.dic[Rollno][0])
            print("Email is: ", self.dic[Rollno][1])
        else:
            print("Roll Number not found!")

    def Register(self, Name, RollNo, Email, Password):
        self.Name = Name
        self.RollNo = RollNo
        self.Email = Email
        self.Password = Password
        key = self.RollNo
        self.dic[key] = [self.Name, self.Email, self.Password]
        print("User Registered Successfully!\n")

    def Login(self, RollNo, Password):
        if (RollNo not in self.dic.keys()):
            print("User not found")
        else:
            if (Password not in self.dic[RollNo]):
                print("Password Incorrect")
            else:
                print("Login Successful")

    def logout(self):
        print("Logged Out Successfully!")


obj = CMS()
while True:
    print("\n1.REGISTER\n 2.LOGIN\n 3.DISPLAY DETAILS\n 4.LOGOUT")
    choice = int(input("\nEnter Your Choice: "))
    match choice:
        case 1:
            Name = input("Enter Name: ")
            RollNo = input("Enter Roll Number: ")
            Email = input("Enter Email: ")
            Password = input("Enter Password: ")
            obj.Register(Name, RollNo, Email, Password)

        case 2:
            RNo = input("Enter Roll Number: ")
            Passs = input("Enter Password: ")
            obj.Login(RNo, Passs)

        case 3:
            rno = input("Enter RollNo to Display Details: ")
            obj.DisplayDetails(rno)

        case 4:
            obj.logout()
            break

        case 5:
            print("Invalid Input")
            break
