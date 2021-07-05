def int_func(s):
    return s.title()


def filter_eng(s):
    new_s = []
    # alph = 'abcdefghijklmnopqrstuvwxyz'
    for word in s.split(' '):
        for letter in word:
            # if letter not in alph:
            if letter < 'a' or letter > 'z':
                break
        else:
            new_s.append(word)
    return int_func(' '.join(new_s))


text = 'Мы learn Python onлайн with fun'
print(filter_eng(text))
