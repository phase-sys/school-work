# C. Create a program which gives the below output:
# Enter Name : Cy
name = input("Enter Name: ")

# Enter Department : IT
dep = input("Enter Department: ")

# Enter ID : 1234
id_num = int(input("Enter ID: "))

# Hello Cy! IT Department Welcomes you. Please use your student number 12345
print("Hello {0}! {1} Department Welcomes you. Please use your student number {2}".format(name, dep, id_num))