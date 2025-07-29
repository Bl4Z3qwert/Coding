start = int(input("Start range: "))
end = int(input("End range: "))

squares = [x**2 for x in range(start, end + 1)]
even_squares = [x for x in squares if x % 2 == 0]
odd_squares = [x for x in squares if x % 2 != 0]

print("Even Squares:", even_squares)
print("Odd Squares:", odd_squares)
