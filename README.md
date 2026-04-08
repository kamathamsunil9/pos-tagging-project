# pos-tagging-project

# 🚀 Cross-Domain POS Tagging Performance Analysis

## 📌 Overview

This project analyzes how Part-of-Speech (POS) tagging performance varies across different text domains using the Brown Corpus.

It demonstrates the **domain shift problem in NLP**, where models trained on one domain perform poorly on another.

---

## 🧠 Features

* Cross-domain POS tagging evaluation
* Multiple models:

  * Default Tagger
  * Unigram Tagger
  * Bigram Tagger
  * Hidden Markov Model (HMM)
* Accuracy comparison across domains
* Heatmap visualization
* Unknown word analysis

---

## 📂 Project Structure

```
pos-tagging-project/
│
├── src/              # Source code
├── outputs/          # Results & visualizations
├── report/           # Project documentation
├── README.md
└── requirements.txt
```

---

## ⚙️ Technologies Used

* Python
* NLTK
* Pandas
* Matplotlib
* Seaborn

---

## ▶️ How to Run

```bash
cd src
python main.py
```

---

## 📊 Output

* `results.csv` → Accuracy results
* `heatmap.png` → Visualization of cross-domain performance

---

## 🔍 Key Observations

* High accuracy when training and testing on the same domain
* Significant performance drop in cross-domain scenarios
* Increase in unknown words leads to lower accuracy

---

## 🧾 Conclusion

POS tagging models are highly domain-dependent.
Improving cross-domain generalization remains an important challenge in NLP.

---

## 🚀 Future Improvements

* Deep learning models (BiLSTM, Transformers)
* Web interface for tagging
* Real-time API integration

---

## 👨‍💻 Author
 **KAMATHAM SUNIL**
