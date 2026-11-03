from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

csv_path = Path(__file__).parent.parent / "ExoplanetsPars_2025.csv"
dataframe = pd.read_csv("ExoplanetsPars_2025.csv")

print(*dataframe.columns.tolist())
