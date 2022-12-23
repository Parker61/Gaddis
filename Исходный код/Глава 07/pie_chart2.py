DPI = 600   # разрешающая способность файла png: дисплей=300, публикация=600

from matplotlib import rcParams
rcParams['font.family']     = 'sans-serif'
rcParams['font.sans-serif'] = ['Ubuntu Condensed']
rcParams['figure.figsize']  = (4, 3.8)
rcParams['legend.fontsize'] = 10
rcParams['xtick.labelsize'] = 9
rcParams['ytick.labelsize'] = 9

# Эта программа выводит простую круговую диаграмму.
import matplotlib.pyplot as plt

def main():
    # Создать список объемов продаж.
    sales = [100, 400, 300, 600]

    # Создать список of меток долей.
    slice_labels = ['1-й кв', '2-й кв', '3-й кв', '4-й кв']

    # Создать из этих значений круговую диаграмму.
    plt.pie(sales, labels=slice_labels)

    # Добавить заголовок.
    plt.title('Продажи с разбивкой по кварталам')

    # Показать круговую диаграмму.
    plt.tight_layout()
    plt.savefig('07_10.png', dpi=DPI)  
    plt.show()

# Вызвать главную функцию.
main()