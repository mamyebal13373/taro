# -*- coding: utf-8 -*-
import telebot
from telebot import types
import os
import sys
import re
import configparser
from random import randrange

import random
bot = telebot.TeleBot("946527759:AAEIpJXhf_wAlgxDSEQGSupBUIEpNr2B-m0")

# config_path = os.path.join(sys.path[0], 'settings.ini')
# config = configparser.ConfigParser()
# config.read(config_path)
# text1 = config.get('name', 'text1')
# text2 =config.get('name', 'text2')



user_dict = {}

class User:
    def __init__(self, name):
        self.name = name



@bot.message_handler(func=lambda m: m.text in ('start', '/start', '/Start'))
def handle_start(message):

    keyboard = types.InlineKeyboardMarkup(row_width=3)

    callback_button1 = types.InlineKeyboardButton(text="🃏 ",
                                                 callback_data="cry")
    callback_button2 = types.InlineKeyboardButton(text="🃏",
                                                  callback_data="cry")
    callback_button3 = types.InlineKeyboardButton(text="🃏 ",
                                                 callback_data="cry")
    callback_button4 = types.InlineKeyboardButton(text="🃏 ",
                                                 callback_data="cry")
    callback_button5 = types.InlineKeyboardButton(text="🃏 ",
                                                 callback_data="cry")
    callback_button6 = types.InlineKeyboardButton(text="🃏 ",
                                                 callback_data="cry")
    callback_button7 = types.InlineKeyboardButton(text="🃏 ",
                                                 callback_data="cry")
    callback_button8 = types.InlineKeyboardButton(text="🃏 ",
                                                 callback_data="cry")
    callback_button9 = types.InlineKeyboardButton(text="🃏 ",
                                                 callback_data="cry")
    callback_button10 = types.InlineKeyboardButton(text="🃏 ",
                                                  callback_data="cry")
    callback_button11 = types.InlineKeyboardButton(text="🃏 ",
                                                  callback_data="cry")
    callback_button12 = types.InlineKeyboardButton(text="🃏 ",
                                                  callback_data="cry")
    callback_button13 = types.InlineKeyboardButton(text="🃏",
                                                   callback_data="cry")
    callback_button14 = types.InlineKeyboardButton(text="🃏",
                                                   callback_data="cry")
    callback_button15 = types.InlineKeyboardButton(text="🃏 ",
                                                   callback_data="cry")
    keyboard.add(callback_button1, callback_button2, callback_button3,
                 callback_button4,callback_button5,callback_button6,
                 callback_button7,callback_button8,callback_button9,
                 callback_button10,callback_button11,callback_button12,
                 callback_button13,callback_button14,callback_button15)
    bot.send_photo(message.from_user.id, open('/qwe/start.jpg', 'rb'), parse_mode="Markdown",reply_markup=keyboard, caption='Каждый день мы '
                                                                                                                             'задаемся '
                                                                                                                          'вопросом, что нас ждет в этот день, пытаемся понять какие перспективы нас ждут, какие решения нужно принять и соответственно сделать свой выбор. Мы надеемся и стремимся сделать наиболее правильный выбор, избежать ошибки. Расклад Карта дня таро позволяет взглянуть на ситуацию под другим углом, разобраться в том, что мы ощущаем интуицией, но до конца понять не можем. по одной карте можно определить ход событий на протяжении дня. Перед тем, как вытащить карту, подумайте — «каким будет мой день»"')
    # bot.send_message(message.chat.id, " Каждый день мы задаемся вопросом, что нас ждет в этот день, пытаемся понять какие перспективы нас ждут, какие решения нужно принять и соответственно сделать свой выбор. Мы надеемся и стремимся сделать наиболее правильный выбор, избежать ошибки. Расклад Карта дня таро позволяет взглянуть на ситуацию под другим углом, разобраться в том, что мы ощущаем интуицией, но до конца понять не можем. по одной карте можно определить ход событий на протяжении дня. Перед тем, как вытащить карту, подумайте — «каким будет мой день»"
    #                                 ,parse_mode="Markdown",reply_markup=keyboard)

@bot.callback_query_handler(func=lambda message: True)
def callback_inline1(message):
    # global text1
    # global text2

    if message.data == "cry":
        message.data = random.randint(0,21)
        text = '*ВАША КАРТА ДНЯ : ШУТ О *' \
               '\n \n ✔  Если сегодня нужно начать какое-то дело с нуля ― делайте это.  ' \
               '\n \n ❗  Проявите любопытство и творческий энтузиазм. Сегодня вы открыты всему новому. Не принимайте ничего близко к сердцу и ' \
               'относитесь ко всему происходящему с одним лишь любопытством. ' \
               '\n\n ⚠  Предупреждение: Сегодня могут подставить в делах ― будьте внимательны в подписании договоров и контрактов. ' \
               '\n\n ⚠  Воздержитесь от планирования крупных дел, покупок. ' \
               '\n\n ⚠  Не торопитесь реализовывать задуманное. ' \
               '\n\n ✅  Совет: *Сегодня,прежде чем действовать, тщательно обдумайте каждый шаг и его последствия. * '
        text1 = '*ВАША КАРТА ДНЯ: МАГ I*\
\n\n ✔️  День инициативы и ответственности. Сегодня вам потребуется решительность и уверенность в себе.\
\n\n ❗️  Действуйте свободно и смело во всех делах и начинаниях, и в дружбе, и в семье. Сегодня вы можете использовать все доступные средства для ' \
                'достижения цели. Трудности могут возникнуть там, где вы не ожидаете.\
\n\n ⚠️  Возможно, вам придется менять свои планы «на ходу» и сохранять спокойствие, так как сегодня вам будет сложно,но все -таки все решается.\
\n\n ⚠️  В делах подьем творческих сил, возможность найти новую работу, рассчитаться с долгами.\
\n\n ♻️  В здоровье может быть улучшение.\
\n\n ⚠️  Предупреждение ^ Не упустите свой шанс.\
\n\n ✅  Совет: *Не отказывайтесь от начатого,и делайте все по своему.*'
        text2 = '*ВАША КАРТА ДНЯ: Императрица III *\
\n\n ✔️  День обещает быть интересным. То, чего вы желаете, сегодня имеет возможность воплотиться в жизнь. Ваши начинания сегодня успешны.\
\n \n ♻️  Бизнес сегодня будет так же успешен, выбрать наиболее прибыльное вложение не составит особого труда, но этот выбор должен быть ' \
                'единоличным и хорошо обдуманным планом долгосрочного продвижения.\
\n \n ♻️  Влюбленные в гармонии и единении. Дружеские отношения, начатые сегодня, могут оказаться «дружбой на всю жизнь».\
\n\n♻️  В семье присутствует взаимопонимание.\
\n\n⚠️  Здоровье сегодня в норме, но не занимайтесь многими делами сразу, дабы не почувствовать упадок сил.\
\n\n⚠️  Предостережение: Избегайте излишеств, но в то же время не упускайте шансов.\
\n\n ✅  Совет: *Используйте свою привлекательность, не забывайте, что чем больше человек хочет добиться чего-либо, тем больше он должен ' \
                'соответствовать этому.*'
        text3 = '*ВАША КАРТА ДНЯ: Верховная жрица II*\
\n\n ✔  Наблюдение и спокойствие.\
\n\n✔  Дайте происходящему идти своим ходом. Сны, которые вы видели накануне этого дня, могут нести важную информацию.\
\n\n♻️  Следуйте своим внутренним побуждениям.\
\n\n♻️  Сегодня можно получить ответы на давно волнующие вопросы, принять некоторые окончательные решения, но не торопясь. Серьезность,интуиция, ' \
                'логика – все это позволит избежать вам ошибок, так как будет не просто справиться с негативными эмоциями.\
\n\n♻️  Не стоит сегодня брать на себя обязательства и верить обещаниям,так как сегодня есть вероятность переоценивания своих и чужих возможностей.\
\n\n⚠️  Предупреждение: Не плывите по течению.\
\n\n✅  Совет: *Доверяйте своему внутреннему голосу, следуйте за интуицией.*\
\n\n✅  Самые первые мысли и есть верные.\
\n\n❗️  Прежде, чем что-то делать, соберите информацию, присмотритесь, не торопитесь.'
        text4 = '*ВАША КАРТА ДНЯ: Имперaтор IV*\
\n\n✔️  День подходит для решения нестандартных задач, сила и энергия, удача и успех.\
\n\n✔️  Сегодня вы, наконец, можете доделать все старые дела, исправить свои ошибки и выполнить обещания.\
\n\n⚠️  Сегодня надо взяться за дело основательно. Но абсолютно все зависит от вашей подвижности и умения убеждать других.\
\n\n❗️  Эмоциональный фон сегодня сложный.\
\n\n❗️  Сегодняшние вложения должны принести прибыль, но, все шаги должны быть заранее обдуманы и просчитаны, а все необходимые документы должны ' \
                'быть внимательно прочитаны.\
\n\n♻️   День приятного общения с лицами противоположного пола, оказание помощи и решения проблем.\
\n\n⚠️  Предупреждение: На чутье полагаться не стоит, делайте расчеты.\
\n\n❗️  Не нарушайте «границы» другого человека.\
\n\n✅  Совет: *Осуществляйте свои планы твердо и последовательно, доводите дело до конца.*'
        text5 = '*ВАША КАРТА ДНЯ:  Верховный жрец V*\
\n\n✔️ Сегодня все дела требуют мудрого управления и контроля.\
Сегодня в бизнесе все решают деньги,ведите дела с проверенными партнерами, избегайте конфликтов, нельзя пускать все на самотек.\
\n\n♻️  Сегодня как никогда необходим совет и консультация соответствующего специалиста и именно сегодня вы сможете получить мудрый и нужный совет.\
\n\n♻️  В отношениях сегодня у многих могут наметиться благоприятные изменения . Может быть принято решение узаконить отношения, ' \
                'объявить о помолвке, а кто-то получит предложение брака.\
\n\n✔️  Сегодня каждый может рассчитывать на поддержку друзей.\
\n\n⚠️  Если вчера вы были здоровы, а сегодня заболели или хотя бы захандрили, значит, ваше состояние спровоцировано внутренними противоречиями.\
\n\n⚠️  Предупреждение: Принимать решение только после логического размышления\
\n\n✅  Совет: *Во всем ищите смысл, и посвящайте себя лишь осмысленному труду. Желательны консультации у соответствующих специалистов.*'
        text6 = '*ВАША КАРТА ДНЯ:  Влюбленные VI*\
\n\n✔️  День выбора между 2-я вариантами решений, действий.\
\n\n✔️  Это самое время для того, чтобы решить многие вопросы, беспокоящие вас в последнее время. Прислушайтесь к себе — внутри скрыты все ответы ' \
                'на вопросы.\
\n\n♻️  Сегодняшний день может обеспечить успех, если вы сегодня заключите новое сотрудничество или укрепите старое, окажете поддержку.\
\n\n❗️  Но сегодняшний день даст также нерешительность во многих вопросах: -какого партнера предпочти? -с кем строить отношения? – на какую работу ' \
                'устроиться? -какой вариант лечения выбрать?\
\n\n❗️  И все же это день правильного выбора с долгосрочными отношениями, и это касается всех сфер жизни: бизнеса, любви, дружбы. Но ваши намерения должны быть серьезными.\
\n\n⚠️  Предупреждение: Ваша нерешительность приведет к задержке в делах.\
\n\n✅  Совет: *Старайтесь не попасть в зависимость от обстоятельств. Взвешивайте все «за « и « против». Не тормозить!*'
        text7 = '*ВАША КАРТА ДНЯ:  Колесница VII*\
\n\n✔️  День решительного настроя и действия для начала любых дел . Действуйте, и вы придете к хорошему, эффектному результату.\
\n\n✔️  Сегодня ваши эмоции и разум должны быть 50/50 для четкого выбора и выполнения задуманного.\
\n\n❗️  В тоже время, сегодня не лучшее время для перемирия и развития отношений из-за напряженных вибраций дня.\
\n\n❗️  С людьми отношения могут быть напряженными. Отложите решение личных вопросов до лучших времен.\
\n\n⚠️  Предупреждение: Если у тебя есть дело, берись за него, не откладывая и не раздумывая.Не сворачивайте от намеченной цели.\
\n\n✅  Совет: *Постарайтесь избавиться от условностей (это можно -это нельзя)*'
        text8 = '*ВАША КАРТА ДНЯ:  Сила *\
\n\n✔️  Сегодняшний день дает вам силы для использования их в своих интересах.\
\n\n♻️  День обещает быть насыщенным на чувства и события.\
\n\n♻️  Используйте энергию дня себе во благо, направив ее на свою работу или на преодоление препятствий.\
\n\n♻️  День максимальной производительности. Вы полны сил и энергии, ваша душа требует действия, поэтому не удивляйтесь, если кто-то или что-то ' \
                'страстно увлечет вас.\
\n\n♻️  Сегодня у вас хватит сил, чтобы преодолеть любые препятствия и заручиться поддержкой других, отказаться от прошлых тянущих связей, ' \
                'привлечь сильных партнеров и покровителей на свою сторону.\
\n\n⚠️  Предупреждение: Не переоценивайте свои силы, но ни на кого не перекладывайте свои обязанности.\
\n\n✅  Совет: *Постарайтесь вовремя оказаться в нужном месте.*'
        text9 = '*ВАША КАРТА ДНЯ:  Отшельник IX*\
\n\n♻️  День уединения, созерцательности.\
\n\n♻️  Вам необходим отдых, так что это время лучше уделить заботе о себе. Займитесь делами, не требующими активности.\
\n\n❗️  Займитесь собой, абстрагировавшись от суеты внешнего мира.\
\n\n❗️  Если же в этот день вы должны выполнить какое-то дело, то делайте не торопясь и не отвлекаясь.\
\n\n❗️  День хорош для людей логичных и расчётливых, а эмоциональных людей может подвести их невнимательность и они могут быть подвержены риску ' \
                'быть обманутыми или стать жертвами мошенников.\
\n\n✔️  Хороший день для начала каких либо оздоровительных мероприятий.\
\n\n⚠️  Предупреждение: Не изолировать себя от внешнего мира, не озлобляться, не суетиться.\
\n\n✅  Совет: *Оставаться самим собой, не торопить события.*'
        text10 = '*ВАША КАРТА ДНЯ:  Колесо фортуны X*\
\n\n✔️  День случайностей и «воли случая». Кому-то повезет, а от кого-то удача отвернется.\
\n\n⚠️  Для финансовых дел день не слишком хорош, так как все может перевернуться.\
\n\n❗️  У кого дела шли удачно, могут вдруг потерпеть крах, а чей бизнес тонул, наоборот начнут сегодня всплывать, или заложат фундамент для новых ' \
                 'дел. Поэтому серьезных планов лучше не намечать на сегодня и быть очень внимательными.\
\n\n♻️   Во всех сферах день сегодня достаточно спокойный и рутинный, но не лишенный каких-то странностей, из-за которых придется менять планы.\
\n\n♻️   Для взаимоотношений день вполне благоприятен при любом развитии событий – будь то разрыв отношений или новая встреча, начало.\
\n\n♻️   Дружеские отношения сегодня укрепляются, а требовательность друг к другу не вызывает недовольства.\
\n\n⚠️  Предупреждение: Непостоянство в делах\
\n\n✅  Совет:* Лови момент в любом деле.*'
        text11 = '*ВАША КАРТА ДНЯ: Справедливость *\
\n\n❗️  Период эмоционального равновесия.\
\n\n❗️  День переоценки событий, фактов, решений.\
\n\n❗️  Возможны контакты с судебными, правоохранительными органами.\
\n\n⚠️  Возможно, сегодня вы ощутите последствия действий, совершенных прежде. В зависимости от того, как вы повели себя тогда, вам станет легко ' \
                 'или наоборот..\
\n\n♻️  Сегодня важно сохранить рациональность — так как предстоит принять важное решение.\
\n\n✔️  С партнерами по бизнесу возможны прекращения невыгодных дел .\
\n\n✔️  Во взаимоотношениях спокойное выяснение отношений. С друзьями возможна переоценка важности контакта.\
\n\n⚠️  Предупреждение: Сохраняйте ясность мысли\
\n\n✅   Совет: *Рассчитаться по всем долгам.*'
        text12 = '*ВАША КАРТА ДНЯ: Повешенный XII*\
\n\n✔️  День зависимостей от чего-то, от кого-то и вряд ли можно что-то сейчас изменить.\
\n\n❗️  Не пытайтесь насильно изменить положение вещей — достаточно пересмотреть свою позицию и сделать выводы.\
\n\n❗️  Сегодняшний день преподаст вам урок терпения. Либо что-то затянется еще больше, либо наступит задержка в каком-то деле, от которого вы ' \
                 'этого никак не ожидали.\
\n\n♻️  В этот день возможны разногласиями между людьми, которые до сих пор поддерживали друг друга везде.\
\n\n❗️  Люди будут говорить о разных вещах, и недопонимания могут возникнуть фактически на пустом месте. Желание настоять на своем сегодня слишком ' \
                 'велико, поэтому компромисса в этот день достичь не удастся.\
\n\n⚠️  Здоровье – переутомление и недомогание, возможно обострение хронических заболеваний, вызванное стрессовыми ситуациями.\
\n\n⚠️  Предостережение: Не цепляйтесь за старое, не пытайтесь ускорить ход событий.\
\n\n✅  Совет : *Не суетитесь, не старайтесь разорвать именно сейчас все и с людьми и с делами.*'
        text13 = '*ВАША КАРТА ДНЯ: Смерть XIII*\
\n\n✔️  День трудных перемен и неожиданных завершений. Но не физическая смерть!\
\n\n❗️  Сложный и неоднозначный день. И партнеры и друзья могут видеть конфликтные моменты во всем и желать завершить конкретные дела или ситуации, считая это точкой конфликта.\
\n\n✔️  Для вас может что-то закончится. Будьте готовы отпустить это без сожаления, и даже если это будет болезненно, в конце концов, ' \
                 'вас ждет облегчение и освобождение. А возможно, вы будете рады, что «это» наконец завершилось.\
\n\n⚠️  Даже хладнокровные люди сегодня могут терять терпение, и чтобы день сложился удачно, примите позицию философского отношения к жизни. Все ' \
                 'ненужное завершится само собой.\
\n\n⚠️  Предупреждение: Не совершайте шагов, у которых нет будущего.\
\n\n✅  Совет: *Отпустите от себя старое, дайте ему завершиться.*\
\n\n❗️  Помните, что плохое всегда заканчивается, и чем быстрее вы начнете действовать в своих интересах, тем быстрее закончится период неудач.'
        text14 = '*ВАША КАРТА ДНЯ:  Дьявол XV*\
\n\n❗️ День зависимости от ситуации, от людей, от своего состояния.\
\n\n✔️  Девиз дня — разделяй и властвуй. Или вы «там « или вы «здесь».\
\n\n♻️  Ситуация может так сложиться, что заставит вас пересмотреть свою позицию.\
\n\n⚠️  Есть возможность,что вас будут склонять к какому то неблаговидному поступку и вам придется изменить своим принципам.\
\n\n⚠️  Вибрации дня могут всколыхнуть зависть, ревность, алчность или жажду власти.\
\n\n❗️  Здоровью могут навредить разного рода зависимости, такие как вредные привычки. Сегодня как никогда нужно знать меру.\
\n\n❗️  В дружбе, любви, семье так же будут мучить сомнения, дух раздора, желание делать всё наперекор.\
\n\n♻️  Чтобы «смягчить» день, попробуйте жить в позитивном ключе, спокойно относясь к происходящему.\
\n\n⚠️  Предупреждение: Искушение изменить своим принципам.\
\n\n✅  Совет: *Вычислить среди своего окружения человека, после общения с которым начинаются неудачи и прекратить с этим человеком контакты.*'
        text15 = '*ВАША КАРТА ДНЯ: Умеренность XIV*\
\n\n✔️  День, когда все усилия четко идут в заданном направлении и цель достижима.\
\n\n♻️  Девиз дня — работа и терпение.\
\n\n♻️  Результаты не сразу, но они будут такими, какими вы их хотите видеть.\
\n\n❗️  Для бизнеса день сложный. Поэтому не делайте сегодня серьезные вложения. А благотворительность может получиться.\
\n\n♻️  День, несущий внезапные открытия. Какие бы события не произошли в этот день, они принесут вам приятные перемены, подарят встречу с нужными ' \
                 'людьми, решат важную задачу.\
\n\n♻️  Здоровье постепенно будет улучшаться.\
\n\n⚠️   Предупреждение: Нужно четко определиться с целями. Рассчитывайте только на себя..\
\n\n✅  Совет: *Все усилия в одну точку.*'
        text16 = '*ВАША КАРТА ДНЯ: Башня XVI*\
\n\n✔️  День неожиданных сюрпризов. Возможно, вас ждет приятное и неожиданное известие, а возможно крушение ваших планов и ожиданий. Будьте готовы ' \
                 'к изменениям.\
\n\n✔️  В бизнесе складываются проволочки, задержки. Не имея нужной информации, можно закабалить себя в непомерных условиях, оказаться не у дел и ' \
                 'потерять вложения, а то и больше.\
\n\n❗️  Если внезапное крушение планов огорчит вас или рассердит, то помните, что карта Башни в итоге означает слом изживших себя представлений.\
\n\n♻️  Через какое то время вы перестанете жалеть о том, что не осуществилось сегодня.\
\n\n⚠️  Сегодня люди конфликтные, обидчивые, с трудом находят компромисс.\
\n\n♻️  Здоровье сегодня довольно уязвимо, вероятен риск сердечно-сосудистых обострений, неврозов, простудных заболеваний.\
\n\n⚠️  Предупреждение: Не переживайте если что-то «перевернулось», «сломалось» в этот день — помогите самому себе «расчистить» место для нового и ' \
                 'свежего.\
\n\n✅  Совет: *Остерегайтесь зависимости от кого-либо или от чего-либо.*'
        text17 = '*ВАША КАРТА ДНЯ: Звезда XVII*\
\n\n♻️  День может дать новый шанс на успех.\
\n\n♻️  Девиз дня — будь готов открывать новые горизонты.\
\n\n♻️  В бизнесе возможны новые сделки , встречи с новыми партнерами.\
\n\n❗️  Если планировали открывать новое дело — сегодня тот самый день.\
\n\n❗️  Во взаимоотношениях возможен новый чувственный виток, встреча с новым человеком, новой любовью.\
\n\n♻️   В семье есть возможность освежить отношения.\
\n\n♻️  Взгляд по-новому на себя и свое здоровье, поможет «выбраться из болячек».\
\n\n⚠️  Предупреждение: Не поддавайтесь на провокации, будьте внимательны к новым знакомствам.\
\n\n✅   Совет:* Прежде чем менять жизнь, определитесь , куда будете направлять свои силы, дабы не потерять время и энергию в дальнейшем*'
        text18 = '*ВАША КАРТА ДНЯ: Луна XVIII*\
\n\n♻️  День подозрений и метаний.\
\n\n✔️  Девиз дня: не просят — не делай. Могут быть вещие сны.\
\n\n✔️  Сегодняшний день в целом довольно благоприятный, но стоит быть готовыми к случайным ситуациям, которые не всегда могут быть приятными, ' \
                 'так как сегодня могут активироваться тайные враги, клеветники, а так же вы сами можете допустить ошибки. Но зато вы сможете посмотреть правде в глаза и выявить скрытых недругов.\
\n\n❗️  Разногласия могут быть во всех сферах — и в бизнесе, и в любви, и в дружбе, и в семье из-за излишней подозрительности. Поэтому,' \
                 'помня об этом, не допускайте темным мыслям испортить сегодняшний день.\
\n\n❗️  Здоровье тоже может быть подвержено вибрациям сегодняшнего дня — возможно обострение хронических заболеваний .\
\n\n♻️  Если же кто может быстро приспосабливаться к ситуации, то тому будет более комфортно сегодня.\
\n\n⚠️  Предупреждение: Преодолейте свои страхи перед неизвестным, выявляйте источник неприятностей.\
\n\n✅  Совет: *Не пускайте ничего на волю случая.*'
        text19 = '*ВАША КАРТА ДНЯ:  Cолнце XIX*\
\n\n✔️  Сегодняшний день дает защиту каждому и всему — неизменное состояние того что уже есть.\
\n\n✔️  В бизнесе – прибыль постоянная, любые источники дохода — постоянные.\
\n\n✔️  На работе стабильно.\
\n\n♻️  В семье, дружбе — какие отношения были, такие и будут .\
\n\n♻️  В любви возможно слияние, сьезд на совместное проживание или решение быть вместе.\
\n\n❗️  Здоровью нет никаких угроз, а вот улучшение возможно.\
\n\n❗️  Сегодняшний день успешен для одиночных свершений, но он не комфортный для тех, кто успешен за счет других людей, так как сегодняшние ' \
                 'достижения происходят целиком из-за самостоятельных решений и действий.\
\n\n⚠️  Предупреждение: Старайтесь сохранить сегодняшнюю ситуацию, не упустить то, что уже есть.\
\n\n✅  Совет: *Не теряйте бдительность. Не меняйте сегодня ничего.*'
        text20 = '*ВАША КАРТА ДНЯ: Суд. Возрождение. XX*\
\n\n✔️  День осознания своего пути, определения своих действий,принятие решений.\
\n\n♻️  Сегодня вы можете решить свою проблему – хоть свежую,хоть давнишнюю.\
\n\n❗️   Хотя день благоприятный, но не подходит для серьезных начинаний.\
\n\n✔️  Вибрации сегодняшнего дня больше подходят возвращению к забытым или нереализованным планам.\
\n\n✔️  Возможность нахождения своего пути через потери, например, расстаться с теми, кто тормозил ваше развитие — причем во всех сферах — и в ' \
                 'бизнесе, и в любви, и в дружбе, и в семье.\
\n\n♻️  Благоприятны дружеские встречи, построение планов на будущее, даже если они не конкретизированы.\
\n\n♻️  Сегодня можно найти нового партнера (везде) или новое место работы .\
\n\n⚠️  Предупреждение: Не давайте старым, давно решенным проблемам, воскреснуть вновь. Не «клинить» на прошлом.\
\n\n✅  Совет: *Позвали- иди!*'
        text21 = '*ВАША КАРТА ДНЯ: МИР XXI*\
\n\n✔️  День спокойствия и достижения желаемого.\
\n\n️ ✔ Нормализация отношений с кем-то, выход из трудной ситуации. Изменение своей жизни собственными силами.\
\n\n♻️  Все дела идут так, как вы задумали, или вы просто не придаете значения возможным помехам и это «фишка» дня — человек видит только хорошее, ' \
                 'не обращая внимание на «обратную сторону медали» – это может аукнуться в дальнейшем.Поэтому «доверяй, но проверяй».\
\n\n♻️  Сегодня есть шанс договориться, распланировать будущее.\
\n\n❗️  Во взаимоотношениях и дружбе приятные знакомства, которые могут перерасти в большее.\
\n\n♻️  Легко начинаются новые романы.\
\n\n♻️  В то же время, сегодня как никогда возможен уход из семьи.\
\n\n♻️  Бытовая техника требует особого внимания сегодня.\
\n\n⚠️  Предупреждение: Не спешите почивать на лаврах,чтобы потом не жалеть об упущенном\
\n\n✅  Совет: *Постарайтесь ускорить события самостоятельно*'
        if message.data == 0:
            bot.send_photo(message.from_user.id, open('D:/qwe/0.jpg', 'rb'), parse_mode="Markdown" ,caption=text)
            # bot.send_photo(message.from_user.id, open('files/video/','rb'), caption='желаемый текст')
        elif message.data == 1:
                bot.send_photo(message.from_user.id, open('/qwe/1.jpg', 'rb'),parse_mode="Markdown", caption=text1)
        elif message.data == 2:
                bot.send_photo(message.from_user.id, open('/qwe/2.jpg', 'rb'),parse_mode="Markdown", caption=text2)
        elif message.data == 3:
                bot.send_photo(message.from_user.id, open('/qwe/3.jpg', 'rb'),parse_mode="Markdown", caption=text3)
        elif message.data == 4:
                bot.send_photo(message.from_user.id, open('/qwe/4.jpg', 'rb'),parse_mode="Markdown", caption=text4)
        elif message.data == 5:
                bot.send_photo(message.from_user.id, open('/qwe/5.jpg', 'rb'),parse_mode="Markdown", caption=text5)
        elif message.data == 6:
                bot.send_photo(message.from_user.id, open('/qwe/6.jpg', 'rb'),parse_mode="Markdown", caption=text6)
        elif message.data == 7:
                bot.send_photo(message.from_user.id, open('/qwe/7.jpg', 'rb'),parse_mode="Markdown", caption=text7)
        elif message.data == 8:
                bot.send_photo(message.from_user.id, open('/qwe/8.jpg', 'rb'),parse_mode="Markdown", caption=text8)
        elif message.data == 9:
                bot.send_photo(message.from_user.id, open('/qwe/9.jpg', 'rb'),parse_mode="Markdown", caption=text9)
        elif message.data == 10:
                bot.send_photo(message.from_user.id, open('/qwe/10.jpg', 'rb'),parse_mode="Markdown", caption=text10)
        elif message.data == 11:
                bot.send_photo(message.from_user.id, open('/qwe/11.jpg', 'rb'),parse_mode="Markdown", caption=text11)
        elif message.data == 12:
                bot.send_photo(message.from_user.id, open('/qwe/12.jpg', 'rb'),parse_mode="Markdown", caption=text12)
        elif message.data == 13:
                bot.send_photo(message.from_user.id, open('/qwe/13.jpg', 'rb'),parse_mode="Markdown", caption=text13)
        elif message.data == 14:
                bot.send_photo(message.from_user.id, open('/qwe/14.jpg', 'rb'),parse_mode="Markdown", caption=text14)
        elif message.data == 15:
                bot.send_photo(message.from_user.id, open('/qwe/15.jpg', 'rb'),parse_mode="Markdown", caption=text15)
        elif message.data == 16:
                bot.send_photo(message.from_user.id, open('/qwe/16.jpg', 'rb'),parse_mode="Markdown", caption=text16)
        elif message.data == 17:
                bot.send_photo(message.from_user.id, open('/qwe/17.jpg', 'rb'),parse_mode="Markdown", caption=text17)
        elif message.data == 18:
                bot.send_photo(message.from_user.id, open('/qwe/18.jpg', 'rb'),parse_mode="Markdown", caption=text18)
        elif message.data == 19:
                bot.send_photo(message.from_user.id, open('/qwe/19.jpg', 'rb'),parse_mode="Markdown", caption=text19)
        elif message.data == 20:
                bot.send_photo(message.from_user.id, open('/qwe/20.jpg', 'rb'),parse_mode="Markdown", caption=text20)
        elif message.data == 21:
                bot.send_photo(message.from_user.id, open('/qwe/21.jpg', 'rb'),parse_mode="Markdown", caption=text21)

        else:
            bot.send_message(message.from_user.id, "end")
       # bot.send_message(message.from_user.id, q)
if __name__ == '__main__':
    bot.polling(none_stop=True)
