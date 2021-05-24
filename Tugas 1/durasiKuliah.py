
# program count time lecture

# input start time lecture

# variable count minute & second
countHour = 0
countMinute = 0
countSecond = 0 


print("Time start lecture");

stHour = int(input("insert hour start 	: "))
stMinute = int(input("insert minute start 	: "))
stSecond = int(input("insert second start 	: "))

# input finish time lecture
print("\nTime finish lecture")

fhHour = int(input("insert hour finish 	: "))

# calculate durasi lecture

countHour = fhHour - stHour


fhMinute = int(input("insert minute finish 	: "))

if fhMinute < stMinute:
	countMinute = stMinute - fhMinute
	pass
else :
	countMinute = fhMinute - stMinute
	pass


fhSecond = int(input("insert second finish 	: "))

if fhSecond < stSecond:
	countSecond = stSecond - fhSecond
	pass
else :
	countSecond = fhSecond - stSecond
	pass

# print to console for user

print("\n\n")
print("Durasi Hour lecture 	: ",countHour)
print("Durasi Minute lecture 	: ",countMinute)
print("Durasi Second lecture 	: ",countSecond)