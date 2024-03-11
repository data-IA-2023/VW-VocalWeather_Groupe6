"""
==========================================
classe :
    
methode : 
    
==========================================
"""

# importations des librairie
import spacy
from spacy.lang.fr import French
from spacy.matcher import Matcher

# Construction from subclass
nlp = French()

# initialise pipeline pré-entrainer en francais de spacy
nlp = spacy.load("fr_core_news_sm")

def nlm_traitement ( spetch_to_text ) :

    doc = nlp(spetch_to_text)

    # Initialise le matcher avec le vocabulaire partagé
    matcher = Matcher(nlp.vocab)

    # Crée un motif qui recherche les deux tokens : "X" et "Pro"
    pattern = [{"TEXT": "X"}, {"TEXT": "Pro"}]

    # Ajoute le motif au matcher
    matcher.add("IPHONE_X_PATTERN", [pattern])

    # Utilise le matcher sur le doc
    matches = matcher(doc)
    print("Résultats :", [doc[start:end].text for match_id, start, end in matches])

    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
                token.shape_, token.is_alpha, token.is_stop, token)
    print("doc :", doc)

result = nlm_traitement("quel temps il vera demain à Tours")
print(result)