questions_for_beginner = [
    {
        'text': 'Что выведет console.log(typeof NaN)?',
        'answer_options': ['number', 'string', 'undefined', 'NaN'],
        'right_answer': 'number'
    },

    {
        'text': 'Как объявить переменную с блочной областью видимости?',
        'answer_options': ['var', 'let', 'const', 'function'],
        'right_answer': 'let'
    },

    {
        'text': 'Что вернет Boolean('')?',
        'answer_options': ['true', 'false', 'null', 'undefined'],
        'right_answer': 'false'
    },

    {
        'text': 'Что такое undefined?',
        'answer_options': ['Тип данных', 'Значения', 'Оператор', 'Функция'],
        'right_answer': 'Значения'
    },

    {
        'text': 'Как добавить элемент в конец массива?',
        'answer_options': ['push()', 'pop()', 'shift()', 'unshift()'],
        'right_answer': 'push()'
    },

    {
        'text': 'Что вернет parseInt("12px")?',
        'answer_options': ['12', 'NaN', '12px', 'Ошибка'],
        'right_answer': '12'
    },

    {
        'text': 'Как проверить массив?',
        'answer_options': ['typeof arr', 'arr.isArray()', 'Array.isArray(arr)', 'arr.typeOf()'],
        'right_answer': 'Array.isArray(arr)'
    },

    {
        'text': 'Что делает оператор ===?',
        'answer_options': ['Приведение типов', 'Проверка без приведения', 'Присваивание', 'Сравнение объектов'],
        'right_answer': 'Проверка без приведения'
    },

    {
        'text': 'Что выведет console.log(1 + "1")?',
        'answer_options': ['2', '11', 'NaN', 'Ошибка'],
        'right_answer': '11'
    },

    {
        'text': 'Как создать объект?',
        'answer_options': ['{}', 'Object.create()', 'new Object', 'Все варианты'],
        'right_answer': 'Все варианты'
    },
    {
        'text': 'Что делает Array.prototype.slice()?',
        'answer_options': ['Мутирует массив', 'Возвращает копию части массива', 'Удаляет  элементы', 'Сортирует массив'],
        'right_answer': 'Возвращает копию части массива'
    },
    {
        'text': 'Как остановить цикл for?',
        'answer_options': ['break', 'return', 'exit', 'continue'],
        'right_answer': 'break'
    },
    {
        'text': 'Что такое null?',
        'answer_options': ['Объект', 'Примитив', 'Функция', 'Операнд'],
        'right_answer': 'Примитив'
    },
    {
        'text': 'Как работает switch?',
        'answer_options': ['Строгое сравнение', 'Приведение типов', 'Только числа', 'Через оператор in'],
        'right_answer': 'Строгое сравнение'
    },
    {
        'text': 'Что делает Math.floor(3.9)?',
        'answer_options': ['4', '3', '3.0', 'NaN'],
        'right_answer': '3'
    },
    {
        'text': 'Как вызвать функцию?',
        'answer_options': ['call()', 'apply()', '()', 'Все варианты'],
        'right_answer': 'Все варианты'
    },
    {
        'text': 'Что такое IIFE?',
        'answer_options': ['Функция-конструктор', 'Самовызывающаяся функция', 'Асинхронная функция', 'Стрелочная функция'],
        'right_answer': 'Самовызывающаяся функция'
    },
    {
        'text': 'Что выведет console.log(typeof [])?',
        'answer_options': ['array', 'object', 'undefined', 'null'],
        'right_answer': 'object'
    }
]

questions_for_advanced = [
    {
        'text': 'Как работает String.prototype.slice(1, 4) для "abcdef"?',
        'answer_options': ['abc', 'bcd', 'abcd', 'bcde'],
        'right_answer': 'bcd'
    },
    {
        'text': 'Что выведет console.log(1 < 2 < 3 > 0)?',
        'answer_options': ['true', 'false', 'Ошибка', 'NaN'],
        'right_answer': 'bcd'
    },
    {
        'text': 'Что такое замыкание??',
        'answer_options': ['Функция внутри объекта', 'Доступ к внешней области', 'Способ наследования', 'Метод массива'],
        'right_answer': 'bcd'
    },
    {
        'text': 'Какой метод преобразует JSON в объект??',
        'answer_options': ['JSON.parse()', 'JSON.stringify()', 'JSON.encode()', 'JSON.decode()'],
        'right_answer': 'bcd'
    },
    {
        'text': 'Что вернет "5" - 3??',
        'answer_options': ['2', '53', 'NaN', 'Ошибка'],
        'right_answer': 'bcd'
    },
    {
        'text': 'Как работает Array.prototype.map()??',
        'answer_options': ['Фильтрует элементы', 'Создает новый массив', 'Изменяет исходный массив', 'Объединяет массивы'],
        'right_answer': 'bcd'
    },
    {
        'text': 'Что такое всплытие (hoisting)??',
        'answer_options': ['Поднятие переменных и функций', 'Оптимизация кода', 'Удаление переменных', 'Сборка мусора'],
        'right_answer': 'bcd'
    },
    {
        'text': 'Что выведет setTimeout(() => console.log(1), 0); console.log(2);?',
        'answer_options': ['1 2', '2 1', '1', '2'],
        'right_answer': 'bcd'
    },
    {
        'text': 'Как работает this в стрелочных функциях?',
        'answer_options': ['Как в обычных функциях', 'Берется из внешнего контекста', 'Всегда undefined', 'Зависит от аргументов'],
        'right_answer': 'bcd'
    },
    {
        'text': 'Что такое каррирование?',
        'answer_options': ['Преобразование функции с несколькими аргументами', 'Способ кэширования', 'Метод массива', 'Синтаксис ES6'],
        'right_answer': 'bcd'
    },
    {
        'text': 'Что вернет 0.1 + 0.2 === 0.3?',
        'answer_options': ['true', 'false', 'Ошибка', 'NaN'],
        'right_answer': 'bcd'
    },
    {
        'text': 'Как получить ключи объекта?',
        'answer_options': ['Object.keys()', 'obj.keys', 'Object.getKeys()', 'keys(obj)'],
        'right_answer': 'bcd'
    },
    {
        'text': 'Что делает use strict?',
        'answer_options': ['Включает строгий режим', 'Оптимизирует код', 'Отключает функции', 'Устаревшая директива'],
        'right_answer': 'bcd'
    },
    {
        'text': 'Как скопировать объект?',
        'answer_options': ['Object.assign()', 'Оператор=', 'JSON.parse(JSON.stringify(obj)', 'Варианты 1 и 3'],
        'right_answer': 'bcd'
    },
    {
        'text': 'Что такое делегирование событий?',
        'answer_options': ['Обработка на родителе', 'Создание новых событий', 'Удаление слушателей', 'Асинхронные события'],
        'right_answer': 'bcd'
    },
    {
        'text': 'Как работает Function.prototype.bind()?',
        'answer_options': ['Создает новую функцию с привязанным контекстом', 'Вызывает функцию', 'Копирует аргументы', 'Меняет прототип'],
        'right_answer': 'bcd'
    },
    {
        'text': 'Что такое CORS??',
        'answer_options': ['Механизм безопасности браузеров', 'Язык программирования', 'Метод кэширования', 'Синтаксис CSS'],
        'right_answer': 'bcd'
    },
    {
        'text': 'Что делает оператор ???',
        'answer_options': ['Проверяет null/undefined', 'Логическое И', 'Тернарный оператор', 'Оператор OR'],
        'right_answer': 'bcd'
    },
    {
        'text': 'Как преобразовать массив в строку?',
        'answer_options': ['toString()', 'join()', 'String()', 'Все варианты'],
        'right_answer': 'bcd'
    },
    {
        'text': 'Что такое прототип объекта?',
        'answer_options': ['Ссылка на другой объект', 'Тип данных', 'Метод класса', 'Свойства функции'],
        'right_answer': 'bcd'
    },
    {
        'text': 'Что делает Array.prototype.reduce()?',
        'answer_options': ['Фильтрует элементы', 'Сворачивает массив в одно значение', 'Создает новый массив', 'Изменяет порядок элементов'],
        'right_answer': 'bcd'
    }
]

questions_for_expert = [
    {
        'text': 'Что вернет "Hello".indexOf("l")?',
        'answer_options': ['2', '3', '1', '-1'],
        'right_answer': '2'
    }
]
