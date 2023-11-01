x = int(input("Please enter a five-digit number: "))

first = x // 10000
second = x // 1000 % 10
third = x // 100 % 10
fourth = x // 10 % 10
fifth = x % 10

y = fifth * 10000 + fourth * 1000 + third * 100 + second * 10 + first
print(y)

print('If the result is displayed incorrectly, ensure you entered a five-digit number, e.g., 12345.')