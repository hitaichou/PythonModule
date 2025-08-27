import re

text = "Udemy - uma plataforma com muitos cursos"
# 1 - índice inicial e final da palavra
# 0 r significa uma raw string (string bruta)
match = re.search(r"uma plataforma", text)
print(f"Índice inicial: {match.start()}")
print(f"Índice final: {match.end()}")


# 2 - buscar o indice que possui um ponto
site = "https://udemy.com"
match = re.search(r"\.", site)
print(match)

# 3 - buscar uma lista de caracteres em uma frase
pattern = "[g-m]"
result = re.findall(pattern, text)
print(result)

# 4 -verificando o inicio de uma string
rule = r'^A'
phrase = ['A casa está suja', 'O dia está lindo','Vamos passear']
for f in phrase:
    if re.match(rule, f):
        print(f"Corresponde: {f}")
    else:
        print(f"Não corresponde: {f}")
        
#"5 - Verificando o final de uma string"
rule_end = r'!$'
phrase2 = "O dia está lindo!"
match = re.search(rule_end, phrase2)
if match:
    print("Corresponde")
else:
    print("Não corresponde")