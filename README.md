# beCoder

#### Буду использовать петон, потому что зачем усложнять.

#### Как работает функция:

* Разбиваем **Input** на строки по "\n"

* Затем каждую строку разбиваем на отдельные числа

* Для того, чтобы узнать число "друзей друзей" буду использовать множества **_set()_**, потому что они могут содеражть элементы только в единственном экземпляре и они имеют удобную операцию типа "вычитания множеств", которая как раз и поволяет найти тех людей, которые являются друзьями друзей, но не знают нашего социофоба

* Создаем множество из первых чисел в каждой строке — список друзей Егора

* Создаем множество друзей друзей из **M** чисел, которые идут после числа **F**, дубликаты автоматически удалятся

* Теперь осталось просто из найденного списка друзей друзей убрать непосредсвенных друзей Егора, для этого просто используем   
**_difference()_** (или краткий синтаксис "-") и теперь находим число друзей друзей, которых позовём, чтобы побороть свою социофобию, с помощью функции **_len()_**
