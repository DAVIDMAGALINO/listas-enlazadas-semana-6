def check_balanced(formula):
    stack = []

    # Mapa de los símbolos de apertura y cierre
    matches = {')': '(', ']': '[', '}': '{'}

    # Recorremos cada caracter en la fórmula
    for char in formula:
        if char in '([{':  # Si es un símbolo de apertura, lo agregamos a la pila
            stack.append(char)
        elif char in ')]}':  # Si es un símbolo de cierre, verificamos que coincida con el símbolo de apertura reciente
            if not stack:  # Si la pila está vacía, no está balanceada
                return False
            top = stack.pop()
            if matches[char] != top:  # Si el símbolo no coincide, no está balanceada
                return False

    # La fórmula está balanceada si la pila está vacía al final
    return not stack


# Ejemplo de fórmula para verificar
formula = "{7+(8*5)-[(9-7)+(4+1)]}"

# Verificación y resultado
if check_balanced(formula):
    print("La fórmula está balanceada.")
else:
    print("La fórmula NO está balanceada.")
