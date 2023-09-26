# é a mesma coisa que o sort, porém se torna uma função 
 
linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))
print(sorted(linguagens, key=lambda x: len(x), reverse=True))
print(sorted(linguagens))

