from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/camembert-ner-with-dates")
model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/camembert-ner-with-dates")
nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")

def get_info(text):
    doc = nlp(text)
    info={}
    for word in doc:
        if word['entity_group'] == 'LOC':
            info.update({'where':word['word']})
        if word['entity_group'] == 'DATE':
            info.update({'when':word['word']})
    return info