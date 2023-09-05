# Modules importation
import os
import base64
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = (Fore.RED + """
 $$$$$$\            $$\                     $$\            $$\                         
$$  __$$\           $$ |                    $$ |           $$ |                        
$$ /  \__| $$$$$$\  $$ | $$$$$$$\ $$\   $$\ $$ | $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  
$$ |       \____$$\ $$ |$$  _____|$$ |  $$ |$$ | \____$$\\_$$  _|  $$  __$$\ $$  __$$\ 
$$ |       $$$$$$$ |$$ |$$ /      $$ |  $$ |$$ | $$$$$$$ | $$ |    $$ /  $$ |$$ |  \__|
$$ |  $$\ $$  __$$ |$$ |$$ |      $$ |  $$ |$$ |$$  __$$ | $$ |$$\ $$ |  $$ |$$ |      
\$$$$$$  |\$$$$$$$ |$$ |\$$$$$$$\ \$$$$$$  |$$ |\$$$$$$$ | \$$$$  |\$$$$$$  |$$ |      
 \______/  \_______|\__| \_______| \______/ \__| \_______|  \____/  \______/ \__|      by 0xCastor
                                                                                       
                                                                                       
                                                                                       
""" + Fore.LIGHTRED_EX)
print(banner)
def additionner(a, b):
    return a + b


def soustraire(a, b):
    return a - b

def multiplier(a, b):
    return a * b

def diviser(a, b):
    if b == 0:
        return "Division par zéro impossible"
    return a / b

# Menu principal
while True:
    print("Options:")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    
    choix = input("Choisissez une option (1/2/3/4/5): ")

    
    nombre1 = float(input("Entrez le premier nombre: "))
    nombre2 = float(input("Entrez le deuxième nombre: "))
    
    if choix == "1":
        print("Résultat:", additionner(nombre1, nombre2))
    elif choix == "2":
        print("Résultat:", soustraire(nombre1, nombre2))
    elif choix == "3":
        print("Résultat:", multiplier(nombre1, nombre2))
    elif choix == "4":
        print("Résultat:", diviser(nombre1, nombre2))
        
    else:
        print("Option invalide. Veuillez choisir une option valide.")
