students={}

print(" ")

for i in range(3):
    name=input("Name?:")
    age=input("Age?:")
    favourite_subject=input("Favourite subject?:")
    favourite_hobby=input("Favourite hobby?:")
    grade_math=input("Grade math?:")
    grade_english=input("Grade english?:")
    grade_biology=input("Grade biology?:")
    best_subject=input("Best subject?:")
    worst_subject=input("Worst subject?:")
    home_address=input("Home address?:")
    student1={
        "name":name,
        "age":age,
        "favourite_subject":favourite_subject,
        "favourite_hobby":favourite_hobby,
        "grade_math":grade_math,
        "grade_english":grade_english,
        "grade_biology":grade_biology,
        "best_subject":best_subject,
        "worst_subject":worst_subject
    }
    students[f"student{i+1}"]=student1
print(students)
print("")