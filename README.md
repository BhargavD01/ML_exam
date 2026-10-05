# Player Selection Support System — Case Study 104

## Project title
**Player Selection Support System Using Machine Learning**

## Problem Definition
Player selection support is formulated as a **binary classification** problem. The model predicts `Selected` or `Not Selected` from measurable player-performance indicators. It is a decision-support prototype, not an automated selector.

## Dataset & source/collection approach
The included dataset is a **reproducible simulated academic dataset of 600 player profiles**. This is explicitly documented because public cricket-statistics datasets generally contain performance variables but not a verified historical selector decision for every player. A public cricket dataset was reviewed as a reference for realistic variable definitions: Ayodhyanandh's `cricket.csv`, which includes Matches, Innings, Runs, Average, Strike Rate, Centuries and Fifties. Source: https://gist.github.com/ayodhyanandh/2ecdb6bd803c4b1bd85cf81ab3cc07d

The target `selected` is an academic proxy generated from a transparent composite performance rubric. It should not be described as real-world historical selection data.

## Data quality
- `player_selection_raw.csv` contains one duplicate record for demonstration.
- A small percentage of numerical fields are missing.
- Duplicate IDs are removed.
- Missing numerical values are median-imputed inside the ML pipeline.
- Identifier columns are excluded from training.

## Features
Age, matches, innings, not-outs, runs, batting average, strike rate, centuries, fifties, ducks, recent form score, fitness score and fielding score.

## Models
- Logistic Regression
- Decision Tree
- Random Forest

## Evaluation
Metrics: Accuracy, Precision, Recall and F1-score. F1 is emphasised because it balances precision and recall.

### Actual experiment results
Best model by test F1: **Logistic Regression**

| Model | Accuracy | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| Logistic Regression | 0.758 | 0.750 | 0.709 | 0.729 |
| Decision Tree | 0.692 | 0.688 | 0.600 | 0.641 |
| Random Forest | 0.708 | 0.679 | 0.691 | 0.685 |

## Run the application

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Files
- `app.py` — Streamlit application
- `data/` — raw and prepared datasets
- `models/` — saved trained model
- `notebooks/player_selection_analysis.ipynb` — full analysis notebook
- `report/Project_Report.docx` — written report

## Limitations
The target is a proxy label, not verified selector history. Real selection can also depend on role requirements, opposition, venue, team balance, injuries, match conditions and expert judgement.

<img width="1470" height="882" alt="Screenshot 2026-10-05 at 12 33 35 PM" src="https://github.com/user-attachments/assets/1906144e-a15a-46e9-9bbd-5507bdbcf7b4" />
<img width="1470" height="833" alt="Screenshot 2026-10-05 at 12 33 45 PM" src="https://github.com/user-attachments/assets/84443f61-4a36-48f9-9e05-333e8042b90f" />
