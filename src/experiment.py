from data_loader import load_categories, load_data
from models import get_taggers

def run_experiment():
    categories = load_categories()
    results = []

    for train_cat in categories:
        for test_cat in categories:
            train_sents = load_data(train_cat)
            test_sents = load_data(test_cat)

            _, _, bigram = get_taggers(train_sents)

            acc = bigram.evaluate(test_sents)

            print(f"Train: {train_cat} → Test: {test_cat} = {acc:.4f}")
            results.append((train_cat, test_cat, acc))

    return results