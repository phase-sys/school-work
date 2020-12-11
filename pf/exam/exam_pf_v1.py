# Enrollment System
# Jose Alfred M. Magat
# BSIT - 2A

# version 1

from os import system

def init_data():
    system('cls')
    """ This part initializes data """
    global subject_list
    global section_list
    global student_list
    subject_list = []
    section_list = []
    student_list = []

    try:
        f = open("subjects.txt","r")
    except FileNotFoundError:
        f = open("subjects.txt", "w")
        f.write("Math\nScience\nFilipino\nEnglish")
        f.close()
        f = open("subjects.txt","r")
    for line in f.readlines(): 
        subject_list.append(line.strip())
    f.close()
    subject_list.sort()

    try:
        f = open("sections.txt","r")
    except FileNotFoundError:
        f = open("sections.txt", "w")
        f.write("BSIT-1A\nBSIT-2A\nBSBA-1A\nBSBA-2A")
        f.close()
        f = open("sections.txt","r")
    for line in f.readlines(): 
        section_list.append(line.strip())
    f.close()
    section_list.sort()

init_data()

# Student Data

class Student():
    def __init__(self, fname, lname, section, subject, tuition):
        self.fname = fname
        self.lname = lname
        self.section = section
        self.subject = subject
        self.tuition = tuition

def add_student(): 
    global fname
    global lname
    global section
    global subject
    global tuition
    section = ""
    subject = ""

    system('cls')
    fname = input("Enter Your First Name: ")
    lname = input("Enter Your Last Name: ")
    
    count = 0
    # Only accepts subjects in the list
    while subject.title() not in subject_list:
        system('cls')
        if count >= 1:
            print("!!!!!!!!!!    Please choose from the choices only    !!!!!!!!!!".upper() + "\n")
        show_subjects()
        subject = input("\nWhich subject do you wish to enroll? ")
        count += 1

    count = 0
    # Only accepts sections in the list
    while section.upper() not in section_list:
        system('cls')
        if count >= 1:
            print("!!!!!!!!!!    Please choose from the choices only    !!!!!!!!!!".upper() + "\n")
        show_sections()
        section = input("\nWhich section do you wish to enroll? ").upper()
        count += 1
    
    system('cls')
    while 1:
        try:
            print("=" * 38 + "\nNOTE : Do not use special characters\n" + "=" * 38)
            tuition = int(input("\nEnter Tuition Fee to Pay: Php "))
            system('cls')
            break
        except ValueError:
            over_index()

def show_students():
    if not student_list:
        print("??????????    No students enrolled yet   ??????????".upper() + "\n")
    else:
        count = 1
        for a in student_list:
            print("{0}. {1}, {2}\nEnrolled in: {3}\nStudying {4} and Paid Php {5}".format(count, a.lname, a.fname, a.section, a.subject, a.tuition))
            count += 1

def del_students():
    while len(student_list) > 0:
        try:
            show_students()
            print("\n" + "=" * 30 + "\nEnter the number of the Student\nEnter [Q] to Quit\n" + "=" * 30)
            stud = input("\nDelete Student: ")
            if stud.lower() == 'q':
                system('cls')
                break
            else:
                del student_list[int(stud) - 1]
                system('cls')
        except IndexError:
            system('cls')
            print("!!!!!!!!!!    Number was not found    !!!!!!!!!!".upper() + "\n")
    else:
        system('cls')
        print("!!!!!!!!!!    No students left    !!!!!!!!!!".upper() + "\n")

def edit_students():
    while len(student_list) > 0:
        try:
            show_students()
            print("\n" + "=" * 30 + "\nEnter the Number of the Student\nEnter [Q] to Quit\n" + "=" * 30)
            stud = input("\nEdit Student: ")
            system('cls')
            if stud.lower() == 'q':
                system('cls')
                break
            else:
                choose = student_list[int(stud) - 1]
                print("{0}, {1}\nEnrolled in: {2}\nStudying {3} and Paid Php{4}".format(choose.lname, choose.fname, choose.section, choose.subject, choose.tuition))
                # separate for clearer printing
                e_input = "\nEnter [1] for First Name\nEnter [2] for Last Name\nEnter [3] for Section\nEnter [4] for Subject\nEnter [5] for Tuition\nEnter [6] to Cancel\n"
                print("\n" + "=" * 25 + e_input + "=" * 25)
                change = int(input("\nChange: "))
                system('cls')
                print("{0}, {1}\nEnrolled in: {2}\nStudying {3} and Paid Php{4}".format(choose.lname, choose.fname, choose.section, choose.subject, choose.tuition))
                if change == 1:
                    choose.fname = input("\nChange {} to: ".format(choose.fname)).title()
                elif change == 2:
                    choose.lname = input("\nChange {} to: ".format(choose.lname)).title()
                elif change == 3:
                    new_sec = ""
                    count = 0
                    while new_sec.upper() not in section_list:
                        if count >= 1:
                            print("!!!!!!!!!!    Please choose from the choices only    !!!!!!!!!!".upper() + "\n")
                        show_sections()
                        new_sec = input("\nChange {} to: ".format(choose.section))
                        count += 1
                        system('cls')
                    else:
                        choose.section = new_sec.upper()
                elif change == 4:
                    new_sub = ""
                    count = 0
                    while new_sub.title() not in subject_list:
                        if count >= 1:
                            print("!!!!!!!!!!    Please choose from the choices only    !!!!!!!!!!".upper() + "\n")
                        show_subjects()
                        new_sub = input("\nChange {} to: ".format(choose.subject))
                        count += 1
                        system('cls')
                    else:
                        choose.subject = new_sub.title()
                elif change == 5:
                    choose.tuition = int(input("\nChange Php {} to: Php ".format(choose.tuition)))
                elif change == 6:
                    break
                else:
                    raise IndexError
                system('cls')
        except IndexError:
            system('cls')
            print("!!!!!!!!!!    Number was not found    !!!!!!!!!!".upper() + "\n")

    else:
        system('cls')
        print("!!!!!!!!!!    No students left    !!!!!!!!!!".upper() + "\n")

# Subject Data

def add_subjects():
    show_subjects()
    add_sub = input("\nEnter New Subject:\n")
    f = open("subjects.txt", "a")
    f.write("\n" + add_sub.title())
    subject_list.append(add_sub.title().strip())
    f.close()

    system('cls')

def show_subjects():
    print(f"Subjects:\n")
    [print(sub, end = "\n") for sub in subject_list]

# Section Data

def add_sections():
    show_sections()
    add_sec = input("\nEnter New Section:\n")
    f = open("sections.txt", "a")
    f.write("\n" + add_sec.title())
    section_list.append(add_sec.upper().strip())
    f.close()

    system('cls')

def show_sections():
    print(f"Sections:\n")
    [print(sec, end = "\n") for sec in section_list]

# Error Handling

def error_handle():
    print("\n!!!!!!!!!!    You've entered a non-integer input    !!!!!!!!!!".upper())
    ans = ""
    # Only accepts closed ended answers
    while not (ans.lower() == "yes" or ans.lower() == "no"):
        ans = input("\nDo you want to restart? [Yes] [No] : ")
        if ans.lower() == "yes":
            system('cls')
        elif ans.lower() == "no":
            quit()
        else:
            over_index()

def over_index():
    system('cls')
    print("\n??????????    Input not recognized    ??????????\n".upper())

# start

while 1:
    try:
        while 1:
            login = int(input("=" * 22 + "\nEnter [1] for Admin\nEnter [2] for Student\nEnter [3] to Quit\n" + "=" * 22 + "\n"))
            if login == 1:
                admin_key = []
                try:
                    f = open("admin.txt","r")
                except FileNotFoundError:
                    f = open("admin.txt", "w")
                    f.write("admin\nroot")
                    f.close()
                    f = open("admin.txt","r")
                
                for line in f.readlines(): 
                    admin_key.append(line.strip())
                f.close()
                user = ""
                key_pass = ""
                count = 0
                while not (user == admin_key[0] and key_pass == admin_key[1]):
                    system('cls')
                    if count >= 1:
                        print("!!!!!!!!!!    Wrong username or password    !!!!!!!!!!".upper() + "\n")
                    user = input("Enter Username: ")
                    key_pass = input("Enter Password: ")
                    count += 1
                else:
                    system('cls')
                # ask_input was separated for clearer code
                ask_input = "\nEnter [1] for Student Data\nEnter [2] for Subjects\nEnter [3] for Sections\nEnter [4] to Show All Students Enrolled\nEnter [5] to Change Admin Credentials\nEnter [6] to Clear Screen\nEnter [7] to Return\n"
                
                # subdivisions
                ask_input1 = "\nEnter [1] to Add Student\nEnter [2] to Delete Student\nEnter [3] to Edit Student Data\nEnter [4] to Return\n"
                ask_input2 = "\nEnter [1] to Add Subjects\nEnter [2] to Show Subjects\nEnter [3] to Return\n"
                ask_input3 = "\nEnter [1] to Add Sections\nEnter [2] to Show Sections\nEnter [3] to Return\n"
                # [1] Add, [2] Delete, [3] Show, [4] Add Sub, [5] Change Credentials[6] Clear Screen, [7] Return
                while 1:
                    # 35 * '=' for separation, within is ask_input
                    try:
                        resp = int(input("=" * 40 + ask_input + "=" * 40 + "\n"))
                        # Checks for the response
                        system('cls')
                        if resp == 1:
                            new_resp = int(input("=" * 35 + ask_input1 + "=" * 35 + "\n"))
                            if new_resp == 1:
                                add_student()
                                student_list.append(Student(fname.title(), lname.title(), section.upper(), subject.title(), tuition))
                                system('cls')
                            elif new_resp == 2:
                                system('cls')
                                del_students()
                            elif new_resp == 3:
                                system('cls')
                                edit_students()
                            elif new_resp == 4:
                                system('cls')
                                continue
                            else:
                                over_index()
                        elif resp == 2:
                            new_resp = int(input("=" * 35 + ask_input2 + "=" * 35 + "\n"))
                            if new_resp == 1:
                                system('cls')
                                add_subjects()
                            elif new_resp == 2:
                                system('cls')
                                show_subjects()
                            elif new_resp == 3:
                                system('cls')
                                continue
                            else:
                                over_index()
                        elif resp == 3:
                            new_resp = int(input("=" * 35 + ask_input3 + "=" * 35 + "\n"))
                            if new_resp == 1:
                                system('cls')
                                add_sections()
                            elif new_resp == 2:
                                system('cls')
                                show_sections()
                            elif new_resp == 3:
                                system('cls')
                                continue
                            else:
                                over_index()
                        elif resp == 4:
                            system('cls')
                            show_students()
                        elif resp == 5:
                            system('cls')
                            n_user = input("Enter New Username: ")
                            n_pass = input("Enter New Password: ")
                            f = open("admin.txt", "w")
                            f.write("{0}\n{1}".format(n_user, n_pass))
                            f.close()
                            print("!!!!!!!!!!    Credentials were changed    !!!!!!!!!!".upper() + "\n")
                        elif resp == 6:
                            system('cls')
                        elif resp == 7:
                            system('cls')
                            break
                        else:
                            over_index()
                    # Error Trap
                    except ValueError:
                        error_handle()
            elif login == 2:
                system('cls')
                while 1:
                    try:
                        ask_input1 ="\nEnter [1] to Show Subjects\nEnter [2] to Show Sections\nEnter [3] to Show All Students Enrolled\n"
                        ask_input2 = "Enter [4] to Clear Screen\nEnter [5] to Return\n"
                        ask_input = ask_input1 + ask_input2
                        resp = int(input("=" * 40 + ask_input + "=" * 40 + "\n"))
                        if resp == 1:
                            system('cls')
                            show_subjects()
                        elif resp == 2:
                            system('cls')
                            show_sections()
                        elif resp == 3:
                            system('cls')
                            show_students()
                        elif resp == 4:
                            system('cls')
                        elif resp == 5:
                            system('cls')
                            break
                        else:
                            over_index()
                    except ValueError:
                        error_handle()
            elif login == 3:
                system('cls')
                quit()
            else:
                over_index()
    except ValueError:
        error_handle()
# Enrollment System
# Jose Alfred M. Magat
# BSIT - 2A