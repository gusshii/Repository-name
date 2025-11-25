numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

a = numbers.index(None)

sred = sum(x for x in numbers if x is not None) / len(numbers)

numbers[a] = sred
print("Измененный список:", numbers)
