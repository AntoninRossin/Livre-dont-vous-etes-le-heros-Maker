# Livre-dont-vous-etes-le-heros-Maker
Bienvenu de ce créateur de livre dont vous êtes le héros.
Pour procéder à la création de votre livre vous devrez écrire des commandes dans le fichier texte ficher_heros.txt .
Il y a dans ce fichier un exemple de livre qu'il est possible de créer facilement grace au programme.
Je vais maintenant vous écrire une liste de commandes utilisables et les arguments que ses commandes prennent.

chapitre n (soit n un entier, sera utile pour la redirection(commande montrée plus tard) à divers endroits du documents txt).

print: votre texte (affiche votre texte à l'écran)

input: votre texte (affiche votre texte à l'écran et vous donnera la possibilité au joueur de dire un chiffre qui servira lors de la commande suivante)

lines: chapitre chapitre (autant d'arguments qu'on veut, doit être un nombre, correspond au chapitre où le joueur sera envoyé. ex: si le joueur a répondu
1 à l'input, il sera redirigé au chapitre du nom de l'argument 1. Soit pour une réponse n, il sera renvoyé au chapitre correspondant à l'n-ième argument après la commande lines:. Voir exemple dans le doc fichier_heros.txt)

add_inventory: item quantité (rajoute un item dans l'inventaire du joueur, de la quantité écrite au deuxième argument)

setup_life: valeur (met la vie du joueur à la valeur inscrite après la commande)

add_life: valeur (la valeur peut être positive ou négative, ajoute ou soustraie la valeur à la vie du joueur)

life_rules: death_no_life (Il y a pour l'instant une seule règle concernant les vies, il s'agit de death_no_life.
Une fois activée si la vie du joueur tombe à 0 ou moins la partie se finit, il est conseillé de l'activer pour une expérience classique.)

line_condition: item chapitre (même principe que pour le lines: et le input:. Va demander une valeur, le joueur ne pourras choisir une option que s'il a au moins un item du nom indiqué,
redirigera au chapitre indiqué, si aucun choix n'est possible, passe à la suite,peut être utilisé pour l'utilisation de potion de vie par ex, ou descendre d'une falaise avec une corde...)

min_attaquejoueur: nombre (minimum de dégat que le joueur peut faire)

max_attaquejoueur: nombre (maximum de dégat que le joueur peut faire)

monstre: nom_du_monstre pointdevie_monstre min_attaquemonstre max_attaquemonstre (pour pointdevie_monstre min_attaquemonstre max_attaquemonstre des entiers sont demandés).
un combat va être engagé entre le joueur et le monstre, l'attaque du joueur sera aléatoire, entre son minimun et son maximum, idem pour le monstre, le combat s'arrête
une fois que un des deux sont morts. Il est hautement recommandé d'avoir la règle death_no_life d'activée

fin: (pas d'argument, arrête le jeu)

Une fois que votre document sera rédigé, veuillez lancer le programme python be_a_heros.py. Il commencera à le déchiffre par la première ligne puis parcoureras le document en fonction des commandes que vous avez écrites.
