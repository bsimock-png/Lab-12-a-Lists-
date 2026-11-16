#CIS Week 12
#List Examples

#Old School
#one example per day

day1 = 72
day2 = 68
day3 = 105
day4 = 22
day5 = -50



temps = [72, 68, 105, 22, -50]

print(temps)
print(temps[0])
print(temps[4])
temps[1] = 77
print(temps)

print(len(temps))
print()
print()
print("================================")


NUM_SCORES = 5

scores = []
for i in range(NUM_SCORES):
    score = int(input("Enter a score: "))
    scores.append(score)



    for i in range(len(scores)):
        print("Quiz", i + 1, "score:", scores[i])

print() 
print()
print("================================")


total = 0
for score in scores:
    total += score
average = total / len(scores)

highest = scores[0]
lowest = scores[0]
for score in scores:
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score

print("Total:", total)
print("Average:", format(average))
print("Highest:", highest)
print("Lowest:", lowest)

