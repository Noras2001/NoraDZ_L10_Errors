def convert_to_int(value):
    try:
        # Преобразовать строку в целое число
        res = int(value)
        print(f"Преобразование: {res}")
        return res
    except ValueError:
        print("Ошибка: невозможно преобразовать в число.")
    except Exception as e:
        # Обрабатываем другие исключения
        print(f"Ошибка: {e}")
    finally:
        # Сообщаем о завершении попытки преобразования
        print("Попытка преобразования завершена.")

print(convert_to_int("123")  )
print("- "*20)
print(convert_to_int("abc")  )
print("- "*20)
print(convert_to_int([1, 2, 3]) )

