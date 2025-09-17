# filepath: /calculadora-python-da-ya/calculadora-python-da-ya/src/calculadora.py

# Python Calculator
# This file contains functions for currency conversion, discount calculation, average calculation, and fuel consumption calculation.

def conversor_moeda(valor_reais, taxa_dolar, taxa_euro):
    valor_dolar = round(valor_reais / taxa_dolar, 2)
    valor_euro = round(valor_reais / taxa_euro, 2)
    print(f"Valor em reais: R$ {valor_reais:.2f}")
    print(f"Convertido para dólares: US$ {valor_dolar:.2f}")
    print(f"Convertido para euros: € {valor_euro:.2f}\n")

def calculadora_desconto(nome_produto, preco_original, porcentagem_desconto):
    valor_desconto = round(preco_original * (porcentagem_desconto / 100), 2)
    preco_final = round(preco_original - valor_desconto, 2)
    print(f"Produto: {nome_produto}")
    print(f"Preço original: R$ {preco_original:.2f}")
    print(f"Desconto: {porcentagem_desconto}%")
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Preço final: R$ {preco_final:.2f}\n")

def calculadora_media_escolar(nota1, nota2, nota3):
    media = round((nota1 + nota2 + nota3) / 3, 2)
    print(f"Notas do aluno: {nota1}, {nota2}, {nota3}")
    print(f"Média final: {media:.2f}\n")

def calculadora_consumo_combustivel(distancia, combustivel):
    consumo_medio = round(distancia / combustivel, 2)
    print(f"Distância percorrida: {distancia} km")
    print(f"Combustível gasto: {combustivel} litros")
    print(f"Consumo médio: {consumo_medio} km/l\n")

def main():
    # 1- Conversor de Moeda
    conversor_moeda(valor_reais=100.00, taxa_dolar=5.20, taxa_euro=6.15)

    # 2- Calculadora de Desconto
    calculadora_desconto(nome_produto="Camiseta", preco_original=50.00, porcentagem_desconto=20)

    # 3- Calculadora de Média Escolar
    calculadora_media_escolar(nota1=7.5, nota2=8.0, nota3=6.5)

    # 4- Calculadora de Consumo de Combustível
    calculadora_consumo_combustivel(distancia=300, combustivel=25)

if __name__ == "__main__":
    main()