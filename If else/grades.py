grade = float(input("Input a grade: ")) # Do not change this line

# Fill in the missing code below

if grade < 0 or grade >10:
  print("Invalid grade!") # Do not change this line
elif grade >= 5 and grade < 10.1:
  print("Passing grade!") # Do not change this line
elif grade < 5 and grade > 0:
  print("Failing grade!") # Do not change this line