import os

#%% first cell
print("============================")
print("This is the calc.py file")
print("============================")

operations = {  
    "+": "Adição",
    "-": "Subtração",
    "*": "Multiplicação",   
    "/": "Divisão",
    "^": "Exponenciação",
}

while True:
    i = 0
    for op, name in operations.items():
        print(f"{i} - {name}")
        i += 1
    print("")

    print("Digite a operação desejada: ")
    op = int(input())
    op_string = list(operations.keys())[int(op)]

    print(op_string)

    print(f"{i} - Sair")



# %%
