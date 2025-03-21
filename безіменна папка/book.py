class Book:
    def __init__(self, pages):
        self.pages = pages
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < len(self.pages):
            page = self.pages(self.current)
            self.current += 1
            return page
        else:
            raise StopIteration
        
book = Book("page 1", "page 2", "page 3")

for page in book:
    print(page)
