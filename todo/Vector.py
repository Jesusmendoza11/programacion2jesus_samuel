lista_vacia = []

lista_mas_5 = [1, 2, 3, 4, 5, 6]

longitud_lista_vacia = len(lista_vacia)
longitud_lista_mas_5 = len(lista_mas_5)

primer_elemento = lista_mas_5[0]
elemento_central = lista_mas_5[len(lista_mas_5)//2]
ultimo_elemento = lista_mas_5[-1]

Datos_personales = []
Datos_personales.append("JESUS")
Datos_personales.append(19)
Datos_personales.append(1.60)
Datos_personales.append("en_una_relacion")
Datos_personales.append("clemencia,bolivar")

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

it_companies.insert(3, "motorola")

empresa = "google"
if empresa in it_companies:
    print(f"{empresa} está en la lista it_companies.")
else:
    print(f"{empresa} no está en la lista it_companies.")

it_companies.sort()

it_companies.reverse()

primer_empresa = it_companies.pop(0)

it_companies.clear()

print("Longitud de lista_vacia:", longitud_lista_vacia)
print("Longitud de lista_mas_5:", longitud_lista_mas_5)
print("Primer elemento:", primer_elemento)
print("Elemento central:", elemento_central)
print("Último elemento:", ultimo_elemento)
print("Datos personales:", Datos_personales)
print("it_companies después de todas las operaciones:", it_companies)
print("Primera empresa eliminada:", primer_empresa)