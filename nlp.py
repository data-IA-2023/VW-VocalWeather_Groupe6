from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import datetime
import dateparser

tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/camembert-ner-with-dates")
model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/camembert-ner-with-dates")
nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")



def get_info(text):
    days = {'hier': datetime.date.today() - datetime.timedelta(days=1), 'aprés demain' : datetime.date.today() + datetime.timedelta(days=2), 'demain' : datetime.date.today() + datetime.timedelta(days=1)}
    doc = nlp(text)
    info={}
    for word in doc:
        if word['entity_group'] == 'LOC':
            info.update({'where':word['word']})
        if word['entity_group'] == 'DATE':
            print(word['word'])
            info.update({'when': dateparser.parse(word['word'])})
    for day in days:
        if info['when'] == day:
            info.update({'when': days[day]})
    return info