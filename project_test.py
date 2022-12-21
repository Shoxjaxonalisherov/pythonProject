import unittest
from Project_python import caesar_encrypt, caesar_decrypt, vigenere_encrypt, vigenere_decrypt, encrypt_atbash, decrypt_atbash

class TestCaesarCipher(unittest.TestCase):
    def test_caesar_encrypt(self):
        # Test that the function correctly encrypts a text using Caesar cipher
        self.assertEqual(caesar_encrypt("Привет, мир!", 1), "Рсйгжу, нйс!")
        self.assertEqual(caesar_encrypt("Привет, мир!", 3), "Тулеих, плу!")
        self.assertEqual(caesar_encrypt("Привет, мир!", 5), "Фхнзкч, снх!")
        self.assertEqual(caesar_encrypt("1234567", 6), "1234567")
        self.assertEqual(caesar_encrypt("Амонуллаев Бахрилло", 7), "Зухфъттзмй Изьчпттх")
        self.assertEqual(caesar_encrypt("", 7), "")

    def test_caesar_decrypt(self):
        # Test that the function correctly decrypts a text using Caesar cipher
        self.assertEqual(caesar_decrypt("Рсйгжу, нйс!", 1), "Привет, мир!")
        self.assertEqual(caesar_decrypt("Тулеих, плу!", 3), "Привет, мир!")
        self.assertEqual(caesar_decrypt("Фхнзкч, снх!", 5), "Привет, мир!")
        self.assertEqual(caesar_decrypt("1234567", 6), "1234567")
        self.assertEqual(caesar_decrypt("Зухфъттзмй Изьчпттх", 7), "Амонуллаев Бахрилло")
        self.assertEqual(caesar_decrypt("", 7), "")

class TestVigenereCipher(unittest.TestCase):
    def test_vigenere_encrypt(self):
        # Test that the function correctly encrypts a text using Vigenere cipher
        self.assertEqual(vigenere_encrypt("Привет, мир!", "ключ"), "Щыжщпэ, кяъ!")
        self.assertEqual(vigenere_encrypt("1234567", "ключ"), "1234567")
        self.assertEqual(vigenere_encrypt("", "ключ"), "")
        self.assertEqual(vigenere_encrypt("Высшая Школа Экономики", "ключ"), "Мжппкк Цбшцю Ффщлецуия")
        self.assertEqual(vigenere_encrypt("Амонуллаев Бахрилло", "ключ"), "Кчмдэцйчпн Ячяыжвхщ")


    def test_vigenere_decrypt(self):
        # Test that the function correctly decrypts a text using Vigenere cipher
        self.assertEqual(vigenere_decrypt("Щыжщпэ, кяъ!", "ключ"), "Привет, мир!")
        self.assertEqual(vigenere_decrypt("1234567", "ключ"), "1234567")
        self.assertEqual(vigenere_decrypt("", "ключ"), "")
        self.assertEqual(vigenere_decrypt("Мжппкк Цбшцю Ффщлецуия", "ключ"), "Высшая Школа Экономики")
        self.assertEqual(vigenere_decrypt("Кчмдэцйчпн Ячяыжвхщ", "ключ"), "Амонуллаев Бахрилло")

class TestAtbash(unittest.TestCase):
    def test_encrypt_atbash(self):
        # Создаем тестовые данные
        test_cases = [
            ("hello", "abcdefghijklmnopqrstuvwxyz", "svool"),
            ("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"),
            ("test", "abcdefghijklmnopqrstuvwxyz", "gvhg"),
            ("1234567890", "abcdefghijklmnopqrstuvwxyz", "1234567890"),
            ("", "abcdefghijklmnopqrstuvwxyz", ""),
            ("Привет, мир!", "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "Поцэъм, тцо!")

        ]

        # Проверяем работу функции для каждого тестового случая
        for plaintext, alphabet, expected_result in test_cases:
            result = encrypt_atbash(plaintext, alphabet)
            self.assertEqual(result, expected_result)

    def test_decrypt_atbash(self):
        # Создаем тестовые данные
        test_cases = [
            ("svool", "abcdefghijklmnopqrstuvwxyz", "hello"),
            ("zyxwvutsrqponmlkjihgfedcba", "abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"),
            ("gvhg", "abcdefghijklmnopqrstuvwxyz", "test"),
            ("1234567890", "abcdefghijklmnopqrstuvwxyz", "1234567890"),
            ("", "abcdefghijklmnopqrstuvwxyz", ""),
            ("Поцэъм, тцо!", "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "Привет, мир!"),

        ]

        # Проверяем работу функции для каждого тестового случая
        for ciphertext, alphabet, expected_result in test_cases:
            result = decrypt_atbash(ciphertext, alphabet)
            self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

