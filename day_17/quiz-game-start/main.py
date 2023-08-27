from question_data2 import question_data2
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for q_set in question_data2:
    new_question = Question(q_set['question'], q_set['correct_answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
