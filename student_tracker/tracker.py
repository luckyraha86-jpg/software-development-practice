import json
import os
FILENAME = "student_tracker/student.json"

def load_all_students():
    try:
        if not os.path.exists(FILENAME):
                return []
        else:
            with open(FILENAME, "r")as f:
                data = json.load(f)
                return data

    except json.JSONDecodeError:
        return []
    
def save_record(student):
    with open(FILENAME, "w")as f:
        json.dump(student, f, indent=4)

def add_student(name, roll_number, subject):
    record = load_all_students()
    student = {
        "name" : name,
        "roll_number" : roll_number,
        "subject" : subject
    }

    record.append(student)
    save_record(record)
    print(f"Student {name} with roll number {roll_number} and subjects: {subject} is added successfully to the database")

def show_all_records():
    return load_all_students()
    
def average():
    records = load_all_students()
    avgs = [
        {"name" : student["name"],
        "avg" : (sum(student["subject"])) / len(student["subject"])}
        for student in records
    ]

    return avgs


def search_student(roll):
    record = load_all_students()
    student = [
            {"name" : student["name"],
             "roll" : student["roll number"],
             "subject_marks" : student["subject"],
             "total_marks" : sum(student["subject"])}
            for student in record
            if student["roll number"] == roll
        ]

    return student