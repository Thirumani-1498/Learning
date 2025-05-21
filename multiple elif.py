score=int(input("enter your score:"))
if (score<35):
    print("FAIL")
elif (score>=35 and score<70):
    print("PASS with average score")
elif (score>=70 and score<100):
    print("PASS with distinction score")
else:
    print("invalid entry")

