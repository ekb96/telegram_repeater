#! /usr/bin/env python3.5
# -*- coding: utf-8 -*-

""" Данный скрипт предназначен для ретрансляции сообщений из нескольких групп, 
на которые подписан данный пользователь, в одну общую. 
Скрипт проверяет сообщения на наличие ссылок и запрещенных слов, 
при их наличии - игнорирует такие сообщения. 
Для подключения требуется получить ID и Hash на сайте телеграма и 
прописать в скрипте в соответствующих строках. 
Также требуется указать группы, которые будут отслеживаться и 
группу в которую будут ретранслироваться сообщения. """

from telethon import TelegramClient, sync, events

ignore = ["iphone",	"аккаунт", "акция", "бесплатно", "бизнес", "бизнесы", "биткоин", 
"бонус",	"бонусы",	"бот", "букмейкер", "букмейкерская", "выйграй", "выйграли", "выйгрыш", 
"выигрывай", "деньги", "депозит",	"закладка", "закладки",	"закрытая", "закрытый", "залетай", 
"залетайте", "залетайте", "зарабатывай", "зарабатывайте", "заработай", "заработали", "заработок", 
"заходи", "заходим", "заходите", "инвестиции", "казино", "канал", "каналы", "команда", 
"криптовалюта", "криптовалюты",	"лотерея", "навального", "навальный", "навальным", "навальному", 
"путин", "путина", "путину", "путиным", "нажимай", "нажми", "нажимайте", "наркотик", 
"наркотики", "наркота", "объявление", "паблик", "паблики", "переходи", "подписка", "подписывайся", 
"подписывайтесь", "подпишись", "подработка", "подработки", "получай", "поднимай", "получи",
"поднял", "порно", "порнуха", "порнухой", "порнуху", "приват", "приватная", "приватный", 
"присоединяйся", "присоединяйтесь", "промо",	"промокод", "промокоды", "регистрации", 
"регистрируемся", "регистрируй", "регистрируйся", "реклама", "рекламу", "розыграем",	
"розыгрываем", "розыгрыш", "розыгрывается", "спайс",	"ссылка", "ссылке", "ссылку", "ставки", 
"ставок", "трейдер", "трейдеры", "халява", "халяву", "халявы", "шалавы",  "шалава", "шлюха", 
"шлюхи", "проститутка", "проститутку", "проституток", "форекс", "forex", "форексе", "донат", "донаты",	
"годный", "канала", "распродажа", "распродаже", "распродажу", "скидка", "скидку", "скидки", "aliexpress",	
"ali", "хач", "хачи", "чурки", "чурка", "чурок", "хачей", "маркет", "подписаться", "1xbet", 
"трамп", "трампу", "трампа"]

api_id = 1234567														# Вставляем свой api_id
api_hash = '6489b02em5e998812m03478899s32a77bt'							# Вставляем свой api_hash

client = TelegramClient('Session2020', api_id, api_hash)
client.start()

@client.on(events.NewMessage(chats=('MDK')))							# Создает событие
@client.on(events.NewMessage(chats=('Чёрный юмор')))					# Создает событие
@client.on(events.NewMessage(chats=('Бро скинул мем')))					# Создает событие
@client.on(events.NewMessage(chats=('TELEGRA4CH')))						# Создает событие
@client.on(events.NewMessage(chats=('Леонардо Дайвинчик')))				# Создает событие
@client.on(events.NewMessage(chats=('Контрольная')))					# Создает событие
@client.on(events.NewMessage(chats=('АХУ*ТЬ')))							# Создает событие
@client.on(events.NewMessage(chats=('Ptencoff_tg')))					# Создает событие

async def normal_handler(event):
	#print(event.message)
	bit = 0
	for word in ignore:
		if word in event.message.message.lower():
			bit = 1
	
	if (event.message.entities != None) or bit == 1:					# Если в сообщении есть ссылки или исключения
		#print("Есть ссылки или исключения")							# тогда ничего не делать
		#print("\n")
		pass
	
	elif event.message.entities == None:								# Иначе переотправить в свою группу
		#print("Нет ссылок")
		#print("\n")
		await client.send_message('MDK * Юмор * Мемы * TELEGRA4CH * Леонардо Дайвинчик', event.message)
		
	#sender = await event.get_sender()
	#if (sender.username == None):
	#	username = "Anonim"
	#else:
	#	username = sender.username
	#print(username)													# Вывести в консоль username
	#print(event.message.to_dict()['message']+"\n")						# Вывести в консоль сообщение
	
client.run_until_disconnected()											# Продолжать выполнение
