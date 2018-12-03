example1="../Python_for_Data_Science/Week_4_Working_with_Data_in_Python/Example1.txt"


# with open(example1) as file1:
#   print(file1.read(4))
#   print(file1.read(4))
#   print(file1.read(7))
#   print(file1.read(15))

# with open(example1,'r') as file1:
#   print(file1.read(16))
#   print(file1.read(5))
#   print(file1.read(9))


with open(example1,"r") as file1:
  i=0
  for line in file1:
    print("Iteration", str(i),":",line)
    i=i+1
