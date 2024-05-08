def to_hex(num: int) -> str:
    es_a = "a"
    es_b = "b"
    es_c = "c"
    es_d = "d"
    es_e = "e"
    es_f = "f"
    if num < 16:
        if num == 10:
            return es_a
        if num == 11:
            return es_b
        if num == 12:
            return es_c
        if num == 13:
            return es_d
        if num == 14:
            return es_e
        if num == 15:
            return es_f
    quoziente = num//16
    resto = num%16
    lista: list = []
    while num != 0:
        resto = num%16
        lista.append(resto)
        num = num//16
    lista.reverse()
    result = ""
    for i in lista:
        if i == 10:
            result += es_a
        elif i == 11:
            result += es_b
        elif i == 12:
            result += es_c
        elif i == 13:
            result += es_d
        elif i == 14:
            result += es_e
        elif i == 15:
            result += es_f
        else:
            result += str(i)
    return result
    if num < 0:
        num_bin = bin(num)
        for i in num_bin