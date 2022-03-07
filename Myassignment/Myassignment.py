#To enter your choice
def choice():
    print(
          "1.Register "
          "2.login "
           "3.forgot password")
    choice = int(input("Enter your choice "))
    if choice == 1:
       valid_email_password()
    elif choice == 2:
        return login()
    elif choice==3:
        return getpassword()
#to sign up
def register(email,password):

    useremail = email
    userpassword =password
    f = open("User_Data.txt",'r')
    info = f.read()
    if useremail in info:
        return "Email Unavailable. Please Try Again"
    f.close()
    f = open("User_Data.txt",'w')
    info = info + " " +useremail + " " + userpassword
    f.write(info)
    print("Succesfully registered")
#to check whether entered email and password is valid
def valid_email_password():
    email=input("Enter an email: ")
    c=0
    counter=0
    sc=('!','#','$','%','&',"'",'*','+','-','/','=','?','^','_','`','{','|','}','~','@')
    if email.startswith(sc) or email.endswith(sc) or email[0].isdigit():
        c+=1
    if c==0:
        for i in email:
            if i=="@":
                counter+=1
        if counter!=1:
            c+=1
    if c==0:
        atind=email.index("@")
        if email[atind+1]==".":
            c+=1
    if c==0:
        if email.endswith(".com") or email.endswith(".in"):
            print("valid email")
        else:
            c+=1
    if c!=0:
        print("Enter a valid email")
        valid_email_password()
    if c==0:
        password=input("Enter password: ")
        up=lo=spc=nu=p=0
        if len(password)>5 and len(password)<16:
            for i in password:
                if i in sc:
                    spc+=1

                if i.isupper():
                    up+=1

                if i.islower():
                    lo+=1

                if i.isnumeric():
                    nu+=1
            if spc>=1 and up>=1 and lo>=1 and nu>=1:
                p=1
                print("valid password")
            else:
                print("password must have special character lower case upper case and a number")
        else:
            print("password length must be between 5 and 16 characters")
        if c==0 and p==1:
            register(email,password)
        else:
            valid_email_password()
#to help user log in
def login():
    email= input("Enter your email: ")
    password = input("Password: ")
    f = open("User_Data.txt",'r')
    info = f.read()
    info = info.split()
    if email in info:
        index = info.index(email) + 1
        usr_password = info[index]
        if usr_password == password:
            return "Welcome Back, " + email
        else:
            return "Password entered is wrong"
    else:
        return "Name not found. Please Sign Up."
#to help uer find the password if forgotten
def getpassword():

    email = str(input("Enter your email: "))

    f = open("User_Data.txt",'r')
    info = f.read()
    info = info.split()
    if email in info:
        index = info.index(email) + 1
        user_password = info[index]
        return "Your password is:"+ user_password

    else:
        return "Email id not present"

print(choice())

