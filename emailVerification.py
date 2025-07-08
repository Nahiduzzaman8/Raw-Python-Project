while(True):
    email = input("Enter your Email or Enter 'Q' for cancel: ").rstrip()
    k = 0
    if email == "Q":
        print("Thank you for your participations")
        break
    if len(email) >= 6:
        if email[0].isalpha():
            if email.count('@') == 1:
                if (email[-4] == '.') ^ (email[-3] == '.'):
                    for i in email: 
                        if i.isalpha():
                            if i == i.upper():
                                k = 1
                        elif i.isspace():
                            k = 1
                        elif i != "_" and i != "." and i != "@":
                            k = 1
                    if k == 1: 
                        print("Wrong BOOM!!")
                    else: 
                        print("Your email is correct")
                else:
                    print(". issue")
            else: 
                print("@ issue")
        else: 
            print("first letter is not alphabate")
    else: 
        print("lenght is too short")
