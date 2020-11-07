from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

q_bank=[]

for question in question_data:
  question_text = question['text']
  question_answer = question['answer']
  new_question = Question(question_text, question_data)
  q_bank.append(new_question)

sample = QuizBrain(q_bank)
sample.next_question()









