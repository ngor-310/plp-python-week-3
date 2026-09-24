There are two syntax errors and one type error in this code:

Missing colon (:) on line 4 after while count < 5.

Type error on line 8 when trying to concatenate a string and an integer ("Sum of 1 to 5 is: " + total). You need to convert total to a string using str(total) or use an f-string.

Logic note: The loop condition count < 5 stops when count reaches 5, so it only adds numbers 1 through 4 (summing to 10). To sum 1 to 5, the condition should be count <= 5.
Here is the corrected code:
count = 1
total = 0

while count <= 5:
    total = total + count
    count = count + 1

print(f"Sum of 1 to 5 is: {total}")
Sum of 1 to 5 is: 15
