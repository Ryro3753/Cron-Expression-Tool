import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp(u"Every even day at January and February between 10th and 20th at 5 past 10")
doc2 = nlp(u"Yeah yeah, January 16:45")
doc3 = nlp(u"Every day, every 2 day, January eleventh")


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




