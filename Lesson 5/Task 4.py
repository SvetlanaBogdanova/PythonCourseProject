en_rus_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять'}

with open('text_4.txt', 'r', encoding='utf-8') as file:
    with open('new_text_4.txt', 'w', encoding='utf-8') as rus_translate:
        for line in file:
            eng_words = set(line.split())
            for word in eng_words:
                if en_rus_dict.get(word) is not None:
                    line = line.replace(word, en_rus_dict.get(word))
            rus_translate.write(line)
