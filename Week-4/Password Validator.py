def pass_valid(password):

    if 6 <= len(password) <= 10:
        numbers = 0
        for i in password:
            i = ord(i)
            if 48 <= i <= 57 or 65 <= i <= 122:

                if 48 <= i <= 57:
                    numbers +=1
                elif 65 <= i <= 122:
                   continue


            else:
                 print("Password must consist only of letters and digits")
                 break
        if numbers >= 2:
            
            print("Password is valid")

        else:
            print("Password must have at least 2 digits")
    else:
        print("Password must be between 6 and 10 characters")
        numbers = 0
        for i in password:
            i = ord(i)
            if 48 <= i <= 57 or 65 <= i <= 122:

                if 48 <= i <= 57:
                    numbers += 1
                elif 65 <= i <= 122:
                    continue
            else:
                 print("Password must consist only of letters and digits")
        if numbers < 2:
            print("Password must have at least 2 digits")







password = input()
pass_valid(password)