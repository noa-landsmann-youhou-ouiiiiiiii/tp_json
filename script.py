# JSON sous forme de texte
import json

json_str = '''
{
    "zone": {
        "id": 1,
        "nom": "z_bureaux",
        "capacite": 25,
        "responsable": {
            "nom": "Dupont",
            "prenom": "Alice",
            "email": "alice.dupont@example.com"
        },
        "equipements": {
            "ordinateurs": 10,
            "imprimantes": 2,
            "projecteur": true
        }
    }
}'''
# Afficher le type de la variable
print("Type de la variable json_str :", type(json_str))

# Conversion en dictionnaire Python dans une variable 'json_data'
json_data = json.loads(json_str)

# Afficher le type de la variable data
print("Type de la variable json_data :", type(json_data))

# Affichage des informations de la zone
print("\n **** Affichage des informations de la zone ****")

# Accéder aux attributs principaux ID et nom de la zone
print(f"ID : {json_data['zone']['id']}\nnom : {json_data['zone']['nom']}")

# compléter : afficher la capacité
print(f"capacité : {json_data['zone']['capacite']}")

# compléter : afficher le nom et le prénom du responsable
print(f"Responsable : {json_data['zone']['responsable']['prenom']} {json_data['zone']['responsable']['nom']} ({json_data['zone']['responsable']['email']})")

# facultatif on peut mettre objet dictionnaire responsable dans une variable spécifique
# responsable = data[.....

responsable = json_data['zone']['responsable']['prenom']+" "+json_data['zone']['responsable']['nom']

# compléter : pour afficher les équipements

print(f"Equipements : \n\t- {json_data['zone']['equipements']['ordinateurs']} ordinateurs\n\t- {json_data['zone']['equipements']['imprimantes']} imprimates\n\t",end="")
if json_data['zone']['equipements']['projecteur']:
    print("1 projecteur")
else:
    print("Pas de projecteur")