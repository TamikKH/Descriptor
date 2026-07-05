def cipher(file_name, number_of_bias):
    cipher_arr = language_definition(file_name)
    bias_arr = cipher_arr.copy()
    bias_arr = bias_arr[number_of_bias:] + bias_arr[:number_of_bias]
    with open(file_name, "r+") as file:
        data = list(file.read())
        for i in range(len(data)):
            if data[i] in cipher_arr:
                index = cipher_arr.index(data[i])
                data[i] = bias_arr[index]
        file.seek(0)
        file.write("".join(data))
    print("Шифровка выполнена успешно")


def decipher(file_name, number_of_bias):
    decipher_arr = language_definition(file_name)
    bias_arr = decipher_arr.copy()
    bias_arr = bias_arr[number_of_bias:] + bias_arr[:number_of_bias]
    with open(file_name, "r+") as file:
        data = list(file.read())
        for i in range(len(data)):
            if data[i] in decipher_arr:
                index = bias_arr.index(data[i])
                data[i] = decipher_arr[index]
        file.seek(0)
        file.write("".join(data))
    print("Дешифровка выполнена успешно")

def language_definition(file_name):
    rus_symbol = 0
    eng_symbol = 0
    rus_alf = [
    'А', 'а', 'Б', 'б', 'В', 'в', 'Г', 'г', 'Д', 'д', 'Е', 'е', 'Ё', 'ё', 'Ж', 'ж', 'З', 'з', 'И', 'и', 'Й', 'й', 'К',
    'к', 'Л', 'л', 'М', 'м', 'Н', 'н', 'О', 'о', 'П', 'п', 'Р', 'р', 'С', 'с', 'Т', 'т', 'У', 'у', 'Ф', 'ф', 'Х', 'х',
    'Ц', 'ц', 'Ч', 'ч', 'Ш', 'ш', 'Щ', 'щ', 'ъ', 'ы', 'ь', 'Э', 'э', 'Ю', 'ю', 'Я', 'я']
    eng_alf = [
    'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L',
    'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w',
    'X', 'x', 'Y', 'y', 'Z', 'z']

    with open(file_name, "r+") as file:
        text = file.read(50)
        for ch in text:
            if ch in eng_alf:
                eng_symbol += 1
            elif ch in rus_alf:
                rus_symbol += 1
    if rus_symbol > eng_symbol:
        return original_arr_russian
    else:
        return original_arr_english



original_arr_english = [
    'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L',
    'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w',
    'X', 'x', 'Y', 'y', 'Z', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    ' ',
    '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[',
    ']', '^', '_', '`', '{', '|', '}', '~']

original_arr_russian = [
    'А', 'а', 'Б', 'б', 'В', 'в', 'Г', 'г', 'Д', 'д', 'Е', 'е', 'Ё', 'ё', 'Ж', 'ж', 'З', 'з', 'И', 'и', 'Й', 'й', 'К',
    'к', 'Л', 'л', 'М', 'м', 'Н', 'н', 'О', 'о', 'П', 'п', 'Р', 'р', 'С', 'с', 'Т', 'т', 'У', 'у', 'Ф', 'ф', 'Х', 'х',
    'Ц', 'ц', 'Ч', 'ч', 'Ш', 'ш', 'Щ', 'щ', 'ъ', 'ы', 'ь', 'Э', 'э', 'Ю', 'ю', 'Я', 'я',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    ' ',
    '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[',
    ']', '^', '_', '`', '{', '|', '}', '~']

def main():
    file_name = input('Введите имя или путь к файлу: ')
    try:
        print('Что вы хотите сделать?')
        print('Для зашифровки файла введите шифровать или введите единицу')
        print('Для дешифровки файла введите дефровать или введите двойку')
        type_of_operation = input()
        number_of_bias = int(input('Введите число для шифровки/дешифровки: '))
        match type_of_operation:
            case 'шифровать' | '1':
                cipher(file_name, number_of_bias)
            case 'дефровать' | '2':
                decipher(file_name, number_of_bias)
            case _:
                print("Нераспознанная команда")
    except FileNotFoundError:
        print('Файл не найден. Проверьте путь или имя.')
    except PermissionError:
        print('Недостаточно прав для открытия файла.')
    except OSError as e:
        print(f'Ошибка при работе с файлом: {e}')


if __name__ == "__main__":
    main()