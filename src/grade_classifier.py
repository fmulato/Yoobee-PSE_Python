''''Grade classifier

Objective: Create a program that takes students' scores as input and assigns a grade based on the score. The grades should be A, B, C, D, or F.
Requirements:
• Ask for user input(format: [score1,score2,score3,…])
• Utilize a list to store scores and their corresponding grades.
• Iterate over the list of scores using a loop.
• Use comparison operators within conditional statements to determine the appropriate grade for each score.
• Print each student's score (keep 1 place after point) along with their respective grade.
A: 90 and above
B: 80 to 89
C: 70 to 79
D: 60 to 69
F: below 60

'''

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
    scores.append(float(input(f"Enter your score {i+1} (0-100): ")))

# calculat the corresponding grade
grade = grade_classifier(qtd, scores)

dic = {}
for i in range(qtd):
    dic[scores[i]] = grade[i]

print(dic)