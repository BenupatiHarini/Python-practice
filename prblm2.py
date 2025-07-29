def kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k):
    if k <= numOnes:
        return k
    if k <= numOnes + numZeros:
        return numOnes
    return numOnes - (k - numOnes - numZeros)

# Example usage
if __name__ == "__main__":
    numOnes = 3
    numZeros = 2
    numNegOnes = 4
    k = 6

    result = kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k)
    print("Maximum sum of k items:", result)
