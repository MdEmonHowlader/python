# tup = (10, 20, 30, 40, 50)
# value = int(input("Enter a value to search: "))

# if value in tup:
#     print(f"Index of {value}: {tup.index(value)}")
# else:
#     print("Value not found in tuple.")

squares = [x ** 2 for x in range(1, 11)]

for num in squares:
    print(f"Square of {int(num ** 0.5)} is {num}")

    
    
scores = {"Alice": 85, "Bob": 90, "Charlie": 80}

max_student = max(scores, key=scores.get)
print(f"Top student: {max_student} with score {scores[max_student]}")

    
            