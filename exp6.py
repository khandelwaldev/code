def sumOfSqrOfEven(numbers):
    def recursiveSum(numbers):
        if not numbers:
            return 0
        else:
            first, *rest = numbers
            square = first**2 if first % 2 == 0 else 0
            return square + recursiveSum(rest)
    evenNum = filter(lambda X: X%2 == 0, numbers)
    squaredEven = map(lambda X: X**2, evenNum)
    
    return recursiveSum(list(squaredEven))
numbers = [1,2,3,4,5,6,7,8,9,10]
print(f'The sum of the square of the even numbers is {sumOfSqrOfEven(numbers)}')