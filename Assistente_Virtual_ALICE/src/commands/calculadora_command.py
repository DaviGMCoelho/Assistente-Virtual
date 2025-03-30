from pyparsing import Word, nums

def calculadora(frase):
    frase = frase.replace('x', '*')

    lista_mais = ["somar", "+", "adicione", "mais", "adição", "x"]
    lista_menos = ["subtração", "subtraia", "-", "diminua", "tire", "arranque", "menos"]
    lista_vezes = ["vezes", "multiplique", "*"]
    lista_divide = ["divide", "divida", "dividido", "/"]
    lista_porcentagem = ["por cento", "é quanto de", "porcentagem", "%"]

    numeros = Word(nums) # identifica sequência de numeros
    numeros_encontrados = numeros.searchString(frase) # filtra os números na frase
    numbers = [int(token[0]) for token in numeros_encontrados]
    
    if len(numbers) < 2:
        return 'Preciso de dois números para realizar o pedido'
    
    try:
        if any(identificador in frase for identificador in lista_mais):
            resultado = numbers[0] + numbers[1]
            return f"{numbers[0]} mais {numbers[1]} é igual a {resultado}"
            
        if any(identificador in frase for identificador in lista_menos):
            resultado = numbers[0] - numbers[1]
            return f"{numbers[0]} menos {numbers[1]} é igual a {resultado}"
            
        if any(identificador in frase for identificador in lista_vezes):
            resultado = numbers[0] * numbers[1]
            return f"{numbers[0]} vezes {numbers[1]} é igual a {resultado}"
        
        if any(identificador in frase for identificador in lista_divide):
            try:
                resultado = numbers[0] / numbers[1]
                return f"{numbers[0]} dividio por {numbers[1]} é igual a {resultado}"
            except ZeroDivisionError:
                return f"Não é possível dividir por zero!"
        
        if any(identificador in frase for identificador in lista_porcentagem):
            resultado = (numbers[0] * numbers[1]) / 100
            return f'{numbers[0]}% de {numbers[1]} é {resultado}'

            
    except Exception as error:
        print(f'Algum erro ocorreu: {error}')
        return f"Algum erro ocorreu"
    
if __name__ == '__main__':
    print(calculadora('1 vezes 3 mais 1'))
