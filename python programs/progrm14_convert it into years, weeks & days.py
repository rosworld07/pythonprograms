# accept number of days from user and convert it into years, weeks & days.




days =int(input("enter days"))
yrs =int( days/365); # Here, leap years are ignored
 
weeks = int((days%365)/7);

days = days-((yrs*365) + (weeks*7));
print("year ="+str(yrs))
print("week ="+str(weeks))
print("days ="+str(days))



