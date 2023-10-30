# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
Peso = []
for I in range(5):
    KG = float(input("Digite seu peso: "))
    Peso.append(KG)
Peso_2 = sorted(Peso)
print (f"O peso menor é {Peso_2[0]}, e o peso maior é {Peso_2[4]}")