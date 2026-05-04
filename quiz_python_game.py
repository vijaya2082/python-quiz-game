import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random

# ---------------- MAIN WINDOW ----------------

root = tk.Tk()
root.title("Quiz World")
root.geometry("1000x700")
root.config(bg="#0b1026")

# ---------------- VARIABLES ----------------

nickname = ""
score = 0
question_index = 0
selected_questions = []
timer_value = 20
timer_running = False

# ---------------- QUIZ DATA ----------------

quiz_data = {

    "Beginner": [

        {
            "question": "What does CPU stand for?",
            "options": [
                "Central Process Unit",
                "Central Processing Unit",
                "Computer Personal Unit",
                "Central Processor Utility"
            ],
            "answer": "Central Processing Unit"
        },

        {
            "question": "Which language is used for web pages?",
            "options": [
                "HTML",
                "Python",
                "Java",
                "C++"
            ],
            "answer": "HTML"
        },

        {
            "question": "What is Python?",
            "options": [
                "Snake",
                "Programming Language",
                "None",
                "A and B"
            ],
            "answer": "Programming Language"
        },

        {
            "question": "Which symbol is used for comments in Python?",
            "options": [
                "//",
                "#",
                "<!-- -->",
                "**"
            ],
            "answer": "#"
        },

        {
            "question": "Which company created Windows?",
            "options": [
                "Google",
                "Apple",
                "Microsoft",
                "Intel"
            ],
            "answer": "Microsoft"
        }
    ],

    "Intermediate": [

        {
            "question": "Which keyword is used for loops in Python?",
            "options": [
                "repeat",
                "loop",
                "for",
                "iterate"
            ],
            "answer": "for"
        },

        {
            "question": "Which collection type is immutable?",
            "options": [
                "List",
                "Dictionary",
                "Tuple",
                "Set"
            ],
            "answer": "Tuple"
        },

        {
            "question": "Which operator checks equality?",
            "options": [
                "=",
                "==",
                "!=",
                ">"
            ],
            "answer": "=="
        },

        {
            "question": "Which keyword creates function?",
            "options": [
                "func",
                "def",
                "define",
                "create"
            ],
            "answer": "def"
        },

        {
            "question": "Which data type stores True or False?",
            "options": [
                "int",
                "float",
                "bool",
                "string"
            ],
            "answer": "bool"
        }
    ],

    "Advanced": [

        {
            "question": "Which library is used for data analysis?",
            "options": [
                "Pandas",
                "Tkinter",
                "Random",
                "Turtle"
            ],
            "answer": "Pandas"
        },

        {
            "question": "Which keyword handles exceptions?",
            "options": [
                "catch",
                "try",
                "error",
                "final"
            ],
            "answer": "try"
        },

        {
            "question": "Which keyword creates class?",
            "options": [
                "class",
                "oop",
                "object",
                "define"
            ],
            "answer": "class"
        },

        {
            "question": "Which library is used for GUI?",
            "options": [
                "NumPy",
                "Pandas",
                "Tkinter",
                "Matplotlib"
            ],
            "answer": "Tkinter"
        },

        {
            "question": "Which operator gives remainder?",
            "options": [
                "%",
                "/",
                "+",
                "*"
            ],
            "answer": "%"
        }
    ]
}

# ---------------- FUNCTIONS ----------------

def clear_screen():
    global timer_running
    timer_running = False

    for widget in root.winfo_children():
        widget.destroy()

# ---------------- HOME SCREEN ----------------

def home_screen():

    clear_screen()

    title = tk.Label(
        root,
        text="🌌 QUIZ WORLD 🌌",
        font=("Arial", 40, "bold"),
        fg="#38bdf8",
        bg="#0b1026"
    )

    title.pack(pady=120)

    subtitle = tk.Label(
        root,
        text="Space Galaxy Quiz Game 🚀",
        font=("Arial", 22),
        fg="white",
        bg="#0b1026"
    )

    subtitle.pack(pady=10)

    start_btn = tk.Button(
        root,
        text="START GAME",
        font=("Arial", 18, "bold"),
        bg="#6d28d9",
        fg="white",
        activebackground="#7c3aed",
        activeforeground="white",
        padx=30,
        pady=15,
        relief="raised",
        bd=5,
        cursor="hand2",
        command=nickname_screen
    )

    start_btn.pack(pady=40)

# ---------------- NICKNAME SCREEN ----------------

def nickname_screen():

    clear_screen()

    title = tk.Label(
        root,
        text="ENTER YOUR NICKNAME",
        font=("Arial", 30, "bold"),
        fg="#38bdf8",
        bg="#0b1026"
    )

    title.pack(pady=100)

    nickname_entry = tk.Entry(
        root,
        font=("Arial", 22),
        width=20,
        justify="center",
        bd=5
    )

    nickname_entry.pack(pady=20, ipady=10)

    def save_nickname():

        global nickname

        nickname = nickname_entry.get()

        if nickname == "":
            messagebox.showwarning(
                "Warning",
                "Please enter nickname"
            )
            return

        level_screen()

    next_btn = tk.Button(
        root,
        text="NEXT ➜",
        font=("Arial", 18, "bold"),
        bg="#6d28d9",
        fg="white",
        padx=30,
        pady=10,
        bd=5,
        command=save_nickname
    )

    next_btn.pack(pady=30)

# ---------------- LEVEL SCREEN ----------------

def level_screen():

    clear_screen()

    title = tk.Label(
        root,
        text=f"Welcome {nickname} 🚀",
        font=("Arial", 30, "bold"),
        fg="#facc15",
        bg="#0b1026"
    )

    title.pack(pady=50)

    level_title = tk.Label(
        root,
        text="SELECT LEVEL",
        font=("Arial", 26, "bold"),
        fg="white",
        bg="#0b1026"
    )

    level_title.pack(pady=20)

    def start_level(level):

        global selected_questions
        global question_index
        global score

        score = 0
        question_index = 0

        selected_questions = random.sample(
            quiz_data[level],
            len(quiz_data[level])
        )

        loading_screen()

    beginner_btn = tk.Button(
        root,
        text="🌟 BEGINNER",
        font=("Arial", 18, "bold"),
        bg="#6d28d9",
        fg="white",
        width=20,
        pady=10,
        bd=5,
        command=lambda: start_level("Beginner")
    )

    beginner_btn.pack(pady=15)

    intermediate_btn = tk.Button(
        root,
        text="⚡ INTERMEDIATE",
        font=("Arial", 18, "bold"),
        bg="#6d28d9",
        fg="white",
        width=20,
        pady=10,
        bd=5,
        command=lambda: start_level("Intermediate")
    )

    intermediate_btn.pack(pady=15)

    advanced_btn = tk.Button(
        root,
        text="🔥 ADVANCED",
        font=("Arial", 18, "bold"),
        bg="#6d28d9",
        fg="white",
        width=20,
        pady=10,
        bd=5,
        command=lambda: start_level("Advanced")
    )

    advanced_btn.pack(pady=15)

# ---------------- LOADING SCREEN ----------------

def loading_screen():

    clear_screen()

    label = tk.Label(
        root,
        text="🚀 Loading Quiz...",
        font=("Arial", 35, "bold"),
        fg="#38bdf8",
        bg="#0b1026"
    )

    label.pack(pady=220)

    progress = ttk.Progressbar(
        root,
        orient="horizontal",
        length=500,
        mode="determinate"
    )

    progress.pack(pady=20)

    for i in range(101):
        progress["value"] = i
        root.update_idletasks()
        root.after(15)

    question_screen()

# ---------------- TIMER ----------------

def update_timer():

    global timer_value
    global timer_running

    if not timer_running:
        return

    timer_label.config(
        text=f"⏰ TIME LEFT: {timer_value}s"
    )

    if timer_value > 0:
        timer_value -= 1
        root.after(1000, update_timer)

    else:
        messagebox.showinfo(
            "Time Up",
            "Moving to next question"
        )

        auto_next_question()

# ---------------- AUTO NEXT ----------------

def auto_next_question():

    global question_index

    question_index += 1

    if question_index < len(selected_questions):
        question_screen()
    else:
        result_screen()

# ---------------- QUESTION SCREEN ----------------

def question_screen():

    clear_screen()

    global timer_value
    global timer_running

    timer_running = True
    timer_value = 20

    current_question = selected_questions[question_index]

    top_frame = tk.Frame(
        root,
        bg="#0b1026"
    )

    top_frame.pack(fill="x", pady=10)

    player_label = tk.Label(
        top_frame,
        text=f"👤 PLAYER: {nickname}",
        font=("Arial", 18, "bold"),
        fg="white",
        bg="#0b1026"
    )

    player_label.pack(side="left", padx=20)

    score_label = tk.Label(
        top_frame,
        text=f"⭐ SCORE: {score}",
        font=("Arial", 18, "bold"),
        fg="#facc15",
        bg="#0b1026"
    )

    score_label.pack(side="right", padx=20)

    global timer_label

    timer_label = tk.Label(
        root,
        text="⏰ TIME LEFT: 20s",
        font=("Arial", 18, "bold"),
        fg="#f87171",
        bg="#0b1026"
    )

    timer_label.pack(pady=10)

    progress = ttk.Progressbar(
        root,
        orient="horizontal",
        length=600,
        mode="determinate"
    )

    progress.pack(pady=20)

    progress["maximum"] = len(selected_questions)
    progress["value"] = question_index + 1

    question_label = tk.Label(
        root,
        text=current_question["question"],
        font=("Arial", 28, "bold"),
        fg="#38bdf8",
        bg="#0b1026",
        wraplength=800
    )

    question_label.pack(pady=40)

    option_var = tk.StringVar()

    option_buttons = []

    for option in current_question["options"]:

        rb = tk.Radiobutton(
            root,
            text=option,
            variable=option_var,
            value=option,
            font=("Arial", 18),
            bg="#0b1026",
            fg="white",
            selectcolor="#312e81",
            activebackground="#0b1026",
            activeforeground="white"
        )

        rb.pack(anchor="w", padx=300, pady=10)

        option_buttons.append(rb)

    def check_answer():

        global question_index
        global score
        global timer_running

        timer_running = False

        selected_option = option_var.get()

        if selected_option == "":
            messagebox.showwarning(
                "Warning",
                "Select an option"
            )
            return

        correct_answer = current_question["answer"]

        for rb in option_buttons:

            if rb.cget("text") == correct_answer:
                rb.config(
                    fg="lime"
                )
                rb.config(
                    text=rb.cget("text") + " ✅ CORRECT"
                )

            elif rb.cget("text") == selected_option:
                rb.config(
                    fg="red"
                )
                rb.config(
                    text=rb.cget("text") + " ❌ WRONG"
                )

        if selected_option == correct_answer:

            score += 1

            result_label = tk.Label(
                root,
                text="😊 CORRECT ANSWER!",
                font=("Arial", 22, "bold"),
                fg="lime",
                bg="#0b1026"
            )

            result_label.pack(pady=20)

        else:

            result_label = tk.Label(
                root,
                text="😢 WRONG ANSWER!",
                font=("Arial", 22, "bold"),
                fg="red",
                bg="#0b1026"
            )

            result_label.pack(pady=20)

        next_btn.config(state="disabled")

        root.after(2500, go_next)

    def go_next():

        global question_index

        question_index += 1

        if question_index < len(selected_questions):
            question_screen()
        else:
            result_screen()

    next_btn = tk.Button(
        root,
        text="SUBMIT",
        font=("Arial", 18, "bold"),
        bg="#6d28d9",
        fg="white",
        padx=30,
        pady=12,
        bd=5,
        command=check_answer
    )

    next_btn.pack(pady=40)

    update_timer()

# ---------------- RESULT SCREEN ----------------

def result_screen():

    clear_screen()

    total_questions = len(selected_questions)

    percentage = (score / total_questions) * 100

    if percentage >= 80:
        result = "EXCELLENT 🌟"
        color = "#22c55e"

    elif percentage >= 50:
        result = "GOOD 😊"
        color = "#facc15"

    else:
        result = "NEED PRACTICE 😢"
        color = "#ef4444"

    trophy = tk.Label(
        root,
        text="🏆",
        font=("Arial", 100),
        bg="#0b1026"
    )

    trophy.pack(pady=10)

    title = tk.Label(
        root,
        text="QUIZ COMPLETED",
        font=("Arial", 35, "bold"),
        fg="#38bdf8",
        bg="#0b1026"
    )

    title.pack(pady=20)

    player_label = tk.Label(
        root,
        text=f"👤 PLAYER: {nickname}",
        font=("Arial", 22),
        fg="white",
        bg="#0b1026"
    )

    player_label.pack(pady=10)

    score_label = tk.Label(
        root,
        text=f"⭐ SCORE: {score}/{total_questions}",
        font=("Arial", 24, "bold"),
        fg="#facc15",
        bg="#0b1026"
    )

    score_label.pack(pady=10)

    percentage_label = tk.Label(
        root,
        text=f"📊 PERCENTAGE: {percentage:.2f}%",
        font=("Arial", 24, "bold"),
        fg="#38bdf8",
        bg="#0b1026"
    )

    percentage_label.pack(pady=10)

    result_label = tk.Label(
        root,
        text=result,
        font=("Arial", 28, "bold"),
        fg=color,
        bg="#0b1026"
    )

    result_label.pack(pady=20)

    play_again_btn = tk.Button(
        root,
        text="PLAY AGAIN 🔄",
        font=("Arial", 18, "bold"),
        bg="#6d28d9",
        fg="white",
        padx=30,
        pady=12,
        bd=5,
        command=home_screen
    )

    play_again_btn.pack(pady=15)

    exit_btn = tk.Button(
        root,
        text="EXIT GAME ❌",
        font=("Arial", 18, "bold"),
        bg="#ef4444",
        fg="white",
        padx=30,
        pady=12,
        bd=5,
        command=root.destroy
    )

    exit_btn.pack(pady=10)

# ---------------- START APP ----------------

home_screen()

root.mainloop()