historique = []

def ajouter_historique(expression, resultat):
    historique.append(f"{expression} = {resultat}")

def afficher_historique():
    if not historique:
        print("Historique vide.")
    else:
        print("Historique des opérations :")
        for operation in historique:
            print(operation)

def effacer_historique():
    global historique
    historique = []
    print("Historique effacé.")

def calculatrice():
    try:
        # Demander les deux nombres à l'utilisateur
        num1 = float(input("Entrez le premier nombre : "))
        num2 = float(input("Entrez le deuxième nombre : "))
        
        # Demander le type d'opération
        operation = input("Choisissez une opération (+, -, *, /) : ")

        # Effectuer l'opération en fonction du choix de l'utilisateur
        if operation == "+":
            resultat = num1 + num2
        elif operation == "-":
            resultat = num1 - num2
        elif operation == "*":
            resultat = num1 * num2
        elif operation == "/":
            # Gérer la division par zéro
            if num2 == 0:
                print("Erreur : Division par zéro.")
                return
            resultat = num1 / num2
        else:
            print("Erreur : Opération non valide.")
            return

        # Afficher le résultat
        print(f"Le résultat de {num1} {operation} {num2} est égal à {resultat}")

        # Ajouter l'opération à l'historique
        ajouter_historique(f"{num1} {operation} {num2}", resultat)

    except ValueError:
        print("Erreur : Entrée invalide. Veuillez entrer des nombres valides.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Exemple d'utilisation
calculatrice()
afficher_historique()
effacer_historique()
afficher_historique()
