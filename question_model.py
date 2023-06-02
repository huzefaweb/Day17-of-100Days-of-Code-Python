# class is a blueprint use to create objects
# syntax:     class ClassName:
# classes are named using pascal clause
class Question:
    def __init__(self, new_question, new_answer):  # constructor
        # attributes are things which object has
        self.text = new_question
        self.answer = new_answer

