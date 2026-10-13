students = [
    {"id":101,"name":"Alice","score":85},
    {"id":102,"name":"Bob","score":78},
    {"id":103,"name":"Charlie","score":92}
    ]

# Name of ea{"id":101,"name":"Alice","score",85}ch studnets using loop
print("Name of All  Students : ")
for i in students:
    print(i["name"])


# Average score of all students
total = 0
for i in students:
    total += i["score"]

print("\nTotal score is : ",total)
print("Average score is : ",total/3)


# Adding new student

students.append({"id":104,"name":"XYZ","score":99})
print("\nStudent Added : ")
for i in students:
    print(i)


# Updating score of 102

students[1]["score"] = 88
print("\nRecord Updated : ")
for i in students:
    print(i)


# deleting record

for i in students:
    if i["name"] == "Charlie":
        students.remove(i)

print("\nCharlie Record Deleted : ")
for i in students:
    print(i)


# students score more than 80
print("\nStudents name who scored more than 80 : ")
for i in students:
    if i["score"] > 80:
        print(i["name"],i["score"])


# Sorting by score(descending)

students.sort(key = lambda i: i["score"],reverse=True)
print("\nStudents sorted by score(descending) : ")
for i in students:
    print(i)


# Find student with highest score 

top = max(students,key = lambda i: i["score"])
print("\nHighest scored student : \n",top)


# Creating Report
print()
for i in students:
    name = i["name"]
    sc = i["score"]
    
    if sc >= 90:
        grade = "A"
    elif sc >= 80:
        grade = "B"
    else:
        grade = "C"

    print(f"Name : {name} | Score : {sc} | Grade : {grade}")


# How many students get each grade
grade_counts = {"A": 0, "B": 0, "C": 0}

for i in students:
    sc = i["score"]
    
    # Determine the grade
    if sc >= 90:
        grade = "A"
    elif sc >= 80:
        grade = "B"
    else:
        grade = "C"
        
    grade_counts[grade] += 1

print("\nGrade Counts : ",grade_counts)


# Convert the list of dictionaries into a pandas DataFrame.
# Export the DataFrame to a CSV file.
# Re-import it and calculate mean, min, and max of the scores.
