'''
Dictionary - made up of Key/Value pairs
A Key's value can be: int, str, float, boolean, LIST, DICTIONARY
'''

students ={}
num_students = int(input("Enter the total number of students: "))

# Student's name (first name)
# Student's Home School
# Student's Age
# Student's Town

'''
What you don't want to do:

students = {'name': 'Hunter', 'school': 'Canton', 'Age': 17, 'Town': 'Canton', 'name': } - key's have to be unique

Instead assosiate the one common element with an nested dictionary as that elements value
'''

for student in range(num_students):
    print("\nStudent ", (student + 1), ': \n')
    name = input("Enter the students first name: ")
    school = input("Enter the student's school: ")
    age = input("Enter the student's age: ")
    town = input("Enter the student's town: ")

    # Store the data in the dictionary
    # the name variable as our key, and create a dictionary of the other variable keys/values as it value
    students[name] = {
        'School': school,
        'Age': age,
        'Town': town
    }

print(students)
