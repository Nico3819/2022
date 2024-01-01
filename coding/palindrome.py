word = raw_input ('enter a word:  ')

firsthalf = []
secondhalf = []
whole = []
n = 0
wordlist = []

for x in word:
   n = n + 1
   whole.append(x)

nn = n
n = n / 2

if nn % 2 == 0:
  n = n + 0.5
nnn = n
#print n

for x in word:
  n = n - 1
  firsthalf.append(x)
  if n == 0:
    break

#print firsthalf
nn = nn - 1
for w in word:
  secondhalf.append(whole[nn])
  nn = nn - 1
  if nn == nnn:
    break

#print secondhalf
nn = nn + 1
for t in secondhalf:
  nn = nn - 1
 # print word[nn]

#print secondhalf
if secondhalf == firsthalf:
  print 'it is a palindrome'
else:
  print 'it is not a palindrome'
