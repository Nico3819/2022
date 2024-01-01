word = 'abcdefghijklmnopqrstuvwxyz'
myword = "test"

n = 0
for x in myword:	
    for q in word:
      n = n + 1
      if x == q:
        print q
        print n
        print word[n]
      
