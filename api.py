import requests


nome = input("Digite o nome do Pokémon: ")
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nome}")
type = requests.get(f"https://pokeapi.co/api/v2/pokemon/2/{nome}")
type = response.json()
dados = response.json()


print(dados["name"])

print(dados["weight"])

print(type["types"][0]["type"]["name"])
