students = [['Harsh', 20], ['Beria', 20], ['Varum', 19], ['Kakunami', 19], ['Viras', 21]]
# students = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     students.append([name, score])

scores = []
newScores = {}
for i in students:
    scores.append(i[1])

minScore = min(scores)

for i in scores:
    if i == minScore:
        students.pop(scores.index(i))

for k in students:
    newScores[k[1]] = students.index(k)

NewMinElement = min(newScores.keys())
names = []
for i in students:
    if i[1] == NewMinElement:
        names.append(i[0])

for k in sorted(names):
    print(k)