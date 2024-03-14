"""
==========================================
classe :
    NLP
methode : 
    get_info(text)=> return info{'where':'', 'when':''}
    date_jours_nom ( DATE ) => date (yyyy, mm, jj) à partir du nom d'un jour
==========================================
"""
# importations des librairie
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import datetime
import dateparser

tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/camembert-ner-with-dates")
model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/camembert-ner-with-dates")
nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")

def get_info(text):

    days = {"aujourd'hui" : datetime.date.today(), 
            'demain' : datetime.date.today() + datetime.timedelta(days=1), 
            'hier': datetime.date.today() + datetime.timedelta(days=-1), 
            'aprés demain' : datetime.date.today() + datetime.timedelta(days=2),
            'dans 2 jours' : datetime.date.today() + datetime.timedelta(days=2), 
            'dans 3 jours' : datetime.date.today() + datetime.timedelta(days=3),
            'dans 4 jours' : datetime.date.today() + datetime.timedelta(days=4), 
            'dans 5 jours' : datetime.date.today() + datetime.timedelta(days=5),
            'dans 6 jours' : datetime.date.today() + datetime.timedelta(days=6),
            'dans une semaine' : datetime.date.today() + datetime.timedelta(days=7),
            'semaine prochaine' : datetime.date.today() + datetime.timedelta(days=7), 
            "aujourd'hui à" : datetime.date.today(), 
            'demain à' : datetime.date.today() + datetime.timedelta(days=1), 
            'hier à': datetime.date.today() + datetime.timedelta(days=-1),
            'aprés demain à' : datetime.date.today() + datetime.timedelta(days=2), 
            'dans 2 jours à' : datetime.date.today() + datetime.timedelta(days=2), 
            'dans 3 jours à' : datetime.date.today() + datetime.timedelta(days=3),
            'dans 4 jours à' : datetime.date.today() + datetime.timedelta(days=4),
            'dans 5 jours à' : datetime.date.today() + datetime.timedelta(days=5),
            'dans 6 jours à' : datetime.date.today() + datetime.timedelta(days=6),
            'dans une semaine à' : datetime.date.today() + datetime.timedelta(days=7),
            'semaine prochaine à' : datetime.date.today() + datetime.timedelta(days=7)}
    
    list_jour = ["lundi", "lundi à", "mardi", "mardi à", "mercredi", "mercredi à", "jeudi", "jeudi à", "vendredi", "vendredi à", 
                 "samedi", "samedi à", "dimanche", "dimanche à"]
    doc = nlp(text)
    info={}
    for word in doc:
        if word['entity_group'] == 'LOC':
            info.update({'where':word['word']})
        if word['entity_group'] == 'DATE':
            if word['word'] in list_jour :
                info.update({'when': date_jours_nom(word['word'])})
            else :
                info.update({'when':dateparser.parse(word['word'], languages=["fr"])})
    for day in days:
        if info['when'] == day:
            info.update({'when': days[day]})
    return info

def date_jours_nom ( DATE ):
    jour_actu = datetime.date.today().weekday()
    if DATE == "lundi" or DATE == "lundi à" :
        jour_cible = 0
    elif DATE == "mardi" or DATE == "mardi à" :
        jour_cible = 1
    elif DATE == "mercredi" or DATE == "mercredi à" :
        jour_cible = 2
    elif DATE == "jeudi" or DATE == "jeudi à" :
        jour_cible = 3
    elif DATE == "vendredi" or DATE == "vendredi à" :
        jour_cible = 4
    elif DATE == "samedi" or DATE == "samedi à":
        jour_cible = 5
    else:
        jour_cible = 6
    
    if jour_actu == 0 :
        dif = abs(jour_actu - jour_cible)
        day = datetime.date.today() + datetime.timedelta(days=dif)
    elif jour_actu == 1 : 
        if jour_cible == 0 :
            dif = 6
            day = datetime.date.today() + datetime.timedelta(days=dif) 
        else :
            dif = abs(jour_actu - jour_cible)
            day = datetime.date.today() + datetime.timedelta(days=dif) 
    elif jour_actu == 2 :
        if jour_cible == 0 :
            dif = 5
            day = datetime.date.today() + datetime.timedelta(days=dif)
        if jour_cible == 1 :
            dif = 6
            day = datetime.date.today() + datetime.timedelta(days=dif)
        else :
            dif = abs(jour_actu - jour_cible)
            day = datetime.date.today() + datetime.timedelta(days=dif)
    elif jour_actu == 3 :
        if jour_cible == 0 :
            dif = 4
            day = datetime.date.today() + datetime.timedelta(days=dif)
        if jour_cible == 1 :
            dif = 5
            day = datetime.date.today() + datetime.timedelta(days=dif)
        if jour_cible == 2 :
            dif = 6
            day = datetime.date.today() + datetime.timedelta(days=dif)
        else :
            dif = abs(jour_actu - jour_cible)
            day = datetime.date.today() + datetime.timedelta(days=dif)
    elif jour_actu == 4 :
        if jour_cible == 0 :
            dif = 3
            day = datetime.date.today() + datetime.timedelta(days=dif)
        if jour_cible == 1 :
            dif = 4
            day = datetime.date.today() + datetime.timedelta(days=dif)
        if jour_cible == 2 :
            dif = 5
            day = datetime.date.today() + datetime.timedelta(days=dif)
        if jour_cible == 3 :
            dif = 6
            day = datetime.date.today() + datetime.timedelta(days=dif)
        else :
            dif = abs(jour_actu - jour_cible)
            day = datetime.date.today() + datetime.timedelta(days=dif)
    elif jour_actu == 5 :
        if jour_cible == 0 :
            dif = 2
            day = datetime.date.today() + datetime.timedelta(days=dif)
        if jour_cible == 1 :
            dif = 3
            day = datetime.date.today() + datetime.timedelta(days=dif)
        if jour_cible == 2 :
            dif = 4
            day = datetime.date.today() + datetime.timedelta(days=dif)
        if jour_cible == 3 :
            dif = 5
            day = datetime.date.today() + datetime.timedelta(days=dif)
        if jour_cible == 4 :
            dif = 6
            day = datetime.date.today() + datetime.timedelta(days=dif)
        else :
            dif = abs(jour_actu - jour_cible)
            day = datetime.date.today() + datetime.timedelta(days=dif)
    elif jour_actu == 6 :
        dif = abs(jour_cible+1)
        day = datetime.date.today() + datetime.timedelta(days=dif)
    
    return datetime.datetime.combine(day, datetime.datetime.min.time())

print(get_info("C'est quoi la meteo pour dimanche à Paris ?"))