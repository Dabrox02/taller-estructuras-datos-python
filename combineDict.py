def combineDicts(dictA, dictB):
    result = {}
    for key, value in zip(dictA, dictB):
        result[key] = value
    return result 

a = {1,3,5,7,9}
b = {"lunes", "martes", "miercoles", "jueves", "viernes"}

print(combineDicts(a,b))