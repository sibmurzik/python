# "Обзор сторонних библиотек Python"
print("Pandas library")
# Pandas
import pandas as pd

file = 'PAINT.xlsx'
data = pd.read_excel(file, sheet_name=0, index_col=0)
print(data)
print(data.describe())
new_data = data['REMARKS'] + "  --- " + data['Type']
print((new_data))

print("Request library")
#requests
import requests as rq

data = rq.get('https://yandex.ru')
if data.status_code == 200:
    print(data.headers)
    print(data.encoding)
    print(data.text)

print("Matplotlib library")
##matplotlib
from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')
x = [5, 8, 8]
y = [12, 10, 1]
x2 = [1, 5, 10]
y2 = [1, 5, 1]
plt.plot(x, y, 'r', label='graph one', linewidth=3)
plt.plot(x2, y2, 'b', label='grap two', linewidth=5)
plt.title('Matplotlib example')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()
plt.grid(True, color='k')
plt.show()