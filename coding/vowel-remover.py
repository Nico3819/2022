import sys
word = raw_input ('enter a word:  ')

for x in word:
  if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u': 
    del x  
  else:
    sys.stdout.write(x)
    
sys.stdout.write("\n")



