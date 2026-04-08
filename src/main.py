import nltk
from experiment import run_experiment
from visualization import create_heatmap

# Download dataset (only first time)
nltk.download('brown')
nltk.download('universal_tagset')

def main():
    results = run_experiment()
    create_heatmap(results)

if __name__ == "__main__":
    main()