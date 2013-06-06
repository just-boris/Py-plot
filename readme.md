# Py-Plot
Модель стыковки волокна с канальным воноводом

[![Build Status](https://api.travis-ci.org/just-boris/Py-plot.png)](https://travis-ci.org/just-boris/Py-plot)

## Описание процесса установки

Установка проверялась на операционные системы windows и linux

* Склонировать данный git-репозиторий или [скачать](https://github.com/just-boris/Py-plot/archive/master.zip)
* Установить интерпретатор Python 2.7, если его еще нет в системе
* Установить [PIP](http://www.pip-installer.org/ru/latest/installing.html) - менеджер пакетов
* Установить [Cython](http://cython.org):  `"pip install cython"`
* Установить [Matplotlib](http://matplotlib.org/): `pip install matplotlib`
* Установить [Numpy](http://www.numpy.org/): `pip install numpy`
* Установить [Scipy](http://www.scipy.org/): `pip install scipy`
*   Установить встроенные библиотеки, запустив команды из папки `include`:

    `python gauss_setup.py build_ext install

    python planar_setup.py build_ext install`

## Работа с программой

Запуск любого модуля осуществляется командой `python "имя модуля"`

## Описание содержащихся модулей
* **app.py** - основной модуль, используется для unit-тестирования
* **main.py** - трехмерное распределение значений интеграла перекрытия
* **heatmap.py** - интерактивная модель стыковки волноводов
* **demo_planar.py** - трехмерное распределение поля канального волновода
* **flat.py** - график значения интеграла перекрытия в осевой плоскости
* **longitudinal.py** - график моделирования продольного смещения
* **optimal_search.py** - консольная утилита, решает задачу нахождения точки оптимального контакта

