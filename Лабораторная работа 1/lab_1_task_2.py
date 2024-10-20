# Входные данные
capacity_mb = 1.44 # Объем дискеты в Мб
pages = 100  # Количество страниц в книге
strings = 50  # Число строк на странице
symbols_string = 25  # Количество символов в строке
symbols = 4  # Количество байт на символ

# Объем дискеты в байтах
capacity_bytes = capacity_mb * 2**20

# Количество символов в книге
total_symbols = pages * strings * symbols_string

# Объем книги в байтах
book_size = total_symbols * symbols

# Количество книг на дискете
num_books = int(capacity_bytes // book_size)


print("Количество книг, помещающихся на дискету:", num_books)
