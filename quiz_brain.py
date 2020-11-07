class QuizBrain:

  def __init__(self, q_list):
    self.q_list = q_list

  def next_question(self):

    for question_number in range (12):
      answer = input(f'Q.{question_number+1} {self.q_list[question_number].text} (True/False):')