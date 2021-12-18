class Article:
    def __init__(self, article, prix_u, stock) -> None:
        self.article = article
        self.prix_u = prix_u
        self.stock = stock

    def __str__(self) -> str:
        return self.article


achat = []
qte = []


test = {}

pains = Article('pain', 1, 50)
eau = Article('eau', 0.5, 40)
riz = Article('riz', 0.75, 60)

produits = [pains, eau, riz]


def liste_articles():
    print("""
        Choisissez un article parmi les suivants :
        1. Pain        prix : 1.00 €  stock : 50
        2. Eau         prix : 0.05 €  stock : 40
        3. Riz         prix : 0.75 €  stock : 60""")


def quantitee() -> int:
    quantite = int(input("combien en voulez vous ?  "))
    print(f"fonction quant : {quantite}")
    return quantite


def choix():
    liste_articles()
    choix_possible = [1, 2, 3, 4, 5]
    no_article = int(input("Votre choix :"))

    if no_article in choix_possible:
        achat.append(produits[no_article - 1])

        # print(achat)
        for produit in test:
            print(produit)
        quantite = quantitee()
        test[f"{produits[no_article - 1]}"] = quantite

        autre_choix = input("Desirez vous un autres article ? ")

        if autre_choix != "o":
            for key, value in test.items():
                print(key, value)
            return
        else:
            return choix()
        # print(f"quantité choix {quantite}")


# print(pains)
choix()
