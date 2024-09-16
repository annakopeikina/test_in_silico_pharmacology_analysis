import pandas as pd
import numpy as np
from scipy import stats

# Данные, которые будут сохранены в CSV файл
data = {
    'User': range(1, 21),
    'Time_with_Mannequin': [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140],
    'Time_with_Table': [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125]
}

# Создание DataFrame
df = pd.DataFrame(data)

# Указываем путь, куда будет сохранен CSV файл
output_path = r"C:\Users\annav\OneDrive\Desktop\test_in_silico_pharmacology_analysis\analitical_data\analitical_data.csv"

# Сохранение DataFrame в CSV файл
df.to_csv(output_path, index=False)

print(f"Файл сохранен : {output_path}")

# Расчет моды и медианы
mode_mannequin = df['Time_with_Mannequin'].mode()[0]
median_mannequin = df['Time_with_Mannequin'].median()
mode_table = df['Time_with_Table'].mode()[0]
median_table = df['Time_with_Table'].median()

print(f"Мода для манекена: {mode_mannequin}, Медиана для манекена: {median_mannequin}")
print(f"Мода для стола: {mode_table}, Медиана для стола: {median_table}")

# t-тест
t_stat, p_value = stats.ttest_ind(df['Time_with_Mannequin'], df['Time_with_Table'])

print(f"t-статистика: {t_stat}, p-значение: {p_value}")
