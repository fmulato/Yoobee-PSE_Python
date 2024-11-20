'Grade classifier'

# function to calculate score in letter
def grade_classifier(qtd, marks):
    grade = list(range(qtd))
    for s in range (qtd):
        if marks[s] >= 90:
            grade[s] = 'A'
        elif 80 <= marks[s] < 90:
            grade[s] = 'B'
        elif 70 <= marks[s] < 80:
            grade[s] = 'C'
        elif 60 <= marks[s] < 70:
            grade[s] = 'D'
        elif marks[s] < 60:
            grade[s] = 'F'
    return grade

scores = []
scores_new = []

qtd = int(input("Enter the amount of scores: "))
for i in range(qtd): # add element into the list scores
    scores.append(float(input(f"Enter your score {i+1}: ")))

# calculat the corresponding grade
grade = grade_classifier(qtd, scores)

dic = {}
for i in range(qtd):
    dic[scores[i]] = grade[i]

print(dic)