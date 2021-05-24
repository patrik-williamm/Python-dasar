
# count final value students
# var count
FinalScore = 0

# input name values 

print("\nInsert Data Students\n");

name = input("Insert name student 	: ")
valueF = int(input("insert Final value 	: "))
valueF *= 50/100
valueT = int(input("Insert Task value 	: "))
valueT *= 30/100
valueA = int(input("insert Activit value 	: "))
valueA *= 20/100

# count all value students

FinalScore = valueA + valueT + valueF
print("\nValue Students\n")
print("student name 	: ",name)
print("Final Score 	: ",FinalScore)