from nltk.corpus import brown

def load_categories():
    return brown.categories()

def load_data(category):
    return brown.tagged_sents(categories=category, tagset='universal')
