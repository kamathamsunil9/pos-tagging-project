import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_heatmap(results):
    df = pd.DataFrame(results, columns=['Train', 'Test', 'Accuracy'])

    pivot = df.pivot(index="Train", columns="Test", values="Accuracy")

    plt.figure(figsize=(12, 10))
    sns.heatmap(pivot, annot=True, fmt=".2f", cmap="coolwarm")

    plt.title("Cross-Domain POS Tagging Accuracy")

    plt.savefig("../outputs/heatmap.png")
    df.to_csv("../outputs/results.csv", index=False)

    plt.show()