dsk_mb = 1.44
pages = 100
lines = 50
chars = 25
byte = 4

disk_b = dsk_mb * 1024 * 1024
symbols_book = pages * lines * chars
book_b = symbols_book * byte
books_count = int(disk_b // book_b)

print("Количество книг, помещающихся на дискету:",books_count)
