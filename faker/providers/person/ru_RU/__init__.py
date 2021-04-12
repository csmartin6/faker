from collections import OrderedDict

from .. import Provider as PersonProvider


# See transliteration table https://en.wikipedia.org/wiki/Romanization_of_Russian#Transliteration_table
def translit(text):
    translit_dict = {
      'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y',
      'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f',
      'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu',
      'я': 'ya', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'Ye', 'Ë': 'E', 'Ж': 'Zh', 'З': 'Z', 'И': 'I',
      'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
      'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ы': 'Y', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya',
     }
    for letter in text:
        if letter.isalpha():
            text = text.replace(letter, translit_dict[letter])
    return text


class Provider(PersonProvider):
    formats_male = OrderedDict((
        ('{{last_name_male}} {{first_name_male}} {{middle_name_male}}', 0.49),
        ('{{first_name_male}} {{middle_name_male}} {{last_name_male}}', 0.49),
        ('{{prefix_male}} {{last_name_male}} {{first_name_male}} {{middle_name_male}}', 0.02),
    ))

    formats_female = OrderedDict((
        ('{{last_name_female}} {{first_name_female}} {{middle_name_female}}', 0.49),
        ('{{first_name_female}} {{middle_name_female}} {{last_name_female}}', 0.49),
        ('{{prefix_female}} {{last_name_female}} {{first_name_female}} {{middle_name_female}}', 0.02),
    ))

    # Using random_element's dictionary weighting means that the
    #     formats = formats_male + formats_female
    # has to be replaced with something dict and python 2.x compatible

    formats = formats_male.copy()
    formats.update(formats_female)

    first_names_male = (
        'Август', 'Авдей', 'Аверкий', 'Аверьян', 'Авксентий', 'Автоном',
        'Агап', 'Агафон', 'Аггей', 'Адам', 'Адриан', 'Азарий',
        'Аким', 'Александр', 'Алексей', 'Амвросий', 'Амос', 'Ананий',
        'Анатолий', 'Андрей', 'Андрон', 'Андроник', 'Аникей', 'Аникита',
        'Анисим', 'Антип', 'Антонин', 'Аполлинарий', 'Аполлон', 'Арефий',
        'Аристарх', 'Аркадий', 'Арсений', 'Артемий', 'Артем', 'Архип',
        'Аскольд', 'Афанасий', 'Афиноген', 'Бажен', 'Богдан', 'Болеслав',
        'Борис', 'Борислав', 'Боян', 'Бронислав', 'Будимир', 'Вадим',
        'Валентин', 'Валерий', 'Валерьян', 'Варлаам', 'Варфоломей', 'Василий',
        'Вацлав', 'Велимир', 'Венедикт', 'Вениамин', 'Викентий', 'Виктор',
        'Викторин', 'Виссарион', 'Виталий', 'Владилен', 'Владлен', 'Владимир',
        'Владислав', 'Влас', 'Всеволод', 'Всемил', 'Всеслав', 'Вышеслав',
        'Вячеслав', 'Гаврила', 'Галактион', 'Гедеон', 'Геннадий', 'Георгий',
        'Герасим', 'Герман', 'Глеб', 'Гордей', 'Гостомысл', 'Гремислав',
        'Григорий', 'Гурий', 'Давыд', 'Данила', 'Дементий', 'Демид',
        'Демьян', 'Денис', 'Дмитрий', 'Добромысл', 'Доброслав', 'Дорофей',
        'Евгений', 'Евграф', 'Евдоким', 'Евлампий', 'Евсей', 'Евстафий',
        'Евстигней', 'Егор', 'Елизар', 'Елисей', 'Емельян', 'Епифан',
        'Еремей', 'Ермил', 'Ермолай', 'Ерофей', 'Ефим', 'Ефрем',
        'Захар', 'Зиновий', 'Зосима', 'Иван', 'Игнатий', 'Игорь',
        'Измаил', 'Изот', 'Изяслав', 'Иларион', 'Илья', 'Иннокентий',
        'Иосиф', 'Ипат', 'Ипатий', 'Ипполит', 'Ираклий', 'Исай',
        'Исидор', 'Казимир', 'Каллистрат', 'Капитон', 'Карл', 'Карп',
        'Касьян', 'Ким', 'Кир', 'Кирилл', 'Клавдий', 'Климент',
        'Кондрат', 'Кондратий', 'Конон', 'Константин', 'Корнил', 'Кузьма',
        'Куприян', 'Лавр', 'Лаврентий', 'Ладимир', 'Ладислав', 'Лазарь',
        'Лев', 'Леон', 'Леонид', 'Леонтий', 'Лонгин', 'Лука',
        'Лукьян', 'Лучезар', 'Любим', 'Любомир', 'Любосмысл', 'Макар',
        'Максим', 'Максимильян', 'Мариан', 'Марк', 'Мартын', 'Мартьян',
        'Матвей', 'Мефодий', 'Мечислав', 'Милан', 'Милен', 'Милий',
        'Милован', 'Мина', 'Мир', 'Мирон', 'Мирослав', 'Митофан',
        'Михаил', 'Михей', 'Модест', 'Моисей', 'Мокей', 'Мстислав',
        'Назар', 'Наркис', 'Натан', 'Наум', 'Нестор', 'Никандр',
        'Никанор', 'Никита', 'Никифор', 'Никодим', 'Николай', 'Никон',
        'Нифонт', 'Олег', 'Олимпий', 'Онуфрий', 'Орест', 'Осип',
        'Остап', 'Остромир', 'Павел', 'Панкратий', 'Панкрат', 'Пантелеймон',
        'Панфил', 'Парамон', 'Парфен', 'Пахом', 'Петр', 'Пимен',
        'Платон', 'Поликарп', 'Порфирий', 'Потап', 'Пров', 'Прокл',
        'Прокофий', 'Прохор', 'Радим', 'Радислав', 'Радован', 'Ратибор',
        'Ратмир', 'Родион', 'Роман', 'Ростислав', 'Рубен', 'Руслан',
        'Рюрик', 'Савва', 'Савватий', 'Савелий', 'Самсон', 'Самуил',
        'Светозар', 'Святополк', 'Святослав', 'Севастьян', 'Селиван', 'Селиверст',
        'Семен', 'Серафим', 'Сергей', 'Сигизмунд', 'Сидор', 'Сила',
        'Силантий', 'Сильвестр', 'Симон', 'Сократ', 'Соломон', 'Софон',
        'Софрон', 'Спартак', 'Спиридон', 'Станимир', 'Станислав', 'Степан',
        'Стоян', 'Тарас', 'Твердислав', 'Творимир', 'Терентий', 'Тимофей',
        'Тимур', 'Тит', 'Тихон', 'Трифон', 'Трофим', 'Ульян',
        'Устин', 'Фадей', 'Федор', 'Федосий', 'Федот', 'Феликс',
        'Феоктист', 'Феофан', 'Ферапонт', 'Филарет', 'Филимон', 'Филипп',
        'Фирс', 'Флорентин', 'Фока', 'Фома', 'Фортунат', 'Фотий',
        'Фрол', 'Харитон', 'Харлампий', 'Христофор', 'Чеслав', 'Эдуард',
        'Эммануил', 'Эмиль', 'Эраст', 'Эрнест', 'Эрнст', 'Ювеналий',
        'Юлиан', 'Юлий', 'Юрий', 'Яков', 'Ян', 'Якуб',
        'Януарий', 'Ярополк', 'Ярослав',
    )

    first_names_female = (
        'Агата', 'Агафья', 'Акулина', 'Алевтина', 'Александра', 'Алина',
        'Алла', 'Анастасия', 'Ангелина', 'Анжела', 'Анжелика', 'Анна',
        'Антонина', 'Валентина', 'Валерия', 'Варвара', 'Василиса', 'Вера',
        'Вероника', 'Виктория', 'Галина', 'Глафира', 'Дарья', 'Евгения',
        'Евдокия', 'Евпраксия', 'Евфросиния', 'Екатерина', 'Елена', 'Елизавета',
        'Жанна', 'Зинаида', 'Зоя', 'Иванна', 'Ираида', 'Ирина',
        'Ия', 'Кира', 'Клавдия', 'Ксения', 'Лариса', 'Лидия',
        'Лора', 'Лукия', 'Любовь', 'Людмила', 'Майя', 'Маргарита',
        'Марина', 'Мария', 'Марфа', 'Милица', 'Надежда', 'Наина',
        'Наталья', 'Нина', 'Нинель', 'Нонна', 'Оксана', 'Октябрина',
        'Олимпиада', 'Ольга', 'Пелагея', 'Полина', 'Прасковья', 'Раиса',
        'Регина', 'Светлана', 'Синклитикия', 'София', 'Таисия', 'Тамара',
        'Татьяна', 'Ульяна', 'Фаина', 'Феврония', 'Фёкла', 'Элеонора', 'Эмилия', 'Юлия',
    )

    first_names = first_names_male + first_names_female

    last_names_male = (
        'Смирнов', 'Иванов', 'Кузнецов', 'Попов', 'Соколов',
        'Лебедев', 'Козлов', 'Новиков', 'Морозов', 'Петров',
        'Волков', 'Соловьев', 'Васильев', 'Зайцев', 'Павлов',
        'Семенов', 'Голубев', 'Виноградов', 'Богданов', 'Воробьев',
        'Федоров', 'Михайлов', 'Беляев', 'Тарасов', 'Белов',
        'Комаров', 'Орлов', 'Киселев', 'Макаров', 'Андреев',
        'Ковалев', 'Ильин', 'Гусев', 'Титов', 'Кузьмин',
        'Кудрявцев', 'Баранов', 'Куликов', 'Алексеев', 'Степанов',
        'Яковлев', 'Сорокин', 'Сергеев', 'Романов', 'Захаров',
        'Борисов', 'Королев', 'Герасимов', 'Пономарев', 'Григорьев',
        'Лазарев', 'Медведев', 'Ершов', 'Никитин', 'Соболев',
        'Рябов', 'Поляков', 'Цветков', 'Данилов', 'Жуков',
        'Фролов', 'Журавлев', 'Николаев', 'Крылов', 'Максимов',
        'Сидоров', 'Осипов', 'Белоусов', 'Федотов', 'Дорофеев',
        'Егоров', 'Матвеев', 'Бобров', 'Дмитриев', 'Калинин',
        'Анисимов', 'Петухов', 'Антонов', 'Тимофеев', 'Никифоров',
        'Веселов', 'Филиппов', 'Марков', 'Большаков', 'Суханов',
        'Миронов', 'Ширяев', 'Александров', 'Коновалов', 'Шестаков',
        'Казаков', 'Ефимов', 'Денисов', 'Громов', 'Фомин',
        'Давыдов', 'Мельников', 'Щербаков', 'Блинов', 'Колесников',
        'Карпов', 'Афанасьев', 'Власов', 'Маслов', 'Исаков',
        'Тихонов', 'Аксенов', 'Гаврилов', 'Родионов', 'Котов',
        'Горбунов', 'Кудряшов', 'Быков', 'Зуев', 'Третьяков',
        'Савельев', 'Панов', 'Рыбаков', 'Суворов', 'Абрамов',
        'Воронов', 'Мухин', 'Архипов', 'Трофимов', 'Мартынов',
        'Емельянов', 'Горшков', 'Чернов', 'Овчинников', 'Селезнев',
        'Панфилов', 'Копылов', 'Михеев', 'Галкин', 'Назаров',
        'Лобанов', 'Лукин', 'Беляков', 'Потапов', 'Некрасов',
        'Хохлов', 'Жданов', 'Наумов', 'Шилов', 'Воронцов',
        'Ермаков', 'Дроздов', 'Игнатьев', 'Савин', 'Логинов',
        'Сафонов', 'Капустин', 'Кириллов', 'Моисеев', 'Елисеев',
        'Кошелев', 'Костин', 'Горбачев', 'Орехов', 'Ефремов',
        'Исаев', 'Евдокимов', 'Калашников', 'Кабанов', 'Носков',
        'Юдин', 'Кулагин', 'Лапин', 'Прохоров', 'Нестеров',
        'Харитонов', 'Агафонов', 'Муравьев', 'Ларионов', 'Федосеев',
        'Зимин', 'Пахомов', 'Шубин', 'Игнатов', 'Филатов',
        'Крюков', 'Рогов', 'Кулаков', 'Терентьев', 'Молчанов',
        'Владимиров', 'Артемьев', 'Гурьев', 'Зиновьев', 'Гришин',
        'Кононов', 'Дементьев', 'Ситников', 'Симонов', 'Мишин',
        'Фадеев', 'Комиссаров', 'Мамонтов', 'Носов', 'Гуляев',
        'Шаров', 'Устинов', 'Вишняков', 'Евсеев', 'Лаврентьев',
        'Брагин', 'Константинов', 'Корнилов', 'Авдеев', 'Зыков',
        'Бирюков', 'Шарапов', 'Никонов', 'Щукин', 'Дьячков',
        'Одинцов', 'Сазонов', 'Якушев', 'Красильников', 'Гордеев',
        'Самойлов', 'Князев', 'Беспалов', 'Уваров', 'Шашков',
        'Бобылев', 'Доронин', 'Белозеров', 'Рожков', 'Самсонов',
        'Мясников', 'Лихачев', 'Буров', 'Сысоев', 'Фомичев',
        'Русаков', 'Стрелков', 'Гущин', 'Тетерин', 'Колобов',
        'Субботин', 'Фокин', 'Блохин', 'Селиверстов', 'Пестов',
        'Кондратьев', 'Силин', 'Меркушев', 'Лыткин', 'Туров',
        'Путин',
    )

    last_names_female = (
        'Смирнова', 'Иванова', 'Кузнецова', 'Попова', 'Соколова',
        'Лебедева', 'Козлова', 'Новикова', 'Морозова', 'Петрова', 'Волкова',
        'Соловьева', 'Васильева', 'Зайцева', 'Павлова', 'Семенова',
        'Голубева', 'Виноградова', 'Богданова', 'Воробьева', 'Федорова',
        'Михайлова', 'Беляева', 'Тарасова', 'Белова', 'Комарова', 'Орлова',
        'Киселева', 'Макарова', 'Андреева', 'Ковалева', 'Ильина', 'Гусева',
        'Титова', 'Кузьмина', 'Кудрявцева', 'Баранова', 'Куликова',
        'Алексеева', 'Степанова', 'Яковлева', 'Сорокина', 'Сергеева',
        'Романова', 'Захарова', 'Борисова', 'Королева', 'Герасимова',
        'Пономарева', 'Григорьева', 'Лазарева', 'Медведева', 'Ершова',
        'Никитина', 'Соболева', 'Рябова', 'Полякова', 'Цветкова', 'Данилова',
        'Жукова', 'Фролова', 'Журавлева', 'Николаева', 'Крылова', 'Максимова',
        'Сидорова', 'Осипова', 'Белоусова', 'Федотова', 'Дорофеева',
        'Егорова', 'Матвеева', 'Боброва', 'Дмитриева', 'Калинина',
        'Анисимова', 'Петухова', 'Антонова', 'Тимофеева', 'Никифорова',
        'Веселова', 'Филиппова', 'Маркова', 'Большакова', 'Суханова',
        'Миронова', 'Ширяева', 'Александрова', 'Коновалова', 'Шестакова',
        'Казакова', 'Ефимова', 'Денисова', 'Громова', 'Фомина', 'Давыдова',
        'Мельникова', 'Щербакова', 'Блинова', 'Колесникова', 'Карпова',
        'Афанасьева', 'Власова', 'Маслова', 'Исакова', 'Тихонова', 'Аксенова',
        'Гаврилова', 'Родионова', 'Котова', 'Горбунова', 'Кудряшова',
        'Быкова', 'Зуева', 'Третьякова', 'Савельева', 'Панова', 'Рыбакова',
        'Суворова', 'Абрамова', 'Воронова', 'Мухина', 'Архипова', 'Трофимова',
        'Мартынова', 'Емельянова', 'Горшкова', 'Чернова', 'Овчинникова',
        'Селезнева', 'Панфилова', 'Копылова', 'Михеева', 'Галкина',
        'Назарова', 'Лобанова', 'Лукина', 'Белякова', 'Потапова', 'Некрасова',
        'Хохлова', 'Жданова', 'Наумова', 'Шилова', 'Воронцова', 'Ермакова',
        'Дроздова', 'Игнатьева', 'Савина', 'Логинова', 'Сафонова',
        'Капустина', 'Кириллова', 'Моисеева', 'Елисеева', 'Кошелева',
        'Костина', 'Горбачева', 'Орехова', 'Ефремова', 'Исаева', 'Евдокимова',
        'Калашникова', 'Кабанова', 'Носкова', 'Юдина', 'Кулагина', 'Лапина',
        'Прохорова', 'Нестерова', 'Харитонова', 'Агафонова', 'Муравьева',
        'Ларионова', 'Федосеева', 'Зимина', 'Пахомова', 'Шубина', 'Игнатова',
        'Филатова', 'Крюкова', 'Рогова', 'Кулакова', 'Терентьева',
        'Молчанова', 'Владимирова', 'Артемьева', 'Гурьева', 'Зиновьева',
        'Гришина', 'Кононова', 'Дементьева', 'Ситникова', 'Симонова',
        'Мишина', 'Фадеева', 'Комиссарова', 'Мамонтова', 'Носова', 'Гуляева',
        'Шарова', 'Устинова', 'Вишнякова', 'Евсеева', 'Лаврентьева',
        'Брагина', 'Константинова', 'Корнилова', 'Авдеева', 'Зыкова',
        'Бирюкова', 'Шарапова', 'Никонова', 'Щукина', 'Дьячкова', 'Одинцова',
        'Сазонова', 'Якушева', 'Красильникова', 'Гордеева', 'Самойлова',
        'Князева', 'Беспалова', 'Уварова', 'Шашкова', 'Бобылева', 'Доронина',
        'Белозерова', 'Рожкова', 'Самсонова', 'Мясникова', 'Лихачева',
        'Бурова', 'Сысоева', 'Фомичева', 'Русакова', 'Стрелкова', 'Гущина',
        'Тетерина', 'Колобова', 'Субботина', 'Фокина', 'Блохина',
        'Селиверстова', 'Пестова', 'Кондратьева', 'Силина', 'Меркушева',
        'Лыткина', 'Турова',
    )

    last_names = last_names_male + last_names_female

    middle_names_male = (
        'Ааронович', 'Абрамович', 'Августович', 'Авдеевич', 'Аверьянович',
        'Адамович', 'Адрианович', 'Аксёнович', 'Александрович', 'Алексеевич',
        'Анатольевич', 'Андреевич', 'Анисимович', 'Антипович', 'Антонович',
        'Ануфриевич', 'Арсенович', 'Арсеньевич', 'Артёмович', 'Артемьевич',
        'Артурович', 'Архипович', 'Афанасьевич', 'Бенедиктович', 'Богданович',
        'Бориславович', 'Бориславович', 'Борисович', 'Брониславович',
        'Валентинович', 'Валерианович', 'Валерьевич', 'Валерьянович',
        'Васильевич', 'Венедиктович', 'Викентьевич', 'Викторович', 'Виленович',
        'Вилорович', 'Витальевич', 'Владиленович', 'Владиславович',
        'Владленович', 'Власович', 'Всеволодович', 'Вячеславович',
        'Гавриилович', 'Гаврилович', 'Геннадиевич', 'Георгиевич', 'Герасимович',
        'Германович', 'Гертрудович', 'Глебович', 'Гордеевич', 'Григорьевич',
        'Гурьевич', 'Давидович', 'Давыдович', 'Даниилович', 'Данилович',
        'Демидович', 'Демьянович', 'Денисович', 'Димитриевич', 'Дмитриевич',
        'Дорофеевич', 'Евсеевич', 'Евстигнеевич', 'Егорович', 'Елизарович',
        'Елисеевич', 'Еремеевич', 'Ермилович', 'Ермолаевич', 'Ерофеевич',
        'Ефимович', 'Ефимьевич', 'Ефремович', 'Ефстафьевич', 'Жанович',
        'Жоресович', 'Захарьевич', 'Зиновьевич', 'Игнатович', 'Игнатьевич',
        'Игоревич', 'Измаилович', 'Изотович', 'Иларионович', 'Ильич',
        'Ильясович', 'Иосипович', 'Иосифович', 'Исидорович', 'Марсович',
        'Матвеевич', 'Тарасович', 'Теймуразович', 'Терентьевич', 'Тимурович',
        'Тихонович', 'Трифонович', 'Трофимович', 'Устинович', 'Фадеевич',
        'Фёдорович', 'Федосеевич', 'Федосьевич', 'Федотович', 'Феликсович',
        'Феодосьевич', 'Феоктистович', 'Феофанович', 'Филатович', 'Филимонович',
        'Филиппович', 'Фокич', 'Фомич', 'Фролович', 'Харитонович', 'Харламович',
        'Харлампович', 'Харлампьевич', 'Чеславович', 'Эдгардович', 'Эдгарович',
        'Эдуардович', 'Юлианович', 'Юльевич', 'Яковлевич', 'Якубович',
        'Ярославович',
    )

    middle_names_female = (
        'Александровна', 'Андреевна', 'Архиповна', 'Алексеевна', 'Антоновна',
        'Аскольдовна', 'Альбертовна', 'Аркадьевна', 'Афанасьевна',
        'Анатольевна', 'Артемовна', 'Богдановна', 'Болеславовна', 'Борисовна',
        'Вадимовна', 'Васильевна', 'Владимировна', 'Валентиновна',
        'Вениаминовна', 'Владиславовна', 'Валериевна', 'Викторовна',
        'Вячеславовна', 'Геннадиевна', 'Георгиевна', 'Геннадьевна',
        'Григорьевна', 'Даниловна', 'Дмитриевна', 'Евгеньевна',
        'Егоровна', 'Ефимовна', 'Ждановна', 'Захаровна', 'Ивановна', 'Игоревна',
        'Ильинична', 'Кирилловна', 'Кузьминична', 'Константиновна',
        'Кузьминична', 'Леонидовна', 'Леоновна', 'Львовна', 'Макаровна',
        'Матвеевна', 'Михайловна', 'Максимовна', 'Мироновна', 'Натановна',
        'Никифоровна', 'Ниловна', 'Наумовна', 'Николаевна', 'Олеговна',
        'Оскаровна', 'Павловна', 'Петровна', 'Робертовна', 'Рубеновна',
        'Руслановна', 'Романовна', 'Рудольфовна', 'Святославовна', 'Сергеевна',
        'Степановна', 'Семеновна', 'Станиславовна', 'Тарасовна', 'Тимофеевна',
        'Тимуровна', 'Федоровна', 'Феликсовна', 'Филипповна', 'Харитоновна',
        'Эдуардовна', 'Эльдаровна', 'Юльевна', 'Юрьевна', 'Яковлевна',
    )

    middle_names = middle_names_male + middle_names_female

    language_names = (
        'Афарский', 'Абхазский', 'Авестийский', 'Африкаанс', 'Акан',
        'Амхарский', 'Арагонский', 'Арабский', 'Ассамский', 'Аварский',
        'Аймарский', 'Азербайджанский', 'Башкирский', 'Белорусский',
        'Болгарский', 'Бислама', 'Бенгальский', 'Тибетский', 'Бретонский',
        'Боснийский', 'Каталанский', 'Чеченский', 'Чаморро', 'Корсиканский',
        'Кри', 'Чешский', 'Чувашский', 'Валлийский', 'Датский', 'Немецкий',
        'Греческий', 'Английский', 'Эсперанто', 'Испанский', 'Эстонский',
        'Персидский', 'Финский', 'Фиджийский', 'Фарси', 'Французский',
        'Ирландский', 'Гэльский', 'Галийский', 'Иврит', 'Хинди',
        'Хорватский', 'Гавайский', 'Болгарский', 'Армянский',
        'Индонезийский', 'Исландский', 'Итальянский', 'Японский',
        'Яванский', 'Грузинский', 'Казахский', 'Корейский', 'Кашмири',
        'Курдский', 'Коми', 'Киргизский', 'Латинский', 'Люксембургский',
        'Лимбургский', 'Лингала', 'Лаосский', 'Литовский', 'Латвийский',
        'Малагасийский', 'Маршалльский', 'Маори', 'Македонский', 'Малаялам',
        'Монгольский', 'Маратхи', 'Малайский', 'Мальтийский', 'Непальский',
        'Нидерландский', 'Норвежский', 'Навахо', 'Оромо', 'Ория',
        'Осетинский', 'Пали', 'Польский', 'Пуштунский', 'Португальский',
        'Романшский', 'Румынский', 'Русский', 'Киньяруанда',
        'Санскрит', 'Сардинский', 'Санго', 'Сингальский',
        'Словацкий', 'Словенский', 'Самоанский', 'Сомалийский', 'Албанский',
        'Сербский', 'Сунданский', 'Шведский', 'Суахили', 'Тамильский',
        'Телугу', 'Таджикский', 'Тайский', 'Тигринья', 'Туркменский',
        'Тагальский', 'Тсвана', 'Тонга', 'Турецкий', 'Тсонга', 'Татарский',
        'Таитянский', 'Уйгурский', 'Украинский', 'Урду', 'Узбекский', 'Венда',
        'Вьетнамский', 'Идиш', 'Йоруба', 'Китайский', 'Зулу',
    )

    prefixes_male = ('г-н', 'тов.')

    prefixes_female = ('г-жа', 'тов.')

    def middle_name(self):
        return self.random_element(self.middle_names)

    def middle_name_male(self):
        return self.random_element(self.middle_names_male)

    def middle_name_female(self):
        return self.random_element(self.middle_names_female)
