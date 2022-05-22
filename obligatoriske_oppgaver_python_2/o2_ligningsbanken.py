from random import randint


def answer_questions(D):
    name = input("Enter your name: ")
    while name not in D:
        name = input("Enter your name: ")
    if name in D:
        for i in range(len(D[name])):
            print(f"{i+1}) {eq2text(D[name][i])}")
            answer_list = D[name][i]
            answer = int(input("x = "))
            answer_list.append(answer)
            D[name][i] = answer_list


def make_test(students, n):
    dictionary = {}
    for i in range(len(students)):
        eqs = make_n_eqs(n)
        dictionary[students[i]] = eqs
    return dictionary


def make_n_eqs(num):
    eqs_list = []
    for i in range(num):
        eq = make_eq(randint(-9, 9), randint(-9, 9), randint(-9, 9), randint(-9, 9))
        if eq not in eqs_list:
            eqs_list.append(eq)
        else:
            make_eq(randint(-9, 9), randint(-9, 9), randint(-9, 9), randint(-9, 9))

    return eqs_list


def make_eq(a, b, c, d):
    random_list = []
    random_list.append(a)
    random_list.append(b)
    random_list.append(c)
    random_list.append(d)
    if ok(random_list):
        return random_list
    else:
        return make_eq(randint(-9, 9), randint(-9, 9), randint(-9, 9), randint(-9, 9))


def ok(L):
    if 0 in L:
        return False
    elif -0 in L:
        return False
    elif L[0] == L[2]:
        return False
    elif L[1] == L[3]:
        return False
    else:
        return True


def eq2text(random_list):

    a = random_list[0]
    b = random_list[1]
    c = random_list[2]
    d = random_list[3]

    if a == 1:
        a = ""
    elif a == -1:
        a = "-"

    if c == 1:
        c = ""
    elif c == -1:
        c = "-"

    if b > 0:
        b = f"+ {b}"

    if d > 0:
        d = f"+ {d}"

    return f"{a}x {b} = {c}x {d}"


def main():

    tests = make_test(["Ola", "Kari", "Fredrik"], 5)
    answer_questions(tests)
    print(tests)


main()
