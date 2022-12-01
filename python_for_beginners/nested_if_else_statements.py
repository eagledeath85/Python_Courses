student_score = int(input("What is the student score? "))
if student_score >= 90:
    print("A grade")
else:
    if student_score >= 80:
        print("B grade")
    else:
        if student_score >= 70:
            print("C grade")
        else:
            if student_score >= 60:
                print("D grade")
            else:
                print("F grade")
