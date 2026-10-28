i=[1,2,3,5667,78,98,25,7,8,9,10]
for x in i :
    sqaure=x*x 
    numdigits=len(str(x))
    modvalue=10**numdigits
    lastdig=sqaure%modvalue
    
    
    if lastdig==x :
         print("The number is automorphic")
    else :
          print("The number is not automorphic")

