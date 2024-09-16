import pandas as pd
import numpy as np
import statsmodels.api as sm

# Установка случайного сидера для воспроизводимости
np.random.seed(0)

# Генерация данных
data = {
    'Age': np.random.randint(15, 65, size=100),  # Возраст от 15 до 65 лет
    'Work_Experience': np.random.randint(1, 20, size=100),  # Опыт работы от 1 до 20 лет
    'Education_Level_Professional': np.random.choice([0, 1], size=100)  # Уровень образования (0 - не профессиональное, 1 - профессиональное)
}

# Создание DataFrame
df = pd.DataFrame(data)

# Генерация зависимой переменной с добавлением нормального шума
df['Time_With_Simulacrum'] = np.round(25 + 0.02 * df['Age'] + 0.15 * df['Work_Experience'] + 0.5 * df['Education_Level_Professional'] + np.random.normal(0, 2, size=100))

# Сохранение данных в CSV
csv_path = r'C:\Users\annav\OneDrive\Desktop\test_in_silico_pharmacology_analysis\analitical_data\data_generated_survey_regression_analysis.csv'
df.to_csv(csv_path, index=False)

# Подготовка данных для регрессии
X = df[['Age', 'Work_Experience', 'Education_Level_Professional']]
X = sm.add_constant(X)  # Добавление константы
y = df['Time_With_Simulacrum']

# Построение модели
model = sm.OLS(y, X)
results = model.fit()

# Вывод результатов
print("Регрессионный анализ:")
print(results.summary2().tables[1])  # Вывод только таблицы с коэффициентами и их значениями
