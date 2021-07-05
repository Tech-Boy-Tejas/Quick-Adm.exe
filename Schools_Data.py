import json

schools_dict = {'School_A':{'I':{},'II':{},'III':{},'IV':{},'V':{},'VI':{},'VII':{},'VIII':{},'IX':{},'X':{}},
                "School_B":{"I":{},"II":{},"III":{},"IV":{},"V":{},"VI":{},"VII":{},"VIII":{},"IX":{},"X":{}},
                "School_C":{"I":{},"II":{},"III":{},"IV":{},"V":{},"VI":{},"VII":{},"VIII":{},"IX":{},"X":{}},
                "School_D":{"I":{},"II":{},"III":{},"IV":{},"V":{},"VI":{},"VII":{},"VIII":{},"IX":{},"X":{}},
                "School_E":{"I":{},"II":{},"III":{},"IV":{},"V":{},"VI":{},"VII":{},"VIII":{},"IX":{},"X":{}},
                "School_F":{"I":{},"II":{},"III":{},"IV":{},"V":{},"VI":{},"VII":{},"VIII":{},"IX":{},"X":{}},
                "School_G":{"I":{},"II":{},"III":{},"IV":{},"V":{},"VI":{},"VII":{},"VIII":{},"IX":{},"X":{}},
                "School_H":{"I":{},"II":{},"III":{},"IV":{},"V":{},"VI":{},"VII":{},"VIII":{},"IX":{},"X":{}},
                "School_I":{"I":{},"II":{},"III":{},"IV":{},"V":{},"VI":{},"VII":{},"VIII":{},"IX":{},"X":{}},
                "School_J":{"I":{},"II":{},"III":{},"IV":{},"V":{},"VI":{},"VII":{},"VIII":{},"IX":{},"X":{}}
                }

for roll_num in range(1,11):
    for alphabet in range(ord('A'),ord('J') + 1):
        roll_num = str(roll_num)
        schools_dict['School_' + str(chr(alphabet))]['I'][roll_num] = 'open'
        schools_dict['School_' + str(chr(alphabet))]['II'][roll_num] = 'open'
        schools_dict['School_' + str(chr(alphabet))]['III'][roll_num] = 'open'
        schools_dict['School_' + str(chr(alphabet))]['IV'][roll_num] = 'open'
        schools_dict['School_' + str(chr(alphabet))]['V'][roll_num] = 'open'
        schools_dict['School_' + str(chr(alphabet))]['VI'][roll_num] = 'open'
        schools_dict['School_' + str(chr(alphabet))]['VII'][roll_num] = 'open'
        schools_dict['School_' + str(chr(alphabet))]['VIII'][roll_num] = 'open'
        schools_dict['School_' + str(chr(alphabet))]['IX'][roll_num] = 'open'
        schools_dict['School_' + str(chr(alphabet))]['X'][roll_num] = 'open'

#creating a custom dictionary contaning all the schools, classes and slots
with open('schools.txt','w') as file:
    file.write(json.dumps(schools_dict))