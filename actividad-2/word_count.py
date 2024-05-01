
with open("lorem_ipsum.txt", "r") as file:
	contenido = file.read()
	palabras_separadas = contenido.split()
      
palabras_unicas = list(set(palabras_separadas))
caracteres_unicos = list(set("".join(palabras_separadas)))

print("El número de caracteres distintos es:", len(caracteres_unicos))
print("El número de palabras distintas es:", len(palabras_unicas))