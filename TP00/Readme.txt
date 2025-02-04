Ce programme traite des algorithmes avancés et des structures de données.

Le dossier principal, TPOO, contient 5 dossiers correspondant à différents exercices :

    1_binary_search : contient le code source de l'algorithme de recherche binaire.
    2_graph_transversal_bfs_dfs : contient le code source des algorithmes Breadth-First Search (BFS) et Depth-First Search (DFS).
    3_knapsack : contient le code source de l'algorithme 0/1 Knapsack utilisant la programmation dynamique.
    4_mergeIntervalle : contient le code source de l'algorithme permettant de fusionner les intervalles qui se chevauchent.
    5_kadane : contient le code source de l'algorithme  Kadane est généralement utilisé pour le problème du sous-tableau de somme maximale.

Prérequis :

    Python 3.x doit être installé sur votre machine.

Installation :

    Clonez ce dépôt ou téléchargez les fichiers sources.
    Aucune dépendance externe n'est requise, le programme utilise uniquement la bibliothèque standard de Python.

Rendez-vous dans le répertoire principal :
    cd TPOO

Exécution du programme :
    Chaque sous-dossier contient un répertoire src qui abrite le fichier .py à exécuter.
    Pour lancer un exercice, rendez-vous dans le sous-dossier souhaité, puis dans son dossier src et exécutez :
         cd src
         python3 nom_du_fichier.py


Dans le dossier '1_binary_search' il y a deux sous dossiers dont 'data' et 'src' :
 le dossier 'src' contient des fichiers .py dont :
     - binary_search_with_sorted_list.py
     - file_binary_search.py
     - linear_search.py
  Dans le fichier 'binary_search_with_sorted_list.py' :  l'uitlisateur doit:
      ~ Entrer la taille du tableau 
      ~ Entrer les valeurs dans l'ordre.
      ~ Entrer la valeur  à rechercher.
  Dans le fichier 'file_binary_search.py' : les nombres sont défini dans un fichier 'file.txt' contenu dans le dossier 'data'
    pour permettre à utilisateur d'entrer facilement une grande quantité de nombre à traiter.
      ~ Il faut se rendre dans le fichier 'data/file.txt' et entrer les nombres verticalement ou horizontalement
      ~ Lancer le programme et entrer la valeur à rechercher
  Dans le fichier 'linear_search.py' : on a implémenter un algorithme de recherche lineaire, les nombres sont prédéfinis dans le code.

  