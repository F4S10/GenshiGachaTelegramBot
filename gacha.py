#Импорты
import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import sqlite3
from datetime import datetime
import random

#токен
TOKEN_API = ''

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

base = sqlite3.connect("gacha.db")
cur = base.cursor()

admList = [1080296062,]

#текстики
HELP_COMMANDS = """/gacha - покрутить гачу(можно 2 раз в день)
 /inventory - сколько и чего вы выбили
 /history - история круток
"""

@dp.message_handler(commands=["start"])
async def start(message : Message):
    user_nickname = message.from_user.full_name
    user_id = message.from_user.id
    user_tag = message.from_user.username
    one = "###"
    two = "###"
    tree = "###"
    four = "###"
    five = "###"
    six = "###"
    seven = "###"
    eight = "###"
    nine = "###"
    ten = "###"
    garant = 0
    epic_garant = 0
    cash = 100
    primogems = 150
    bonus = 1
    deyli = datetime.now()
    deyli.strftime("%Y-%m-%d %H:%M")
    pisa = 0
    cur.execute("SELECT user_id FROM gachaProfile WHERE user_id = ?", (user_id,))
    if cur.fetchone() is None:
        base.execute('CREATE TABLE IF NOT EXISTS gachaProfile(user_nickname, user_id, user_tag, cash, primogems)')
        cur.execute('INSERT INTO gachaProfile VALUES(?,?,?,?,?)',(user_nickname, user_id, user_tag, cash, primogems))
    else:
        pass
    cur.execute("SELECT user_id FROM inv WHERE user_id = ?", (user_id,))
    if cur.fetchone() is None:
        base.execute("CREATE TABLE IF NOT EXISTS inv(user_nickname, user_id, Меч_небесного_всадника, Филейный_нож, Меч_путешественника, Предвестник_зари, Холодное_лезвие, Лук_ворона, Посыльный, Клятва_стрелка, Рогатка, Изогнутый_лук, Чёрная_кисть, Алебарда_Миллелита, Парный_нефрит, Эпос_о_драконоборцах, Руководство_по_магии, Изумрудный_шар, Меч_драконьей_крови, Металлическая_тень, Меч_из_белого_железа, Дубина_переговоров, Меч_Фавония, Меч_флейта, Церемониальный_меч, Драконий_рык, Вспышка_во_тьме, Лунное_сияние_ксифоса, Бесструнный, Церемониальный_лук, Ржавый_лук, Зелёный_лук, Боевой_лук_Фавония, Охотник_во_тьме, Вальс_Нирваны_Ночи, Луна_Моун, Пика_полумесяца, Гроза_драконов, Каменное_копьё, Копьё_Фавония, Режущий_волны_плавник, Око_сознания, Кодекс_Фавония, Морская_карта, Церемониальные_мемуары, Песнь_странника, Вино_и_песни, Скитающаяся_звезда, Дождерез, Меч_колокол, Церемониальный_двуручный_меч, Двуручный_меч_Фавония, Каменный_меч, Акуомару, Аквамарин_Махайры, Барбара, Беннет, Бей_Доу, Кейа, Лиза, Нин_Гуан, Ноэль, Рейзор, Сахароза, Син_Цю, Сян_Лин, Фишль, Чунь_Юнь, Эмбер, Диона, Синь_Янь, Розария, Ян_Фей, Саю, Сара, Тома, Горо, Юнь_Цзинь, Куки_Синобу, Хэйдзо, Коллеи, Дори, Кандакия, Лайла, Фарузан, Яо_Яо, Мика, Кавех, Кирара, Бай_Чжу, Дэхья, Аль_Хайтам, Странник, Нахида, Нилу, Сайно, Тигнари, Е_Лань, Аято, Яэ_Мико, Шень_Хэ, Итто, Кокоми, Райден, Ёимия, Аяка, Кадзуха, Эола, Ху_Тао, Сяо, Гань_Юй, Альбедо, Чжун_Ли, Тарталья, Кли, Венти, Ци_Ци, Мона, Ке_Цин, Дилюк, Джинн, Драгоценный_омут, Кромсатель_пиков, Небесный_меч, Меч_сокола, Клятва_свободы, Рассекающий_туман, Харан_гэппаку_фуцу, Ключ_Хадж_нисут, Свет_лиственного_разреза, Лук_Амоса, Небесное_крыло, Элегия_погибели, Громовой_пульс, Полярная_звезда, Аква_симулякрум, Охотничья_тропа, Посох_Хомы, Нефритовый_коршун, Небесная_ось, Покоритель_вихря, Сияющая_жатва, Усмиритель_бед, Посох_алых_песков, Память_о_пыли, Небесный_атлас, Молитва_святых_ветрам, Вечное_лунное_сияние, Истина_кагура, Сновидения_тысячи_ночей, Воспоминания_Тулайтуллы, Великолепие_лазурного_свода, Некованый, Волчья_погибель, Небесное_величие, Песнь_разбитых_сосен, Краснорогий_камнеруб, Маяк_тростникового_моря)")
        cur.execute("INSERT INTO inv VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (user_nickname, user_id, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa))
    else:
        pass
    cur.execute("SELECT user_id FROM history WHERE user_id = ?", (user_id,))
    if cur.fetchone() is None:
        base.execute("CREATE TABLE IF NOT EXISTS history(user_nickname, user_id, one, two, tree, four, five, six, seven, eight, nine, ten)")
        cur.execute("INSERT INTO history VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", (user_nickname, user_id, one, two, tree, four, five, six, seven, eight, nine, ten))
    else:
        pass
    cur.execute("SELECT user_id FROM gacha WHERE user_id = ?", (user_id,))
    if cur.fetchone() is None:
        base.execute("CREATE TABLE IF NOT EXISTS gacha(user_nickname, user_id, epic_garant, garant)")
        cur.execute("INSERT INTO gacha VALUES(?,?,?,?)", (user_nickname, user_id, epic_garant, garant))
    else:
        pass
    cur.execute("SELECT user_id FROM gacha WHERE user_id = ?", (user_id,))
    if cur.fetchone() is None:
        base.execute('CREATE TABLE IF NOT EXISTS texnical(user_nickname, user_id, user_tag, bonus, deyli)')
        cur.execute('INSERT INTO texnical VALUES(?,?,?,?,?)',(user_nickname, user_id, user_tag, bonus, deyli))
    else:
        pass
    base.commit()
    ikbStart = InlineKeyboardMarkup(row_width=1)
    start = InlineKeyboardButton("Тгк создателя", url="https://t.me/K0tikYT")
    ikbStart.add(start)
    username = message.from_user.full_name
    await message.answer(f"Приветствую {username}\nЯ гача бот который создан, чтоб ты, лудоман, мог успокоить себя и не тратить деньги в китай казино\nЛучше задонать их мне: https://www.donationalerts.com/r/f4si", reply_markup = ikbStart)
    await message.delete()

@dp.message_handler(commands=["help"])
async def help(message : Message):
    await message.reply(f"Создатель:@ne_fek \nСписок всех команд:\n {HELP_COMMANDS}")

#Для дальнейшей обновы с дейликами, потом заебись с datetime и сделай норм начисление, а не ебись с командой в ручную, шедулер тоже нахуй, он залупа
#@dp.message_handler(commands=["deyli"])
#async def deyli(message : Message):
#    user_id = message.from_user.id
#    laste = cur.execute("SELECT deyli FROM texnical WHERE user_id = ?", (user_id,)).fetchone()
#    new_time = datetime.strptime(f"{str(laste[0])}", '%Y-%m-%d %H:%M')
#    print(laste[0])
#    print(new_time)
#    last = datetime.strptime(laste[0], '%y-%m-%d %H:%M:%S.%f')
#    await message.answer(last)

@dp.message_handler(commands=["inventory"])
async def inventory(message : Message):
    user_id = message.from_user.id
    nickname = message.from_user.first_name
    drop = ["Меч небесного всадника", "Филейный нож", "Меч путешественника", "Предвестник зари", "Холодное лезвие", "Лук ворона", "Посыльный", "Клятва стрелка", "Рогатка", "Изогнутый лук", "Чёрная кисть", "Алебарда Миллелита", "Парный нефрит", "Эпос о драконоборцах", "Руководство по магии", "Изумрудный шар", "Меч драконьей крови", "Металлическая тень", "Меч из белого железа", "Дубина переговоров", "Меч Фавония", "Меч-флейта", "Церемониальный меч", "Драконий рык", "Вспышка во тьме", "Лунное сияние ксифоса", "Бесструнный", "Церемониальный лук", "Ржавый лук", "Зелёный лук", "Боевой лук Фавония", "Охотник во тьме", "Вальс Нирваны Ночи", "Луна Моун", "Пика полумесяца", "Гроза драконов", "Каменное копьё", "Копьё Фавония", "Режущий волны плавник", "Око сознания", "Кодекс Фавония", "Морская карта", "Церемониальные мемуары", "Песнь странника", "Вино и песни", "Скитающаяся звезда", "Дождерез", "Меч-колокол", "Церемониальный двуручный меч", "Двуручный меч Фавония", "Каменный меч", "Акуомару", "Аквамарин Махайры", "Барбара", "Беннет", "Бей Доу", "Кейа", "Лиза", "Нин Гуан", "Ноэль", "Рейзор", "Сахароза", "Син Цю", "Сян Лин", "Фишль", "Чунь Юнь", "Эмбер", "Диона", "Синь Янь", "Розария", "Ян Фей", "Саю", "Сара", "Тома", "Горо", "Юнь Цзинь", "Куки Синобу", "Хэйдзо", "Коллеи", "Дори", "Кандакия", "Лайла", "Фарузан", "Яо Яо", "Мика", "Кавех", "Кирара", "Бай Чжу", "Дэхья", "Аль-Хайтам", "Странник", "Нахида", "Нилу", "Сайно", "Тигнари", "Е Лань", "Аято", "Яэ Мико", "Шень Хэ", "Итто", "Кокоми", "Райден", "Ёимия", "Аяка", "Кадзуха ", "Эола", "Ху Тао", "Сяо", "Гань Юй", "Альбедо", "Чжун Ли", "Тарталья", "Кли", "Венти", "Ци Ци", "Мона", "Ке Цин", "Дилюк", "Джинн", "Драгоценный омут", "Кромсатель пиков", "Небесный меч", "Меч сокола", "Клятва свободы", "Рассекающий туман", "Харан гэппаку фуцу", "Ключ Хадж-нисут", "Свет лиственного разреза", "Лук Амоса", "Небесное крыло", "Элегия погибели", "Громовой пульс", "Полярная звезда", "Аква симулякрум", "Охотничья тропа", "Посох Хомы", "Нефритовый коршун", "Небесная ось", "Покоритель вихря", "Сияющая жатва", "Усмиритель бед", "Посох алых песков", "Память о пыли", "Небесный атлас", "Молитва святых ветрам", "Вечное лунное сияние", "Истина кагура", "Сновидения тысячи ночей", "Воспоминания Тулайтуллы", "Великолепие лазурного свода", "Некованый", "Волчья погибель", "Небесное величие", "Песнь разбитых сосен", "Краснорогий камнеруб", "Маяк тростникового моря"]
    inven = cur.execute("SELECT Меч_небесного_всадника, Филейный_нож, Меч_путешественника, Предвестник_зари, Холодное_лезвие, Лук_ворона, Посыльный, Клятва_стрелка, Рогатка, Изогнутый_лук, Чёрная_кисть, Алебарда_Миллелита, Парный_нефрит, Эпос_о_драконоборцах, Руководство_по_магии, Изумрудный_шар, Меч_драконьей_крови, Металлическая_тень, Меч_из_белого_железа, Дубина_переговоров, Меч_Фавония, Меч_флейта, Церемониальный_меч, Драконий_рык, Вспышка_во_тьме, Лунное_сияние_ксифоса, Бесструнный, Церемониальный_лук, Ржавый_лук, Зелёный_лук, Боевой_лук_Фавония, Охотник_во_тьме, Вальс_Нирваны_Ночи, Луна_Моун, Пика_полумесяца, Гроза_драконов, Каменное_копьё, Копьё_Фавония, Режущий_волны_плавник, Око_сознания, Кодекс_Фавония, Морская_карта, Церемониальные_мемуары, Песнь_странника, Вино_и_песни, Скитающаяся_звезда, Дождерез, Меч_колокол, Церемониальный_двуручный_меч, Двуручный_меч_Фавония, Каменный_меч, Акуомару, Аквамарин_Махайры, Барбара, Беннет, Бей_Доу, Кейа, Лиза, Нин_Гуан, Ноэль, Рейзор, Сахароза, Син_Цю, Сян_Лин, Фишль, Чунь_Юнь, Эмбер, Диона, Синь_Янь, Розария, Ян_Фей, Саю, Сара, Тома, Горо, Юнь_Цзинь, Куки_Синобу, Хэйдзо, Коллеи, Дори, Кандакия, Лайла, Фарузан, Яо_Яо, Мика, Кавех, Кирара, Бай_Чжу, Дэхья, Аль_Хайтам, Странник, Нахида, Нилу, Сайно, Тигнари, Е_Лань, Аято, Яэ_Мико, Шень_Хэ, Итто, Кокоми, Райден, Ёимия, Аяка, Кадзуха, Эола, Ху_Тао, Сяо, Гань_Юй, Альбедо, Чжун_Ли, Тарталья, Кли, Венти, Ци_Ци, Мона, Ке_Цин, Дилюк, Джинн, Драгоценный_омут, Кромсатель_пиков, Небесный_меч, Меч_сокола, Клятва_свободы, Рассекающий_туман, Харан_гэппаку_фуцу, Ключ_Хадж_нисут, Свет_лиственного_разреза, Лук_Амоса, Небесное_крыло, Элегия_погибели, Громовой_пульс, Полярная_звезда, Аква_симулякрум, Охотничья_тропа, Посох_Хомы, Нефритовый_коршун, Небесная_ось, Покоритель_вихря, Сияющая_жатва, Усмиритель_бед, Посох_алых_песков, Память_о_пыли, Небесный_атлас, Молитва_святых_ветрам, Вечное_лунное_сияние, Истина_кагура, Сновидения_тысячи_ночей, Воспоминания_Тулайтуллы, Великолепие_лазурного_свода, Некованый, Волчья_погибель, Небесное_величие, Песнь_разбитых_сосен, Краснорогий_камнеруб, Маяк_тростникового_моря FROM inv WHERE user_id = ?", (user_id,)).fetchall()
    inv = inven[0]
    txt = f"{nickname}\n=-=-=Инвентарь=-=-=\n"
    x = 0
    lenivo = len(inv)
    while x < lenivo:
        if int(inv[x]) == 0:
            x = x + 1
        else:
            if x <= 20:
                txt = str(txt) + str(drop[x]) + " 3*" +  ": " + str(inv[x]) + "\n"
            elif x <= 87:
                txt = str(txt) + str(drop[x]) + " 4*" +  ": " + str(inv[x]) + "\n"
            elif x <= 156:
                txt = str(txt) + str(drop[x]) + " 5*" +  ": " + str(inv[x]) + "\n"
            x = x + 1
    await message.answer(f"{txt}")

@dp.message_handler(commands=["gacha"])
async def gacha(message : Message):
    user_id = message.from_user.id
    bonus = cur.execute("SELECT bonus FROM texnical WHERE user_id = ?", (user_id,))
    common = [1,2,3,4,6,7,8,9,11,12,13,14,16,17,18,19,21,22,23,24,26,27,28,29,31,32,33,34,36,37,38,39,41,42,43,44,46,47,48,49,51,52,53,54,56,57,58,59,61,62,63,64,66,67,68,69,71,72,73,74,76,77,78,79,81,82,83,84,86,87,87,88,89]
    commonDrop = ["Меч небесного всадника", "Филейный нож", "Меч путешественника", "Предвестник зари", "Холодное лезвие", "Лук ворона", "Посыльный", "Клятва стрелка", "Рогатка", "Изогнутый лук", "Чёрная кисть", "Алебарда Миллелита", "Парный нефрит", "Эпос о драконоборцах", "Руководство по магии", "Изумрудный шар", "Меч драконьей крови", "Металлическая тень", "Меч из белого железа", "Дубина переговоров"]
    TcommonDrop = ["Меч_небесного_всадника", "Филейный_нож", "Меч_путешественника", "Предвестник_зари", "Холодное_лезвие", "Лук_ворона", "Посыльный", "Клятва_стрелка", "Рогатка", "Изогнутый_лук", "Чёрная_кисть", "Алебарда_Миллелита", "Парный_нефрит", "Эпос_о_драконоборцах", "Руководство_по_магии", "Изумрудный_шар", "Меч_драконьей_крови", "Металлическая_тень", "Меч_из_белого_железа", "Дубина_переговоров"]
    epic = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,85]
    TepicDrop = ["Меч_Фавония", "Меч_флейта", "Церемониальный_меч", "Драконий_рык", "Вспышка_во_тьме", "Лунное_сияние_ксифоса", "Бесструнный", "Церемониальный _лук", "Ржавый_лук", "Зелёный_лук", "Боевой_лук_Фавония", "Охотник_во_тьме", "Вальс_Нирваны_Ночи", "Луна_Моун", "Пика_полумесяца", "Гроза_драконов", "Каменное_копьё", "Копьё_Фавония", "Режущий_волны_плавник", "Око_сознания", "Кодекс_Фавония", "Морская_карта", "Церемониальные_мемуары", "Песнь_странника", "Вино_и_песни", "Скитающаяся_звезда", "Дождерез", "Меч_колокол", "Церемониальный_двуручный_меч", "Двуручный_меч_Фавония", "Каменный_меч", "Акуомару", "Аквамарин_Махайры", "Барбара", "Беннет", "Бей_Доу", "Кейа", "Лиза", "Нин_Гуан", "Ноэль", "Рейзор", "Сахароза", "Син_Цю", "Сян_Лин", "Фишль", "Чунь_Юнь", "Эмбер", "Диона", "Синь_Янь", "Розария", "Ян_Фей", "Саю", "Сара", "Тома", "Горо", "Юнь_Цзинь", "Куки_Синобу", "Хэйдзо", "Коллеи", "Дори", "Кандакия", "Лайла", "Фарузан", "Яо_Яо", "Мика", "Кавех", "Кирара"]
    epicDrop = ["Меч Фавония", "Меч-флейта", "Церемониальный меч", "Драконий рык", "Вспышка во тьме", "Лунное сияние ксифоса", "Бесструнный", "Церемониальный лук", "Ржавый лук", "Зелёный лук", "Боевой лук Фавония", "Охотник во тьме", "Вальс Нирваны Ночи", "Луна Моун", "Пика полумесяца", "Гроза драконов", "Каменное копьё", "Копьё Фавония", "Режущий волны плавник", "Око сознания", "Кодекс Фавония", "Морская карта", "Церемониальные мемуары", "Песнь странника", "Вино и песни", "Скитающаяся звезда", "Дождерез", "Меч-колокол", "Церемониальный двуручный меч", "Двуручный меч Фавония", "Каменный меч", "Акуомару", "Аквамарин Махайры", "Барбара", "Беннет", "Бей Доу", "Кейа", "Лиза", "Нин Гуан", "Ноэль", "Рейзор", "Сахароза", "Син Цю", "Сян Лин", "Фишль", "Чунь Юнь", "Эмбер", "Диона", "Синь Янь", "Розария", "Ян Фей", "Саю", "Сара", "Тома", "Горо", "Юнь Цзинь", "Куки Синобу", "Хэйдзо", "Коллеи", "Дори", "Кандакия", "Лайла", "Фарузан", "Яо Яо", "Мика", "Кавех", "Кирара"]
    legendary = [90]
    legendaryDrop = ["Бай Чжу", "Дэхья", "Аль-Хайтам", "Странник", "Нахида", "Нилу", "Сайно", "Тигнари", "Е Лань", "Аято", "Яэ Мико", "Шень Хэ", "Итто", "Кокоми", "Райден", "Ёимия", "Аяка", "Кадзуха ", "Эола", "Ху Тао", "Сяо", "Гань Юй", "Альбедо", "Чжун Ли", "Тарталья", "Кли", "Венти", "Ци Ци", "Мона", "Ке Цин", "Дилюк", "Джинн", "Драгоценный омут", "Кромсатель пиков", "Небесный меч", "Меч сокола", "Клятва свободы", "Рассекающий туман", "Харан гэппаку фуцу", "Ключ Хадж-нисут", "Свет лиственного разреза", "Лук Амоса", "Небесное крыло", "Элегия погибели", "Громовой пульс", "Полярная звезда", "Аква симулякрум", "Охотничья тропа", "Посох Хомы", "Нефритовый коршун", "Небесная ось", "Покоритель вихря", "Сияющая жатва", "Усмиритель бед", "Посох алых песков", "Память о пыли", "Небесный атлас", "Молитва святых ветрам", "Вечное лунное сияние", "Истина кагура", "Сновидения тысячи ночей", "Воспоминания Тулайтуллы", "Великолепие лазурного свода", "Некованый", "Волчья погибель", "Небесное величие", "Песнь разбитых сосен", "Краснорогий камнеруб", "Маяк тростникового моря"]
    TlegendaryDrop = ["Бай_Чжу", "Дэхья", "Аль_Хайтам", "Странник", "Нахида", "Нилу", "Сайно", "Тигнари", "Е_Лань", "Аято", "Яэ_Мико", "Шень_Хэ", "Итто", "Кокоми", "Райден", "Ёимия", "Аяка", "Кадзуха ", "Эола", "Ху_Тао", "Сяо", "Гань_Юй", "Альбедо", "Чжун_Ли", "Тарталья", "Кли", "Венти", "Ци_Ци", "Мона", "Ке_Цин", "Дилюк", "Джинн", "Драгоценный_омут", "Кромсатель_пиков", "Небесный_меч", "Меч_сокола", "Клятва_свободы", "Рассекающий_туман", "Харан_гэппаку_фуцу", "Ключ_Хадж_нисут", "Свет_лиственного_разреза", "Лук_Амоса", "Небесное_крыло", "Элегия_погибели", "Громовой_пульс", "Полярная_звезда", "Аква_симулякрум", "Охотничья_тропа", "Посох_Хомы", "Нефритовый_коршун", "Небесная_ось", "Покоритель_вихря", "Сияющая_жатва", "Усмиритель_бед", "Посох_алых_песков", "Память_о_пыли", "Небесный_атлас", "Молитва_святых_ветрам", "Вечное_лунное_сияние", "Истина_кагура", "Сновидения_тысячи_ночей", "Воспоминания_Тулайтуллы", "Великолепие_лазурного_свода", "Некованый", "Волчья_погибель", "Небесное_величие", "Песнь_разбитых_сосен", "Краснорогий_камнеруб", "Маяк _тростникового_моря"]
    garant = cur.execute("SELECT garant FROM gacha WHERE user_id = ?", (user_id,)).fetchone()
    epic_garant = cur.execute("SELECT epic_garant FROM gacha WHERE user_id = ?", (user_id,)).fetchone()
    if bonus in [1,2]:
        rare = random.randint(1,90)
        if garant[0] < 90:
            if epic_garant[0] < 10:
                if rare in common:
                    leniv = len(commonDrop)
                    lenivo = leniv - 1
                    pis = random.randint(0, lenivo)
                    upGarant = garant[0] + 1
                    upEpic_garant = epic_garant[0] + 1
                    cur.execute("UPDATE gacha SET garant = ? WHERE user_id = ?", (upGarant, user_id))
                    cur.execute("UPDATE gacha SET epic_garant = ? WHERE user_id = ?", (upEpic_garant, user_id))
                    drop = commonDrop[pis]
                    TDrop = TcommonDrop[pis]
                    one = drop
                    two = cur.execute("SELECT one FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    tree = cur.execute("SELECT two FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    four = cur.execute("SELECT tree FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    five = cur.execute("SELECT four FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    six = cur.execute("SELECT five FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    seven = cur.execute("SELECT six FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    eight = cur.execute("SELECT seven FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    nine = cur.execute("SELECT eight FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    ten = cur.execute("SELECT nine FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    dropCount = cur.execute(f"SELECT {TDrop} FROM inv WHERE user_id = ?", (user_id,)).fetchone()
                    newDropCount = dropCount[0] + 1
                    cur.execute(f"UPDATE inv SET {TDrop} = ? WHERE user_id = ?", (newDropCount, user_id))
                    cur.execute("UPDATE history SET one = ? WHERE user_id = ?", (one, user_id))
                    cur.execute("UPDATE history SET two = ? WHERE user_id = ?", (two[0], user_id))
                    cur.execute("UPDATE history SET tree = ? WHERE user_id = ?", (tree[0], user_id))
                    cur.execute("UPDATE history SET four = ? WHERE user_id = ?", (four[0], user_id))
                    cur.execute("UPDATE history SET five = ? WHERE user_id = ?", (five[0], user_id))
                    cur.execute("UPDATE history SET six = ? WHERE user_id = ?", (six[0], user_id))
                    cur.execute("UPDATE history SET seven = ? WHERE user_id = ?", (seven[0], user_id))
                    cur.execute("UPDATE history SET eight = ? WHERE user_id = ?", (eight[0], user_id))
                    cur.execute("UPDATE history SET nine = ? WHERE user_id = ?", (nine[0], user_id))
                    cur.execute("UPDATE history SET ten = ? WHERE user_id = ?", (ten[0], user_id))
                    await message.answer(f"Вам выпал \"{drop}\"")
                if rare in epic:
                    leniv = len(epicDrop)
                    lenivo = leniv - 1
                    pis = random.randint(0, lenivo)
                    print(lenivo)
                    drop = epicDrop[pis]
                    TDrop = TepicDrop[pis]
                    one = drop
                    two = cur.execute("SELECT one FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    tree = cur.execute("SELECT two FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    four = cur.execute("SELECT tree FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    five = cur.execute("SELECT four FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    six = cur.execute("SELECT five FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    seven = cur.execute("SELECT six FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    eight = cur.execute("SELECT seven FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    nine = cur.execute("SELECT eight FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    ten = cur.execute("SELECT nine FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    dropCount = cur.execute(f"SELECT {TDrop} FROM inv WHERE user_id = ?", (user_id,)).fetchone()
                    newDropCount = dropCount[0] + 1
                    cur.execute(f"UPDATE inv SET {TDrop} = ? WHERE user_id = ?", (newDropCount, user_id))
                    cur.execute("UPDATE history SET one = ? WHERE user_id = ?", (one, user_id))
                    cur.execute("UPDATE history SET two = ? WHERE user_id = ?", (two[0], user_id))
                    cur.execute("UPDATE history SET tree = ? WHERE user_id = ?", (tree[0], user_id))
                    cur.execute("UPDATE history SET four = ? WHERE user_id = ?", (four[0], user_id))
                    cur.execute("UPDATE history SET five = ? WHERE user_id = ?", (five[0], user_id))
                    cur.execute("UPDATE history SET six = ? WHERE user_id = ?", (six[0], user_id))
                    cur.execute("UPDATE history SET seven = ? WHERE user_id = ?", (seven[0], user_id))
                    cur.execute("UPDATE history SET eight = ? WHERE user_id = ?", (eight[0], user_id))
                    cur.execute("UPDATE history SET nine = ? WHERE user_id = ?", (nine[0], user_id))
                    cur.execute("UPDATE history SET ten = ? WHERE user_id = ?", (ten[0], user_id))
                    upGarant = garant[0] + 1
                    upEpic_garant = epic_garant[0] - epic_garant[0]
                    cur.execute("UPDATE gacha SET garant = ? WHERE user_id = ?", (upGarant, user_id))
                    cur.execute("UPDATE gacha SET epic_garant = ? WHERE user_id = ?", (upEpic_garant, user_id))
                    await message.answer(f"Вам вапал \"{drop}\"")
                if rare in legendary:
                    leniv = len(legendaryDrop)
                    lenivo = leniv - 1
                    pis = random.randint(0, lenivo)
                    drop = legendaryDrop[pis]
                    TDrop = TlegendaryDrop[pis]
                    one = TDrop
                    two = cur.execute("SELECT one FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    tree = cur.execute("SELECT two FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    four = cur.execute("SELECT tree FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    five = cur.execute("SELECT four FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    six = cur.execute("SELECT five FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    seven = cur.execute("SELECT six FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    eight = cur.execute("SELECT seven FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    nine = cur.execute("SELECT eight FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    ten = cur.execute("SELECT nine FROM history WHERE user_id = ?", (user_id,)).fetchone()
                    dropCount = cur.execute(f"SELECT {drop} FROM inv WHERE user_id = ?", (user_id,)).fetchone()
                    newDropCount = dropCount[0] + 1
                    cur.execute(f"UPDATE inv SET {TDrop} = ? WHERE user_id = ?", (newDropCount, user_id))
                    cur.execute("UPDATE history SET one = ? WHERE user_id = ?", (one, user_id))
                    cur.execute("UPDATE history SET two = ? WHERE user_id = ?", (two[0], user_id))
                    cur.execute("UPDATE history SET tree = ? WHERE user_id = ?", (tree[0], user_id))
                    cur.execute("UPDATE history SET four = ? WHERE user_id = ?", (four[0], user_id))
                    cur.execute("UPDATE history SET five = ? WHERE user_id = ?", (five[0], user_id))
                    cur.execute("UPDATE history SET six = ? WHERE user_id = ?", (six[0], user_id))
                    cur.execute("UPDATE history SET seven = ? WHERE user_id = ?", (seven[0], user_id))
                    cur.execute("UPDATE history SET eight = ? WHERE user_id = ?", (eight[0], user_id))
                    cur.execute("UPDATE history SET nine = ? WHERE user_id = ?", (nine[0], user_id))
                    cur.execute("UPDATE history SET ten = ? WHERE user_id = ?", (ten[0], user_id))
                    upGarant = garant[0] - garant[0]
                    upEpic_garant = epic_garant[0] + 1
                    cur.execute("UPDATE gacha SET garant = ? WHERE user_id = ?", (upGarant, user_id))
                    cur.execute("UPDATE gacha SET epic_garant = ? WHERE user_id = ?", (upEpic_garant, user_id))
                    await message.answer(f"Вам вапал \"{drop}\"")
            elif epic_garant[0] == 10:
                leniv = len(epicDrop)
                lenivo = leniv - 1
                pis = random.randint(0, lenivo)
                drop = epicDrop[pis]
                TDrop = TepicDrop[pis]
                one = drop
                two = cur.execute("SELECT one FROM history WHERE user_id = ?", (user_id,)).fetchone()
                tree = cur.execute("SELECT two FROM history WHERE user_id = ?", (user_id,)).fetchone()
                four = cur.execute("SELECT tree FROM history WHERE user_id = ?", (user_id,)).fetchone()
                five = cur.execute("SELECT four FROM history WHERE user_id = ?", (user_id,)).fetchone()
                six = cur.execute("SELECT five FROM history WHERE user_id = ?", (user_id,)).fetchone()
                seven = cur.execute("SELECT six FROM history WHERE user_id = ?", (user_id,)).fetchone()
                eight = cur.execute("SELECT seven FROM history WHERE user_id = ?", (user_id,)).fetchone()
                nine = cur.execute("SELECT eight FROM history WHERE user_id = ?", (user_id,)).fetchone()
                ten = cur.execute("SELECT nine FROM history WHERE user_id = ?", (user_id,)).fetchone()
                dropCount = cur.execute(f"SELECT {drop} FROM inv WHERE user_id = ?", (user_id,)).fetchone()
                newDropCount = dropCount[0] + 1
                cur.execute(f"UPDATE inv SET {TDrop} = ? WHERE user_id = ?", (newDropCount, user_id))
                cur.execute("UPDATE history SET one = ? WHERE user_id = ?", (one, user_id))
                cur.execute("UPDATE history SET two = ? WHERE user_id = ?", (two[0], user_id))
                cur.execute("UPDATE history SET tree = ? WHERE user_id = ?", (tree[0], user_id))
                cur.execute("UPDATE history SET four = ? WHERE user_id = ?", (four[0], user_id))
                cur.execute("UPDATE history SET five = ? WHERE user_id = ?", (five[0], user_id))
                cur.execute("UPDATE history SET six = ? WHERE user_id = ?", (six[0], user_id))
                cur.execute("UPDATE history SET seven = ? WHERE user_id = ?", (seven[0], user_id))
                cur.execute("UPDATE history SET eight = ? WHERE user_id = ?", (eight[0], user_id))
                cur.execute("UPDATE history SET nine = ? WHERE user_id = ?", (nine[0], user_id))
                cur.execute("UPDATE history SET ten = ? WHERE user_id = ?", (ten[0], user_id))
                upGarant = garant[0] + 1
                upEpic_garant = epic_garant[0] - epic_garant[0]
                cur.execute("UPDATE gacha SET garant = ? WHERE user_id = ?", (upGarant, user_id))
                cur.execute("UPDATE gacha SET epic_garant = ? WHERE user_id = ?", (upEpic_garant, user_id))
                await message.answer(f"Вам вапал \"{drop}\"")
        elif garant[0] == 90:
            leniv = len(legendaryDrop)
            lenivo = leniv - 1
            pis = random.randint(0, lenivo)
            drop = legendaryDrop[pis]
            TDrop = TlegendaryDrop[pis]
            one = drop
            two = cur.execute("SELECT one FROM history WHERE user_id = ?", (user_id,)).fetchone()
            tree = cur.execute("SELECT two FROM history WHERE user_id = ?", (user_id,)).fetchone()
            four = cur.execute("SELECT tree FROM history WHERE user_id = ?", (user_id,)).fetchone()
            five = cur.execute("SELECT four FROM history WHERE user_id = ?", (user_id,)).fetchone()
            six = cur.execute("SELECT five FROM history WHERE user_id = ?", (user_id,)).fetchone()
            seven = cur.execute("SELECT six FROM history WHERE user_id = ?", (user_id,)).fetchone()
            eight = cur.execute("SELECT seven FROM history WHERE user_id = ?", (user_id,)).fetchone()
            nine = cur.execute("SELECT eight FROM history WHERE user_id = ?", (user_id,)).fetchone()
            ten = cur.execute("SELECT nine FROM history WHERE user_id = ?", (user_id,)).fetchone()
            dropCount = cur.execute(f"SELECT {drop} FROM inv WHERE user_id = ?", (user_id,)).fetchone()
            newDropCount = dropCount[0] + 1
            cur.execute(f"UPDATE inv SET {TDrop} = ? WHERE user_id = ?", (newDropCount, user_id))
            cur.execute("UPDATE history SET one = ? WHERE user_id = ?", (one, user_id))
            cur.execute("UPDATE history SET two = ? WHERE user_id = ?", (two[0], user_id))
            cur.execute("UPDATE history SET tree = ? WHERE user_id = ?", (tree[0], user_id))
            cur.execute("UPDATE history SET four = ? WHERE user_id = ?", (four[0], user_id))
            cur.execute("UPDATE history SET five = ? WHERE user_id = ?", (five[0], user_id))
            cur.execute("UPDATE history SET six = ? WHERE user_id = ?", (six[0], user_id))
            cur.execute("UPDATE history SET seven = ? WHERE user_id = ?", (seven[0], user_id))
            cur.execute("UPDATE history SET eight = ? WHERE user_id = ?", (eight[0], user_id))
            cur.execute("UPDATE history SET nine = ? WHERE user_id = ?", (nine[0], user_id))
            cur.execute("UPDATE history SET ten = ? WHERE user_id = ?", (ten[0], user_id))
            upGarant = garant[0] - garant[0]
            upEpic_garant = epic_garant[0] + 1
            cur.execute("UPDATE gacha SET garant = ? WHERE user_id = ?", (upGarant, user_id))
            cur.execute("UPDATE gacha SET epic_garant = ? WHERE user_id = ?", (upEpic_garant, user_id))
            await message.answer(f"Вам выпал \"{drop}\"")
        newBonus = bonus - 1
        cur.execute("UPDATE texnical SET bonus = ? WHERE user_id = ?", (newBonus, user_id))
    else:
        await message.answer("Сегодня вы потратили все свои крутки")
    base.commit()

@dp.message_handler(commands=["history"])
async def history(message : Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    garant = cur.execute("SELECT garant FROM gacha WHERE user_id = ?", (user_id,)).fetchone()
    one = cur.execute("SELECT one FROM history WHERE user_id = ?", (user_id,)).fetchone()
    two = cur.execute("SELECT two FROM history WHERE user_id = ?", (user_id,)).fetchone()
    tree = cur.execute("SELECT tree FROM history WHERE user_id = ?", (user_id,)).fetchone()
    four = cur.execute("SELECT four FROM history WHERE user_id = ?", (user_id,)).fetchone()
    five = cur.execute("SELECT five FROM history WHERE user_id = ?", (user_id,)).fetchone()
    six = cur.execute("SELECT six FROM history WHERE user_id = ?", (user_id,)).fetchone()
    seven = cur.execute("SELECT seven FROM history WHERE user_id = ?", (user_id,)).fetchone()
    eight = cur.execute("SELECT eight FROM history WHERE user_id = ?", (user_id,)).fetchone()
    nine = cur.execute("SELECT nine FROM history WHERE user_id = ?", (user_id,)).fetchone()
    ten = cur.execute("SELECT ten FROM history WHERE user_id = ?", (user_id,)).fetchone()
    await message.answer(f"""История {user_name}
<u><b>Отображаются только последние 10 круток</b></u>
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Откручено {garant[0]}
1){one[0]}
2){two[0]}
3){tree[0]}
4){four[0]}
5){five[0]}
6){six[0]}
7){seven[0]}
8){eight[0]}
9){nine[0]}
10){ten[0]}
""", parse_mode = "HTML")

#/blyatfixgovna
@dp.message_handler(commands=["blyatfixgovna"])
async def blyatfixgovna(message : Message):
    user_id = message.from_user.id
    if user_id in admList:
        cur.execute("UPDATE texnical SET bonus = 2")
        base.commit()
        print("Бонус обновлён")
    else:
        await message.answer("Пошёл нахуй хитрец ебани")
        await message.delete()

@dp.message_handler()
async def midlvar(message : Message):
    user_nickname = message.from_user.full_name
    user_id = message.from_user.id
    user_tag = message.from_user.username
    one = "###"
    two = "###"
    tree = "###"
    four = "###"
    five = "###"
    six = "###"
    seven = "###"
    eight = "###"
    nine = "###"
    ten = "###"
    garant = 0
    epic_garant = 0
    cash = 100
    primogems = 150
    bonus = 1
    deyli = datetime.now()
    deyli.strftime("%Y-%m-%d %H:%M")
    pisa = 0
    cur.execute("SELECT user_id FROM gachaProfile WHERE user_id = ?", (user_id,))
    if cur.fetchone() is None:
        base.execute('CREATE TABLE IF NOT EXISTS gachaProfile(user_nickname, user_id, user_tag, cash, primogems)')
        cur.execute('INSERT INTO gachaProfile VALUES(?,?,?,?,?)',(user_nickname, user_id, user_tag, cash, primogems))
    else:
        pass
    cur.execute("SELECT user_id FROM inv WHERE user_id = ?", (user_id,))
    if cur.fetchone() is None:
        base.execute("CREATE TABLE IF NOT EXISTS inv(user_nickname, user_id, Меч_небесного_всадника, Филейный_нож, Меч_путешественника, Предвестник_зари, Холодное_лезвие, Лук_ворона, Посыльный, Клятва_стрелка, Рогатка, Изогнутый_лук, Чёрная_кисть, Алебарда_Миллелита, Парный_нефрит, Эпос_о_драконоборцах, Руководство_по_магии, Изумрудный_шар, Меч_драконьей_крови, Металлическая_тень, Меч_из_белого_железа, Дубина_переговоров, Меч_Фавония, Меч_флейта, Церемониальный_меч, Драконий_рык, Вспышка_во_тьме, Лунное_сияние_ксифоса, Бесструнный, Церемониальный_лук, Ржавый_лук, Зелёный_лук, Боевой_лук_Фавония, Охотник_во_тьме, Вальс_Нирваны_Ночи, Луна_Моун, Пика_полумесяца, Гроза_драконов, Каменное_копьё, Копьё_Фавония, Режущий_волны_плавник, Око_сознания, Кодекс_Фавония, Морская_карта, Церемониальные_мемуары, Песнь_странника, Вино_и_песни, Скитающаяся_звезда, Дождерез, Меч_колокол, Церемониальный_двуручный_меч, Двуручный_меч_Фавония, Каменный_меч, Акуомару, Аквамарин_Махайры, Барбара, Беннет, Бей_Доу, Кейа, Лиза, Нин_Гуан, Ноэль, Рейзор, Сахароза, Син_Цю, Сян_Лин, Фишль, Чунь_Юнь, Эмбер, Диона, Синь_Янь, Розария, Ян_Фей, Саю, Сара, Тома, Горо, Юнь_Цзинь, Куки_Синобу, Хэйдзо, Коллеи, Дори, Кандакия, Лайла, Фарузан, Яо_Яо, Мика, Кавех, Кирара, Бай_Чжу, Дэхья, Аль_Хайтам, Странник, Нахида, Нилу, Сайно, Тигнари, Е_Лань, Аято, Яэ_Мико, Шень_Хэ, Итто, Кокоми, Райден, Ёимия, Аяка, Кадзуха, Эола, Ху_Тао, Сяо, Гань_Юй, Альбедо, Чжун_Ли, Тарталья, Кли, Венти, Ци_Ци, Мона, Ке_Цин, Дилюк, Джинн, Драгоценный_омут, Кромсатель_пиков, Небесный_меч, Меч_сокола, Клятва_свободы, Рассекающий_туман, Харан_гэппаку_фуцу, Ключ_Хадж_нисут, Свет_лиственного_разреза, Лук_Амоса, Небесное_крыло, Элегия_погибели, Громовой_пульс, Полярная_звезда, Аква_симулякрум, Охотничья_тропа, Посох_Хомы, Нефритовый_коршун, Небесная_ось, Покоритель_вихря, Сияющая_жатва, Усмиритель_бед, Посох_алых_песков, Память_о_пыли, Небесный_атлас, Молитва_святых_ветрам, Вечное_лунное_сияние, Истина_кагура, Сновидения_тысячи_ночей, Воспоминания_Тулайтуллы, Великолепие_лазурного_свода, Некованый, Волчья_погибель, Небесное_величие, Песнь_разбитых_сосен, Краснорогий_камнеруб, Маяк_тростникового_моря)")
        cur.execute("INSERT INTO inv VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (user_nickname, user_id, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa, pisa , pisa , pisa, pisa, pisa, pisa, pisa, pisa, pisa , pisa))
    else:
        pass
    cur.execute("SELECT user_id FROM history WHERE user_id = ?", (user_id,))
    if cur.fetchone() is None:
        base.execute("CREATE TABLE IF NOT EXISTS history(user_nickname, user_id, one, two, tree, four, five, six, seven, eight, nine, ten)")
        cur.execute("INSERT INTO history VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", (user_nickname, user_id, one, two, tree, four, five, six, seven, eight, nine, ten))
    else:
        pass
    cur.execute("SELECT user_id FROM gacha WHERE user_id = ?", (user_id,))
    if cur.fetchone() is None:
        base.execute("CREATE TABLE IF NOT EXISTS gacha(user_nickname, user_id, epic_garant, garant)")
        cur.execute("INSERT INTO gacha VALUES(?,?,?,?)", (user_nickname, user_id, epic_garant, garant))
    else:
        pass
    cur.execute("SELECT user_id FROM gacha WHERE user_id = ?", (user_id,))
    if cur.fetchone() is None:
        base.execute('CREATE TABLE IF NOT EXISTS texnical(user_nickname, user_id, user_tag, bonus, deyli)')
        cur.execute('INSERT INTO texnical VALUES(?,?,?,?,?)',(user_nickname, user_id, user_tag, bonus, deyli))
    else:
        pass
    base.commit()

#полинг
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = False)