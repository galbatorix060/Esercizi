print("ESERIZIO 1\n\n\n")

def divisible():
    lista : list = []
    for i in range(2000, 3200):
        if i % 7 == 0:
            if i % 5 != 0:
                lista.append(i)
    return lista

print(divisible())

print("\n\n\nESERIZIO 2\n\n\n")

numero : int = 8 #int(input("inserire il numero: "))

def factorial(n) -> int:
    fattoriale : int = 1
    i = 1
    while i <= n:
        fattoriale = fattoriale * i
        i += 1
    return fattoriale

print(factorial(numero))


print("\n\n\nESERIZIO 3\n\n\n")


numeri_fattoriali : list = [2,5,8,10]
factorial_output : list = []

for i in numeri_fattoriali:
    factorial_output.append(factorial(i))

print(factorial_output)


print("\n\n\nESERIZIO 4\n\n\n")

numero = 10

def factorial_dictionary(n) -> dict:
    i = 0
    fact_dict : dict = {}
    while i <= n:
        i += 1
        fact_dict[i] = i*i
    return fact_dict

print(factorial_dictionary(numero))


print("\n\n\nESERIZIO 5\n\n\n")


stringa : str = "without,hello,bag,world"

def separate(value) -> str:
    res = value.split(",")
    output_str : str = ""
    res = sorted(res)

    for i in res:
        output_str += i + ","
    return output_str


print(separate(stringa))

 