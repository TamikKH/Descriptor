rus_alf = [
    'А', 'а', 'Б', 'б', 'В', 'в', 'Г', 'г', 'Д', 'д', 'Е', 'е', 'Ё', 'ё', 'Ж', 'ж', 'З', 'з', 'И', 'и', 'Й', 'й', 'К',
    'к', 'Л', 'л', 'М', 'м', 'Н', 'н', 'О', 'о', 'П', 'п', 'Р', 'р', 'С', 'с', 'Т', 'т', 'У', 'у', 'Ф', 'ф', 'Х', 'х',
    'Ц', 'ц', 'Ч', 'ч', 'Ш', 'ш', 'Щ', 'щ', 'ъ', 'ы', 'ь', 'Э', 'э', 'Ю', 'ю', 'Я', 'я']
eng_alf = [
    'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L',
    'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w',
    'X', 'x', 'Y', 'y', 'Z', 'z']

special_symbols = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    ' ',
    '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[',
    ']', '^', '_', '`', '{', '|', '}', '~']

class CaesarCipher:
    def __init__(self, file_name, number_of_shift, all_arr):
        self.file_name = file_name
        self.number_of_shift = number_of_shift
        self.all_arr = all_arr

    def cipher(self):
        arr_shift = self.array_shift()
        with open(self.file_name, "r+") as file:
            data = list(file.read())
            for i in range(len(data)):
                if data[i] in self.all_arr:
                    index = arr_shift.index(data[i])
                    data[i] = self.all_arr[index]
            file.seek(0)
            file.write("".join(data))
            print("Шифровка выполнена успешно")


    def decipher(self):
        arr_shift = self.array_shift()
        with open(self.file_name, "r+") as file:
            data = list(file.read())
            for i in range(len(data)):
                if data[i] in self.all_arr:
                    index = arr_shift.index(data[i])
                    data[i] = self.all_arr[index]
            file.seek(0)
            file.write("".join(data))
            print("Дешифровка выполнена успешно")

    def array_shift(self):
        shift = self.number_of_shift % len(self.all_arr)
        return self.all_arr[shift:] + self.all_arr[:shift]

def language_definition(file_name, rus_alf, eng_alf):
    rus_symbol = 0
    eng_symbol = 0
    with open(file_name, "r+") as file:
        text = file.read(50)
        for ch in text:
            if ch in eng_alf:
                eng_symbol += 1
            elif ch in rus_alf:
                rus_symbol += 1
    if rus_symbol > eng_symbol:
        return rus_alf + special_symbols
    else:
        return eng_alf + special_symbols


def main():
    file_name = input('Введите имя или путь к файлу: ')
    try:
        print('Что вы хотите сделать?')
        print('Для зашифровки файла введите шифровать или введите единицу')
        print('Для дешифровки файла введите дешифровать или введите двойку')
        type_of_operation = input()
        number_of_shift = int(input('Введите число для шифровки/дешифровки: '))
        all_arr = language_definition(file_name, rus_alf, eng_alf)
        caesar = CaesarCipher(file_name, number_of_shift, all_arr)
        match type_of_operation:
            case 'шифровать' | '1':
                caesar.cipher()
            case 'дешифровать' | '2':
                caesar.decipher()
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