# Zaliznyak-s-grammatical-dictionary

This module predicts grammatical markers for unknown Russian words in Zaliznyak's Grammar Dictionary tags.
It takes a text string as an input, and returns a list of unknown words with markers predicted for them.

Try it here: http://web-corpora.net/wsgi3/GDictionary/

Project description in Russian: https://www.hse.ru/ma/ling/st-projects

##Tips

* What we do: analyze unknown verbs and nouns.
* What we do not: analyze other parts of speech.
* Noun tags denote stem type and declension class. 
* Verb tags denote only stem type.
* Quality metrics were measured manually using top-1000 frequent "new" nouns/verbs:
	<br><b>Nouns:<b>
	<br>Stem type and declension class: 99%
	<br>Gender: 90%
	<br>Both correct: 89%
	<br><b>Verbs:<b>
	<br>Verb conjugation class 89%
* Quality metrics are extremely sensitive to dataset. 

##Installation

Way 1. If you do not want to change the code in any way, you can download the .whl file and run ``pip install gdictionary-0.756a0-py3-none-any.whl`` from your command line.

Way 2. If you want to see the code and maybe even change it, you can clone this repository and use the modules "as is", or you can run ``python setup.py install`` in the folder and be able to import it whenever you use Python.

##Usage: 

`from gdictionary import rusgrab`

`rusgrab.main("your input text")`

##Output

* predicted.csv - results

* frequency.csv - "new words", sorted accordingly

##Prerequisites 

* modules *pymorphy2* and *liac-arff* need to be installed.

* *mystem 3.0* and the *Weka* jar file are required in your working folder if you choose way 1 installation, and in the project folder if you choose way 2.

----------------

Это модуль для предсказания грамматических характеристик незнакомых слов, в соответствии с "Грамматическим словарем русского языка" А.А. Зализняка. Он принимает на вход текстовую строку, находит в ней слова, отсутствующие в словаре Зализняка и пытается предсказать для них лемму и ее тип склонения или спряжения в соответствии с нотацией Грамматичекого словаря.

##Установка

Способ 1. Если вы не заинтересованы в просмотре и изменении кода, можно просто скачать .whl файл и установить его с помощью команды `pip install gdictionary-0.756a0-py3-none-any.whl` в консоли.

Способ 2. Если вас интересует код проекта, можно клонировать репозиторий себе на компьютер и либо пользоваться им из его папки, либо установить с помощью команды `python setup.py install`. 

##Подробности

Для работы модуля необходимы исполняемый файл *mystem* версии 3.0 и jar-архив программы *Weka* версии 3.7 и выше: в вашей рабочей папке, если модуль установлен способом 1, и в папке репозитория, если способом 2.
Также требуется установка библиотек *pymorphy2* и *liac-arff*.

Чтобы импортировать модуль: `from gdictionary import rusgrab`.

Чтобы запустить модуль: `rusgrab.main("your input text")`.

##Вывод:

* predicted.csv - результат

* frequency.csv - "новые слова" (сортировка по частоте)

##Вложенные модули:

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

