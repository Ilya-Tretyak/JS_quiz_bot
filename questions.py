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
        'text': 'Что такое замыкание?',
        'answer_options': ['Функция внутри объекта', 'Доступ к внешней области', 'Способ наследования', 'Метод массива'],
        'right_answer': 'Доступ к внешней области'
    },
    {
        'text': 'Какой метод преобразует JSON в объект?',
        'answer_options': ['JSON.parse()', 'JSON.stringify()', 'JSON.encode()', 'JSON.decode()'],
        'right_answer': 'JSON.parse()'
    },
    {
        'text': 'Что вернет "5" - 3?',
        'answer_options': ['2', '53', 'NaN', 'Ошибка'],
        'right_answer': '2'
    },
    {
        'text': 'Как работает Array.prototype.map()?',
        'answer_options': ['Фильтрует элементы', 'Создает новый массив', 'Изменяет исходный массив', 'Объединяет массивы'],
        'right_answer': 'Создает новый массив'
    },
    {
        'text': 'Что такое всплытие (hoisting)?',
        'answer_options': ['Поднятие переменных и функций', 'Оптимизация кода', 'Удаление переменных', 'Сборка мусора'],
        'right_answer': 'Поднятие переменных и функций'
    },
    {
        'text': 'Что выведет setTimeout(() => console.log(1), 0); console.log(2);?',
        'answer_options': ['1 2', '2 1', '1', '2'],
        'right_answer': '2 1'
    },
    {
        'text': 'Как работает this в стрелочных функциях?',
        'answer_options': ['Как в обычных функциях', 'Берется из внешнего контекста', 'Всегда undefined', 'Зависит от аргументов'],
        'right_answer': 'Берется из внешнего контекста'
    },
    {
        'text': 'Что такое каррирование?',
        'answer_options': ['Преобразование функции с несколькими аргументами', 'Способ кэширования', 'Метод массива', 'Синтаксис ES6'],
        'right_answer': 'Преобразование функции с несколькими аргументами'
    },
    {
        'text': 'Что вернет 0.1 + 0.2 === 0.3?',
        'answer_options': ['true', 'false', 'Ошибка', 'NaN'],
        'right_answer': 'false'
    },
    {
        'text': 'Как получить ключи объекта?',
        'answer_options': ['Object.keys()', 'obj.keys', 'Object.getKeys()', 'keys(obj)'],
        'right_answer': 'Object.keys()'
    },
    {
        'text': 'Что делает use strict?',
        'answer_options': ['Включает строгий режим', 'Оптимизирует код', 'Отключает функции', 'Устаревшая директива'],
        'right_answer': 'Включает строгий режим'
    },
    {
        'text': 'Как скопировать объект?',
        'answer_options': ['Object.assign()', 'Оператор=', 'JSON.parse(JSON.stringify(obj))', 'Варианты 1 и 3'],
        'right_answer': 'Варианты 1 и 3'
    },
    {
        'text': 'Что такое делегирование событий?',
        'answer_options': ['Обработка на родителе', 'Создание новых событий', 'Удаление слушателей', 'Асинхронные события'],
        'right_answer': 'Обработка на родителе'
    },
    {
        'text': 'Как работает Function.prototype.bind()?',
        'answer_options': ['Создает новую функцию с привязанным контекстом', 'Вызывает функцию', 'Копирует аргументы', 'Меняет прототип'],
        'right_answer': 'Создает новую функцию с привязанным контекстом'
    },
    {
        'text': 'Что такое CORS?',
        'answer_options': ['Механизм безопасности браузеров', 'Язык программирования', 'Метод кэширования', 'Синтаксис CSS'],
        'right_answer': 'Механизм безопасности браузеров'
    },
    {
        'text': 'Что делает оператор ?? ?',
        'answer_options': ['Проверяет null/undefined', 'Логическое И', 'Тернарный оператор', 'Оператор OR'],
        'right_answer': 'Проверяет null/undefined'
    },
    {
        'text': 'Как преобразовать массив в строку?',
        'answer_options': ['toString()', 'join()', 'String()', 'Все варианты'],
        'right_answer': 'Все варианты'
    },
    {
        'text': 'Что такое прототип объекта?',
        'answer_options': ['Ссылка на другой объект', 'Тип данных', 'Метод класса', 'Свойства функции'],
        'right_answer': 'Ссылка на другой объект'
    },
    {
        'text': 'Что делает Array.prototype.reduce()?',
        'answer_options': ['Фильтрует элементы', 'Сворачивает массив в одно значение', 'Создает новый массив', 'Изменяет порядок элементов'],
        'right_answer': 'Сворачивает массив в одно значение'
    }
]

questions_for_expert = [
    {
        'text': 'Что выведет console.log(new Date(0))?',
        'answer_options': ['1970-01-01T00:00:00.000Z', 'Текущая дата', 'Ошибка', 'undefined'],
        'right_answer': '1970-01-01T00:00:00.000Z'
    },
    {
        'text': 'Как работает Object.freeze()?',
        'answer_options': ['Запрещает добавление свойств', 'Делает объект неизменяемым', 'Шифрует объект', 'Удаляет свойства'],
        'right_answer': 'Запрещает добавление свойств'
    },
    {
        'text': 'Что такое Event Loop?',
        'answer_options': ['Цикл обработки событий', 'Тип данных', 'Метод анимации', 'Синтаксис ES6'],
        'right_answer': 'Цикл обработки событий'
    },
    {
        'text': 'Как работает Promise.all()?',
        'answer_options': ['Ждет все промисы', 'Останавливается на первой ошибке', 'Возвращает первый успешный промис', 'Не поддерживается в ES6'],
        'right_answer': 'Ждет все промисы'
    },
    {
        'text': 'Что такое Symbol?',
        'answer_options': ['Примитивный тип', 'Функция-конструктор', 'Метод строки', 'Синтаксис деструктуризации'],
        'right_answer': 'Примитивный тип'
    },
    {
        'text': 'Что такое микротаски (microtasks)?',
        'answer_options': ['Задачи с высшим приоритетом', 'Асинхронные операции', 'Web API', 'Часть Event Loop'],
        'right_answer': 'Часть Event Loop'
    },
    {
        'text': 'Как работает Object.defineProperty()?',
        'answer_options': ['Добавляет свойство с дескриптором', 'Удаляет свойство', 'Копирует объект', 'Изменяет прототип'],
        'right_answer': 'Добавляет свойство с дескриптором'
    },
    {
        'text': 'Что такое декораторы?',
        'answer_options': ['Функции для модификации классов/методов', 'Синтаксис HTML', 'Стили CSS', 'Метод анимации'],
        'right_answer': 'Функции для модификации классов/методов'
    },
    {
        'text': 'Как работает Proxy?',
        'answer_options': ['Перехватывает операции с объектом', 'Создает копию', 'Шифрует данные', 'Удаляет методы'],
        'right_answer': 'Перехватывает операции с объектом'
    },
    {
        'text': 'Что такое TCO (Tail Call Optimization)?',
        'answer_options': ['Оптимизация хвостовых вызовов', 'Сжатие кода', 'Удаление рекурсии', 'Синтаксис циклов'],
        'right_answer': 'Оптимизация хвостовых вызовов'
    },
    {
        'text': 'Как работает async/await?',
        'answer_options': ['Синтаксический сахар для промисов', 'Новый тип данных', 'Метод обработки ошибок', 'Web API'],
        'right_answer': 'Синтаксический сахар для промисов'
    },
    {
        'text': 'Что такое Web Workers?',
        'answer_options': ['Потоки браузера', 'Серверные скрипты', 'Модули Node.js', 'Синтаксис ES6'],
        'right_answer': 'Потоки браузера'
    },
    {
        'text': 'Как устроено наследование в ES6 классах?',
        'answer_options': ['Через ключевое слово extends', 'Через прототипы', 'Через Object.create()', 'Варианты 1 и 2'],
        'right_answer': 'Через ключевое слово extends'
    },
    {
        'text': 'Что такое WeakMap?',
        'answer_options': ['Коллекция с weak-ссылками', 'Аналог Map', 'Список функций', 'Синтаксис деструктуризации'],
        'right_answer': 'Коллекция с weak-ссылками'
    },
    {
        'text': 'Как работает garbage collection?',
        'answer_options': ['Удаляет недостижимые объекты', 'Собирает мусор вручную', 'Шифрует данные', 'Оптимизирует циклы'],
        'right_answer': 'Удаляет недостижимые объекты'
    },
    {
        'text': 'Что такое CSP (Content Security Policy)?',
        'answer_options': ['Защита от XSS', 'Метод кэширования', 'Синтаксис CSS', 'Протокол HTTP'],
        'right_answer': 'Защита от XSS'
    },
    {
        'text': 'Как использовать генераторы?',
        'answer_options': ['Функции с yield', 'Методы массива', 'Циклы for', 'Стрелочные функции'],
        'right_answer': 'Функции с yield'
    },
    {
        'text': 'Что такое WebAssembly?',
        'answer_options': ['Бинарный формат для веба', 'Язык разметки', 'Библиотека JS', 'Синтаксис CSS'],
        'right_answer': 'Бинарный формат для веба'
    },
    {
        'text': 'Как отслеживать утечки памяти?',
        'answer_options': ['Инструменты разработчика', 'console.log()', 'try/catch', 'use strict'],
        'right_answer': 'Инструменты разработчика'
    },
    {
        'text': 'Что такое дескрипторы свойств?',
        'answer_options': ['writable, enumerable, configurable', 'Типы данных', 'Методы объекта', 'Параметры функций'],
        'right_answer': 'writable, enumerable, configurable'
    }
]
