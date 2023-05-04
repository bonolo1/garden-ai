import spacy

# Load the english module
nlp = spacy.load('en_core_web_sm')

# Create list including at least 2 gardenpath sentences from the web and the sentences provided
gardenpathSentences =['While I was surfing the internet went down', 'The girl told the story cried',
                      'The sour drink from the ocean', 'Mary gave the child a Band-Aid.',
                      'That Jill is never here hurts.', 'The cotton clothing is made of grows in Mississippi.']

# Tokenise each sentence in the list and and perform named entity recognition
# Assuming that the term "named entity recognition" is used interchangeably with the term "entity recognition"
# Parse the list of sentence through the english model
# Access the named identies for the list of sentences
for sentence in gardenpathSentences:
    nlp_sentence = nlp(sentence)
    named_entity_nlp_sentence = nlp_sentence.ents
    # Run a for loop to identify the tokens in each sentence
    # Run another for loop to identify the named entities in the named entity sentence that used the .ents method
    # If a token string is also a named entity, print both the token and the named entity with its type
    # Else, where a token string does not have a named entity, print that out to indicate that
    for token in nlp_sentence:
        for named_entity in named_entity_nlp_sentence:
            if token.orth_ == named_entity.orth_:
                print(f'{token}- {named_entity}- {named_entity.label_}')
            else:
                print(f'{token} - Not named entity')

# Use spacy.explain to look up and print the meaning of entities that you don’t understand.
# Entities selected to look up: "GPE" (which I don't understand) and "person" (to check how this works)
print(spacy.explain("GPE"))
print(spacy.explain("PERSON"))

# Comment about the two entities looked up
# 1. GPE
# Explanation: Countries, cities, states
# Does it make sense: Yes, as Mississippi (the named entity) is a state in the US
# 2. PERSON
# Explanation: People, including fictional
# Does it make sense:: Yes, as "Jill" and "Mary" are both names of people
