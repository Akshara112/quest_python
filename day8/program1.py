'''i = "MATHS, ART"
print(type(i))
listMarks = i.split(',')
print(type(listMarks))
print(len(listMarks))'''

# try:
#input branch: 1   #only 1
#input pref : 1,2,3  #1 or more
#input marks: 97,96,97   #exact 3
# except:
    #please provide valid inputs

#use dictionary to convert console number input to actual text

# occupation=='3'

# branch loop
    # pref loop
        #applicant should be pass in all subject
            # if #Marketing (ECE): Art>90 + Literature>90, pass in all subject (maths > 35)
            # elif Accounts (BCOM): Maths>95, pass in all subject (English and Arts > 35)
            # elif Sales (MECH): Maths>90 + Literature>90, pass in all subject (Art > 35)
            # else : no openings for provided creiteria


branch_dict = {
    1:'ECE',
    2:'BCOM',
    3:'MECH'
}
try:
    branch_number = int(input("Enter the branch (1: ECE, 2: BCOM, 3: MECH): "))
    branch_name = branch_dict[branch_number]

    preferences_input = input("Input preferences separated by ',' (1: Maths, 2: English, 3: Arts) : ")
    preferences = [int(preference) for preference in preferences_input.split(',')]

    marks_input = input("Enter marks for Maths, English, Arts separated by ',' : ")
    marks = [int(mark) for mark in marks_input.split(',')]
    maths, literature, art  = marks

except:
    print("Enter a valid input")


pass_mark = (art > 35 and literature > 35 and maths > 35)
if pass_mark:
    for pref in preferences:
        if branch_name == 'ECE':
            if art > 90 and literature > 90:
                print(f"Eligible for Marketing.")
            else:
                print(f"Not eligible for Marketing.")
        
        elif branch_name == 'BCOM':
            if maths > 95:
                print(f"Eligible for Accounts.")
            else:
                print(f"Not eligible for accounts.")
        
        elif branch_name == 'MECH':
            if maths > 90 and literature > 90:
                print(f"Eligible for Sales.")
            else:
                print(f"Not eligible for Sales.")
        
        else:
            print("Not satisfied the eligibility criteria.")