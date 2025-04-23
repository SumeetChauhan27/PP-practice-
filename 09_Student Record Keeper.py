
# Creating initial student data
student = {
    101: "Aditi",
    102: "Aman",
    103: "Vishal"
}
student_marks = {
    101: 78,
    102: 88,
    103: 79
}
student_att = {
    101: 90,
    102: 81,
    103: 72
}

# Displaying initial records
print("Roll No : Name ->", student)
print("Roll No : Marks ->", student_marks)
print("Roll No : Attendance% ->", student_att)

# Adding new student record
print('\nAdding Elements to the Dictionary:')
Roll_no = int(input('Enter Roll No to be added: '))
name = input('Enter Student Name: ')
marks = int(input('Enter Marks: '))
att = int(input('Enter Attendance (%): '))

student[Roll_no] = name
student_marks[Roll_no] = marks
student_att[Roll_no] = att

# Displaying updated records
print("\nUpdated Records After Addition:")
print("Roll No : Name ->", student)
print("Roll No : Marks ->", student_marks)
print("Roll No : Attendance% ->", student_att)

# Deleting a student record
print('\nDeleting Elements from the Dictionary:')
Roll_no = int(input('Enter Roll No to be deleted: '))

# Validating before deletion
if Roll_no in student:
    del student[Roll_no]
    del student_marks[Roll_no]
    del student_att[Roll_no]
    print("\nUpdated Records After Deletion:")
else:
    print("Roll number not found.")

print("Roll No : Name ->", student)
print("Roll No : Marks ->", student_marks)
print("Roll No : Attendance% ->", student_att)
