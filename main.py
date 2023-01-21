import math


def generalized_entropy(data, level):
    conj_freq = {}
    prev_freq = {}
    for i in range(len(data) - level - 1):
        prev = tuple(data[i:i + level])
        sym = data[i + level]
        if (prev, sym) in conj_freq:
            conj_freq[(prev, sym)] += 1
        else:
            conj_freq[(prev, sym)] = 1
        if prev in prev_freq:
            prev_freq[prev] += 1
        else:
            prev_freq[prev] = 1
    omega = sum(conj_freq.values())
    return -sum([conj_freq[(p, s)] / omega * math.log(conj_freq[(p, s)] / prev_freq[p], 2) for (p, s) in conj_freq])


def exercise1(file):
    print("Zadanie 1:")
    print("Entropia znaków w języku angielskim:")
    with open(file, 'r') as file:
        data = file.read().replace('\n', '')
    print(generalized_entropy(data, 0))


def exercise2(filename):
    print("Zadanie 2:")
    print('Entropia słów w języku angielskim:')
    with open(filename, 'r') as file:
        data = file.read().strip().split()
    print(generalized_entropy(data, 0))


def exercise3(filename):
    print("Zadanie 3:")
    print('Entropia warunkowa pierwszego rzędu znaków w języku angielskim:')
    with open(filename, 'r') as file:
        data = file.read()
    print(generalized_entropy(data, 1))


def exercise4():
    print("Zadanie 4:")
    for filename in ("norm_wiki_en.txt", "norm_wiki_la.txt", "norm_wiki_eo.txt", "norm_wiki_et.txt", "norm_wiki_ht.txt",
                     "norm_wiki_so.txt", "norm_wiki_nv.txt"):
        with open(filename, 'r') as file:
            data = file.read()
            for i in range(4):
                print(
                    "Entropia" + ("" if i == 0 else " warunkowa rzędu " + str(i)) + " znaków w pliku " + filename + ":")
                print(generalized_entropy(data, i))
            data = data.strip().split()
            for i in range(4):
                print("Entropia" + ("" if i == 0 else " warunkowa rzędu " + str(i)) + " słów w pliku " + filename + ":")
                print(generalized_entropy(data, i))


def exercise5():
    print("Zadanie 5:")
    for n in range(6):
        filename = "sample" + str(n) + ".txt"
        with open(filename, 'r') as file:
            data = file.read()
            for i in range(4):
                print(
                    "Entropia" + ("" if i == 0 else " warunkowa rzędu " + str(i)) + " znaków w pliku " + filename + ":")
                print(generalized_entropy(data, i))
            data = data.strip().split()
            for i in range(4):
                print("Entropia" + ("" if i == 0 else " warunkowa rzędu " + str(i)) + " słów w pliku " + filename + ":")
                print(generalized_entropy(data, i))


def main():
    file = "./norm_wiki_en.txt"
    exercise1(file)
    exercise2(file)
    exercise3(file)
    exercise4()
    exercise5()


if __name__ == "__main__":
    main()