student = {"name":"Alice",
           "age":20,
           "grade":"A"}

print("Student : ",student)

# Keys
print("\nKeys : ",student.keys())

# Values
print("Values : ",student.values())

#Adding new pair
student["city"] = "Delhi"
print("New List : ",student)

# update age
student["age"] = 21
print("Updated age : ",student)

# delete grade
student.pop("grade")
print("Delete Grade : ",student)
