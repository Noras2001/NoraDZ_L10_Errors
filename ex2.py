def validate_user_input(data):
    # Проверяем, что data является словарем
    if not isinstance(data, dict):
        raise TypeError("Ожидался словарь с данными пользователя.")

    # Проверяем наличие и тип ключа 'name'
    if 'name' not in data:
        raise ValueError("Отсутствует ключ 'name'.")
    elif not isinstance(data['name'], str):
        raise ValueError("Значение ключа 'name' должно быть строкой.")

    # Проверяем наличие и тип ключа 'age'
    if 'age' not in data:
        raise ValueError("Отсутствует ключ 'age'.")
    elif not isinstance(data['age'], (int, float)) or data['age'] <= 0:
        raise ValueError("Значение ключа 'age' должно быть положительным числом.")

    print("Данные пользователя корректны.")
    return True

#print( validate_user_input({"name": "Alice", "age": 30}) )
print("- "*20)
#print(validate_user_input({"age": 30})  )
#print("- "*20)
print(validate_user_input({"name": "Alice", "age": "thirty"}) )
