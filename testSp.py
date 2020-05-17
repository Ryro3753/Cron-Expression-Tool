import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp(u"At every minute from 35 through 38 past hour 14 in every month from January through February.")

print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

for entity in doc.ents:
    print(entity.text, entity.label_)

print(doc.ents)