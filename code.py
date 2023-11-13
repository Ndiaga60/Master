def pourboire(montant_note,pourcentage_note):

	calcul_pourboire=(montant_note*pourcentage_pourboire)/100)
	r=montant_note+calcul_pourboire
	
	print(f"Montant de la note : {montant_note}$")
	print(f"Pourboire({pourcentage_note}$): {calcul_pourboire}$")
	print(f"Montant total a payer : {r}$")

x=float(input("quel est la note a payer? : "))
y=float(input("quel est le pourcentage de la note que vous vouliez attribuer comme pourboire?"))
pourboire(x,y)
