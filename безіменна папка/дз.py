data = [("яблуко", 3), ("банан", 2), ("вишня", 5), ("груша", 1)]

# Сортуємо список за другим елементом кортежу
sorted_data = sorted(data, key=lambda x: x[1])

print(sorted_data)
