student_marks = {"Harsh" : [25, 26.5, 28], "Anurag" : [26, 28, 30]}

query_name = "Harsh"

for k in student_marks.items():
    if (k[0]) == query_name:
        average = sum(k[1])/len(k[1])

print(f"{average:.2f}")