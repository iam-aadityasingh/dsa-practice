def traingle(l):
    total = [1]
    for i in range(len(l) - 1):
        total.append(l[i] + l[i + 1])
    total.append(1)
    return total

def generate(numRows):
    finalList = []
    if numRows >= 1:
        finalList.append([1])
    if numRows >= 2:
        finalList.append([1, 1])
    for i in range(2, numRows):
        next_row = traingle(finalList[-1])
        finalList.append(next_row)
    return finalList

# Example usage:
print(generate(5)) #use numRows i.e the input length
