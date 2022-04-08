import random

fichier_heros = open("fichier_heros.txt","r")
with open("fichier_heros.txt") as fichier_heros:
	heros_ligne = fichier_heros.read().splitlines()


fin = False
fin_line = False

print_temporaire = ""
lines_temporaire = []
heros_ligne_temporaire = []

inventory = {}

condition = []

option_possible = []

inventaire_objet_manquant = True

death_no_life = False

life = 1

ennemi_joueur_battu = False

change = True

ligne = 1
nbiteration = 0

def death_test_monster():
	global life_monstre, ennemi_joueur_battu
	if life_monstre<=0:
		print("Vous avez battu le monstre, bravo!")
		ennemi_joueur_battu = True


def death_test():
	global life, fin, fin_line
	if life<=0:
		print("Vous n'avez plus de vie, vous avez donc perdu!")
		fin = True
		fin_line = True

while not fin:
	while not fin_line:

		ligne_tour = ligne-1+nbiteration

		heros_ligne_temporaire = heros_ligne[ligne_tour].split()
		
		if heros_ligne_temporaire[0] == "print:":
			print(heros_ligne[ligne_tour].replace("print:",""))

		if heros_ligne_temporaire[0] == "input:":
			input_temporaire = int(input(heros_ligne[ligne_tour].replace("input:","")))

		if heros_ligne_temporaire[0] == "lines:":
			lines_for_input = heros_ligne[ligne_tour].replace("lines:","")
			lines_for_input = lines_for_input.split()
			redirection = int(lines_for_input[int(input_temporaire)-1])
			for i in range(len(heros_ligne)):
				try:
					if int(heros_ligne[i]) == redirection:
						ligne = i+1
						fin_line = False
				except:
					pass

			fin_line = True

		if heros_ligne_temporaire[0] == "fin:":
			fin = True
			fin_line = True

		if heros_ligne_temporaire[0] == "add_inventory:":
			append_dict_temporaire = heros_ligne[ligne_tour].replace("add_inventory:","")
			append_dict_temporaire = append_dict_temporaire.split()



			if (append_dict_temporaire[0] in inventory):
				inventory[append_dict_temporaire[0]] += int(append_dict_temporaire[1])
			else:
				inventory[append_dict_temporaire[0]] = int(append_dict_temporaire[1])

			print("Il y a dans votre inventaire :", inventory)

		if heros_ligne_temporaire[0] == "line_condition:":
			condition = []
			append_dict_temporaire = heros_ligne[ligne_tour].replace("line_condition:","")
			append_dict_temporaire = append_dict_temporaire.split()

			nombre_tour = 0

			for i in range(int(len(append_dict_temporaire)/2)):
				condition.append(append_dict_temporaire[nombre_tour]) 
				condition.append(append_dict_temporaire[nombre_tour+1])
				nombre_tour+=2

			nombre_tour = 0
			option_possible = []
			for i in range(int(len(condition)/2)):

				if condition[nombre_tour] in inventory:
					if inventory[condition[nombre_tour]] > 0:
						print("Vous pouvez faire l'option",i+1)
						option_possible.append(i+1)

				nombre_tour += 2
				print(len(option_possible))
			if len(option_possible) == 0:
				change = False
			if change:
				while inventaire_objet_manquant:
					valeur_temporaire = int(input("Choisissez l'option "))
					for i in range(len(option_possible)):
						if valeur_temporaire == option_possible[i]:
							inventaire_objet_manquant = False

				inventaire_objet_manquant = True

				nombre_tour = 0

				for i in range(valeur_temporaire-1):
					nombre_tour+=2

				redirection = int(condition[nombre_tour+1])
				for i in range(len(heros_ligne)):
					try:
						if int(heros_ligne[i]) == redirection:
							ligne = i+1
							fin_line = True
					except:
						pass
				inventory[condition[nombre_tour]] -=1
				print(inventory)
			change = True

		if heros_ligne_temporaire[0] == "setup_life:":
			append_dict_temporaire = heros_ligne[ligne_tour].replace("setup_life:","")
			append_dict_temporaire = append_dict_temporaire.split()
			life = int(append_dict_temporaire[0])

			print("Vous avez : ",life,"points de vie")

		if heros_ligne_temporaire[0] == "add_life:":
			append_dict_temporaire = heros_ligne[ligne_tour].replace("add_life:","")
			append_dict_temporaire = append_dict_temporaire.split()
			append_dict_temporaire[0] = int(append_dict_temporaire[0])
			life += append_dict_temporaire[0]

			if append_dict_temporaire[0] >=0:
				print("Vous avez gagner", append_dict_temporaire[0],"points de vie.")

			elif append_dict_temporaire[0]<=0:
				print("Vous avez perdu",-append_dict_temporaire[0],"points de vie")

			print("Vous avez : ",life,"points de vie")

		if heros_ligne_temporaire[0] == "life_rules:":
			append_dict_temporaire = heros_ligne[ligne_tour].replace("life_rules:","")
			append_dict_temporaire = append_dict_temporaire.split()

			for i in range(len(append_dict_temporaire)):
				if append_dict_temporaire[i] == "death_no_life":
					death_no_life = True
					print("La regle mortelle a été activée, si votre compteur de vie tombe à zéro, vous mourrez.")

		if heros_ligne_temporaire[0] == "min_attaquejoueur:":
			append_dict_temporaire = heros_ligne[ligne_tour].replace("min_attaquejoueur:","")
			append_dict_temporaire = append_dict_temporaire.split()
			min_attaquejoueur = int(append_dict_temporaire[0])

		if heros_ligne_temporaire[0] == "max_attaquejoueur:":
			append_dict_temporaire = heros_ligne[ligne_tour].replace("max_attaquejoueur:","")
			append_dict_temporaire = append_dict_temporaire.split()
			max_attaquejoueur = int(append_dict_temporaire[0])


		if heros_ligne_temporaire[0] == "monstre:":
			append_dict_temporaire = heros_ligne[ligne_tour].replace("monstre:","")
			append_dict_temporaire = append_dict_temporaire.split()
			nom_monstre = append_dict_temporaire[0]
			life_monstre = int(append_dict_temporaire[1])
			attack_min_monstre = int(append_dict_temporaire[2])
			attack_max_monstre = int(append_dict_temporaire[3])
			print("Un monstre du nom de", nom_monstre,"est apparu, il engage le combat")

			while not ennemi_joueur_battu and not fin:
				print("Vous avez actuellement",life,"point de vie.")
				print(nom_monstre,"a",life_monstre,"point de vie.")
				dega_monstre = random.randint(attack_min_monstre,attack_max_monstre)
				dega_joueur = random.randint(min_attaquejoueur,max_attaquejoueur)
				life -= dega_monstre
				life_monstre -= dega_joueur
				death_test()
				death_test_monster()
				print("Vous avez fait", dega_joueur,"degats.")
				print("Le monstre vous a fait",dega_monstre,"degats.")

			ennemi_joueur_battu = False
			print("Il vous reste",life,"points de vie.")

		if heros_ligne_temporaire[0] == "quiz:":
			input_temporaire = input()
			append_dict_temporaire = heros_ligne[ligne_tour].replace("quiz:","")
			append_dict_temporaire = append_dict_temporaire.split()
			if append_dict_temporaire[0] == input_temporaire:
				redirection = int(append_dict_temporaire[1])
				for i in range(len(heros_ligne)):
					try:
						if int(heros_ligne[i]) == redirection:
							ligne = i+1
							fin_line = True

					except:
						pass
			else:
				redirection = int(append_dict_temporaire[2])
				for i in range(len(heros_ligne)):
					try:
						if int(heros_ligne[i]) == redirection:
							ligne = i+1
							fin_line = True

					except:
						pass




		if death_no_life:
			death_test()


		nbiteration+=1

	nbiteration = 0
	fin_line = False





