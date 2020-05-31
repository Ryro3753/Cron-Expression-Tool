import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp(u"")
doc2 = nlp(u"16:45 at January thirteenth")
doc3 = nlp(u"Meet me in France, Especially at Hospital")


print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

for entity in doc.ents:
    print(entity.text, entity.label_)




print("Noun phrases:", [chunk.text for chunk in doc2.noun_chunks])
for entity in doc2.ents:
    print(entity.text, entity.label_)

print("Noun phrases:", [chunk.text for chunk in doc3.noun_chunks])
for entity in doc3.ents:
    print(entity.text, entity.label_)

for entity in doc3.ents:
    if(entity.label_ == 'DATE' or entity.label_ == 'TIME'):
        print(entity.text)




