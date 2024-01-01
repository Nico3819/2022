import random
number = random.randint (1,20)

guess = input ('enter a number 1-20:  ')

#while True:
if number == guess:
  print 'you guessed correct'
#   break
elif number > guess:
  print 'guess higher'
elif number < guess:
  print 'guess lower'
