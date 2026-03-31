# ML DQ – HR Employee Attrition

ML pipeline for **HR Employee Attrition** prediction with **data quality checks** (Great Expectations). The notebook trains classifiers (XGBoost, LightGBM, etc.) and optimizes for **recall** so HR can prioritize “at risk” employees.

## Repository layout

```
HR_Attrition/
├── data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv   # Input dataset
├── HR_Employee_Attrition.ipynb                 # Full pipeline (EDA → DQ → modeling)
├── requirements.txt
├── README.md
├── REVIEW.md                                   # Code & data review
└── .gitignore
```

## Setup and run

1. **Clone** (or use this folder as repo root).
2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the notebook** from the **project root** (`HR_Attrition`), so the path `data/WA_Fn-UseC_-HR-Employee-Attrition.csv` resolves:
   - Open `HR_Employee_Attrition.ipynb` in Jupyter or VS Code.
   - Execute all cells (or run step by step).

## Data

- **File:** `data/WA_Fn-UseC_-HR-Employee-Attrition.csv`
- **Rows × columns:** 1,470 × 35
- **Target:** `Attrition` (Yes/No)
- **Quality:** No missing values or duplicates in the current dataset; Great Expectations validates schema and value ranges before modeling.

## Metrics (for HR)

- **AUC-ROC** ≥ 0.80 – ranking of risk
- **Recall** ≥ 0.70 – % of leavers detected (main priority)
- **Precision** ~0.40+ – of those flagged, how many actually leave
- **F1** ≥ 0.55 – balance of precision and recall

## Code and data review

See **[REVIEW.md](REVIEW.md)** for a short review of the code, data, and repo layout.


