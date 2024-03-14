from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import datetime
import dateparser
from database import sendresultnlp, senderrornlp

tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/camembert-ner-with-dates")
model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/camembert-ner-with-dates")
nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")

def get_info(text):
    try:
        days = {'hier': datetime.date.today() - datetime.timedelta(days=1), 'après-demain' : datetime.date.today() + datetime.timedelta(days=2), 'demain' : datetime.date.today() + datetime.timedelta(days=1)}
        doc = nlp(text)
        info={}
        for word in doc:
            if word['entity_group'] == 'LOC':
                info.update({'where':word['word']})
            if word['entity_group'] == 'DATE':
                info.update({'when': dateparser.parse(word['word'], languages = ['fr'])})
        for day in days:
            if info['when'] == day:
                info.update({'when': days[day]})
        sendresultnlp(info['when'], info['where'])
        return info
    except Exception as error:
        senderrornlp(error)
