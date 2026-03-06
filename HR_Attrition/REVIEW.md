# Code and data review – ML DQ (HR Employee Attrition)

**Location:** Project root `HR_Attrition` with `data/` subfolder.  
**Artifacts:** `data/WA_Fn-UseC_-HR-Employee-Attrition.csv`, `HR_Employee_Attrition.ipynb`, `requirements.txt`.

---

## Data review

| Item | Status |
|------|--------|
| **Source** | IBM-style HR Employee Attrition dataset (`WA_Fn-UseC_-HR-Employee-Attrition.csv`) |
| **Rows × Cols** | 1,470 × 35 |
| **Missing values** | 0 (noted in notebook) |
| **Duplicates** | 0 |
| **Target** | `Attrition` (Yes/No) – imbalanced; recall is the main metric for “catching leavers” |
| **Key columns** | Age, Department, JobRole, MonthlyIncome, OverTime, YearsAtCompany, JobSatisfaction, WorkLifeBalance, etc. |

**Verdict:** Data is clean and consistent with the notebook’s expectations. Path used in code: `data/WA_Fn-UseC_-HR-Employee-Attrition.csv` (relative to project root) – correct for repo layout.

---

## Code review

- **Notebook:** `HR_Employee_Attrition.ipynb` – “pipeline v3 (fixed)”.
- **Flow:** Imports → load CSV → EDA → **Great Expectations** validation gate → preprocessing (e.g. encoding, scaling) → modeling → metrics.
- **Stack:** pandas, numpy, matplotlib, seaborn, scikit-learn, imbalanced-learn (SMOTE), XGBoost, LightGBM (optional fallback), Great Expectations.
- **Data path:** `DATA_PATH = 'data/WA_Fn-UseC_-HR-Employee-Attrition.csv'` – assumes notebook is run from project root; matches current layout.
- **Data quality:** GE suite validates table shape (35 cols, 1k–5k rows), no nulls on key columns, value sets (e.g. Attrition, OverTime), and ranges (Age, MonthlyIncome, JobSatisfaction, WorkLifeBalance). Pipeline stops if validation fails.
- **Metrics:** AUC-ROC (≥0.80), Recall (≥0.70), Precision (0.40+), F1 (≥0.55), with focus on recall for HR.
- **Dependencies:** Reflected in `requirements.txt` (pandas, numpy, matplotlib, seaborn, scikit-learn, imbalanced-learn, xgboost, lightgbm, great-expectations).

**Suggestions (optional for later):**

1. Run notebook from repo root so `data/` resolves; document this in README.
2. Consider clearing heavy notebook outputs before commit (or use a pre-commit hook) to keep repo size small.
3. Pin major/minor versions in `requirements.txt` if you need reproducible builds (e.g. `pandas>=1.5,<3`).

---

## Repo layout (GitHub-ready)

```
ML DQ/
├── data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
├── HR_Employee_Attrition.ipynb
├── requirements.txt
├── .gitignore
├── README.md
└── REVIEW.md   (this file)
```

All of the above can be pushed to GitHub together; no extra files are required for a minimal public repo.

