import nltk

def get_taggers(train_sents):
    default_tagger = nltk.DefaultTagger('NOUN')
    unigram = nltk.UnigramTagger(train_sents, backoff=default_tagger)
    bigram = nltk.BigramTagger(train_sents, backoff=unigram)

    return default_tagger, unigram, bigram