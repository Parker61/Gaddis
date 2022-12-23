DPI = 600   # разрешающая способность файла png: дисплей=300, публикация=600

from matplotlib import rcParams
rcParams['font.family']     = 'sans-serif'
rcParams['font.sans-serif'] = ['Ubuntu Condensed']
rcParams['figure.figsize']  = (4, 3.8)
rcParams['legend.fontsize'] = 10
rcParams['xtick.labelsize'] = 9
rcParams['ytick.labelsize'] = 9

# Эта программа выводит простую столбчатую диаграмму.
import matplotlib.pyplot as plt

def main():
    # Создать список с координатами X левого края каждого столбика
    left_edges = [0, 10, 20, 30, 40]

    # Создать список с высотами каждого столбика.
    heights = [100, 200, 300, 400, 500]

    # Построить столбчатую диаграмму.
    plt.bar(left_edges, heights)

    # Построить столбчатую диаграмму.
    plt.tight_layout()
    plt.savefig('07_06.png', dpi=DPI)   
    plt.show()

# Показать столбчатую диаграмму.
main()