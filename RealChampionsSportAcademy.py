#Tan Jun Wei
#TP062153

#Main menu function
def Main_Menu():
    flag = 0
    while flag==0:
        menu_opt = int(input("\n***Champions train, losers complain***\nWelcome to REAL CHAMPIONS SPORT ACADEMY\nTo proceed, please select which type of champion are you\n1.Admin \n2.Student \n3.Exit\nSelection:"))
        if (menu_opt == 1):
            flag = 1
            AdminLogin()
        elif (menu_opt == 2):
            flag = 1
            StudentMenu()
        elif(menu_opt == 3):
            flag = 1
            print("\nHave a nice day")
            exit()
        else:
            print("Invalid Option! Please Try again")

#Function for Admin Login
def AdminLogin():
    print("\nPlease login to continue")

    adminNameList = []
    adminPassword = []
    adminPasswordList = []

    Admin_file = open("Admin_Credentials.txt", "r")
    for line in Admin_file:
        line = line.strip()
        adminNameList.append(line.split(",")[0])
        adminPasswordList.append(line.split(",")[1])
    Admin_file.close()

    flag = 0
    trylogin = True
    while flag == 0:
        Admin_Name = str(input("Name:"))
        Admin_Pass = str(input("Password:"))
        for i in adminNameList:
            if Admin_Name == i:
                nameIndex = adminNameList.index(i)
                foundName = True
                break
            else:
                foundName = False
                continue

        for j in adminPasswordList:
            if Admin_Pass == j:
                passwordIndex = adminPasswordList.index(j)
                foundPassword = True
                break

            else:
                foundPassword = False
                continue


        if nameIndex == passwordIndex:
            print("Login Successfully!")
            flag = 1
            AdminMenu()
            break

        else:
            if foundName == False:
                print("\nInvalid Username! Please try again!\n")
            elif foundPassword == False:
                print("\nInvalid Password! Please try again!\n")
            else:
                print("\nUsername and Password doesn't exist! Please try again!\n")

#Function for Student Login
def StudentLogin():
    print("\nPlease login to continue")
    studentNameList = []
    studentPassword = []
    studentPasswordList = []

    Student_file = open("Student_Credentials.txt", "r")
    for line in Student_file:
        line = line.strip()
        studentNameList.append(line.split(",")[0])
        studentPasswordList.append(line.split(",")[1])
    Student_file.close()

    flag = 0
    trylogin = True
    while flag == 0:
        Student_Name = str(input("Name:"))
        Student_Pass = str(input("Password:"))
        for i in studentNameList:
            if Student_Name == i:
                nameIndex = studentPasswordList.index(i)
                foundName = True
                break
            else:
                foundName = False
                continue

        for j in studentPasswordList:
            if Student_Pass == j:
                passwordIndex = studentPasswordList.index(j)
                foundPassword = True
                break

            else:
                foundPassword = False
                continue

        if nameIndex == passwordIndex:
            print("Login Successfully!")
            flag = 1
            StudentMenu()
            break

        else:
            if foundName == False:
                print("\nInvalid Username! Please try again!\n")
            elif foundPassword == False:
                print("\nInvalid Password! Please try again!\n")
            else:
                print("\nUsername and Password doesn't exist! Please try again!\n")

#Function for Admin Menu
def AdminMenu():
    flag = 0
    while flag==0:
        AdminFunc_input = int(input("\nWelcome to REAL CHAMPION SPORTS ACADEMY Admin Menu\n1.Add records\n2.Display records\n3.Search specific records\n4.Sort and Display records\n5.Modify records\n6.Exit\nPlease select an action:"))
        if (AdminFunc_input == 1):
            while flag == 0:
                Addrecord_input = int(input("\nAdd Menu\n1.Coach\n2.Sport\n3.Sport Schedule\n4.Admin\n5.Back \nSelect an Option:"))
                if (Addrecord_input == 1):
                    flag = 1
                    Add_Coach()
                elif (Addrecord_input == 2):
                    flag = 1
                    Add_Sport()
                elif (Addrecord_input == 3):
                    flag = 1
                    Add_Sport_Schedule()
                elif(Addrecord_input == 4):
                    flag = 1
                    Add_Admin()
                elif(Addrecord_input == 5):
                    flag = 1
                    AdminMenu()
                else:
                    print("Invalid input!Please Try Again!")

        elif (AdminFunc_input == 2):
            while flag == 0:
                Displayrecord_input = int(input("\nDisplay Menu\n1.Coach\n2.Sport\n3.Registered Students\n4.Admin\n5.Back\nSelect an Option:"))
                if (Displayrecord_input == 1):
                    flag = 1
                    Display_Coach()
                elif (Displayrecord_input == 2):
                    flag = 1
                    Display_Sport()
                elif (Displayrecord_input == 3):
                    flag = 1
                    Display_Registered_Student()
                elif (Displayrecord_input == 4):
                    flag = 1
                    Display_Admin()
                elif (Displayrecord_input == 5):
                    flag = 1
                    AdminMenu()
                else:
                    print("Invalid input!Please Try Again!")

        elif (AdminFunc_input == 3):
            while flag == 0:
                Searchrecord_input = int(input("\nSearch Menu\n1.Coach by coach ID\n2.Coach by overall rating\n3.Sport by sportID\n4.Student by Student ID\n5.Back\nSelect an Option:"))
                if (Searchrecord_input == 1):
                    flag = 1
                    Search_Coach_by_CoachID()
                elif (Searchrecord_input == 2):
                    flag = 1
                    Search_Coach_by_Rating()
                elif (Searchrecord_input == 3):
                    flag = 1
                    Search_Sport_by_SportID()
                elif (Searchrecord_input == 4):
                    flag = 1
                    Search_Student_by_StudentID()
                elif (Searchrecord_input == 5):
                    flag = 1
                    AdminMenu()
                else:
                    print("Invalid input!Please Try Again!")

        elif (AdminFunc_input == 4):
            while flag == 0:
                Sort_displayrecord_input = int(input("\nSort Menu\n1.Coaches in ascending order by names\n2.Coaches Hourly Pay Rate in ascending order\n3.Coaches Overall Performance in ascending order\n4.Back\n"))
                if (Sort_displayrecord_input == 1):
                    flag = 1
                    Coaches_names_ascending_order()
                elif (Sort_displayrecord_input == 2):
                    flag = 1
                    Coaches_rate_ascending_order()
                elif (Sort_displayrecord_input == 3):
                    flag = 1
                    Coaches_performance_ascending_order()
                elif (Sort_displayrecord_input == 4):
                    flag = 1
                    AdminMenu()
                else:
                    print("Invalid input!Please Try Again!")

        elif (AdminFunc_input == 5):
            while flag == 0:
                Modifyrecord_input = int(input("Modify Menu\n1.Coach\n2.Sport\n3.Sport Schedule\n4.Back\n"))
                if (Modifyrecord_input == 1):
                    Modify_Coach()
                elif (Modifyrecord_input == 2):
                    Modify_Sport()
                elif (Modifyrecord_input == 3):
                    Modify_Sport_Schedule()
                elif (Modifyrecord_input == 4):
                    AdminMenu()
                else:
                    print("Invalid input!Please Try Again!")

        elif (AdminFunc_input == 6):
            flag == 1
            print("Have a nice day!")
            Main_Menu()
        else:
            print("Invalid Option! Please Try again!")

#Function for Student Menu
def StudentMenu():
    flag = 0;
    while flag == 0:
        StudentFunc_input = int(input("Welcome to REAL CHAMPION SPORTS ACADEMY Student Menu.\n1.View details of sport and sport schedule\n2.Register to gain access to other details\n3.Log in to access more details\n4.Exit\nPlease select an action:"))
        if (StudentFunc_input == 1):
            while flag == 0:
                AllStudentDisplay_input = int(input("Kindly select which records you would like to display\n1.Sport\n2.Sport Schedule\nor any other number to terminate\nOption:"))
                if (AllStudentDisplay_input == 1):
                    flag = 1
                    Display_Sport()
                elif (AllStudentDisplay_input == 2):
                    flag = 1
                    Display_Sport_Schedule()
                else:
                    print("have a nice day")

        elif(StudentFunc_input == 2):
            flag = 1
            Student_Registration()
        elif(StudentFunc_input == 3):
            flag = 1
            Registered_Student()
        elif(StudentFunc_input == 4):
            flag == 1
            print("Have a nice day!")
            Main_Menu()
        else:
            print("Invalid Option! Please Try again!")

#Function to add admin
def Add_Admin():
    admin_Details = open("Admin_Credentials.txt", "a")
    contents = admin_Details.read()
    cnt = 0
    while (cnt == 0):
        adminName = input("Name: ")
        adminPassword = input("Password: ")
        admin_Details.write(adminName+","+adminPassword)
        cnt = int(input("Would you like to continue? Enter 0 continue or any other number to terminate\n"))
        admin_Details.close()

#Function to add coach
def Add_Coach():
    flag = 0
    while (flag == 0):
        coach_Details = open("Coach_Details.txt","a")
        coach_ID = input("Enter ID: ")
        name = input("Name: ")
        date_Joined = input("Date Joined: ")
        date_Terminated = input("Date Terminated: ")
        rate = input("Hourly Rate: ")
        phone = input("Phone: ")
        address = input("Address: ")
        sport_CentreCode = input("Sport Centre Code: ")
        sport_CentreName = input("Sport Centre Name: ")
        sport_Code = input("Sport Code: ")
        sport_Name = input("Sport Name: ")
        rating = input("Rating(1-5): ")
        coach_Details.write(coach_ID+","+name+","+date_Joined+","+date_Terminated+","+rate+","+phone+","+address+","+sport_CentreCode+","+sport_CentreName+","+sport_Code+","+sport_Name+","+rating)
        flag = int(input("Would you like to continue? Enter 0 continue or any other number to terminate\n"))
    coach_Details.close()
        

#Function to add sport
def Add_Sport():
    flag = 0
    while (flag == 0):
        sport_Details = open("Sport.txt", "a")
        New_Sport_ID = input("Add ID of new sport: ")
        New_Sport_Name = input("Add name of new sport: ")
        sport_Details.write(New_Sport_ID+","+New_Sport_Name+"\n")
        flag = int(input("Would you like to continue? Press 0 continue or any other key to terminate\n"))
    sport_Details.close()

#Function to add sport schedule details in file    
def Add_Sport_Schedule():
    flag = 0
    while (flag == 0):
        sport_Schedule = open("Sport_Schedule.txt", "a")
        sport_Code = input("Sport Code: ")
        sport_Name = input("Sport Name: ")
        day = input("Day: ")
        time_start = input("Enter start time (e.g. 12:00PM): ")
        time_end = input("Enter end time (e.g. 12:00PM): ")
        sport_Schedule.write(sport_Code+","+sport_Name+","+day+","+time_start+","+time_end+"\n")
        flag = int(input("Would you like to continue? Press 0 continue or any other number to terminate\n"))
    sport_Schedule.close()

#Function to display all admin details
def Display_Admin():
    admin_Details = open("Admin_Credentials.txt", "r")
    print(admin_Details.read())
    admin_Details.close()

#Function to display all coach details    
def Display_Coach():
    coach_Details = open("Coach_Details.txt","r")
    print(coach_Details.read())
    coach_Details.close()

#Function to display all sport details    
def Display_Sport():
    sport_Details = open("Sport.txt","r")
    print(sport_Details.read())
    sport_Details.close()

#Function to display all sport schedule details    
def Display_Sport_Schedule():
    sport_Schedule = open("Sport_Schedule.txt","r")
    print(sport_Schedule.read())
    sport_Schedule.close()

#Function to display students that have registered 
def Display_Registered_Student():
    student_Details = open("Student_Details.txt","r")
    print(student_Details.read())
    student_Details.close()

#Function to search specific records of coach by Coach ID   
def Search_Coach_by_CoachID():
    data = input("Enter coach ID to search: ")
    coach_Details = open("coach_Details.txt")
    first_line = coach_Details.readline()
    print(first_line)
    for line in coach_Details:
        if line.startswith(data):
            print(line)

#Function to search specific records of coach by Coach overall performance (rating)    
def Search_Coach_by_Rating():
    data = input("Enter coach rating to search: ")
    coach_Details = open("Coach_Details.txt")
    first_line = coach_Details.readline()
    print(first_line)
    for line in coach_Details:
        words = line.split()        
        for cnt in words:
            if (data == cnt):
                print(line)

#Function to search specific records of sport by Sport ID            
def Search_Sport_by_SportID():
    data = input("Enter Sport ID to search: ")
    sport_Details = open("Sport.txt")
    first_line = sport_Details.readline()
    print(first_line)
    for line in sport_Details:
        if line.startswith(data):
            print(line)

#Function to search specific records of student by Student ID    
def Search_Student_by_StudentID():
    data = input("Enter Student ID to search: ")
    student_Details = open("Student_Details.txt")
    first_line = student_Details.readline()
    print(first_line)
    for line in student_Details:
        if line.startswith(data):
            print(line)

#Function to sort and display record of coaches in ascending order by names    
def Coaches_names_ascending_order():
    new_list = []
    newest_list = []
    coach_Details = open("Coach_Details.txt")
    first_line = coach_Details.readline()
    print(first_line)
    Coach_Details = open("Coach_Details.txt")
    for line in coach_Details.readlines()[4:]:
        words = line.split()[1]
        new_list.append(words)        
    for i in range(0,len(new_list)):
        for j in range(len(new_list)):
            if new_list[j] > new_list[i]:
                temp = new_list[i]
                new_list[i] = new_list[j]
                new_list[j] = temp      
    for cnt in new_list:
        coach_Details = open("Coach_Details.txt")
        for line in coach_Details:
            single_words = line.split()        
            for counter in single_words:
                if (cnt == counter):
                    print(line)

#Function to sort and display record of coaches hourly pay rate in ascending order    
def Coaches_rate_ascending_order():
    new_list = []
    newest_list = []
    coach_Details = open("Coach_Details.txt")
    first_line = coach_Details.readline()
    print(first_line)
    coach_Details = open("Coach_Details.txt")
    for line in coach_Details.readlines()[4:]:
        words = line.split()[4]
        new_list.append(words)    
    for i in new_list:
        i = int(i)    
    while new_list:
        minimum = new_list[0]
        for x in new_list:
            if x < minimum:
                minimum = x
        newest_list.append(minimum)
        new_list.remove(minimum)    
    for i in newest_list:
        i = str(i)    
    for cnt in newest_list:
        coach_Details = open("Coach_Details.txt")
        for line in coach_Details:
            single_words = line.split()        
            for counter in single_words:
                if (cnt == counter):
                    print(line)            

#Function to sort and display record of coaches overall performance in ascending order    
def Coaches_performance_ascending_order():    
    coach_Details = open("Coach_Details.txt")
    first_line = coach_Details.readline()
    print(first_line)
    for line in coach_Details:
        words = line.split()        
        for cnt in words:
            if ('*' == cnt):
                print(line)
    coach_Details = open("Coach_Details.txt")
    for line in coach_Details:
        words = line.split()        
        for cnt in words:
            if ('**' == cnt):
                print(line)
    coach_Details = open("Coach_Details.txt")
    for line in coach_Details:
        words = line.split()        
        for cnt in words:
            if ('***' == cnt):
                print(line)
    coach_Details = open("Coach_Details.txt")
    for line in coach_Details:
        words = line.split()        
        for cnt in words:
            if ('****' == cnt):
                print(line)
    coach_Details = open("Coach_Details.txt")
    for line in coach_Details:
        words = line.split()        
        for cnt in words:
            if ('*****' == cnt):
                print(line)   
    

#Function to modify record of coach    
def Modify_Coach():
    current_list = []
    old = input("Enter current data: ")
    new = input("Enter new data: ")
    coach_Details = open("Coach_Details.txt","r")
    for line in coach_Details.readlines():
        current_list.append(line)
    new_list = []
    for item in current_list:
        whatweneed = item.replace(old,new)
        new_list.append(whatweneed)
    coach_Details = open("Coach_Details.txt","w")
    for i in new_list:
        coach_Details.write(i)
    coach_Details.close()
    
    
#Function to modify record of sport    
def Modify_Sport():
    current_list = []
    old = input("Enter current data: ")
    new = input("Enter new data: ")
    Sport = open("Sport.txt","r")
    for line in Sport.readlines():
        current_list.append(line)
    new_list = []
    for item in current_list:
        whatweneed = item.replace(old,new)
        new_list.append(whatweneed)
    sport_Records = open("Sport.txt","w")
    for i in new_list:
        sport_Records.write(i)
    sport_Records.close()


#Function to modify record of sport schedule    
def Modify_Sport_Schedule():
    current_list = []
    old = input("Enter current data: ")
    new = input("Enter new data: ")
    sport_Schedule = open("Sport_Schedule.txt","r")
    for line in sport_Schedule.readlines():
        current_list.append(line)
    new_list = []
    for item in current_list:
        whatweneed = item.replace(old,new)
        new_list.append(whatweneed)
    sport_Schedule = open("Sport_Schedule.txt","w")
    for i in new_list:
        sport_Schedule.write(i)
    sport_Schedule.close()
    
#Function to register student    
def Student_Registration():
    student_Credentials = open("Student_Credentials.txt")
    contents = student_Credentials.read()
    Student_ID = input("Choose Student ID: ")
    while (int(Student_ID) < 1000 or int(Student_ID) > 9999 or Student_ID in contents):
        Student_ID = input("Please choose Student ID between 1000 and 9999: ")     
    
    student_Credentials = open("Student_Credentials.txt","a")
    Password = input("Please choose a password: ")        
    student_Credentials.write(Student_ID+"\t"+Password+"\n")
    student_Credentials.close()
    student_Details = open("Student_Details.txt","a")
    Name = input("Please enter your name: ")
    Phone = input("Please enter contact number: ")
    Sport_ID = input("Please enter chosen Sport ID: ")
    Sport_Name = input("Please enter chosen Sport Name: ")
    student_Details.write(","+Student_ID+","+Name+","+Phone+","+Sport_ID+","+Sport_Name)
    student_Details.close()
    print("Thank you, you have successfully been registered")

#Function for registered student    
def Registered_Student():
    student_Credentials = open("Student_Credentials.txt","r")
    student_ID = input("Enter Student ID: ")
    password = input("Enter password: ")
    if (student_ID+","+password+"\n") in student_Credentials.readlines():
        choice = int(input("Please select which function you would like to proceed with.\n1.View details of coach, self-record your sport schedule\n2.Modify your self records\n3.Provide feedback and star to coach\nor any other key to terminate\n"))
        if (choice == 1):
            Display = int(input("Kindly select which records you would like to display\n1.Coach\n2.Self record\n3.Your Sport Schedule\nor any other key to terminate\n"))
            if (Display == 1):
                Display_Coach()
            elif (Display == 2):
                Student_View_Self_Record(student_ID)
            elif (Display == 3):
                Student_View_Sport_Schedule(student_ID)
            else:
                print("have a nice day")
        elif(choice == 2):
            Student_Modify_Self_Record(student_ID)
        elif(choice == 3):
            Student_Provide_Coach_Feedback(student_ID)
        else:
            print("have a nice day")    
    else:
        print("Invalid ID or Password")    
      

#Function for Students to view self-record    
def Student_View_Self_Record(student_ID):
    student_Details = open("Student_Details.txt")
    for line in student_Details:
        if line.startswith(student_ID):
            print(line)

#Function for Students to view registered sport schedule
def Student_View_Sport_Schedule(Student_ID):
    student_Details = open("Student_Details.txt")
    for line in student_Details:
        if line.startswith(Student_ID):
            words = line.split()
            for cnt in words:
                sport_Schedule = open("Sport_Schedule.txt")
                for rows in sport_Schedule:
                    if rows.startswith(cnt):
                        print(rows)

#Function for Students to modify self-record    
def Student_Modify_Self_Record(Student_ID):
    temp_list = []
    new_list = []
    old = input("Enter current data: ")
    new = input("Enter new data: ")
    student_Details = open("Student_Details.txt","r")
    for line in student_Details.readlines():
        if line.startswith(Student_ID):
            temp_list.append(line)
            for item in temp_list:                
                whatweneed = item.replace(old,new)
                new_list.append(whatweneed)
        else:
            new_list.append(line)           
            
    student_Details = open("Student_Details.txt","w")
    for i in new_list:
        student_Details.write(i)
    student_Details.close()

#Function for Students to provide feedback and star for coach
def Student_Provide_Coach_Feedback(Student_ID):
    coach_Feedback = open("Coach_Feedback.txt","a")
    Coach_ID = input("Please enter Coach ID: ")
    Rating = input("Please enter your rating for this coach: ")
    Feedback = input("Please provide your feedback: ")
    coach_Feedback.write(","+Student_ID+","+Coach_ID+","+Rating+","+Feedback+"\n")
    print("Thank you, your response has been saved")


Main_Menu()
    
#Tan Jun Wei
#TP062153