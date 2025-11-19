#Name :Yash Vishwari
#Enrollment No:0176EC231037
#Batch :6 (MTF) 
#Batch time: 12:10pm - 1:50pm 

logged_user = ''
logged = False
names ={}
branchs ={}
enrollment_no ={}
academic_year ={}
semester ={}
phone_no ={}
usernames =[]
passwords ={}
mail_id={}
scholar_no={}
class_rollno={}
class_sections ={}
def register():
  print("---REGISTRATION---")
  name=  input("Please Enter Your name :")
  mno= input("Please enter your Mobile Number :")
  mail = input("Please Enter your mail-id :")
  enrno =input("Enter Your Enrollment no :")
  sno = input("Enter Your Scholar no :") 
  branch =input("Enter Your Branch :")
  year = input("Enter your Academic year :")
  sem = input("Enter your current Academic semester :")
  crno =input("Enter your class roll number :")
  sec =input("Enter your class section :")
  uname = input("Enter a username :")
  usernames.append(uname)
  pswd = input("Enter Your Password :")
  passwords[uname] =pswd
  phone_no[uname] =mno
  names[uname]= name
  branchs[uname] =branch
  semester[uname] =sem
  academic_year[uname] =year
  enrollment_no[uname] =enrno
  scholar_no[uname] =sno
  mail_id[uname] =mail
  class_rollno[uname] =crno
  class_sections[uname]=sec
  print("Registration Successfull")


def login():
    user = input("Please enter Username :")
    pswd = input("Please enter Password :")
    if user not in usernames:
        print("Invalid Username !")
        return
    if pswd not in passwords.values():
        print("Invalid Password !")
        return
    global logged_user
    global logged
    logged_user=user
    logged = True
    print("Login Successfull")
    

def show_profile():
    if logged == False:
        print("Please Login First")
        return
    print("--------Student Profile--------")
    print(f"Name :{names[logged_user]}")
    print(f"Branch :{branchs[logged_user]} \t Year :{academic_year[logged_user]} \t Semester :{semester[logged_user]} ")
    print(f"Enrollment no :{enrollment_no[logged_user]} \t Scholar no :{scholar_no[logged_user]}")
    print(f"Class roll no :{class_rollno[logged_user]} \t Section :{class_sections[logged_user]}")
    print(f"Mobile Number :{phone_no[logged_user]} \t Mail-id :{mail_id[logged_user]}")
   
    
def update_profile():
    if logged == False:
        print("Please Login First")
        return

    response = input('''
        What do you want to update:
        1. Name
        2. Academic year
        3. Academic Semester
        4. Phone Number
        5. Mail id
        6. Class roll_no
        7. Class section

            select option 1/2/3/4/5/6/7: ''')
    
    if response == '1':
        names[logged_user] =input("Enter updated name :")
    elif response == '2':
        academic_year[logged_user] =input("Enter academic year :")
    elif response == '3':
        semester[logged_user] =input("Enter academic semester :")
    elif response == '4':
        phone_no[logged_user] =input("Enter updated phone number :")
    elif response == '5':
        mail_id[logged_user] =input("Enter updated mail id:")
    elif response == '6':
       class_rollno[logged_user] =input("Enter Class roll no :")
    elif response == '7':
       class_sections[logged_user] =input("Enter Class section:")
    else:
        print("Invalid Choice, Please select correct option")
        

   


def logout():
    global logged_user
    global logged
    if logged== False:
        print("Please Login First")
        return
    logged = False
    logged_user=''
    print("Logout Successfull")


def terminate():
    print("Thankyou for visiting!!")
    exit()

def main():
    print()
    print()
    print("Welcome in LNCT")
    response = input('''
        Choose option:
        1. Registration
        2. Login
        3. Profile
        4. Update profile
        5. Logout
        6. Main Menu
        7. Exit

            select option 1/2/3/4/5/6/7: ''')

    if response == '1':
        register()
    elif response == '2':
        login()
    elif response == '3':
        show_profile()
    elif response == '4':
        update_profile()
    elif response == '5':
        logout()
    elif response == '6':
        main()
    elif response == '7':
        terminate()
    else:
        print("Invalid Choice, Please select correct option")
    main()   

        

main()