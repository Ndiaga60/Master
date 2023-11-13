montant_note = float(input('Entrez le montant de la note : '))
pourcentage_pourboire=float(input("quel est le pourcentage du pourboire que vous voulez donner comparé a la note?"))
calcul_pourboire=(montant_note*pourcentage_pourboire)/100)
r=montant_note+calcul_pourboire

print(f"Montant de la note : {montant_note}$")
print(f"Pourboire({pourcentage_note}$): {calcul_pourboire}$")
print(f"Montant total a payer : {r}$")

