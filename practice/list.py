student1 = {
    "age": 20,
    "name": "Fred",
    "phone_number": "555-5555"
}

student2 = {
    "age": 30,
    "name": "Jenny",
    "phone_number": "777-7777"
}

print("The name of the student is " + student2['name'])

#combing those two list, which creates a curly inside of bracket
student_list = [
    student1, student2
]

print(student_list)

#while loop example of code above
#while loop is more code for looping through list
# i = 0
# while (i < len(student_list)):
#     print(student_list[i])
#     i += 1


#for loop example of code above
# for loop does the exact same thing much faster when looping through
# total_age = 0
# for student in student_list:
#     total_age+= student['age']

# average_age = total_age / len(student_list)
# print(average_age)


# index of list   0       1      2
student_names = ['jed', 'jen', 'john']

# will pull out    jed
print(student_names[0])


# i = len(student_names) - 1
# while (i >= 0):
#     print(student_names[i])
#     i -= 1


#how to add to list
