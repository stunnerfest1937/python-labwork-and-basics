a=int(input ("no of students in class a "))
b=int(input ("no of students in class b "))
c=int(input ("no of students in class c "))

if a%2==0:
    bench_a=int(a/2)
else:
    bench_a=int(a/2)+1

if b%2==0:
    bench_b=int(b/2)
else:
    bench_b=int(b/2)+1

if c%2==0:
    bench_c=int(c/2)
else:
    bench_c=int(c/2)+1

print("no of benches required in class a is ",bench_a)
print (" no of benches required in class b is ",bench_b)
print ( "no of benches required in class c is ",bench_c)
bench=bench_a+bench_b+bench_c
print ("total no of benches required is ",bench)    