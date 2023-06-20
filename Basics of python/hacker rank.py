
# n = int(input(6))
# if n % 2 != 0:
#     print("Weird")
# for n in range (2,5):
#     print ("Not Weird")
             
# else:
#     for n in range (6,20):
#       print ("Not weird")






# a=int(input("Enter the value of a:"))
# b=int(input("Enter the value of b:"))
# sum=a+b
# sub=a-b
# mul=a*b
# print(a,b)
# print("Sum =", sum) 
# print("Sub =", sub)
# print("mul =", mul)   


# n = int(input("Enter a non-negative integer: "))
# for i in range(n+1):        #  n+1 to iterate 0 to 1
#      print=(i**2)

# n = int(input("Enter a non-negative integer: "))

# for i in range(n):
#     print(i**2)
n = int(input("Enter an integer: "))

for i in range(1, n+1):
    print(i, end="")
    if i != n:
        print("*", end="")

print()