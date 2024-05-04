import sys

conversiones = {
    "Soles": sys.argv[1],
    "Pesos Argentinos": sys.argv[2],
    "Dólares": sys.argv[3]
}

pesos_chileno = int(sys.argv[4])

print("Los", pesos_chileno, "equivalen a:")
for k,v in conversiones.items():
    print(pesos_chileno * float(v), k)