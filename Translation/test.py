import json
import pytest
import os
from find_to_translate import find_not_translated


test_dict = {
    "product_list": "Liste des Produits",
    "add_product": "Ajouter Produit",
    "edit_product": "Modifier Produit",
    "delete_product": "Supprimer Produit",
    "product_settings": {
        "product-general": "TBT:Product General Settings",
        "product_details": "Détails Produit",
        "price": "Prix",
        "availability": "Disponibilité"
    },
    "category": "Catégorie",
    "product-help": "TBT:Product Help",
    "product_search": {
        "basic": "Recherche Produit",
        "product-advanced": "TBT:Product Advanced Search",
        "filter": "Filtrer"
    },
    "sort_by": "Trier Par",
    "actions": "Actions",
    "product-search": "TBT:Product Search",
    "recently_added": "Ajouté Récemment",
    "popular": "Populaire",
    "rating": "Évaluation",
    "product-new": "TBT:Product New",
    "quantity": "Quantité",
    "description": "Description",
    "supplier": "Fournisseur",
    "product-calendar": "TBT:Product Calendar",
    "date_added": "Date d'Ajout",
    "last_modified": "Dernière Modification"
}
test_result = {
    "temp.json": {
        "product_settings": {
            "product-general": "TBT:Product General Settings"
        },
        "product-help": "TBT:Product Help",
        "product_search": {
            "product-advanced": "TBT:Product Advanced Search"
        },
        "product-search": "TBT:Product Search",
        "product-new": "TBT:Product New",
        "product-calendar": "TBT:Product Calendar"
    }
}

with open('temp.json', 'w', encoding='utf8') as temp_file:
    json.dump(test_dict,temp_file, indent=4)


def test_find_not_translated():
    assert find_not_translated(['temp.json'], 'TBT') == test_result
    os.remove('temp.json')

