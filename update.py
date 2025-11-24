from bs4 import BeautifulSoup, NavigableString, Tag
import os

# --- 1. Вспомогательные функции ---

def get_user_input(prompt, default_value):
    """Получает ввод от пользователя с дефолтным значением."""
    user_input = input(f"{prompt} (По умолчанию: '{default_value}'): ").strip()
    return user_input if user_input else default_value

def get_user_int(prompt, default_value, min_val=0, max_val=100):
    """Получает числовой ввод (процент) от пользователя."""
    while True:
        value = input(f"{prompt} (По умолчанию: {default_value}%, от {min_val} до {max_val}): ").strip()
        if not value:
            return default_value
        try:
            num = int(value)
            if min_val <= num <= max_val:
                return num
            else:
                print(f"Пожалуйста, введите число в диапазоне от {min_val} до {max_val}.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

# --- 2. Сбор данных ---

def collect_user_data():
    """Собирает все данные для портфолио от пользователя."""
    data = {}
    images = {}
    skills = {}
    projects = []
    
    print("=== 📝 Ввод Общих Данных ===")
    data["home_title"] = get_user_input("Заголовок главной страницы", "Веб-разработчик")
    data["home_desc"] = get_user_input("Описание главной страницы", "Создаю современные и адаптивные веб-сайты")
    
    print("\n=== 🧑‍💻 Ввод Данных 'Обо мне' ===")
    images["profile_photo"] = get_user_input("Путь к фото профиля (images/my_photo.jpg или URL)", "images/my_photo.jpg")
    data["about_title"] = get_user_input("Заголовок 'Обо мне'", "Веб-разработчик")
    data["about_para1"] = get_user_input("Первый параграф описания", "Я студент специальности 'Информационные системы'. Увлекаюсь веб-разработкой.")
    data["about_para2"] = get_user_input("Второй параграф описания", "Этот шаблон создан для демонстрации работ.")
    data["age"] = get_user_input("Возраст", "21")
    data["city"] = get_user_input("Город", "Красноярск")
    data["education"] = get_user_input("Образование", "Высшее")
    data["email"] = get_user_input("Email", "example@mail.ru")
    data["phone"] = get_user_input("Телефон", "+7 (XXX) XXX-XX-XX")
    data["status"] = get_user_input("Статус", "Студент")
    
    print("\n=== 📊 Ввод Навыков (проценты) ===")
    skills["HTML5"] = get_user_int("HTML5", 90)
    skills["CSS3"] = get_user_int("CSS3", 85)
    skills["JavaScript"] = get_user_int("JavaScript", 75)
    skills["Git"] = get_user_int("Git", 80)
    skills["Figma"] = get_user_int("Figma", 70)
    skills["Tailwind CSS"] = get_user_int("Tailwind CSS", 85)
    
    print("\n=== 🔢 Счетчики ===")
    data["projects_count"] = get_user_input("Количество завершенных проектов", "15")
    data["clients_count"] = get_user_input("Количество довольных клиентов", "10")
    data["awards_count"] = get_user_input("Количество наград", "2")
    data["experience_years"] = get_user_input("Опыт работы (лет)", "1")
    
    print("\n=== 🖼️ Проекты (Портфолио) ===")
    i = 1
    while True:
        add_more = get_user_input(f"Добавить проект #{i}? (y/n)", "y").lower()
        if add_more != 'y':
            break
        project_data = {}
        project_data["img_path"] = get_user_input(f"Изображение проекта #{i} (images/project_{i}.jpg или URL)", f"images/project_{i}.jpg")
        project_data["title"] = get_user_input(f"Название проекта #{i}", f"Проект {i}")
        project_data["desc"] = get_user_input(f"Описание проекта #{i}", f"Описание проекта {i}")
        category = get_user_input(f"Категория #{i} (web/app/design)", "web").lower()
        while category not in ["web", "app", "design"]:
            print("Категория: web, app или design.")
            category = get_user_input(f"Категория #{i}", "web").lower()
        project_data["category"] = category
        project_data["url"] = get_user_input(f"Ссылка на проект #{i}", "#")
        projects.append(project_data)
        i += 1
    
    print("\n=== 📧 Контакты ===")
    data["address"] = get_user_input("Адрес", "г. Красноярск, Россия")

    print("\n=== 🔗 Социальные сети ===")
    data["vk_url"] = get_user_input("Ссылка VK", "https://vk.com/yourprofile")
    data["telegram_url"] = get_user_input("Ссылка Telegram", "https://t.me/yourusername")
    data["github_url"] = get_user_input("Ссылка GitHub", "https://github.com/yourusername")

    return data, images, skills, projects

# --- 3. Функция обновления HTML ---

def update_html(input_file, output_file, data, images, skills, projects):
    """Обновляет все значения в HTML используя BeautifulSoup."""
    if not os.path.exists(input_file):
        print(f"❌ Файл '{input_file}' не найден!")
        return False

    print(f"🔄 Загрузка {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')

    # Главная
    home_h1 = soup.select_one('#home h1.fade-in')
    if home_h1:
        home_h1.string = data["home_title"]
    home_p = soup.select_one('#home p.fade-in')
    if home_p:
        home_p.string = data["home_desc"]

    # Обо мне
    profile_img = soup.select_one('#about img[alt="Фото профиля"]')
    if profile_img:
        profile_img['src'] = images["profile_photo"]
    about_title = soup.select_one('#about h3')
    if about_title:
        about_title.string = data["about_title"]
    about_paras = soup.select('#about p.text-gray-600')
    if len(about_paras) >= 2:
        about_paras[0].string = data["about_para1"]
        about_paras[1].string = data["about_para2"]
    
    # Факты
    facts = {
        "Возраст:": f"Возраст: {data['age']}",
        "Город:": f"Город: {data['city']}",
        "Образование:": f"Образование: {data['education']}",
        "Email:": f"Email: {data['email']}",
        "Телефон:": f"Телефон: {data['phone']}",
        "Статус:": f"Статус: {data['status']}",
    }
    for old_text, new_text in facts.items():
        for span in soup.select('#about span.text-gray-700'):
            if span.string and span.string.startswith(old_text):
                span.string = new_text
                break

    # Навыки
    all_skills = {
        "HTML5": skills["HTML5"], "CSS3": skills["CSS3"], "JavaScript": skills["JavaScript"],
        "Git": skills["Git"], "Figma": skills["Figma"], "Tailwind CSS": skills["Tailwind CSS"]
    }
    for name, percent in all_skills.items():
        skill_span = soup.find('span', string=name)
        if skill_span:
            percent_span = skill_span.find_next_sibling('span', class_='text-gray-700')
            if percent_span:
                percent_span.string = f"{percent}%"
            skill_container = skill_span.parent.parent
            skill_bar = skill_container.select_one('.skill-bar')
            if skill_bar:
                skill_bar['data-width'] = f"{percent}%"

    # Счетчики
    counters = [
        ("Завершенных проектов", data["projects_count"]),
        ("Довольных клиентов", data["clients_count"]),
        ("Награды", data["awards_count"]),
        ("Опыта работы", data["experience_years"])
    ]
    for label, value in counters:
        p_tag = soup.find('p', string=label)
        if p_tag:
            h3_counter = p_tag.find_previous_sibling('h3', class_='counter')
            if h3_counter:
                h3_counter['data-target'] = value

    # Портфолио
    print("🔄 Обновление портфолио...")
    portfolio_grid = soup.select_one('#portfolio .grid')
    if portfolio_grid:
        for item in portfolio_grid.select('.portfolio-item'):
            item.decompose()
        
        tech_icons = {
            "web": ['fab fa-html5 text-red-500', 'fab fa-css3-alt text-blue-500', 'fab fa-js-square text-yellow-500'],
            "app": ['fab fa-react text-blue-400', 'fab fa-node-js text-green-500'],
            "design": ['fas fa-pen-nib text-purple-500', 'fas fa-palette text-pink-500']
        }
        
        for proj in projects:
            item = soup.new_tag('div', attrs={
                'class': 'portfolio-item bg-white rounded-xl overflow-hidden shadow-lg fade-in',
                'data-category': proj["category"]
            })
            
            img_div = soup.new_tag('div', attrs={'class': 'h-48 overflow-hidden portfolio-img'})
            img = soup.new_tag('img', src=proj["img_path"], alt=proj["title"], attrs={'class': 'w-full h-full object-cover'})
            img_div.append(img)
            item.append(img_div)
            
            content_div = soup.new_tag('div', attrs={'class': 'p-6'})
            
            h3 = soup.new_tag('h3', attrs={'class': 'text-xl font-bold text-gray-800 mb-2'})
            h3.string = proj["title"]
            content_div.append(h3)
            
            p_desc = soup.new_tag('p', attrs={'class': 'text-gray-600 mb-4'})
            p_desc.string = proj["desc"]
            content_div.append(p_desc)
            
            flex_div = soup.new_tag('div', attrs={'class': 'flex justify-between items-center'})
            
            link_a = soup.new_tag('a', href=proj["url"], attrs={'class': 'text-indigo-500 hover:text-indigo-700 font-medium flex items-center'})
            link_a.string = "Подробнее "
            arrow_i = soup.new_tag('i', attrs={'class': 'fas fa-arrow-right ml-2'})
            link_a.append(arrow_i)
            flex_div.append(link_a)
            
            tech_div = soup.new_tag('div', attrs={'class': 'flex space-x-2'})
            for icon_class in tech_icons.get(proj["category"], []):
                tech_i = soup.new_tag('i', attrs={'class': icon_class})
                tech_div.append(tech_i)
            flex_div.append(tech_div)
            
            content_div.append(flex_div)
            item.append(content_div)
            
            portfolio_grid.append(item)

    # Контакты
    contacts = {
        "Адрес": data["address"],
        "Email": data["email"],
        "Телефон": data["phone"]
    }
    for key, value in contacts.items():
        h4 = soup.find('h4', string=key)
        if h4:
            p_next = h4.find_next_sibling('p')
            if p_next:
                p_next.string = value

    # Социальные сети
    social_links = {
        "fab fa-vk": data["vk_url"],
        "fab fa-telegram": data["telegram_url"],
        "fab fa-github": data["github_url"]
    }
    for icon_class, url in social_links.items():
        for a_tag in soup.find_all('a'):
            i_tag = a_tag.find('i')
            if i_tag and icon_class in ' '.join(i_tag.get('class', [])):
                a_tag['href'] = url

    # Сохранение
    print(f"💾 Сохранение в {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("✅ Готово! Откройте update_index.html в браузере.")
    return True

# --- Главный блок ---
if __name__ == "__main__":
    INPUT_FILE = "index.html"
    OUTPUT_FILE = "update_index.html"
    
    os.makedirs("images", exist_ok=True)
    
    data, images, skills, projects = collect_user_data()
    success = update_html(INPUT_FILE, OUTPUT_FILE, data, images, skills, projects)
    if success:
        print("\n🚀 Запустите снова для нового ввода данных.")
