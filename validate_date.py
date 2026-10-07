def is_leap_year (year):
    if year %400==0 :
     return True
    if year % 100==0  :      
     return False
    if year %4==0 :
      return True
    return False

def is_valid_date (day , month , year) :
   if year<1 :
     return False
   if month <1 or month > 12 :
     return False

   if month in (1,3,5,7,8,10,12) :
    max_days=31 
   elif month in (4,6,9,11):
     max_days=30
   elif month ==2 :
     if is_leap_year (year):
       max_days=29
     else :
       max_days  =28


   if day<1 or day>max_days :
    return False

   return True



print (is_valid_date(29,2,2024))
print(is_valid_date(29,2,2025))

     

