import pandas as pd
import numpy as np

# Параметры данных
subscription_costs = [11111, 111111]
development_hours = 200
hourly_rates = [7, 20]
time_per_request_drugbank = 10  # В минутах
time_per_request_free = 30     # В минутах

# Создание DataFrame для оценки стоимости и эффективности
data = {
    'Source': ['DrugBank API (Low Cost)', 'DrugBank API (High Cost)', 'Free Sources'],
    'Subscription_Cost': subscription_costs + [0],
    'Development_Hours': [0, 0, development_hours],
    'Hourly_Rate': [hourly_rates[0], hourly_rates[1], hourly_rates[1]],
    'Time_Per_Request': [time_per_request_drugbank, time_per_request_drugbank, time_per_request_free]
}

df = pd.DataFrame(data)

# Расчет общей стоимости
df['Development_Cost'] = df['Development_Hours'] * df['Hourly_Rate']
df['Total_Cost'] = df['Subscription_Cost'] + df['Development_Cost']

# Расчет эффективности
df['Requests_Per_Hour'] = 60 / df['Time_Per_Request']

# Сохранение данных в CSV
csv_path_costs = r'C:\Users\annav\OneDrive\Desktop\test_in_silico_pharmacology_analysis\analitical_data\freesource-vs-drugbankAPI_data_generated.csv'
df.to_csv(csv_path_costs, index=False)

print("Общая стоимость и эффективность:")
print(df[['Source', 'Total_Cost', 'Requests_Per_Hour']])

# Расчет ROI и точки безубыточности
# Параметры для ROI и точки безубыточности
revenue_per_request = 50  # Доход с одного запроса

# Расчет ROI
df['ROI'] = (revenue_per_request * df['Requests_Per_Hour'] * 8760 - df['Total_Cost']) / df['Total_Cost'] * 100  # ROI в процентах

# Расчет точки безубыточности
df['Break_Even_Requests'] = df['Total_Cost'] / (revenue_per_request - df['Total_Cost'] / (60 / df['Time_Per_Request']))

# Сохранение данных в CSV
csv_path_roi_break_even = r'C:\Users\annav\OneDrive\Desktop\test_in_silico_pharmacology_analysis\analitical_data\roi_and_break_even_analysis.csv'
df.to_csv(csv_path_roi_break_even, index=False)

print("Рентабельность и точка безубыточности:")
print(df[['Source', 'ROI', 'Break_Even_Requests']])
