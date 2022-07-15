import csv
import os
#Class of student
class person():
    def __init__(self, name, id, phone, notes):
        self.name = name
        self.id = id
        self.phone = phone
        self.notes = notes
    
    def changeID(self, id):
        self.id = id

    def changeName(self, name):
        self.name = name

    def changePhone(self, phone):
        self.phone = phone

    def changeNotes(self, notes):
        self.notes = notes
    
    def print(self):
        print("{} - ID: {} - Phone: {} - Notes: {}".format(self.name, self.id, self.phone, self.notes))


def remove_spaces():
    {
        
    }

#start program
start = input("Search/add/show all?")
start = start.lower()

if start == "add":
    # Initializing the student
    Your_name = input("Name: ").lower()
    Your_id = input("Id: ")
    Your_phone = int(input("Phone: "))
    Your_notes = input("Notes: ").lower()
    you = person(Your_name, Your_id, Your_phone, Your_notes)

    # People's list
    my_people = [
        you
    ]
    def person_to_tuple(person):
        return(person.name, person.id, person.phone, person.notes)
    with open(r'Contacts\database_1.csv','a') as file:
        writer = csv.writer(file)
        for person in my_people:
            row = person_to_tuple(person)
            writer.writerow(row)

    with open(r'Contacts\database_1.csv') as input, open(r'Contacts\database_2.csv', 'w', newline='') as output:
        writer = csv.writer(output)
        for row in csv.reader(input):
            if any(field.strip() for field in row):
                writer.writerow(row)
    print("Saved")

elif start == "search":
    name = input("name: ")
    name = name.lower()


    
    file = open(r'Contacts\database_2csv', 'r')
    reader = csv.reader(file)
    
    for row in reader:
        if row:
            if name == row[0]:
                print("found!")
                #print(row[0].upper() + " - " + row[1])
                print("{} - ID: {} - Phone: {} - Notes: {}".format(row[0], row[1], row[2], row[3]))
                break

elif start == "show all":
    file = open(r'Contacts\database_2.csv', 'r')
    reader = csv.reader(file)
    for row in reader:
        print("{} - ID: {} - Phone: {} - Notes: {}".format(row[0].upper(), row[1], row[2], row[3]))
else:
    print("Usage: search/add/show all")









#file = open(r'C:\Users\DELL\Desktop\DESKTOP\Python_practice\Classes\classes1.csv', 'r')
 #   reader = csv.reader(file)



