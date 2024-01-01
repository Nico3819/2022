while True:
  month = raw_input ('enter a month:  ')

  if month == 'january' or month == 'march' or month == 'may' or month == 'july' or month == 'august' or month == 'october' or month == 'december':
    print '31 days'
  elif month == 'febuary':
    print '29 days'
  elif month == 'april' or month == 'june' or month == 'september' or month == 'novemver':
    print '30 days'  
  elif month == 'exit':   
    break
  else:
    print 'invalid month'
