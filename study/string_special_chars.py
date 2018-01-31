test1 = 'abc#de'
test2 = 'ab#cd&fg'
test3 = '@$hg,fed#cba'


def is_special_char(char):
    return not char.isalpha()


def swap_at_indices(text, head, tail):
    text[head], text[tail] = text[tail], text[head]


def reverse_string_wo_moving_special_chars(text):
    text = list(text)
    print(text)
    head = 0
    tail = len(text) - 1
    while head < tail:
        if is_special_char(text[head]):
            head += 1
        elif is_special_char(text[tail]):
            tail -= 1
        else:
            swap_at_indices(text, head, tail)
            head += 1
            tail -= 1
    print(text)
    return ''.join(text)

print(reverse_string_wo_moving_special_chars(test1) == 'edc#ba')
print(reverse_string_wo_moving_special_chars(test2) == 'gf#dc&ba')
reverse_string_wo_moving_special_chars(test3)
