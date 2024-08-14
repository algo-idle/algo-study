import math

def main():
    userInput = input().split()

    diagonal, heightRatio, widthRatio = userInput

    heightSquare = int(diagonal)**2 / (1 + int(widthRatio)**2 / int(heightRatio)**2)
    height = math.sqrt(heightSquare)
    width = height * int(widthRatio)/int(heightRatio)

    print(math.floor(height))
    print(math.floor(width))


main()