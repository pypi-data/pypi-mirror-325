Библиотека для работы с TXT файлами.
Установка: pip install txt-reader
Пример использования:
from txt_reader import TXTReader

# Создаем объект для работы с TXT файлами
reader = TXTReader(directory=".")

# Создание нового TXT-файла
reader.create("example.txt", "Привет, это тестовый файл.")

# Чтение содержимого файла
content = reader.read("example.txt")
print("Содержимое файла:", content)

# Редактирование файла
reader.edit("example.txt", "Это обновленный текст в файле.")
updated_content = reader.read("example.txt")
print("Обновленное содержимое файла:", updated_content)

# Получение списка всех .txt файлов в директории
txt_files = reader.list_files()
print("TXT файлы в папке:", txt_files)

# Удаление файла
reader.delete("example.txt")
print("Файл 'example.txt' удален.")

# Проверка списка файлов после удаления
txt_files_after_delete = reader.list_files()
print("TXT файлы после удаления:", txt_files_after_delete)

Ожидаемый вывод:
Содержимое файла: Привет, это тестовый файл.
Обновленное содержимое файла: Это обновленный текст в файле.
TXT файлы в папке: ['example.txt']
Файл 'example.txt' удален.
TXT файлы после удаления: []
