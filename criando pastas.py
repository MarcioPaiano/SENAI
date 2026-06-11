from pathlib import Path

pastas = [
    "data/raw",
    "data/processed/v1_com_outliers",
    "data/processed/v2_outliers_tratado",
    "data/final",
    "notebooks",
    "outputs/graficos"
]

for pasta in pastas:
    Path(pasta).mkdir(parents=True, exist_ok=True)