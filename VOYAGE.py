#IMPORT LIBRARIES
import time
import random
import datetime

#MAIN VARIABLES
flightdata = ["Air Asia","Lion Air","Cathay Airways","Lion Air","Etihad Airways","British Airlines"]
typedata = ["Domestic","Domestic","International","Domestic","International","International"]
datedata = ["29 March 2024","30 July 2024","12 December 2024","15 March 2025","20 May 2025","1 September 2025"]
destdata = ["Bali","Surabaya","London","Palembang","Los Angeles","Madrid"]
flighttype = ["Economic","Business","Business","Economic","Economic","Economic"]
timedata = ["Day","Night","Day","Night","Day","Night"]
runningapp = 1
enter = 0
name = ""
phone = 0
password = ""
email = "NOT SET"
address = "NOT SET"
nationality = "NOT SET"
gender = "NOT SET"

#THIS IS THE CALENDAR FUNCTION
def calendar(name):
    import calendar
    c = calendar.TextCalendar(calendar.MONDAY)
    runningprogram = 1
    thirtyonedays = [1,3,5,7,8,10,12]
    thirtydays = [4,6,9,11]
    twentyeightdays = [2]
    timedata = []
    infoarray = []
    while runningprogram == 1:
        print("\n"*2)
        print("***************************")
        print("Welcome",name,"to calendar!")
        print("1. View a date")
        print("2. Back to home screen")
        print("***************************")
        print("\n"*2)
        validity = 0
        while validity == 0:
            a = int(input(" > "))
            if a == 1 or a == 2:
                choice = a
                validity = 1
            else:
                print("ONLY INPUT 1 OR 2")
        if choice == 1:
            validity = 0
            while validity == 0:
                print("\n"*2)
                a = int(input("INPUT THE MONTH (1-12) > "))
                print("\n"*2)
                if a >= 1 and a <= 12:
                    validity = 1
                    month = a
                else:
                    print("INPUT A VALID MONTH")
            str = c.formatmonth(2023,month)
            print(str)
            validity = 0
            while validity == 0:
                print("\n"*2)
                d = int(input("SELECT A DATE > "))
                print("\n"*2)
                if month in thirtyonedays:
                    if d >= 1 and d <= 31:
                        validity = 1
                        date = d
                    else:
                        print("INPUT A DATE BETWEEN 1 and 31")
                elif month in thirtydays:
                    if d >= 1 and d <= 30:
                        validity = 1
                        date = d
                    else:
                        print("INPUT A DATE BETWEEN 1 and 30")
                elif month in twentyeightdays:
                    if d >= 1 and d <= 28:
                        validity = 1
                        date = d
                    else:
                        print("INPUT A DATE BETWEEN 1 and 28")
            print("\n"*2)
            print("You have selected date",date)
            print("\n"*2)
            if [month,date] in timedata:
                index = timedata.index([month,date])
                print("\n"*2)
                for i in range(len(infoarray[index])):
                    print("Event",i+1)
                    print(infoarray[index][i])
                print("\n"*2)
                print("Do you want to add an event? (Y/N)")
                a = input(" > ")
                if a == "Y":
                    print("Write event description")
                    event = input()
                    infoarray[index].append(event)
                    print("You have added the event!")
            else:
                print("\n"*2)
                print("You have no events.")
                print("\n"*2)
                print("Do you want to add an event? (Y/N)")
                a = input(" > ")
                if a == "Y":
                    print("Write event description")
                    event = input(" > ")
                    infoarray.append([event])
                    timedata.append([month,date])
                    print("You have added the event!")
        elif choice == 2:
            runningprogram = 0

#NAME, PHONE, PASSWORD ARE FIXED AT THE BEGINNING
class Account:
    def __init__(self,name,phone,password,email,address,nationality,gender):
        self.name = name
        self.phone = phone
        self.password = password
        self.email = email
        self.address = address
        self.nationality = nationality
        self.gender = gender

    def page(self):
        l = [["Name:",self.name],["Phone number:",self.phone],["Password:","*"*len(self.password)],["Email:",self.email],["Address:",self.address],["Nationality:",self.nationality],["Gender:",self.gender]]
        print("************")
        print("YOUR ACCOUNT")
        for item in l:
            print("{0:2} {1:15} {2:35} {3:2}".format("|",item[0],item[1],"|"))
        print("\n"*2)

    def prompt(self):
        print("What do you want to set?")
        counter = 1
        for item in ["Email","Address","Nationality","Gender"]:
            print(str(counter)+". "+item)
            counter = counter + 1
        v = False
        while v == False:
            c = int(input(" > "))
            if c >= 1 and c <= 4:
                v = True
                return c
            else:
                print("Please input from 1 to 4 only!")

    def authentication(self):
        print("Please validate your password!")
        p = input(" > ")
        if p == password:
            return True
        elif p != password:
            print("Wrong password! Access denied!")
            return False

    def setemail(self):
        e = str(input("Please set your email! > "))
        self.email = e

    def setaddress(self):
        a = str(input("Please set your address! > "))
        self.address = a

    def setnationality(self):
        n = str(input("Please set your nationality! > "))
        self.nationality = n

    def setgender(self):
        g = str(input("Please set your gender (M/F)! > "))
        v = False
        while v == False:
            if g.upper() == "M" or g.upper() == "F":
                v = True
                self.gender = g
            else:
                print("Please input only M or F")


#THESE ARE THE SORTING FUNCTIONS
def table():
    global lst
    print("{0:2} {1:15} {2:15} {3:10}".format("I","FIRST","PRICE","RATING"))
    for i in range(len(lst)):
        words = "{0:2} {1:15} {2:15} {3:10}".format(str(lst[i][0]),str(lst[i][1]),str(lst[i][2]),str(lst[i][3]))
        print(words)
    print("\n"*3)

def custom_key(lst):
    return lst[1]

def sort():
    global lst
    print("\n"*2)
    print("**********************")
    print("SORT BY?")
    print("1. Price Ascending")
    print("2. Price Descending")
    print("3. Rating Ascending")
    print("4. Rating Descending")
    print("5. Exit")
    print("**********************")
    print("\n"*2)
    validity = 0
    while validity == 0:
        a = int(input(" > "))
        if a >= 1 and a <= 5:
            validity = 1
            choice = a
        else:
            print("Choose only from 1 to 5")
    if choice == 1:
        lst = sorted(lst, key=lambda x: x[2])
        return True
    elif choice == 2:
        lst = sorted(lst, key=lambda x: x[2], reverse=True)
        return True
    elif choice == 3:
        lst = sorted(lst, key=lambda x: x[3])
        return True
    elif choice == 4:
        lst = sorted(lst, key=lambda x: x[3], reverse=True)
        return True
    elif choice == 5:
        return False

#THESE ARE THE CANCELLING FUNCTIONS
def cancel(name):
    print("Hello,",name,", welcome to cancel a flight!")
    print("Press enter to continue")
    input()
    showall()
    validity = 0
    print("CHOOSE A FLIGHT")
    while validity == 0:
        a = int(input(" > "))
        if a >= 1 and a <= len(flightdata):
            flightdata.pop(a-1)
            typedata.pop(a-1)
            datedata.pop(a-1)
            destdata.pop(a-1)
            flighttype.pop(a-1)
            timedata.pop(a-1)
            validity = 1
        else:
            print("INPUT A VALID FLIGHT NUMBER")

#THESE ARE THE BOOKING FUNCTIONS
def book(name):
    print("\n"*2)
    print("*******************************************")
    print("Hello,",name,", welcome to book a flight!")
    print("Press enter to continue")
    print("*******************************************")
    print("\n"*2)
    input()
    print("Choose one of the following airlines")
    print("1. Air Asia\n2. Garuda Indonesia\n3. Citilink\n4. Lion Air\n5. Malaysia Airlines\n6. Singapore Airlines\n7. Cathay Airways\n8. Etihad Airways\n9. British Airlines\n10. American Airlines")
    validity = 0
    while validity == 0:
        a = int(input(" > "))
        if a >= 1 and a <= 10:
            validity = 1
            airline = a
        else:
            print("INPUT ONLY 1 UNTIL 10")
    airlinechoice = ["Air Asia","Garuda Indonesia","Citilink","Lion Air","Malaysia Airlines","Singapore Airlines","Cathay Airways","Etihad Airways","British Airlines","American Airlines"]
    flightdata.append(airlinechoice[airline-1])
    print("Choose your location type")
    print("1. Domestic\n2. International")
    validity = 0
    while validity == 0:
        a = int(input(" > "))
        if a == 1:
            validity = 1
            location = "Domestic"
        elif a == 2:
            validity = 1
            location = "International"
        else:
            print("INPUT ONLY 1 OR 2!")
    typedata.append(location)
    datestring = ""
    print("Input the date of your visit")
    validity = 0
    while validity == 0:
        a = int(input(" > "))
        if a >=1 and a <= 31:
            validity = 1
            datestring = datestring + str(a)
        else:
            print("INPUT A VALID DATE!")
    print("Input the month of your visit (1-12)")
    validity = 0
    while validity == 0:
        a = int(input(" > "))
        if a >=1 and a <= 12:
            validity = 1
            if a == 1:
                datestring = datestring + " January"
            elif a == 2:
                datestring = datestring + " February"
            elif a == 3:
                datestring = datestring + " March"
            elif a == 4:
                datestring = datestring + " April"
            elif a == 5:
                datestring = datestring + " May"
            elif a == 6:
                datestring = datestring + " June"
            elif a == 7:
                datestring = datestring + " July"
            elif a == 8:
                datestring = datestring + " August"
            elif a == 9:
                datestring = datestring + " September"
            elif a == 10:
                datestring = datestring + " October"
            elif a == 11:
                datestring = datestring + " November"
            elif a == 12:
                datestring = datestring + " December"
        else:
            print("INPUT A VALID MONTH!")
    print("Input the year of your visit")
    validity = 0
    while validity == 0:
        a = int(input(" > "))
        if a >=2022 and a <= 2030:
            validity = 1
            datestring = datestring + " " + str(a)
        else:
            print("INPUT A VALID YEAR!")
    datedata.append(datestring)
    print("Input your visit destination")
    a = str(input(" > "))
    destdata.append(a)
    print("Input your flight type")
    print("1. Economic")
    print("2. Business")
    validity = 0
    while validity == 0:
        a = int(input(" > "))
        if a == 1:
            validity = 1
            flight = "Economic"
        elif a == 2:
            validity = 1
            flight = "Business"
        else:
            print("INPUT ONLY 1 OR 2!")
    flighttype.append(flight)
    print("Choose for day or night flight")
    print("1. Day")
    print("2. Night")
    validity = 0
    while validity == 0:
        a = int(input(" > "))
        if a == 1:
            validity = 1
            time = "Day"
        elif a == 2:
            validity = 1
            time = "Night"
        else:
            print("INPUT ONLY 1 OR 2!")
    timedata.append(time)



#THESE ARE THE VIEW FUNCTIONS
def showall():
    for i in range(len(flightdata)):
        print("FLIGHT",i+1)
        print("Airline:",flightdata[i])
        print("Type:",typedata[i])
        print("Date:",datedata[i])
        print("Destination:",destdata[i])
        print("Flight:",flighttype[i])
        print("Time:",timedata[i])
        print("\n")
    print("\n"*3)


def typefilter():
    print("FILTER FOR?")
    print("1. Domestic")
    print("2. International")
    print("\n"*3)
    validity = 0
    while validity == 0:
        a = int(input(" > "))
        if a == 1:
            validity = 1
            filter = "Domestic"
        elif a == 2:
            validity = 1
            filter = "International"
        else:
            print("INPUT ONLY 1 OR 2!")
    for i in range(len(flightdata)):
        if typedata[i] == filter:
            print("FLIGHT",i+1)
            print("Airline:",flightdata[i])
            print("Type:",typedata[i])
            print("Date:",datedata[i])
            print("Destination:",destdata[i])
            print("Flight:",flighttype[i])
            print("Time:",timedata[i])
            print("\n")

def flightfilter():
    print("FILTER FOR?")
    print("1. Economic")
    print("2. Business")
    print("\n"*3)
    validity = 0
    while validity == 0:
        a = int(input(" > "))
        if a == 1:
            validity = 1
            filter = "Economic"
        elif a == 2:
            validity = 1
            filter = "Business"
        else:
            print("INPUT ONLY 1 OR 2!")
    for i in range(len(flightdata)):
        if flighttype[i] == filter:
            print("FLIGHT",i+1)
            print("Airline:",flightdata[i])
            print("Type:",typedata[i])
            print("Date:",datedata[i])
            print("Destination:",destdata[i])
            print("Flight:",flighttype[i])
            print("Time:",timedata[i])
            print("\n")

def timefilter():
    print("FILTER FOR?")
    print("1. Day")
    print("2. Night")
    print("\n"*3)
    validity = 0
    while validity == 0:
        a = int(input(" > "))
        if a == 1:
            validity = 1
            filter = "Day"
        elif a == 2:
            validity = 1
            filter = "Night"
        else:
            print("INPUT ONLY 1 OR 2!")
    for i in range(len(flightdata)):
        if timedata[i] == filter:
            print("FLIGHT",i+1)
            print("Airline:",flightdata[i])
            print("Type:",typedata[i])
            print("Date:",datedata[i])
            print("Destination:",destdata[i])
            print("Flight:",flighttype[i])
            print("Time:",timedata[i])
            print("\n")


#THIS IS THE QUIZ CLASS
class Quiz:
    scoring = [(200,"D"),(200,"B"),(200,"C"),(300,"D"),(300,"A"),(300,"B"),(400,"D"),(400,"C"),(400,"A"),(400,"D")]
    easynumbers = [0,1,2]
    mediumnumbers = [0,1,3,4,5,6]
    hardnumbers = [0,1,2,3,4,5,6,7,8,9]
    questions = [("Approximately how many people are afraid of flying?","10%","20%","30%","40%"),("Which airport is the largest by size?","Denver International","King Fahd International","Beijing Daxing International","Orlando International"),("The Lockheed SR-71 Blackbird, the fastest jet aircraft, has a top speed of?","1300 mph","2800 mph","2100 mph","890 mph"),("Who successfully invented the first working motor-operated airplane?","Victor Tatin","Doug Parker","Charles Richet","Wright brothers"),("Which of the airports mentioned is the busiest one?","Hartsfield-Jackson Atlanta","Beijing Capital","Los Angeles","Dubai"),("Which airline made the largest revenue in 2021?","Delta Airlines","American Airlines","China Southern Airlines","Air China"),("As of 2022, which airplane can carry the largest amount of passengers?","Airbus A340-600","Boeing 747-400","Boeing 747-800","Airbus A380-800"),("Which country is the most visited?","Spain","Italy","France","Turkey"),("Approximately how likely is a plane crash?","One in 1.2 million","One in 100 thousand","One in 2 million","One in 500 thousand"),("Which of these rooms/suites below cost the most per night?","The Mark Penthouse","Royal Penthouse Suite","Harbour House","Empathy Suite")]
    defaultnumbers = []
    rules = [("easy",7,"no addition of score",3),("medium",5,"a minus of 100 points",6),("hard",3,"a minus of 150 points",10)]
    score = 0
    useranswer = ""

    def __init__(self,name):
        Quiz.score = 0
        print("\n"*3)
        print("**********************************")
        print("Welcome to the Voyage flight quiz!")
        print("")
        print("Choose from level 1-3...")
        print("**********************************")
        print("\n"*3)
        level = int(input(" > "))
        self.player = name
        self.level = level

    def setrules(self):
        if self.level == 1:
            Quiz.defaultnumbers = Quiz.easynumbers
        elif self.level == 2:
            Quiz.defaultnumbers = Quiz.mediumnumbers
        elif self.level == 3:
            Quiz.defaultnumbers = Quiz.hardnumbers
        print("\n"*3)
        print("RULES")
        print(f"You have chosen {Quiz.rules[self.level-1][0]} difficulty")
        print(f"An incorrect answer will result you in {Quiz.rules[self.level-1][2]}")
        print(f"You will have to answer {Quiz.rules[self.level-1][3]} questions in this level")
        print("Please answer is uppercase only")
        print("Press enter to start")
        print("\n"*3)
        input()

    def resultstatement(self):
        print(f"{self.player}, you got {Quiz.score} points in level {self.level}.")
        print("Thanks for taking the quiz!")
        input()

    def readystatement(self):
        print(f"{self.player}, you have chosen level {self.level}, press enter")
        input()

    def loading(self):
        for i in range(3):
            print("Loading "+"."*i)
            print("Please wait for "+str(3-i)+" seconds")
            time.sleep(1)

    def qna(self):
        for nums in Quiz.defaultnumbers:
            Quiz.useranswer = ""
            print("\n"*3)
            print(Quiz.questions[nums][0])
            print(f"A. {Quiz.questions[nums][1]}")
            print(f"B. {Quiz.questions[nums][2]}")
            print(f"C. {Quiz.questions[nums][3]}")
            print(f"D. {Quiz.questions[nums][4]}")
            print()
            print()
            print()
            print()
            print("What is your answer?")
            print("\n"*3)
            Quiz.useranswer = input(" > ")
            if Quiz.useranswer == Quiz.scoring[nums][1]:
                Quiz.score += Quiz.scoring[nums][0]
            elif Quiz.useranswer != Quiz.scoring[nums][1] and self.level == 2:
                Quiz.score -= 100
            elif Quiz.useranswer != Quiz.scoring[nums][1] and self.level == 3:
                Quiz.score -= 150
        


#THESE ARE THE MAIN FUNCTIONS
def validateinput(array,type):
    validity = False
    while validity == False:
        if type == 1:
            a = input(" > ")
            if a in array:
                validity = True
                return a
            else:
                print("Invalid input! Try again!")
        elif type == 2:
            a = int(input(" > "))
            if a in array:
                validity = True
                return a
            else:
                print("Invalid input! Try again!")
                
def startscreen():
    print("\n"*3)
    print("**************************************")
    print("          WELCOME TO VOYAGE           ")
    print("")
    print("TIP: SET THE SHELL TO FULL SCREEN!")
    print("")
    print("      Click anywhere to begin!        ")
    print("**************************************")
    print("\n"*3)
    input()

def loading(secs):
    for i in range(secs):
        print("Loading"+"."*i)
        time.sleep(1)

def mainmenu():
    print("\n"*3)
    print("***************************************")
    print("Choose one of the following activities!")
    print("1. View flight bookings")
    print("2. Book a flight")
    print("3. Cancel a flight")
    print("4. Play a flight quiz")
    print("5. Journey calendar")
    print("6. Hotel list")
    print("7. Random code generator")
    print("8. Manage account")
    print("9. Exit the app")
    print("\n"*2)
    x = datetime.datetime.now()
    print(x.strftime("%A, %d %B %Y"))
    print(x.strftime("Current time: %I:%M %p"))
    print("***************************************")
    print("\n"*3)

#RANDOM CODE GENERATOR
dictio = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z"}

def testinput():
    num = int(input("Choose one of the choices > "))
    v = 0
    while v == 0:
        if num == 1 or num == 2:
            v = 1
            return num
        else:
            num = int(input("Choose only 1 or 2 > "))

def generator():
    running = True
    while running == True:
        keys = []
        print("\n"*3)
        print("1. Generate a flight code")
        print("2. Back to main screen")
        print("\n"*3)
        choice = testinput()
        if choice == 1:
            for i in range(2):
                a = random.randint(1,26)
                keys.append(dictio[a])
            for i in range(3):
                a = random.randint(1,9)
                keys.append(str(a))
            final = keys[0]+keys[1]+"-"+keys[2]+keys[3]+keys[4]
            print("\n"*3)
            print("Your random code is",final)
            print("PRESS ENTER TO CONTINUE")
            print("\n"*3)
            input()
        elif choice == 2:
            running = False

#VALIDATION
def phonevalid():
    num = str(input("Please input your phone number! > "))
    v = False
    while v == False:
        if num.isdigit():
            v = True
            return num
        else:
            num = input("Please input only numbers > ")

def passwordvalid():
    v = False
    while v == False:
        print()
        prompt = str(input("Please input your password! > "))
        if len(prompt) <= 10:
            print("Your password should be more than 10 characters long.")
        else:
            sprompt = str(input("Confirm your password! > "))
            if sprompt == prompt:
                v = True
                return prompt
            else:
                print("Your passwords do not match! Try again!")


#THIS IS THE FLOWCODE
startscreen()
print("\n"*3)
name = input("Please input your name! > ")
print("\n"*3)
phone = phonevalid()
print("\n"*3)
password = passwordvalid()
print("\n"*3)
acc = Account(name,phone,password,email,address,nationality,gender)
while runningapp == 1:
    mainmenu()
    enter = validateinput([1,2,3,4,5,6,7,8,9],2)
    if enter == 4:
        loading(4)
        user = Quiz(name)
        user.loading()
        user.readystatement()
        user.setrules()
        user.qna()
        user.resultstatement()
        user.loading()
    elif enter == 3:
        loading(3)
        cancel(name)
    elif enter == 2:
        loading(3)
        book(name)
    elif enter == 1:
        loading(3)
        runningview = 1
        while runningview == 1:
            print("\n"*3)
            print("***********************")
            print("1. No filter")
            print("2. Type filter")
            print("3. Flight filter")
            print("4. Time filter")
            print("5. Back to home screen")
            print("***********************")
            print("\n"*3)
            a = int(input("SELECT YOUR CUSTOMIZED VIEW > "))
            if a == 1:
                showall()
                print("Press enter to continue")
                input()
            elif a == 2:
                typefilter()
                print("Press enter to continue")
                input()
            elif a == 3:
                flightfilter()
                print("Press enter to continue")
                input()
            elif a == 4:
                timefilter()
                print("Press enter to continue")
                input()
            elif a == 5:
                runningview = 0
    elif enter == 9:
        loading(3)
        runningapp = 0
    elif enter == 6:
        loading(3)
        lst = [[1,"Express Hotel",2000000,6],
       [2,"Sheraton",3000000,8],
       [3,"Shangri-La",5000000,10],
       [4,'Rachna',2000000,9],
       [5,'Shubham',1500000,7]]
        running = 1
        while running == 1:
            table()
            a = sort()
            table()
            if a == False:
                running = 0
            print("Press enter to continue")
            input()
            print("\n"*8)
            lst = sorted(lst, key=lambda x: x[0])
    elif enter == 5:
        loading(3)
        calendar(name)
    elif enter == 7:
        loading(3)
        generator()
    elif enter == 8:
        loading(3)
        acc.page()
        choice = acc.prompt()
        if choice == 1:
            a = acc.authentication()
            if a == True:
                acc.setemail()
        elif choice == 2:
            a = acc.authentication()
            if a == True:
                acc.setaddress()
        elif choice == 3:
            a = acc.authentication()
            if a == True:
                acc.setnationality()
        elif choice == 4:
            a = acc.authentication()
            if a == True:
                acc.setgender()








