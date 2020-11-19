from data import question_data

final_score = '0'

class QuizBrain:

  def __init__(self, q_list):
    self.q_list = q_list
    self.score = 0

  def check_answer(self, user_answer, correct_answer, question_number):
    if user_answer.lower() == correct_answer.lower():
      self.score += 1
      print('You got it right!')
    else:
      print('Nope!')
    print(f'The correct answer is {correct_answer}')
    print(f'Your score is: {self.score}/{question_number+1}')
  def next_question(self):

    for question_number in range (12):
      answer = input(f'Q.{question_number+1} {self.q_list[question_number].text} (True/False):')
      correct_answer = question_data[question_number]['answer']
      self.check_answer(answer,correct_answer, question_number)
    final_score = self.score
    return final_score

print(final_score)




    