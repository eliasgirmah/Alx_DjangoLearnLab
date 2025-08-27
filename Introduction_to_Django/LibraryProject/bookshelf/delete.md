```python

from bookshelf.modules import Book

book=Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
