lst=[3,4,5,6,7,8]

square=[num**2 for num in lst]

print(square)

cubes=[num**3 for num in lst]

print(cubes)

add_two=[num+2 for num in lst]

print(add_two)

even=[num for num in lst if num%2==0]

print(even)

odd=[num for num in lst if num%2!=0]

print(odd)