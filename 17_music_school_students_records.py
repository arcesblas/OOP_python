"""
Tasks: 
Your job is to add three methods to the existing program:

1. A method print_students_data that prints the name of each one of the students in the dictionary, their age, and the classes they are taking, 
one student per line.

2. A method print_student that prints the string shown above with the name, age, and classes of a student. 
It should take the name of the student as an argument and print only the data of that particular student. 
(Tip: you might consider using this method in the print_students_data method to avoid repetition).

. A method add_student  that adds a student to the existing students dictionary. 
The key used to add the student to the dictionary should be the name of the student and the value should be a list with the age, phone number, 
and classes that the student is taking. 
The method should take the name of the student as a parameter and a list with the data associated with that name as another parameter.
"""

class MusicSchool:
 
    students = {"Gino":   [15, "653-235-345", ["Piano", "Guitar"]],
            "Talina": [28, "555-765-452", ["Cello"]],
            "Eric":   [12, "583-356-223", ["Singing"]]}
 
    def __init__(self, working_hours, revenue):
        self.working_hours = working_hours
        self.revenue = revenue
  
    # Add your methods below this line  
    def print_students_data(self):
        for key, data in MusicSchool.students.items():
            print(f"Student name: {key}, info: {data[0::2]}")
            
    def print_student(self, name):
        for key, data in MusicSchool.students.items():
            if name == key:
                print(f"You request info about {key}, here it is: {data[0::2]}")  
    
    def add_student(self, name: str, data: list):
        MusicSchool.students.update({name: data})

     
# Create the instance
class2a = MusicSchool(30, 400)
 
# Call the methods
class2a.print_students_data()
class2a.add_student("Joel", [18, "555-344-321", ["Violin","Bass"]])
class2a.print_students_data()
class2a.print_student("Joel")
