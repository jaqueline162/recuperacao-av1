#  Faça um programa que solicite ao usuário sua idade, depois disso, exiba a classificação etária de acordo com as faixas de valores:
idade = int (input("Digite sua idade: "))

if idade >=0 and idade <= 11:
    print("Criança")

elif idade >= 12 and idade <= 18:
    print("Adolescente")

elif idade >= 19 and idade  <= 24:
    print("Jovem")
elif idade >= 25 and idade  <= 40:
    print("Aulto")
elif idade >= 41 and idade  <= 60:
    print("Meia Idade")
elif idade >60:
    print("Idoso")
