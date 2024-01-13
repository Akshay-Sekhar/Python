min_two=lambda n1,n2: n1 if n1<n2 else n2

odd_even=lambda n: "even" if n%2==0 else "odd"

num_chk=lambda n: "+ve" if n>0 else "-ve" 

print(odd_even(10))

print(min_two(10,20))

print(num_chk(25))