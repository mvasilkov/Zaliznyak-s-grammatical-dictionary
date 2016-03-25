# Zaliznyak-s-grammatical-dictionary

This is a module for predicting grammatical markers for unknown Russian words, according to notation from A.A. Zaliznyak's "Grammar Dictionary of the Russian Language". 
It takes a text string as an input, and returns a list of unknown words with markers predicted for them.

Try it here: http://web-corpora.net/wsgi3/GDictionary/

**Usage**: 

|``from gdictionary import rusgrab``
|``rusgrab.main("your input text")``

**Output**

* predicted.csv - results

* frequency.csv - "new words", sorted accordingly

**Prerequisites** 

* modules *pymorphy2* and *liac-arff* will need to be installed
* *mystem 3.0* and the *Weka* jar file are required in the working directory for the module to work

----------------

Это модуль для предсказания грамматических характеристик незнакомых слов, в соответствии с "Грамматическим словарем русского языка" А.А. Зализняка. Он принимает на вход текстовую строку, находит в ней слова, отсутствующие в словаре Зализняка и пытается предсказать для них лемму и ее тип склонения или спряжения в соответствии с нотацией Грамматичекого словаря.

**Подробности**

В папке с исходным кодом обязательно должны лежать исполняемый файл *mystem* версии 3.0 и jar-архив программы *Weka* версии 3.7 и выше.
Также требуется установка библиотек *pymorphy2* и *liac-arff*.
Чтобы импортировать модуль: ``from gdictionary import rusgrab``.
Чтобы запустить модуль: ``rusgrab.main("your input text")``

**Вывод:**

* predicted.csv - результат
* frequency.csv - "новые слова" (сортировка по частоте)

**Вложенные модули:**

* fileworks - кодировки
* kill_small - фильтрует итоговую выдачу
* freq - считает частотность
* write_freq - записывает частоты в файл
* morph - приводит словоформу к лемме
* postprocessing - правила постобработки лемматизации
* recalculation - пересчитывает частотность лемм после постобработки
* targetdata - генерирует признаки для предсказания
* ARFFconversion - генерирует arff для новых слов
* postARFF - объединяет набор признаков 
* predictor - делает предсказание с помощью Weka
* getfinal - собирает итоговый результат в файл

