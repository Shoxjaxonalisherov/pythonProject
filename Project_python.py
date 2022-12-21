
def caesar_decrypt(text, key):
    ''' caesar_decrypt(text, key) - функция для расшифровки текста, зашифрованного шифром Цезаря.

       Аргументы:

       text: Строка с текстом, который нужно расшифровать.

       key: Целое число, указывающее, на сколько нужно сдвинуть символы текста для расшифровки.

       Возвращаемое значение:

       Строка с расшифрованным текстом.'''
    decrypted_text = ""      #Первым делом функция создает пустую строку decrypted_text, которую будет использовать для сохранения расшифрованного текста.
    for letter in text:      #Затем в цикле for letter in text: перебираются все символы строки text. Каждый символ будет называться letter.
        if letter.isalpha():    #Если letter является буквой (проверка выполняется с помощью метода isalpha), то выполняется блок кода, который производит расшифровку этого символа.
            ascii_val = ord(letter)    #В переменную ascii_val сохраняется ASCII-код символа letter.
            if letter.isupper():    # Далее, если letter является заглавной буквой (проверка выполняется с помощью метода isupper), то из ascii_val вычитается key. Если ascii_val станет меньше кода символа 'А' в UTF-8 (то есть 1040), то ascii_val увеличивается на 32 (это разница между кодами символов 'А' и 'а' в UTF-8).
                ascii_val -= key
                if ascii_val < 1040:  # код символа 'А' в UTF-8
                    ascii_val += 32
            else:
                ascii_val -= key    # Если letter является строчной буквой, то из ascii_val также вычитается key. Если ascii_val станет меньше кода символа 'а' в UTF-8 (то есть 1072), то ascii_val увеличивается на 32.
                if ascii_val < 1072:  # код символа 'а' в UTF-8
                    ascii_val += 32
            decrypted_text += chr(ascii_val)    # После того, как ascii_val была подсчитана, она преобразуется в символ с помощью функции chr и добавляется к расшифрованной строке decrypted_text
        else:
            decrypted_text += letter  # Если letter не является буквой, то он просто добавляется к decrypted_text без изменений.
    return decrypted_text

def caesar_encrypt(text, key):
    ''' caesar_encrypt(text, key) - функция для шифрования текста шифром Цезаря.

    Аргументы:

    text: Строка с текстом, который нужно зашифровать.

    key: Целое число, указывающее, на сколько нужно сдвинуть символы текста для шифрования.

    Возвращаемое значение:

    Строка с зашифрованным текстом. '''
    encrypted_text = ""
    for letter in text:    # Цикл for letter in text: перебирает каждый символ в строке text.
        if letter.isalpha():    # Цикл if letter.isalpha(): проверяет, является ли символ буквой. Если да, то выполняется тело цикла, иначе идет переход к следующему символу.
            ascii_val = ord(letter)
            if letter.isupper():    # Цикл if letter.isupper(): проверяет, является ли символ заглавной буквой. Если да, то выполняется тело цикла, иначе идет переход к следующему условию.
                ascii_val += key
                if ascii_val > 1071:  # код символа 'Я' в UTF-8,  Цикл if ascii_val > 1071: проверяет, больше ли значение ascii_val кода символа 'Я' в UTF-8. Если да, то выполняется тело цикла, иначе идет переход к следующему условию. Этот цикл используется для того, чтобы при добавлении ключа к значению ASCII символа не выйти за пределы русского алфавита.
                    ascii_val -= 32
            else:
                ascii_val += key
                if ascii_val > 1103:  # код символа 'я' в UTF-8,  Цикл if ascii_val > 1103: аналогичен предыдущему, но используется для строчных букв.
                    ascii_val -= 32
            encrypted_text += chr(ascii_val)    # Цикл encrypted_text += chr(ascii_val): добавляет к строке encrypted_text символ, соответствующий значению ASCII хранящемуся в переменной ascii_val.
        else:
            encrypted_text += letter
    return encrypted_text

def vigenere_decrypt(text, key):
    ''' vigenere_decrypt(text, key) - функция для расшифровки текста, зашифрованного методом Виженера.

    Аргументы:

    text: Строка с текстом, который нужно расшифровать.

    key: Строка с ключом, используемым для шифрования.

    Возвращаемое значение:

    Строка с расшифрованным текстом.
    '''
    decrypted_text = ""
    key_len = len(key)
    key_index = 0
    for letter in text:   # Цикл "for letter in text:" - это цикл перебора каждой буквы в тексте
        if letter.isalpha():   # в этом цикле проверяется, является ли текущая буква буквой алфавита
            unicode_val = ord(letter)
            if letter.isupper():   # в этом цикле проверяется, является ли текущая буква буквой алфавита
                unicode_val -= ord(key[key_index].upper()) - ord('А')
                if unicode_val < ord('А'):    # Цикл "if unicode_val < ord('А'):" - это условный цикл, который проверяет, является ли значение unicode_val меньше значения кода символа 'А'.
                    unicode_val += 32
            else:
                unicode_val -= ord(key[key_index].lower()) - ord('а')
                if unicode_val < ord('а'):
                    unicode_val += 32
            decrypted_text += chr(unicode_val)
            key_index += 1
            if key_index == key_len:    # Цикл "if key_index == key_len:" - это условный цикл, который проверяет, равно ли значение key_index длине ключа key_len.
                key_index = 0
        else:
            decrypted_text += letter
    return decrypted_text

def vigenere_encrypt(text, key):
    ''' vigenere_encrypt(text, key) - функция для шифрования текста методом Виженера.

        Аргументы:

        text: Строка с текстом, который нужно зашифровать.

        key: Строка с ключом, используемым для шифрования.

        Возвращаемое значение:

        Строка с зашифрованным текстом. '''
    encrypted_text = ""
    key_len = len(key)
    key_index = 0
    for letter in text:    # это цикл по каждому символу текста, который нужно зашифровать. На каждой итерации цикла будет получен следующий символ из текста.
        if letter.isalpha():   # в этом цикле проверяется, является ли текущая буква буквой алфавита
            unicode_val = ord(letter)
            if letter.isupper():     # в этом цикле проверяется, является ли текущая буква буквой алфавита
                unicode_val += ord(key[key_index].upper()) - ord('А')
                if unicode_val > ord('Я'):
                    unicode_val -= 32
            else:
                unicode_val += ord(key[key_index].lower()) - ord('а')
                if unicode_val > ord('я'):
                    unicode_val -= 32
            encrypted_text += chr(unicode_val)
            key_index += 1
            if key_index == key_len:    # это условие, которое проверяет, следует ли перейти к началу ключа после обработки текущего символа. Если key_index (индекс текущего символа в ключе) равен key_len (длине ключа), то это значит, что мы достигли конца ключа, поэтому нужно перейти к его началу. Таким образом, цикл предназначен для перезапуска ключа после его завершения.
                key_index = 0
        else:
            encrypted_text += letter
    return encrypted_text

def encrypt_atbash(plaintext: str, alphabet: str) -> str:
    ''' Функция encrypt_atbash(plaintext: str, alphabet: str) -> str
     предназначена для шифрования текста с использованием шифра Атбаш.

     Входные параметры:

     plaintext - текст, который необходимо зашифровать(строка).

     alphabet - алфавит, который используется для шифрования(строка).

     Выходные значения:

     result - зашифрованный текст(строка). '''
    # Создаем словарь для замены букв
    substitution = {}
    # Обходим все буквы в алфавите
    for i, letter in enumerate(alphabet):
        # Записываем в словарь замену: буква - буква, находящаяся с конца алфавита
        substitution[letter] = alphabet[-i - 1]
    # Инициализируем результирующую строку
    result = ""
    # Обходим все символы в тексте
    for char in plaintext:
        # Если символ - буква, то заменяем ее на соответствующую букву из словаря
        if char in substitution:
            result += substitution[char]
        # Иначе, если символ - не буква, то просто добавляем его в результирующую строку
        else:
            result += char
        # Возвращаем результат
    return result

def decrypt_atbash(ciphertext: str, alphabet: str) -> str:
    ''' Функция decrypt_atbash(ciphertext: str, alphabet: str) -> str
     предназначена для расшифровки текста, зашифрованного с использованием шифра Атбаш.

     Входные параметры:

     ciphertext - зашифрованный текст(строка).

     alphabet - алфавит, который используется для расшифровки(строка).

     Выходные значения:

     result - расшифрованный текст(строка). '''
    # Создаем словарь для замены букв
    substitution = {}
    # Обходим все буквы в алфавите
    for i, letter in enumerate(alphabet):
        # Записываем в словарь замену: буква, находящаяся с конца алфавита - буква
        substitution[alphabet[-i - 1]] = letter
    # Инициализируем результирующую строку
    result = ""
    # Обходим все символы в тексте
    for char in ciphertext:
         # Если символ - буква, то заменяем ее на соответствующую букву из словаря
        if char in substitution:
            result += substitution[char]
        # Иначе, если символ - не буква, то просто добавляем его в результирующую строку
        else:
            result += char
    # Возвращаем результат
    return result