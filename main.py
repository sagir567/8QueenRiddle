# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import copy


def diagonal(n):
    for i in n:

        for j in range(0,8,1):

            if (i == j):
                continue

            row = abs(n[i] - n[j])
            coll = abs(i - j)

            if (row == coll):
                return False

    return True
if __name__ == '__main__':

    collection = []
    res = [[]]
    offset = (0, 1, 2, 3, 4, 5, 6, 7)
    temp = [0, 0, 0, 0, 0, 0, 0, 0]
    counter = 0
    for i in offset:
        temp[0] = i

        for j in offset:
            if (i == j):
                continue
            temp[1] = j

            for k in offset:
                if (k == i or k == j):
                    continue
                temp[2] = k

                for z in offset:
                    if (z == k or z == j or z == i):
                        continue
                    temp[3] = z
                    for x in offset:
                        if (x == i or x == j or x == k or x == z):
                            continue
                        temp[4] = x

                        for y in offset:
                            if (y == i or y == j or y == k or y == z or y == x):
                                continue
                            temp[5] = y
                            for w in offset:
                                if (w == i or w == j or w == k or w == z or w == x or w == y):
                                    continue
                                temp[6] = w
                                for s in offset:
                                    if (s == i or s == j or s == k or s == z or s == x or s == y or s == w):
                                        continue
                                    temp[7] = s
                                    counter += 1

                                    if (diagonal(temp) ==True):
                                        print (temp)
                                        collection.append(copy.copy(temp))
    for i in collection:
        print(i)

