hr=int(input("enter the hour (in 12 hour format) "))
min=int(input("enter the minutes "))
sec=int(input("enter the seconds "))
if hr>11 or min>60 or sec>60:
    print("invalid input")

else:
 if hr==12:
    hr=0

hrdegree=30*hr
mindegree=0.5*min
secdegree=0.041*sec
totaldegree=hrdegree+mindegree+secdegree
print("the angle between hour hand and minute hand is ",totaldegree)
