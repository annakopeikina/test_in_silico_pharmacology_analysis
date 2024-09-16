import pandas as pd
import numpy as np
from scipy.stats import f_oneway

# Увеличение выборки до 100 пользователей
np.random.seed(42)  # Для воспроизводимости

# Создание DataFrame с данными для 100 пользователей
data = {
    'User': range(1, 101),
    'Group': np.random.choice(['A', 'B', 'C'], size=100),  # 3 группы пользователей
    'Time_with_Mannequin': np.random.randint(40, 70, size=100),  # Время с манекеном от 40 до 70 минут
    'Time_with_Table': np.random.randint(25, 55, size=100)  # Время с анатомическим столом от 25 до 55 минут
}

df = pd.DataFrame(data)

# ANOVA для времени взаимодействия с манекеном по группам
anova_result_mannequin = f_oneway(df[df['Group'] == 'A']['Time_with_Mannequin'],
                                  df[df['Group'] == 'B']['Time_with_Mannequin'],
                                  df[df['Group'] == 'C']['Time_with_Mannequin'])

# ANOVA для времени взаимодействия с анатомическим столом по группам
anova_result_table = f_oneway(df[df['Group'] == 'A']['Time_with_Table'],
                              df[df['Group'] == 'B']['Time_with_Table'],
                              df[df['Group'] == 'C']['Time_with_Table'])

# Вывод результата для манекена
print(f"ANOVA результат (симулякр-манекен: F-статистика = {anova_result_mannequin.statistic}, p-значение = {anova_result_mannequin.pvalue}")

# Вывод результата для анатомического стола
print(f"ANOVA результат (интерактивный анатомический экран): F-статистика = {anova_result_table.statistic}, p-значение = {anova_result_table.pvalue}")

# Сохранение DataFrame в CSV файл
csv_path = r'C:\Users\annav\OneDrive\Desktop\test_in_silico_pharmacology_analysis\analitical_data\anova_groups.csv'
df.to_csv(csv_path, index=False)
