def Saluer(nom: str) -> str:
    print(f"Bonjour, {nom} !")
    
def add(a: int, b: int) -> int:
    return a + b

def divide(a: float, b: float = 1.0) -> float:
    if b == 0:
        raise ValueError("Le dénominateur ne peut pas être zéro.")
    return a / b

def addition_multiple(*params: int) -> int:
    print(f"Paramètres reçus : {params}")
    print(f"Type de params : {type(params)}")
    total = 0
    for nbr in params:
        total += nbr
    return total

def afficher_info(**info: str) -> None:
    print("type de info :", type(info))
    for cle, valeur in info.items():
        print(f"{cle} : {valeur}")