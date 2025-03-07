from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
# print(question_data)
question_bank=[]
for i in question_data:
    text=i['question']
    answer=i['correct_answer']
    question_bank.append(Question(text,answer))


quiz=QuizBrain(question_bank)
# quiz.next_question()
while quiz.still_hasquestions():

    quiz.next_question()
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
# print(question_bank)
# for i in question_bank:
#     print(i.text)
#     print(i.answer)