import random
# Finding the median of a random set of even and odd integers
randomOdd = random.sample(range(0, 99), 15)
randomEven = random.sample(range(0, 99), 14)
print("15 random numbers:", randomOdd)
print("14 random numbers:", randomEven)


def medianfinder(median):
    x = len(median)
    count = x // 2
    if x % 2:
        return sorted(median)[count]
    else:
        return sum(sorted(median)[count - 1:count + 1]) / 2


print("The median of the list", randomOdd, "is", medianfinder(randomOdd), ".")
print("The median of the list", randomEven, "is", medianfinder(randomEven), ".")
print()
