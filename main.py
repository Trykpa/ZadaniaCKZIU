class Zlot:
    alphaa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
              'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X',
              'Y', 'Z']
    array1 = ["J", "K", "L", "K", "P", "I", "J", "E", "P", "T"]

    for j in range(0, len(array1)):
        for i in range(0, len(array1)):
            _sorted = False
            if i != len(array1) - 1:
                for k in range(0, len(array1[i])):
                    if not _sorted:
                        if k != (len(array1[i]) and len(array1[i + 1])):
                            if alphaa.index(array1[i][k]) > alphaa.index(array1[i + 1][k]):
                                array1[i], array1[i + 1] = array1[i + 1], array1[i]
                                _sorted = True
                            elif alphaa.index(array1[i][k]) < alphaa.index(array1[i + 1][k]):
                                _sorted = True
                            else:
                                if len(array1[i + 1]) < len(array1[i]):
                                    array1[i], array1[i + 1] = array1[i + 1], array1[i]
                                    _sorted = True


    array2 = array1
    podwojne = 0

    n = len(array2)
    for i in range(n):
        for j in range(n - i - 1):
            if alphaa.index(array2[i]) == alphaa.index(array2[i + 1]):
                podwojne = podwojne + 1
                print(array2[i])
                array2[i], array2[i + 1] = array2[i + 1], array2[i]
                break

    print(podwojne)


