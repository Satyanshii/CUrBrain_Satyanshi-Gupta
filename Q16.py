def second_highest(scores):
    highest = -1
    second = -1

    for score in scores:
        if score > highest:
            second = highest
            highest = score
        elif score < highest and score > second:
            second = score

    return second


scores = list(map(int, input("Enter scores separated by spaces: ").split()))
print("Second-highest distinct score:", second_highest(scores))
