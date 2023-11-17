import tkinter as tk
from tkinter import messagebox
import csv


def read_comments_from_csv(file_name):
    comments = {}
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for key in row:
                if key != 'Grade':
                    comments[key + row['Grade']] = row[key]
    return comments

def get_student_feedback(name, grades, comments):
    feedback = f"Hi {name}, thanks for your work this semester. "
    for i, grade in enumerate(grades):
        criterion = chr(65 + i)
        feedback += comments[criterion + grade] + " "
    feedback += "Good luck!"
    return feedback

def submit():
    name = name_entry.get()
    grades = grades_entry.get()
    feedback = get_student_feedback(name, grades, comments)
    feedback_text.delete("1.0", tk.END)
    feedback_text.insert(tk.END, feedback)
    feedback_text.tag_add("highlight", "1.0", "end")
    feedback_text.tag_config("highlight", background="white")
    #pyperclip.copy(feedback)
    name_entry.delete(0, tk.END)
    grades_entry.delete(0, tk.END)

# Main program
comments = read_comments_from_csv('comments.csv')

# Set up the tkinter window
root = tk.Tk()
root.title("Student Feedback Generator")

# Create and place widgets
tk.Label(root, text="Student Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Grades (e.g., 345):").grid(row=1, column=0)
grades_entry = tk.Entry(root)
grades_entry.grid(row=1, column=1)

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=2, column=0, columnspan=2)

# Text widget to display feedback
feedback_text = tk.Text(root, height=4, width=50)
feedback_text.grid(row=3, column=0, columnspan=2)

# Start the GUI event loop
root.mainloop()
