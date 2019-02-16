# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
import collections


class HaffNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

        if type(self.left) is HaffNode:
            self.left.num = 0
            self.left.parent = self
        if type(self.right) is HaffNode:
            self.right.num = 1
            self.right.parent = self

    def get_code_dict(self, code_dict, path=''):
        if self.value is not None:
            code_dict[self.value] = path
        else:
            if self.left is not None:
                self.left.get_code_dict(code_dict, f'{path}0')
            if self.right is not None:
                self.right.get_code_dict(code_dict, f'{path}1')

    def __repr__(self):
        if self.value:
            return f'--{self.value}--'
        return f'{self.left}  {self.right}\n'


def haffman(string):
    array = []
    array.extend(string)
    lst = collections.Counter(array)
    lst = collections.deque(lst.most_common(len(lst))[::-1])
    print(lst)
    for i in range(len(lst)):
        lst[i] = HaffNode(value=lst[i][0]), lst[i][1]
    # print(lst)

    while len(lst) > 1:

        lst[1] = (HaffNode(left=lst[0][0], right=lst[1][0]), lst[0][1] + lst[1][1])
        lst.popleft()

        for i in range(len(lst) - 1):
            if lst[i][1] > lst[i + 1][1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
            else:
                break
    code_dict = dict()
    lst[0][0].get_code_dict(code_dict)
    print(code_dict)

    arch = ''
    for i in range(len(array)):
        # print(f'{code_dict[array[i]]} ', end='')
        arch += code_dict[array[i]]
    # print()
    return (arch, code_dict)


def dehaffman(string, code_dict):
    code_dict = {v: k for k, v in code_dict.items()}
    i = 0
    len_ = 2
    dearch = ''
    while i < len(string):
        find_str = string[i:i + len_]
        if find_str in code_dict:
            dearch += code_dict[find_str]
            i += len_
            len_ = 2
        else:
            len_ += 1

    return dearch


check_string = 'Проверка алгоритма Хаффмана'
print(check_string)
arch, code_dict = haffman(check_string)
print(arch)
print(dehaffman(arch, code_dict))
