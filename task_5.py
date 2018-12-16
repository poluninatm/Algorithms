# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
letters = input("Введите две строчные буквы английского алфавита: ")
letter1 = letters[0]
letter2 = letters[1]

ord_a = ord("a")

ord_letter_1 = ord(letter1) - ord_a + 1
ord_letter_2 = ord(letter2) - ord_a + 1

letters_between = abs(ord_letter_2 - ord_letter_1)

print(f'Порядковый номер буквы {letter1} - {ord_letter_1}.')
print(f'Порядковый номер буквы {letter2} - {ord_letter_2}.')
print(f'Расстояние между ними -  {letters_between} букв')
