def run(): 
  grade1 = input("Enter your course 1 letter grade: ")
  course1 = float(input("Enter your course 1 credit: "))
  gradepoint1 = getGradePoint(grade1)
  print(f"Grade point for course 1 is: {gradepoint1}")
  grade2 = input("Enter your course 2 letter grade: ")
  course2 = float(input("Enter your course 2 credit: "))
  gradepoint2 = getGradePoint(grade2)
  print(f"Grade point for course 2 is: {gradepoint2}")
  grade3 = input("Enter your course 3 letter grade: ")
  course3 = float(input("Enter your course 3 credit: "))
  gradepoint3 = getGradePoint(grade3)
  print(f"Grade point for course 3 is: {gradepoint3}")
  GPA = (float(course1) * gradepoint1 + float(course2) * gradepoint2 + float(course3) * gradepoint3)/ (float(course1) + float(course2) + float(course3))
  print(f"Your GPA is: {GPA}") 
def getGradePoint(grade):
  if grade == "A":
    return 4.0
  elif grade == "A-":
    return 3.67
  elif grade == "B+":
    return 3.33
  elif grade == "B":
    return 3.0
  elif grade == "B-":
    return 2.67
  elif grade == "C+":
    return 2.33
  elif grade == "C":
    return 2.0
  elif grade == "D":
    return 1.0
  elif grade == "F":
    return 0.0
  else:
    return 0.0

if __name__ == "__main__":
  run()