def single_root_words(root_word, *other_words):                 # Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
    same_words = []                                             # Создайте внутри функции пустой список same_words, который пополнится нужными словами.
    root_word_up = root_word.upper()                            # При проверке наличия одного слова в составе другого стоит учесть, что регистр символов не должен влиять ни на что. (

    for i in other_words:                                       # При помощи цикла for переберите предполагаемо подходящие слова.
        other_words_up = i.upper()
        if root_word_up in other_words_up or other_words_up in root_word_up: # Пропишите корректное относительно задачи условие,
                same_words.append(i)                            # при котором добавляются слова в результирующий список same_words.
    return same_words                                           # После цикла верните образованный функцией список same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies') # Вызовите функцию single_root_words
print(result1)                                                  # и выведете на экран(консоль) возвращённое ей значение.
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel') # Вызовите функцию single_root_words
print(result2)                                                  # и выведете на экран(консоль) возвращённое ей значение.

# Вывод на консоль:
# ['richiest', 'orichalcum', 'richies']
# ['Able', 'Disable']