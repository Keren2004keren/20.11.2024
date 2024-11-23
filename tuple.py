# a
only_99: tuple[int] = (99,)

# b
tup: tuple[int, int, int] = (77, 88, 99)


# c
def length(len_tup: tuple) -> int:
    return len(len_tup)


# d
def combine(x: tuple, y: tuple) -> tuple:
    return x + y


# e
def shared(a: tuple, b: tuple) -> tuple:
    share = [char for char in a if char in b]
    return tuple(share)


# f
def not_shared(d: tuple, c: tuple) -> tuple:
    not_share = [char for char in d if char not in c] + [char for char in c if char not in d]
    return tuple(not_share)


# g
def placement(chars: tuple, index: int) -> int:
    if 0 <= index < len(chars):
        return chars[index]
    else:
        return None


# h
def inverted(t: tuple) -> tuple:
    return t[::-1]


# i
def mul(tup_mul: tuple, x: int) -> tuple:
    return tup_mul * x


# j
def pop(tup_pop: tuple, n: int) -> tuple:
    return tuple([char for char in tup_pop if char != n])


# k
def no_repeat(r_tup: tuple) -> tuple:
    r_list: list = []
    for char in r_tup:
        if char not in r_list:
            r_list.append(char)
    return tuple(r_list)


# l
def index_tup(i_tup: tuple, num: int) -> tuple:
    indexes = []
    for i in range(len(i_tup)):
        if i_tup[i] == num:
            indexes.append(i)
    return tuple(indexes)


# m
names: list[str] = []
while True:
    name: str = input("Enter a name: ")
    if name == "done":
        break
    else:
        names.append(name)
grades: list[int] = []
while True:
    try:
        grade: int = int(input("Enter a grade: "))
        if grade == -999:
            break
        elif grade < 0 or grade > 100:
            continue
        else:
            grades.append(grade)
    except ValueError:
        print("invalid input.")
combine_tuple: tuple[tuple[any]] = tuple(zip(names, grades))
print(combine_tuple)
