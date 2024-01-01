playera = input ('''enter player a's score:  ''')
playerb = input ('''enter player b's score:  ''')
playerc = input ('''enter player c's score:  ''')

if playera > playerb and playera > playerc:
  print 'player a wins'
elif playerb > playera and playerb > playerc:
  print 'player b wins'
elif playerc > playera and playerc > playerb:
  print 'player c wins'
elif playera == playerb and playera > playerc:
  print 'player a and player b tied'
elif playera == playerc and playera > playerb:
  print 'player a and player c tied'
elif playerb == playerc and playerb > playera:
  print 'player b and player c tied'
elif playera == playerb and playera == playerc:
  print 'player a and player b and player c tied'
