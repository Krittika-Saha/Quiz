class User:

  def __init__(self, name, game_score):
    self.name = name
    self.game_score = game_score

  def record_me(self):
    users = open('users.txt', 'r+')
    users.write(f'{self.name}, {self.game_score}\n')
    users.close()





# user_name = input('Name:')
# globals()[user_name] = 4
# print(globals()[user_name])
# users = open('users.txt', 'r+')
# print(len(users.readlines()))
