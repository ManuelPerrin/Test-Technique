# Test-Technique


Test technique d'un composant logiciel qui à partir d’une base de données, représentant une base de discussion d’une application de messagerie, génère en sortie des fichiers JSON dans un répertoire où chacun d’entre eux représente un message de cette base.



### Test général :

Code : "Test_General"

Le code permet de vérifier que le fichier JSON entré :

- contient tous les paramètres obligatoires attendus (required)
- contient des valeurs dont le type est celui attendu
- contient la valeur "originating" ou "destinating" pour le paramètre "direction"


Pour tester, quatre fichiers json sont disponibles :

- le fichier "message1.json" présente un cas passant
- le fichier "message2.json" présente un cas d'erreur dans lequel un paramètre obligatoire est manquant
- le fichier "message3.json" présente un cas d'erreur dans lequel le format d'un paramètre diffère de celui attendu
- le fichier "message4.json" présente un cas d'erreur dans lequel la valeur du paramètre "direction" ne correspond à aucune des valeurs attendues



### Test des fichiers obtenus :

Code : "Test_FichiersObtenus"

Le code permet de tester les 10 fichiers obtenus afin de vérifier qu'ils sont conformes à la base de données.
