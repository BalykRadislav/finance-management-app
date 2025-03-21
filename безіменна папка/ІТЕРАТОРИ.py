# __iter__ - метод що повертає ітератор
# __next__ - метод що повертає наступний елемент ітератора


# ---------------------------------------

# num = [1, 2, 3, 4, 5]
# num_iter = iter(num)


# print(next(num_iter))
# print(next(num_iter))
# print(next(num_iter))
# print(next(num_iter))
# print(next(num_iter))


# ---------------------------------------

# class Count_down:
#     def __init__(self, start):
#         self.current = start


#     def __iter__(self):
#         return self
    

#     def __next__(self):
#         if self.current > 0:
#             num = self.current
#             self.current -= 1
#             return num

#         else:
#             raise StopIteration

# count_down = Count_down(10)

# for num in count_down:
#     print(num)


# ---------------------------------------

# class Book:
#     def __init__(self, pages):
#         self.pages = pages
#         self.current = 0

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current < len(self.pages):
#             page = self.pages(self.current)
#             self.current += 1
#             return page
#         else:
#             raise StopIteration
        
# book = Book("page 1", "page 2", "page 3")

# for page in book:
#     print(page)

# ---------------------------------------

