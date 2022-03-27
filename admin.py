# file for admin
def register() :
    username = input('Username : ')
    if username.isdigit() :
        print('Error pls write character')
        register()
    elif username == '' :
        print('Pls enter character')
        register()
    else :
        pass
    import re   
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
    email = input('Email : ')
    if(re.search(regex,email)):   
        pass  
    else:   
        print('Invalid Email, pls try again')   
        register() 
    for line in open("admin.txt","r").readlines(): 
        login_info = line.split(':') 
        if email in login_info :
            print('this email is found pls enter anther mail')
            register()
        else :
            pass
    if email == "" :
        print('pls entre your email !!')
        register()
    else :
        pass
    import getpass
    password = getpass.getpass('Entre your password : ')
    if len(password) < 6 :
        print('password is too short')
        register()
    elif len(password) > 15 :
        print('Password is too long, pls enter more than 15 character')
    else :
        pass
    import getpass
    confirm_password = getpass.getpass('Confirm Password : ')
    if confirm_password != password :
        print('Not conform password, restart')
        register()
    else :
        pass
    phone =input('phone : ')
    if phone == "" :
        print('pls entre your phone !!')
        register()
    elif not phone.isdigit() :
        print('dont entre Letters, pls entre your number restart !!')
        register()
    else :
        pass
    salary = (input('Salary : '))
    if salary == '' :
        print('Error pls enter your salary')
        register()
    elif not salary.isdigit() :
        print('Error pls enter number')
        register() 
    else :
        pass
    age = input('Age : ')
    if age == '' :
        print('Error pls enter your age')
        register()
    elif not age.isdigit() :
        print('Error pls enter number')
        register() 
    else :
        pass
    positions = input('Position : ')
    if positions.isdigit() :
        print('Error pls write character')
        register()
    elif positions == '' :
        print('Pls enter character')
        register()
    else :
        pass
    technology = input('Technology : ')
    if technology.isdigit() :
        print('Error pls write character')
        register()
    elif technology == '' :
        print('Pls enter character')
        register()
    else :
        pass
    management_type = input('Management : ')
    if management_type.isdigit() :
        print('Error pls write character')
        register()
    elif management_type == '' :
        print('Pls enter character')
        register()
    elif management_type =='admin' :
        pass
    elif management_type == 'employee' :
        pass
    else :
        print('unknow management,pls enter admin or employee')
        register()

    database = open ('admin.txt',mode = 'a')
    database.write(email+':'+password+':'+username+':'+phone+':'+salary+':'+age+':'+positions+':'+technology+':'+management_type+':''\n')
    print('success')
    database.close()
    
    
    ask =input('Back y/n : ')
    if ask == 'y' :
        Admin_choice()
    elif ask == 'n' :
        ask_login()
    elif ask == '' :
        print('pls enter y or n !')
        ask()
    else :
        print('pls enter y or n ! ')
        ask() 
# End option for Admin
        
# Remove
def remove():
    with open("admin.txt", "r") as f:
        delete_usr = input("Enter employee mail : ").lower().strip()
        lines = f.readlines() 
        with open("admin.txt", "w") as new_f:
            for line in lines:
                if not line.startswith(delete_usr):
                    new_f.write(line)
                    print("\nUser removed !")
    Admin_choice()


# start Edit specific current employee data
def edit() :
    with open("admin.txt", "r") as f:
        update = input("Enter employee mail : ").lower().strip()
        lines = f.readlines() 
        with open("admin.txt", "w") as new_f:
            for line in lines:
                if not line.startswith(update):
                    new_f.write(line)
    register()
                    




# end Edit specific current employee data

# Start option for employee



# Start Calculate his salary data.
def salary_data() :  
    for line in open("admin.txt","r").readlines(): 
        login_info = line.split(':') 
        search_word = open('employee_access.txt','r')
        if search_word.read() in login_info:
            print(f'Your salary is : {login_info[4]}\n')  
            search_word.close()
        
    ask = input('Back y/n : ')
    if ask == 'y' :
        Employee_choice()
    elif ask == 'n' :
        ask_login()
    elif ask == '' :
        print('pls enter y or n !')
        ask()
    else :
        print('pls enter y or n ! ')
        ask() 

    

# End Calculate his salary data

# the age of a specific employee by searching with his email.
def age () :
    mail = input('Enter email : ').lower()
    for line in open("admin.txt","r").readlines(): 
        login_info = line.split(':') 
        if mail == login_info[0] :
            print(f'The age is : {login_info[5]}')
            break
    if mail == '' : 
        print('Enter email pls')
        age()
    elif mail != login_info[0] :
        print('this email not found !\n')   
        age()
    ask = input('Back y/n : ')
    if ask == 'y' :
        Employee_choice()
    elif ask == 'n' :
        ask_login()
    elif ask == '' :
        print('pls enter y or n !\n')
        ask()
    else :
        print('pls enter y or n ! \n')
        ask() 
    
# the age of a specific employee by searching with his email.
# Start Calculate all employees salaries.

def employees_salaries() :
    num = 0
    for line in open("admin.txt","r").readlines():
        login_info = line.split(':')
        number = int(login_info[4])
        num = (num) + (number)
    print (f'All employies salaries : {num}\n')
    ask = input('Back y/n : ')
    if ask == 'y' :
        Employee_choice()
    elif ask == 'n' :
        employees_salaries()
    elif ask == '' :
        print('pls enter y or n !\n')
        employees_salaries
    else :
        print('pls enter y or n ! \n')
        employees_salaries

# end Calculate all employies salaries.

# end option for employee

# Admin rules
def Admin_choice() :
    print('\n-----Rules-----\n')
    print('1- Add new employee')
    print('2- Add new Admin')
    print('3- Remove current employee by the employee email')
    print('4- Edit specific current employee data')
    print('5- back ')

    option= input('Number choice : ')
    if option == '1' :
        print('\n-----Add new employee-----\n')
        register()
    elif option == '2' :
        print('\n-----Add new Admin-----\n')
        register()
    elif option == '3' :
        print('\n-----Remove current employee-----\n')
        remove()
    elif option == '4' :
        print('\n-----Edit specific current employee data-----\n')
        edit()
    elif option == '5' :
        ask_login()
    else :
        print('\npls enter number choice !!')
        Admin_choice()


     
# Employee 
def Employee_choice() :
    print('\n-----option-----\n')  
    print('1- Calculate his salary data')
    print('2- Calculate all employies salaries')
    print('3- The age of a specific employee by searching with his email.')
    print('4- back ')

    
    option= input('\nNumber choice : ')
    if option == '1' :
        print('\n-----Calculate his salary data-----\n')
        salary_data()
    elif option == '2' :
        print('\n-----Calculate all employies salaries-----\n')
        employees_salaries()
    elif option == '3' :
        print('\n-----The age of a specific employee by searching with his email-----\n')
        age()
    elif option == '4' :
        ask_login()
    else :
        print('\npls enter number choice !!\n')
        Employee_choice()

# check login then login
def login():    
    mail = input("Enter your email : ")
    import getpass
    password = getpass.getpass("Entre your password : ")
    with open ('employee_access.txt',mode = 'w') as employee :
        access = employee.write(mail)  
    employee.close()
    for line in open("admin.txt","r").readlines(): 
        login_info = line.split(':') 
        if mail == login_info[0] and password == login_info[1] :
            if login_info[8] == 'admin' :
                print(f'Welcome {login_info[2]}\n')
                Admin_choice()
            elif login_info[8] == 'employee' :
                print(f'Welcome {login_info[2]}\n')
                Employee_choice()
    
    print('wrong data, pls login again !!\n')
    ask_login()
        
    

# Ask for login or exit 
def ask_login() : 
    print('\nWelcome')
    value = (input('Pls enter 1 for login : '))
    if value == '1' :
        login()
    else :
        print('GoodBye sir')

ask_login()
