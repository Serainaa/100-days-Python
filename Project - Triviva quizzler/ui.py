from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Canvas.
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=200, text="QUESTION", fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons.
        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.my_answer_is_false)
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.my_answer_is_true)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        # Labels.
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.show_question()
        self.window.mainloop()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def show_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You finished the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def my_answer_is_true(self):
        if self.quiz.check_answer("True"):
            self.update_score()
            self.give_feedback(0)
        else:
            self.give_feedback(1)

    def my_answer_is_false(self):
        if self.quiz.check_answer("False"):
            self.update_score()
            self.give_feedback(0)
        else:
            self.give_feedback(1)

    def give_feedback(self, output):
        if output:
            self.canvas.config(bg="red")
        else:
            self.canvas.config(bg="green")
        self.window.after(1000, self.show_question)

