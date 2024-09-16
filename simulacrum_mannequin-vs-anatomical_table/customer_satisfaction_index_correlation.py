import pandas as pd
import numpy as np
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

# Создание DataFrame
data = {
    'User': range(1, 22),
    'Time_with_Mannequin': [45, 50, 55, 60, 65,45, 50, 55, 35, 76, 48, 36, 4, 20, 123, 14, 36, 36, 20, 22, 22],
    'Satisfaction_Level': [7, 8, 9, 6, 7, 9, 8, 9, 6, 7, 9, 6, 7, 9, 6, 8, 8, 8, 9, 6, 8,]
}

df = pd.DataFrame(data)

# Расчет корреляции
correlation, p_value = pearsonr(df['Time_with_Mannequin'], df['Satisfaction_Level'])

print(f"Корреляция: {correlation}, p-значение: {p_value}")

# Сохранение данных в CSV
csv_path = r'C:\Users\annav\OneDrive\Desktop\test_in_silico_pharmacology_analysis\analitical_data\satisfaction_index.csv'
df.to_csv(csv_path, index=False)
print(f"Файл сохранен в : {csv_path}")
