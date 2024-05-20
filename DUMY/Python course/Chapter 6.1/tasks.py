#  <h1>Task</h1>
#     Make an list of dictionary (an list that will have dictionary)
#      to store the student information and
#      access it as hard-coded.
#     <h2>Information to store:</h2> 
#     Name, age, registration number, course, favorite programming 
#     languages (should be an list), 
#      Marks of 5 different subjects (should be an dictionary).
#     <h2>The operations to perform:</h2>
#     <ul>
#         <li>Display every single property of any student.</li>
#         <li>Display the first and last favorite 
#             programming language of any student.</li>
#         <li>Display the marks of any 2 subjects of any student.</li>
#     </ul>

# Make a list of dictionaries to store a student information

student = [
     { 
        'name': 'ALi',
        'age' : 25,
        'reg_no': 12364,
        'course': 'Python Programming',
        'frov_lang' : ['Python','JavaScript','PHP'],
        'marks' : {
            'English': 55, 'URDU': 80,'Computer':90,'Physics':80
            }
    },
    {
        'name': 'Ahmad',
        'age' : 20,
        'reg_no': 22364,
        'course': 'Python Programming',
        'frov_lang' : ['Python','JavaScript','PHP'],
        'marks' : {'English': 60, 'URDU': 80,'Computer':90,'Physics':80}
     }
]

#Display every single property of any student
# for std in student:
print('Name:', student[0]['name'])
print('Age:', student[0]['age'])
print('Reg_No:', student[0]['reg_no'])
print('Course:', student[0]['course'])
print('Marks', student[0]['marks'] )

for std in student:
    print('First Frov Language',student[0]['frov_lang'])
    print('First Frov Language',student[0]['frov_lang'])
print()


print('English Marks',student[0]['marks'].get('English','Not Found'))
print('Physics Marks',student[1]['marks'].get('Physics','Not Found'))