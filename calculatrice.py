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

    except ValueError:
        print("Erreur : Entrée invalide. Veuillez entrer des nombres valides.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Appeler la fonction de la calculatrice
calculatrice()
