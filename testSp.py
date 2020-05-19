import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp(u"At 14:15 on eleventh day of January")

print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

for entity in doc.ents:
    print(entity.text, entity.label_)

print(doc.ents)