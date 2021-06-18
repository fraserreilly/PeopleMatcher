preferredStudentChoices = {
    "peter": ["mit", "stanford", "berkley", "cornell"],
    "tim": ["mit", "cornell", "berkley", "stanford"],
    "julie": ["stanford", "cornell", "mit", "berkley"],
    "sarah": ["berkley", "mit", "stanford", "cornell"],
}

preferredUniversityChoices = {
    "mit": ["peter", "tim", "sarah", "julie"],
    "cornell": ["tim", "julie", "sarah", "peter"],
    "stanford": ["sarah", "julie", "tim", "peter"],
    "berkley": ["sarah", "julie", "tim", "peter"]
}

# keeps track of the current matches for students and unis
currentUniversitiesStudents = []

# keeps track of students that don't currently have a uni
unassignedStudents = []


def initUnassignedStudents():
    for student in preferredStudentChoices:
        unassignedStudents.append(student)


def matching():
    while(len(unassignedStudents) > 0):
        for student in unassignedStudents:
            matchStudent(student)


def matchStudent(student):
    print(f"Matching {student} with university")
    for university in preferredStudentChoices[student]:
        currentMatch = [
            pair for pair in currentUniversitiesStudents if university in pair]
        if (len(currentMatch) == 0):
            currentUniversitiesStudents.append([student, university])
            unassignedStudents.remove(student)
            print(f"{student} no longer has no university")
            break
        elif (len(currentMatch) > 0):
            print(f"{university} has multiple different student interests")
            currentStudent = preferredUniversityChoices[university].index(
                currentMatch[0][0])
            potentialStudent = preferredUniversityChoices[university].index(
                student)

            if (currentStudent < potentialStudent):
                print(f"{university} thinks {student} is the better choice")
            else:
                print(f"{currentStudent} is a better match than {potentialStudent}")
                unassignedStudents.remove(student)
                unassignedStudents.append(currentMatch[0][0])

                currentMatch[0][0] = student
                break


def main():
    initUnassignedStudents()
    matching()
    print("Complete list of universities and chosen students")
    print(currentUniversitiesStudents)


if __name__ == "__main__":
    main()
