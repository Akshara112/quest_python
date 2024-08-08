
branch_dict = {
    1:'ECE',
    2:'BCOM',
    3:'MECH'
}
try:
    #input for branch
    branch_number = int(input("Enter the branch (1: ECE, 2: BCOM, 3: MECH): "))
    branch_name = branch_dict[branch_number]

    #input for preferences
    preferences_input = input("Input preferences separated by ',' (1: Maths, 2: English, 3: Arts) : ")
    #convert input string to a list of integers
    preferences = [int(preference) for preference in preferences_input.split(',')]

    #input for marks
    marks_input = input("Enter marks for Maths, English, Arts separated by ',' : ")
    #convert input string to a list of integers
    marks = [int(mark) for mark in marks_input.split(',')]
    #assign marks to 3 different variables
    maths, literature, art  = marks                  

except:
    print("Enter a valid input")

#check pass condition all marks are above pass mark35
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