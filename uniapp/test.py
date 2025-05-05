import random



# Generate a list of random courses, ids, grades, and marks
courses = [
    "Mathematics", "Physics", "Chemistry", "Biology", "History",
    "Geography", "English", "Computer Science", "Economics", "Philosophy"
]

grades = ["A", "B", "C", "D", "E", "F"]

data = {
        "id": random.randint(1000, 9999),
        "course": random.choice(courses),
        "grade": random.choice(grades),
        "marks": random.randint(0, 100)
    }


def print_to_table(d):
    col_width = [x for x in d.keys()]
    # col_width = [x for x in col_width if len(x) == max(len(x))]
    print(col_width)

print_to_table(data)