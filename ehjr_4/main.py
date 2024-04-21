

def input_int(message):
    while True:
        try:

            result = int(input(message))
            return result
        except Exception:
            print("Ой..")
        else:
            break

number = input_int("Введите число: ")
print(number)


