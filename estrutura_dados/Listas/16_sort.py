# sort() -> irá ordenar a lista em ordem alfabetica
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()
print(linguagens)

# irá ordenar de modo espelhado
linguagens.sort(reverse=True)
print(linguagens)

# irá ordernar por tamanho da palavra do menor para o maior
linguagens.sort(key=lambda x: len(x))
print(linguagens)

# irá ordernar por tamanho da palavra do maior para o menor
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)