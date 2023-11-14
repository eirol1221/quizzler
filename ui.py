import tkinter
from tkinter import *
from tkinter import ttk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
CORRECT_COLOR = "#23AC6C"
WRONG_COLOR = "#EC5953"
WHITE = "#FFFFFF"


class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.category_label = Label(text="Select category:", font=("Arial", 12, "normal"), bg=THEME_COLOR, fg="white")
        self.category_label.grid(row=0, column=0, sticky='s')

        self.category = StringVar()
        self.combobox = ttk.Combobox(self.window, width=30, textvariable=self.category)
        self.combobox['values'] = ('Science', 'English')
        self.combobox.grid(row=1, column=0)

        self.score_label = Label(text="Score: 0", font=("Arial", 12, "normal"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=1, column=1, sticky='s')

        self.canvas = Canvas(width=400, height=280, bg=WHITE)
        self.canvas.grid(row=2, column=0, rowspan=2, padx=20, pady=20)

        self.quiz_text = self.canvas.create_text(200, 140, width=350, text=f"Some questions here",
                                                 font=("Arial", 18, "italic"), justify=CENTER)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_btn = Button(image=true_img, highlightthickness=0, borderwidth=0, bg=THEME_COLOR,
                               activebackground=THEME_COLOR, command=self.check_if_true)
        self.true_btn.grid(row=2, column=1, padx=20, pady=20)

        self.false_btn = Button(image=false_img, highlightthickness=0, borderwidth=0, bg=THEME_COLOR,
                                activebackground=THEME_COLOR, command=self.check_if_false)
        self.false_btn.grid(row=3, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def check_if_true(self):
        self.check_result(self.quiz.check_answer("True"))

    def check_if_false(self):
        self.check_result(self.quiz.check_answer("False"))

    def check_result(self, result):
        if result:
            self.canvas.config(bg=CORRECT_COLOR)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg=WRONG_COLOR)

        self.window.after(1000, self.get_next_question)

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.quiz_text, text=self.quiz.next_question())
            self.canvas.config(bg=WHITE)
        else:
            self.canvas.itemconfig(self.quiz_text, text=f"You've reached the end of the quiz.\n\n"
                                                        f"Your final score is "
                                                        f"{self.quiz.score}/{len(self.quiz.question_list)}.")
            self.canvas.config(bg=WHITE)
            self.true_btn.config(state=DISABLED)
            self.false_btn.config(state=DISABLED)


# TODO 1: Add a new feature: list of categories.
# TODO 2: Add a dropdown box or list box for the categories
# TODO 2: Reset score and question number when changing categories.