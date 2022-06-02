from data import question_data
from quze_brain import QuizBrain
from question_model import Question


question_bank = []

for question in question_data:
    text_question = question['question']
    answer_question = question['correct_answer']
    new_question = Question(text_question, answer_question)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()


print('You\'ve completed the quiz')
print(f'Your final score was: {quiz.question_number}/{len(question_bank)}')

