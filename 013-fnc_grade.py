def calGrade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

scoreKor = int(input("국어 점수: "))
scoreEng = int(input("영어 점수: "))
scoreMath = int(input("수학 점수: "))

gradeKor = calGrade(scoreKor)
gradeEng = calGrade(scoreEng)
gradeMath = calGrade(scoreMath)

print("국어 학점: ", gradeKor)
print("영어 학점: ", gradeEng)
print("수학 학점: ", gradeMath)