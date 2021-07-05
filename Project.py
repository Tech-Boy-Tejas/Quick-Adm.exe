from time import sleep, strftime 
from datetime import date

import json

schools_dict = {'School_A':{'I':{},'II':{},'III':{},'IV':{},'V':{},'VI':{},'VII':{},'VIII':{},'IX':{},'X':{}},
                "School_B":{"I":{},"II":{},"III":{},"IV":{},"V":{},"VI":{},"VII":{},"VIII":{},"IX":{},"X":{}},
                "School_C":{"I":{},"II":{},"III":{},"IV":{},"V":{},"VI":{},"VII":{},"VIII":{},"IX":{},"X":{}},
                "School_D":{"I":{},"II":{},"III":{},"IV":{},"V":{},"VI":{},"VII":{},"VIII":{},"IX":{},"X":{}},
                "School_E":{"I":{},"II":{},"III":{},"IV":{},"V":{},"VI":{},"VII":{},"VIII":{},"IX":{},"X":{}},
                "School_F":{"I":{},"II":{},"III":{},"IV":{},"V":{},"VI":{},"VII":{},"VIII":{},"IX":{},"X":{}},
                "School_G":{"I":{},"II":{},"III":{},"IV":{},"V":{},"VI":{},"VII":{},"VIII":{},"IX":{},"X":{}},
                "School_H":{"I":{},"II":{},"III":{},"IV":{},"V":{},"VI":{},"VII":{},"VIII":{},"IX":{},"X":{}},
                "School_I":{"I":{},"II":{},"III":{},"IV":{},"V":{},"VI":{},"VII":{},"VIII":{},"IX":{},"X":{}},
                "School_J":{"I":{},"II":{},"III":{},"IV":{},"V":{},"VI":{},"VII":{},"VIII":{},"IX":{},"X":{}}
                }

for roll_num in range(1,11):
    for alphabet in range(ord('A'),ord('J') + 1):
        roll_num = str(roll_num)
        schools_dict['School_' + str(chr(alphabet))]['I'][roll_num] = 'open'
        schools_dict['School_' + str(chr(alphabet))]['II'][roll_num] = 'open'
        schools_dict['School_' + str(chr(alphabet))]['III'][roll_num] = 'open'
        schools_dict['School_' + str(chr(alphabet))]['IV'][roll_num] = 'open'
        schools_dict['School_' + str(chr(alphabet))]['V'][roll_num] = 'open'
        schools_dict['School_' + str(chr(alphabet))]['VI'][roll_num] = 'open'
        schools_dict['School_' + str(chr(alphabet))]['VII'][roll_num] = 'open'
        schools_dict['School_' + str(chr(alphabet))]['VIII'][roll_num] = 'open'
        schools_dict['School_' + str(chr(alphabet))]['IX'][roll_num] = 'open'
        schools_dict['School_' + str(chr(alphabet))]['X'][roll_num] = 'open'



current_date = int(date.today().strftime("%d"))

if current_date % 5 == 0:
    offer = True

#defining functions for different sectors of the program
def info_for_adm_sector(name,school_name,school_class):
    # INFORMATIONS SECTOR
    print("Hello " + name + " Welcome to the Informations Sector")
    print("")
    print("Connecting to School " +  school_name + "'s Real time Database")
    sleep(2)
    print("Fetching Empty Slots in Class " + school_class)
    sleep(2)

    school_info = schools_dict["School_" + school_name][school_class]
    print("The vacant seats for SCHOOL " + school_name + " in CLASS " + school_class + " is ",end=" ")

    
    
    for i in school_info:
       if school_info[i] == 'open':
           print(i,end=", ")
    print('\n')
    if offer:
        print("We also have an ongoing offer which will give parents 50% discounts on admissions today")
    else:
        pass

    continue_Program = input("Enter \"Yes\" if you wish to continue with the program and \"No\" if you don't: ").lower()

    if continue_Program == "yes" or continue_Program == "Yes" or continue_Program == "yEs" or continue_Program == "yeS" or continue_Program == "YeS":
        welcome_User(name)
    elif continue_Program == "no":
        print("Thank You for Using Admission Partner.exe management System, Bye " + name)
        return

    else:
        print("Please try again")
        sleep(2.5)
        welcome_User(name)


def adm_sector(name): 
    # ADMISSIONS SECTOR
    print("Hello " + name + " Welcome to the Admission Sector")
    print("")
    print("Please enter name, phone number, age ,password, school name ,class number and roll number like")
    admission_details = input("\"adm Tejas 1234567890 13 coronawin A IX 3 \"\n : ").split()

    user_school = admission_details[-3]
    user_class = admission_details[-2]
    user_roll = admission_details[-1]
    user_roll_num = int(user_roll)

    if offer:
        print("There is an offer for 50% discount today")
    else:
        pass

    if(user_roll_num >= 1 and user_roll_num <= 10):
        schools_dict_val = schools_dict["School_" + user_school][user_class][user_roll]
    else:
        print("Roll number entered is out of range, Sorry " + name)
        return
    if user_school < chr(65) or user_school > chr(74):
        print("School entered does not exist in the database, Sorry " + name)
        return

    if schools_dict_val == 'open':
        schools_dict["School_" + user_school][user_class][user_roll] = "booked"
        print("The Slot is available")
        print("Connecting to School " + user_school + "'s database server")

        if offer:
            print("Applying offers today for 50% discount")
            sleep(1.5)
        else:
            pass

        sleep(2)
        print("Booking the slot for you, " + name)
        sleep(2)
        print("The slot has been succesfully booked, Thank you ")
    else:
        print("The slot is already booked,Sorry " + name)

    continue_Program = input("Enter \"Yes\" if you wish to continue with the program and \"No\" if you don't: ").lower()

    if continue_Program == "yes":
        welcome_User(name)
    elif continue_Program == "no":
        print("Thank You for Using Admission Partner.exe management System, Bye " + name)
        return

 
def leave_sector(name):
    # TRANSFER OR LEAVE SECTOR
    print("Hello" + name + " Welcome to the Transfer Sector")
    print("")
    print("Please enter leave followed by your password,School name, class and roll number if you want to leave a school like") 

    leaving_details = input("\"leave secureshield A IX 3\"\n : ").split()
    user_school = leaving_details[-3]
    user_class = leaving_details[-2]
    user_roll = leaving_details[-1]
    user_roll_num = int(user_roll)

    if(user_roll_num >= 1 and user_roll_num <= 10):
        schools_dict_val = schools_dict["School_" + user_school][user_class][user_roll]
    else:
        print("Roll number entered is out of range, Sorry " + name)
        return
    if user_school < chr(65) or user_school > chr(74):
        print("School entered does not exist in the database, Sorry " + name)
        return 

    if schools_dict_val == "booked":
        schools_dict["School_" + user_school][user_class][user_roll] = "open"
        print("The slot is getting Emptied, Please Wait!! ")
        sleep(2.5)
        print("You have succesfully left School " + user_school + ", Thank You ")
    else:
        print("Invalid Details Entered")

    continue_Program = input("Enter \"Yes\" if you wish to continue with the program and \"No\" if you don't: ").lower()

    if continue_Program == "yes":
        welcome_User(name)
    elif continue_Program == "no":
        print("Thank You for Using Admission Partner.exe management System, Bye " + name)
        return




def welcome_User(name=""):
    # Welcoming the user to the Program
    if name != "":
        pass
    else:
        print("Welcome to Admission_Partner.exe, your admission partner")
        print("Here we help students to gain hassle-free admission in top schools of our city")
        name = input("Hey there buddy please enter your name so we can be friends: ")
        print("Processing.....")
        sleep(3.5)
    
    print(name + " please enter \"Vac_adm school_name class\" like Vac_adm C I if you are interested in finding vacant slots")
    sleep(1)
    print(name + " please enter \"adm\" if you are interested in admissions")
    sleep(1)
    print(name + " please enter \"leave\" if you are interested in leaving a school")

    user_interest_sector = input().split()
    user_interest_sector[0] =  user_interest_sector[0].lower()

    print(user_interest_sector[0])

    if user_interest_sector[0] == "vac_adm":
        info_for_adm_sector(name,user_interest_sector[1],user_interest_sector[2])
    elif user_interest_sector[0] == "adm":
        adm_sector(name)
    elif user_interest_sector[0] == "leave":
        leave_sector(name)
    else:
        print("Invalid Information entered ,Pls try again")

#calling functions to start the program
welcome_User()

#creating a custom dictionary contaning all the schools, classes and slots
with open('schools.txt','w') as file:
    file.write(json.dumps(schools_dict))

