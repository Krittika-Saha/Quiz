from question_model import Question
from data import question_data
from quiz_brain import QuizBrain, final_score
from user import User

q_bank=[]

user_name = input('Hi! Pls input your first name:')
for question in question_data:
  question_text = question['text']
  question_answer = question['answer']
  new_question = Question(question_text, question_data)
  q_bank.append(new_question)

quiz = QuizBrain(q_bank)
quiz.next_question()

globals()[user_name] = User(user_name, final_score)
globals()[user_name].record_me()


