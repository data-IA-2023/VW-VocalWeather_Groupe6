from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import datetime

tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/camembert-ner-with-dates")
model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/camembert-ner-with-dates")
nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")



def get_info(text):
    days = {'demain' : datetime.date.today() + datetime.timedelta(days=1), 'hier': datetime.date.today() + datetime.timedelta(days=-1)
    ,'aprésdemain' : datetime.date.today() + datetime.timedelta(days=2)}
    doc = nlp(text)
    info={}
    for word in doc:
        if word['entity_group'] == 'LOC':
            info.update({'where':word['word']})
        if word['entity_group'] == 'DATE':
            info.update({'when':word['word']})
    for day in days:
        if info['when'] == day:
            info.update({'when': days[day]})
    return info

print(datetime.date(2024, 3, 12))