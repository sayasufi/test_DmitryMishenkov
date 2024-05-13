import json

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def json_to_df(path: str):
    with open(path) as f:
        data = f.read().replace("'", "\"")
        data = json.loads(data)

    return pd.DataFrame(data)


def setting_up_graph(name_x: str, name_y: str, name_graph: str):
    # Устанавливаем подписи оси x и y
    plt.xlabel(name_x, fontsize=14)
    plt.ylabel(name_y, fontsize=14)
    plt.title(name_graph, fontsize=16)  # Устанавливаем заголовок графика
    for spine in plt.gca().spines.values():
        spine.set_color('black')  # Устанавливаем цвет границы в черный
        spine.set_linewidth(1.5)  # Устанавливаем толщину границы равной 1.5
    plt.grid(color='gray', alpha=0.7, linestyle='--')
    plt.gca().set_facecolor('white')  # Устанавливаем цвет фона графика в белый


def graph_2_params(x, y, name_x: str, name_y: str, name_graph: str):
    plt.figure(figsize=(12, 8))
    plt.plot(x, y)
    setting_up_graph(name_x, name_y, name_graph)
    plt.savefig(f'png/{name_graph}.png', dpi=600)
    plt.show()


def graph_some_params(x, y, name_x: str, name_y: str, name_graph: str):
    plt.figure(figsize=(12, 8))
    for i in y:
        plt.plot(x, i, label=i.name)
    setting_up_graph(name_x, name_y, name_graph)
    plt.legend()
    plt.savefig(f'png/{name_graph}.png', dpi=600)
    plt.show()


if __name__ == '__main__':
    df = json_to_df("data/313669_4.json")

    graph_2_params(df["time"],
                   np.degrees(df["pitch"]),
                   "Время, с",
                   "Тангаж, град",
                   "Зависимость угла тангажа от времени")

    graph_2_params(df["time"],
                   np.degrees(df["roll"]),
                   "Время, с",
                   "Крен, град",
                   "Зависимость угла крена от времени")

    graph_2_params(df["time"],
                   np.degrees(df["yaw"]),
                   "Время, с",
                   "Курс, град",
                   "Зависимость угла курса от времени")

    graph_2_params(df["time"],
                   df["throttle"],
                   "Время, с",
                   "",
                   "Зависимость тяги от времени")

    graph_some_params(df["time"],
                      (df["error_x"], df["error_y"]),
                      "Время, с",
                      "Ошибка по координатам, м",
                      "Зависимость ошибок координат от времени")
