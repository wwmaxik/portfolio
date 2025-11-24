## Пошаговая разработка

### Шаг 1: Базовая структура и подключение библиотек

**Задача:** Создать "скелет" нашего HTML-документа и подключить все необходимые внешние ресурсы.

Любой веб-сайт начинается с базовой HTML-структуры. В секции `<head>` мы размещаем мета-информацию и подключаем стили и скрипты.

**Код:**
```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Портфолио - Шаблон</title>

    <!-- Подключение Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Подключение jQuery -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <!-- Подключение иконок Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <!-- Блок для пользовательских CSS-стилей -->
    <style>
        /* Плавная прокрутка по якорям */
        html {
            scroll-behavior: smooth;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <!-- Содержимое сайта будет здесь -->
</body>
</html>
```

**Подробное объяснение:**

-   `<!DOCTYPE html>`: Указывает браузеру, что это современный HTML5-документ.
-   `<html lang="ru">`: Корневой элемент, `lang="ru"` помогает поисковым системам и браузерам понять, что страница на русском языке.
-   `<meta charset="UTF-8">`: Задает кодировку UTF-8, чтобы все символы, включая кириллицу, отображались корректно.
-   `<meta name="viewport" ...>`: Критически важный тег для адаптивности. Он говорит браузеру на мобильных устройствах использовать реальную ширину экрана, а не пытаться отмасштабировать десктопную версию.
-   `<title>`: Текст в этой вкладке будет виден в заголовке браузера.
-   `<script src="...">` и `<link rel="stylesheet" ...>`: Так мы подключаем внешние библиотеки. Скрипты (JS) и стили (CSS) загружаются с удаленных серверов (CDN).
-   `<style>`: В этот тег мы будем добавлять небольшие CSS-правила, которые сложно или неудобно реализовывать через классы Tailwind.
-   `<body class="bg-gray-50 text-gray-800">`: Тег `<body>` — это все видимое содержимое страницы. Мы сразу задаем ему с помощью классов Tailwind светло-серый фон (`bg-gray-50`) и основной цвет текста (`text-gray-800`).

---

### Шаг 2: Создание "шапки" сайта (Header)

**Задача:** Добавить навигационную панель, которая будет зафиксирована вверху экрана.

Шапка сайта — один из важнейших элементов. Она должна быть удобной и функциональной как на больших, так и на маленьких экранах.

**Код (добавляется внутрь `<body>`):**
```html
<header class="fixed w-full bg-white shadow-md z-50">
    <div class="container mx-auto px-4">
        <nav class="flex justify-between items-center py-4">
            <a href="#" class="text-2xl font-bold text-indigo-600">Портфолио</a>
            
            <div class="md:hidden">
                <button id="menu-toggle" class="text-gray-600 hover:text-indigo-600">
                    <i class="fas fa-bars text-xl"></i>
                </button>
            </div>
            
            <ul class="hidden md:flex space-x-8">
                <li><a href="#home" class="text-gray-600 hover:text-indigo-600 font-medium transition">Главная</a></li>
                <li><a href="#about" class="text-gray-600 hover:text-indigo-600 font-medium transition">Обо мне</a></li>
                <li><a href="#skills" class="text-gray-600 hover:text-indigo-600 font-medium transition">Навыки</a></li>
                <li><a href="#portfolio" class="text-gray-600 hover:text-indigo-600 font-medium transition">Портфолио</a></li>
                <li><a href="#contact" class="text-gray-600 hover:text-indigo-600 font-medium transition">Контакты</a></li>
            </ul>
        </nav>
        
        <div id="mobile-menu" class="hidden md:hidden py-4 border-t">
            <ul class="space-y-4">
                <li><a href="#home" class="block text-gray-600 hover:text-indigo-600 font-medium">Главная</a></li>
                <li><a href="#about" class="block text-gray-600 hover:text-indigo-600 font-medium">Обо мне</a></li>
                <li><a href="#skills" class="block text-gray-600 hover:text-indigo-600 font-medium">Навыки</a></li>
                <li><a href="#portfolio" class="block text-gray-600 hover:text-indigo-600 font-medium">Портфолио</a></li>
                <li><a href="#contact" class="block text-gray-600 hover:text-indigo-600 font-medium">Контакты</a></li>
            </ul>
        </div>
    </div>
</header>
```

**Подробное объяснение классов Tailwind:**

-   `fixed w-full`: Делает шапку "липкой", она всегда остается вверху экрана (`fixed`) и занимает всю его ширину (`w-full`).
-   `bg-white shadow-md z-50`: Задает белый фон, легкую тень под шапкой для объема и `z-index: 50`, чтобы шапка была гарантированно выше других элементов.
-   `container mx-auto px-4`: Стандартная обертка. `container` задает максимальную ширину, `mx-auto` центрирует ее, а `px-4` добавляет внутренние отступы по горизонтали.
-   `flex justify-between items-center`: Это магия Flexbox. `flex` — включает режим, `justify-between` — разносит дочерние элементы (лого и навигацию) по разным краям, `items-center` — выравнивает их по центру по вертикали.
-   `md:hidden` и `hidden md:flex`: Ключевые классы для адаптивности. Префикс `md:` означает "применить этот стиль на экранах среднего размера (medium) и больше".
    -   `md:hidden`: Элемент (кнопка-бургер) будет скрыт на экранах `md` и больше.
    -   `hidden md:flex`: Элемент (основная навигация) будет скрыт по умолчанию, но станет видимым (`display: flex`) на экранах `md` и больше.
-   `hover:text-indigo-600 transition`: При наведении (`hover:`) цвет текста меняется на индиго, а `transition` делает это изменение плавным.

---

### Шаг 3: Секция "Главная" (Hero)

**Задача:** Создать первый экран, который производит впечатление и содержит основной призыв к действию.

Это "лицо" нашего сайта. Мы используем большой заголовок, подзаголовок и две кнопки. Фон сделаем эффектным градиентом.

**Код (добавляется после `<header>`):**
```html
<section id="home" class="gradient-bg text-white pt-24 pb-20 md:pt-32 md:pb-28">
    <div class="container mx-auto px-4 text-center">
        <div class="max-w-3xl mx-auto">
            <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold mb-6">Веб-разработчик</h1>
            <p class="text-xl md:text-2xl mb-8 opacity-90">Создаю современные и адаптивные веб-сайты с использованием HTML5, CSS3 и JavaScript</p>
            <div class="flex flex-col sm:flex-row justify-center gap-4">
                <a href="#portfolio" class="bg-white text-indigo-600 px-6 py-3 rounded-lg font-semibold hover:bg-gray-100 transition shadow-lg">
                    <i class="fas fa-eye mr-2"></i>Смотреть работы
                </a>
                <a href="#contact" class="bg-transparent border-2 border-white text-white px-6 py-3 rounded-lg font-semibold hover:bg-white hover:text-indigo-600 transition">
                    <i class="fas fa-paper-plane mr-2"></i>Связаться
                </a>
            </div>
        </div>
    </div>
</section>
```
*Также в тег `<style>` добавим сам градиент:*
```css
.gradient-bg {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

**Подробное объяснение:**

-   `<section id="home">`: Мы используем тег `<section>` для семантического разделения страницы на логические блоки. `id="home"` — это "якорь", к которому будет вести ссылка из меню.
-   `pt-24 pb-20 md:pt-32 md:pb-28`: Адаптивные внутренние отступы сверху (`padding-top`) и снизу (`padding-bottom`). На мобильных они меньше, на десктопах (`md:`) — больше, чтобы компенсировать высоту шапки и дать больше "воздуха".
-   `max-w-3xl mx-auto`: Ограничиваем максимальную ширину текстового блока (`max-width`) и центрируем его. Это улучшает читаемость.
-   `text-4xl md:text-5xl lg:text-6xl`: Адаптивный размер шрифта. Чем больше экран, тем крупнее заголовок.
-   `flex flex-col sm:flex-row`: Кнопки на самых маленьких экранах будут в столбик (`flex-col`), а на экранах побольше (`sm:`) — в ряд (`flex-row`).
-   `rounded-lg`, `shadow-lg`: Скругляет углы и добавляет тень, делая элементы более "материальными".

---

### Шаг 4: Секция "Обо мне"

**Задача:** Добавить блок с фотографией, кратким описанием и личной информацией.

**Код (добавляется после секции `#home`):**
```html
<section id="about" class="py-16 bg-white">
    <div class="container mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-bold text-center mb-12 section-title relative">Обо мне</h2>
        
        <div class="flex flex-col lg:flex-row items-center gap-12">
            <div class="lg:w-1/3">
                <div class="rounded-2xl overflow-hidden shadow-xl">
                    <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80" 
                         alt="Фото профиля" class="w-full h-auto">
                </div>
            </div>
            
            <div class="lg:w-2/3">
                <h3 class="text-2xl font-bold text-gray-800 mb-4">Веб-разработчик</h3>
                <p class="text-gray-600 mb-6">Я студент специальности "Информационные системы и программирование". Увлекаюсь веб-разработкой и созданием современных пользовательских интерфейсов.</p>
                <p class="text-gray-600 mb-8">В этом проекте я разработал шаблон сайта-портфолио, который может быть использован студентами и начинающими специалистами для демонстрации своих работ и навыков.</p>
                
                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
                    <div class="flex items-center">
                        <i class="fas fa-calendar-alt text-indigo-500 mr-2"></i>
                        <span class="text-gray-700">Возраст: 21</span>
                    </div>
                    <div class="flex items-center">
                        <i class="fas fa-map-marker-alt text-indigo-500 mr-2"></i>
                        <span class="text-gray-700">Город: Красноярск</span>
                    </div>
                    <!-- ... и так далее для других полей -->
                </div>
            </div>
        </div>
    </div>
</section>
```
*И добавим стиль для заголовка в `<style>`:*
```css
.section-title::after {
    content: '';
    position: absolute;
    width: 50px; /* Ширина линии */
    height: 3px;
    background: #667eea; /* Цвет линии (индиго) */
    bottom: -10px; /* Расположение под текстом */
    left: 50%; /* Центрирование */
    transform: translateX(-50%);
}
```

**Подробное объяснение:**

-   `py-16`: Большие вертикальные отступы, чтобы секции не "слипались".
-   `section-title relative`: Мы делаем заголовок `position: relative`, чтобы можно было абсолютно спозиционировать псевдоэлемент `::after` (декоративную линию) относительно него.
-   `flex flex-col lg:flex-row`: Классический паттерн для адаптивности. На мобильных — колонка, на больших экранах (`lg:`) — ряд.
-   `gap-12`: Задает расстояние между flex-элементами (между фото и текстом).
-   `rounded-2xl overflow-hidden shadow-xl`: Создаем красивую карточку для фото: сильно скругленные углы, `overflow-hidden` (чтобы изображение не вылезало за скругления) и выразительная тень.
-   `grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4`: Используем CSS Grid для создания сетки контактов. На мобильных — 1 колонка, на `sm:` — 2, на `md:` — 3. `gap-4` задает отступы между ячейками сетки.


---

### Шаг 5: Секция "Навыки"

**Задача:** Визуализировать уровень владения технологиями с помощью прогресс-баров и показать статистику в виде карточек.

**Код (добавляется после секции `#about`):**
```html
<section id="skills" class="py-16 bg-gray-100">
    <div class="container mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-bold text-center mb-12 section-title relative">Мои навыки</h2>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto">
            <!-- Карточка Frontend -->
            <div class="bg-white p-6 rounded-xl shadow-md">
                <h3 class="text-xl font-bold text-gray-800 mb-4">Frontend разработка</h3>
                <div class="space-y-4">
                    <div>
                        <div class="flex justify-between mb-1"><span>HTML5</span><span>90%</span></div>
                        <div class="w-full bg-gray-200 rounded-full h-2">
                            <div class="bg-indigo-500 h-2 rounded-full skill-bar" data-width="90%"></div>
                        </div>
                    </div>
                    <!-- ... другие навыки ... -->
                </div>
            </div>
            <!-- Карточка Инструменты -->
            <div class="bg-white p-6 rounded-xl shadow-md">
                <!-- ... аналогично ... -->
            </div>
        </div>

        <!-- Статистика -->
        <div class="mt-12 grid grid-cols-2 md:grid-cols-4 gap-6 max-w-4xl mx-auto">
            <div class="bg-white p-6 rounded-xl shadow-md text-center">
                <i class="fas fa-project-diagram text-indigo-500 text-3xl mb-4"></i>
                <h3 class="text-xl font-bold text-gray-800 counter" data-target="15">0</h3>
                <p class="text-gray-600">Завершенных проектов</p>
            </div>
            <!-- ... другие карточки статистики ... -->
        </div>
    </div>
</section>
```
*И добавим стиль для анимации в `<style>`:*
```css
.skill-bar {
    width: 0; /* Изначально ширина 0 */
    transition: width 1.5s ease-in-out; /* Плавный переход */
}
```

**Подробное объяснение:**

-   `max-w-4xl mx-auto`: Снова ограничиваем ширину контента для лучшего вида на широких экранах.
-   `space-y-4`: Добавляет вертикальный отступ между дочерними элементами (между прогресс-барами).
-   `w-full bg-gray-200 rounded-full h-2`: Это фон прогресс-бара. `w-full` — на всю ширину, `bg-gray-200` — серый цвет, `rounded-full` — делает его полностью круглым по краям, `h-2` — высота.
-   `skill-bar`: Наш кастомный класс для анимированной полоски. Изначально ее ширина 0.
-   `data-width="90%"` и `data-target="15"`: Это `data-`атрибуты. Мы используем их для хранения данных прямо в HTML. JavaScript позже прочитает эти значения, чтобы знать, до какой ширины анимировать полоску (`data-width`) или до какого числа считать счетчик (`data-target`).

---

### Шаг 6: Секция "Портфолио"

**Задача:** Создать галерею работ с возможностью фильтрации по категориям.

**Код (добавляется после секции `#skills`):**
```html
<section id="portfolio" class="py-16 bg-white">
    <div class="container mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-bold text-center mb-12 section-title relative">Мои работы</h2>
        
        <div class="flex flex-wrap justify-center gap-4 mb-10">
            <button class="filter-btn bg-indigo-500 text-white px-4 py-2 rounded-lg" data-filter="all">Все</button>
            <button class="filter-btn bg-gray-200 text-gray-700 px-4 py-2 rounded-lg" data-filter="web">Веб-сайты</button>
            <button class="filter-btn bg-gray-200 text-gray-700 px-4 py-2 rounded-lg" data-filter="app">Приложения</button>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div class="portfolio-item bg-white rounded-xl overflow-hidden shadow-lg" data-category="web">
                <div class="h-48 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1551650975-87deedd944c3?ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80" 
                         alt="Проект 1" class="w-full h-full object-cover">
                </div>
                <div class="p-6">
                    <h3 class="text-xl font-bold mb-2">Корпоративный сайт</h3>
                    <p class="text-gray-600">Описание проекта...</p>
                </div>
            </div>
            <!-- ... другие проекты с разными data-category ... -->
        </div>
    </div>
</section>
```

**Подробное объяснение:**

-   `flex-wrap justify-center`: Кнопки-фильтры будут центрированы, и если они не поместятся в одну строку, `flex-wrap` перенесет их на следующую.
-   `data-filter="web"` и `data-category="web"`: Ключевые атрибуты для работы фильтра. JavaScript будет по клику на кнопку с `data-filter` искать элементы с соответствующим `data-category`.
-   `object-cover`: Этот класс для изображений — очень полезная вещь. Он масштабирует картинку так, чтобы она полностью заполнила свой контейнер, сохраняя пропорции (лишнее обрезается). Это предотвращает искажение изображений.

---

### Шаг 7: Секция "Контакты" и "Подвал" (Footer)

**Задача:** Завершить страницу блоком с контактной информацией и ссылками на соцсети, а также добавить подвал.

**Код (добавляется после секции `#portfolio`):**
```html
<!-- Секция Контакты -->
<section id="contact" class="py-16 bg-gray-100">
    <div class="container mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-bold text-center mb-12 section-title relative">Контакты</h2>
        <div class="max-w-4xl mx-auto text-center">
            <p class="text-lg mb-8">Готов обсудить ваш проект. Свяжитесь со мной любым удобным способом.</p>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
                <!-- Карточка Адрес -->
                <div class="bg-white p-6 rounded-xl shadow-md">
                    <i class="fas fa-map-marker-alt text-indigo-500 text-2xl mb-4"></i>
                    <h4 class="font-semibold">Адрес</h4>
                    <p>г. Красноярск, Россия</p>
                </div>
                <!-- ... другие карточки ... -->
            </div>
            <div class="flex justify-center space-x-6">
                <a href="#" class="bg-indigo-500 text-white p-4 rounded-full"><i class="fab fa-vk text-xl"></i></a>
                <!-- ... другие соцсети ... -->
            </div>
        </div>
    </div>
</section>

<!-- Подвал -->
<footer class="bg-gray-800 text-white py-8">
    <div class="container mx-auto px-4 text-center">
        <p class="text-gray-400">&copy; 2024 Портфолио. Все права защищены.</p>
    </div>
</footer>
```

**Подробное объяснение:**

-   Структура этих блоков уже знакома: секция, контейнер, заголовок, сетка (`grid`) для карточек.
-   `space-x-6`: Добавляет горизонтальный отступ между иконками соцсетей.
-   `rounded-full`: Делает фон для иконок идеально круглым.
-   `<footer>`: Семантический тег для подвала сайта. `bg-gray-800 text-white` — темный фон и светлый текст, классическое решение для футера.

---

### Шаг 8: Добавление JavaScript для интерактивности

**Задача:** "Оживить" сайт. Добавить обработчики событий для меню, фильтра, а также запустить анимации при прокрутке.

Теперь, когда вся разметка и стили готовы, пришло время для JavaScript. Весь код помещается в тег `<script>` в самом конце `<body>`.

**Код (добавляется в `<script>`):**
```javascript
$(document).ready(function() {
    // 1. Логика для мобильного меню
    $('#menu-toggle').click(function() {
        $('#mobile-menu').slideToggle();
    });

    // 2. Логика для фильтра портфолио
    $('.filter-btn').click(function() {
        // Стилизация активной кнопки
        $('.filter-btn').removeClass('bg-indigo-500 text-white').addClass('bg-gray-200 text-gray-700');
        $(this).addClass('bg-indigo-500 text-white').removeClass('bg-gray-200 text-gray-700');

        const filterValue = $(this).data('filter');
        if (filterValue === 'all') {
            $('.portfolio-item').fadeIn(300);
        } else {
            $('.portfolio-item').fadeOut(0);
            $('.portfolio-item[data-category="' + filterValue + '"]').fadeIn(300);
        }
    });

    // 3. Плавная прокрутка к якорям
    $('a[href^="#"]').click(function(e) {
        e.preventDefault();
        const targetId = $(this).attr('href');
        if ($(targetId).length) {
            $('html, body').animate({
                scrollTop: $(targetId).offset().top - 80 // 80px - смещение для шапки
            }, 800);
        }
    });

    // 4. Анимации при прокрутке
    function handleScrollAnimations() {
        const viewportTop = $(window).scrollTop();
        const viewportBottom = viewportTop + $(window).height();

        // Анимация появления элементов
        $('.fade-in').each(function() {
            const elementTop = $(this).offset().top;
            if (elementTop < viewportBottom - 50) {
                $(this).addClass('active');
            }
        });

        // Анимация прогресс-баров
        $('.skill-bar').each(function() {
            const elementTop = $(this).offset().top;
            if (elementTop < viewportBottom) {
                $(this).css('width', $(this).data('width'));
            }
        });

        // Анимация счетчиков
        $('.counter').each(function() {
            if (!$(this).hasClass('animated') && $(this).offset().top < viewportBottom) {
                $(this).addClass('animated');
                const target = +$(this).data('target');
                $({ countNum: $(this).text()}).animate({ countNum: target }, {
                    duration: 2000,
                    easing: 'swing',
                    step: function() {
                        $(this).text(Math.floor(this.countNum));
                    },
                    complete: function() {
                        $(this).text(this.countNum);
                    }
                });
            }
        });
    }

    // Вызов функции при загрузке и скролле
    $(window).on('scroll load', handleScrollAnimations);

    // Добавим все остальные стили для анимаций в <style>
});
```
*Также нужно добавить все классы для анимаций в тег `<style>`, как в оригинальном файле.*

**Подробное объяснение:**

-   `$(document).ready(function() { ... });`: Код внутри этой функции выполнится только после того, как вся страница будет загружена. Это стандартная и безопасная практика.
-   `$('#menu-toggle').click(...)`: Мы "слушаем" событие клика по элементу с `id="menu-toggle"`. Когда клик происходит, выполняется функция, которая плавно открывает/закрывает мобильное меню (`slideToggle`).
-   `$(this)`: Внутри обработчика события `$(this)` всегда ссылается на элемент, который вызвал это событие (например, на конкретную кнопку, по которой кликнули).
-   `.offset().top`: Метод jQuery, который возвращает расстояние от верха документа до элемента. Мы используем его, чтобы узнать, где на странице находятся элементы и пора ли их анимировать.
-   `$(window).on('scroll load', ...)`: Мы привязываем нашу функцию с анимациями сразу к двум событиям: `load` (когда страница загрузилась) и `scroll` (каждый раз, когда пользователь крутит страницу). Это гарантирует, что анимации сработают и для первого экрана, и для всех последующих при прокрутке.
