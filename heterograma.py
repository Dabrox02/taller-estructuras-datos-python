def isHeterogram(cad):
    letters = set(cad)
    for letter in letters:
        count = 0
        for char in cad:
            if letter == char:
                count += 1
        if count > 1:
            return False
    return True


cad = input("Ingrese una cadena: ")
if isHeterogram(cad.lower()):
    print("Es heterograma")
else:
    print("No es heterograma")
