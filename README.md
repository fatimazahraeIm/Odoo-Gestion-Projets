# Module GestionProjets

## Description du projet et objectif
Le module `gestionProjets` est conçu pour gérer les projets au sein de l'entreprise. Il permet de suivre les différentes étapes des projets, de gérer les ressources humaines et matérielles, et de générer des rapports détaillés sur l'avancement des projets. Dans ce projet, on affecte les véhicules, employés, produits aux projets en définissant les délais et les coûts. Il inclut également la gestion des véhicules (maintenance, remplacement, entrepôt, ville).

## Outils utilisés
- **Langages de programmation** : Python, XML
- **Framework** : Odoo
- **IDE** : Visual Studio Code


## Utilisation
   - Clonez le dépôt GitHub dans le répertoire des modules Odoo.
   - Mettez à jour la liste des modules dans Odoo.
   - Installez le module `gestionProjets` depuis l'interface d'administration d'Odoo.

## Précautions

- **Suppression des boutons de reporting avant l'activation du module** : Avant d'activer le module, il est nécessaire de supprimer les boutons de reporting présents dans le dossier `views`, dans chaque fichier `view.xml`. En effet, Odoo compile les vues avant de créer les modèles de reporting, ce qui peut provoquer une erreur si les modèles associés n'ont pas encore été créés. Une fois le module activé, vous pouvez récupérer les boutons de reporting.

- **Erreur de permission lors de l'utilisation des boutons de reporting** : Il est possible qu'une erreur de permission apparaisse lorsque vous tentez d'utiliser le bouton de reporting, indiquant que l'utilisateur n'a pas les permissions nécessaires. Pour résoudre ce problème, il suffit de modifier l'entreprise associée à l'employé ou associée aux autres modules créés en cochant cette entreprise.