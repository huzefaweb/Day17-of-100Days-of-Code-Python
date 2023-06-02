from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []  # empty list

for x in question_data:  # loop to transfer data from data module to empty list "question bank"
    question_text = x["text"]
    question_answer = x["answer"]
    new_question = Question(question_text, question_answer)  # Object created to pass parameters to class
    # attribute syntax: object_name.attribute_name
    question_bank.append(new_question)  # append the object to empty list

quiz = QuizBrain(question_bank)  # object passes the question_bank as
quiz.next_question()  # Method calling performs the specific action inside the method

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz")
print(f"You total score is {quiz.score}/{quiz.question_number}")
