from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from Сотрудники.models import Сотрудники
#from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField

VALUE = [

	("шт","шт"),
	("м","м"),

]

STATUS = [

	("В наличии","В наличии"),
	("Рабочее состояние","Рабочее состояние"),
	("Заменить срочно","Заменить срочно"),
	("Не работает","Не работает"),
	("Требуется замена","Требуется замена"),
	("Требуется ремонт","Требуется ремонт"),
	("Требуется диагностика","Требуется диагностика"),
	("Требуется закупить","Требуется закупить"),
	("В ремонте","В ремонте"),
	("На складе","На складе"),
	

]

CATEGORIES = [


	("Компьютер","Компьютер"),
	("Переферийное оборудование","Переферийное оборудование"),
	("Сетевое оборудование","Сетевое оборудование"),
	("Комплектующие","Комплектующие"),
	("Расходный материал","Расходный материал"),
	("Аксессуары","Аксессуары"),
	("Бытовая техника","Бытовая техника"),
	("Прочее","Прочее"),
	
]	

Computers_and_other_equipment = [
	
	("#### КОМПЬЮТЕР ####","#### КОМПЬЮТЕР ####"),
	("Моноблок","Моноблок"),
	("Сиcтемный блок","Системный блок"),
	("Монитор","Монитор"),
	("Материнская плата","Материнская плата"),
	("Процессор","Процессор"),
	("#### ПЕРЕФЕРИЙНОЕ ОБОРУДОВАНИЕ ####","#### ПЕРЕФЕРИЙНОЕ ОБОРУДОВАНИЕ ####"),
	("Источник бесперебойного питания","Источник бесперебойного питания"),
	("Принтер-лазерный","Принтер-лазерный"),
	("Принтер-струйный","Принтер-струйный"),
	("Мфу","Мфу"),
	("Сканер","Сканер"),
	("Флешка","Флешка"),
	("Факс","Факс"),
	("#### АКСЕССУАРЫ ####","#### АКСЕССУАРЫ ####"),
	("Мышка","Мышка"),
	("Клавиатура","Клавиатура"),
	("Сетевой фильтр","Сетевой фильтр"),
	("#### РАСХОДНЫЙ МАТЕРИАЛ ####","#### РАСХОДНЫЙ МАТЕРИАЛ ####"),
	("Картридж","Картридж"),
	("Коннекторы","Коннекторы"),
	("Интернет кабель","Интернет кабель"),
	("#### СЕТЕВОЕ ОБОРУДОВАНИЕ ####","#### СЕТЕВОЕ ОБОРУДОВАНИЕ ####"),
	("Сетевая карта","Сетевая карта"),
	("Роутер","Роутер"),
	("Маршрутизатор","Маршрутизатор"),
	("#### КОМПЛЕКТУЮЩИЕ ####","#### КОМПЛЕКТУЮЩИЕ ####"),
	("Жесткий диск","Жесткий диск"),
	("Внешний жесткий диск","Внешний жесткий диск"),
	("Процессор","Процессор"),
	("Блок питания","Блок питания"),
	("Оперативная память","Оперативная память"),
	("#### БЫТОВАЯ ТЕХНИКА ####","#### БЫТОВАЯ ТЕХНИКА ####"),
	("Кондиционер","Кондиционер"),
	("Мобильный кондиционер","Мобильный кондиционер"),
	("Мультисплит-внешний","Мультисплит-внешний"),
	("Мультисплит-внутренний","Мультисплит-внутренний"),
	("Комплект сплит-система","Комплект сплит-система"),
	("Уничтожитель документов","Уничтожитель документов"),
	("#### ПРОЧЕЕ ####","#### ПРОЧЕЕ ####"),
	("Накопитель на ЖМД","Накопитель на ЖМД"),
	("ИК-термометр","ИК-термометр"),
	("Фотоаппарат","Фотоаппарат"),
	("Система многоканальной записи","Система многоканальной записи"),
	("Электрический воздухонагреватель","Электрический воздухонагреватель"),
	("Data Logger","Data Logger"),





]




KABINET = [
	("#### МОЛОДЦОВА 9 ####","#### МОЛОДЦОВА 9 ####"),
	("1","1"),
	("2","2"),
	("3","3"),
	("4","4"),
	("5","5"),
	("6","6"),
	("7","7"),
	("8","8"),
	("9","9"),
	("10","10"),
	("11","11"),
	("12","12"),
	("13","13"),
	("14","14"),
	("15","15"),
	("16","16"),
	("17","17"),
	("18","18"),
	("19","19"),
	("20","20"),
	("21","21"),
	("#### ЯСНЫЙ ПРОЕЗД 4к3 ####","#### ЯСНЫЙ ПРОЕЗД 4к3 ####"),
	("21","21"),
	("20","20"),
	("19","19"),
	("18","18"),
	("17","17"),
	("16","16"),
	("#### ДЕЖНЕВА 9к2 ####","#### ДЕЖНЕВА 9к2 ####"),
	("8","8"),
	("7","7"),
	("6","6"),
	("1","1"),

]

ADDRES = [

	

	("улица Молодцова 9","улица Молодцова 9"),
	("Ясный проезд 4к3","Ясный проезд 4к3"),
	("проезд Дежнева 22к4","проезд Дежнева 22к4"),
	("проезд Дежнева 9к2","проезд Дежнева 9к2"),
	("проезд Дежнева 34 - склад","проезд Дежнева 34 - склад"),
	("ОДС-1 ул. - Полярная 15к3","ОДС-1 ул. - Полярная 15к3"),
	("ОДС-2 ул. - Полярная 15к3","ОДС-2 ул. - Полярная 15к3"),
	("ОДС-3 ул. - Полярная 15к3","ОДС-3 ул. - Полярная 15к3"),
	("ОДС-4 ул. - Шокальского 3к1","ОДС-4 ул. - Шокальского 3к1"),
	("ОДС-5 ул. - Шокальского 3к1","ОДС-5 ул. - Шокальского 3к1"),
	("ОДС-6 ул. - Дежнева 9к2","ОДС-6 ул. - Дежнева 9к2"),
	("ОДС-7 ул. - Полярная 9к2","ОДС-7 ул. - Полярная 9к2"),
	("Вилюйская ул. строение5","Вилюйская ул. строение5"),

]


ODS = [

	("1","1"),
	("2","2"),
	("3","3"),
	("4","4"),
	("5","5"),
	("6","6"),
	("7","7"),


]

class Уникальный_номер(models.Model):
	инвентарный_номер = models.CharField(max_length=35, unique = True, blank=True, null = False, default= None)
	#наименование = models.CharField(max_length=125, choices=Computers_and_other_equipment)

	def __str__(self):
		return "%s" % self.инвентарный_номер # отображаем в админке атрибут: email

	class Meta:
		verbose_name = "инвентарный номер"
		verbose_name_plural = 'инвентарные номера' # переименуем название в админке



class Справочник_мест_установки(models.Model):
	id_места_установки = models.AutoField(primary_key=True)
	фио_ответственного = models.ForeignKey(Сотрудники, help_text='Выберите сотрудника ответственного за данный кабинет')
	#телефон = PhoneNumberField(blank=False, default='+7', null=True, unique=True, help_text = 'укажите номер телефона: +7###-###-##-##')
	одс = models.CharField(max_length=125, blank=True, choices=ODS)
	адрес = models.CharField(max_length=125, choices=ADDRES)
	кабинет = models.CharField(max_length=125, choices=KABINET, blank=True)
	# created = models.DateTimeField(auto_now_add = True, auto_now=False, verbose_name="дата_создания")
	# updated = models.DateTimeField(auto_now=True,verbose_name="дата_обновления")
	#фактическое_местонахожение = models.BooleanField(default=True, db_index=True)

	def __str__(self):   # функция отображает название атрибута из таблицы базы данных
		
		return "%s, кабинет-%s" % (self.адрес, self.кабинет ) # отображаем в админке атрибут: 

	class Meta:
		#ordering = ['фио_ответственного']
		verbose_name = "справочник мест установки"
		verbose_name_plural = 'справочник мест установки' # переименуем название в админке



class Компьютеры_оргтехника(models.Model):
	barcode = models.OneToOneField(Уникальный_номер, on_delete=models.CASCADE, unique=True,blank=True, null = True, default= None,verbose_name="инвентарный_номер")
	категория = models.CharField(max_length=125, choices=CATEGORIES)
	наименование = models.CharField(max_length=125, choices=Computers_and_other_equipment)
	модель_устройства = models.CharField(max_length= 50)
	год_выпуска = models.DateField(blank=True,  null=True, default=None)
	материально_ответственный = models.ForeignKey(Сотрудники)
	id_места_установки = models.ForeignKey(Справочник_мест_установки)
	#фаил = models.FileField(upload_to='user_media/files', blank =True, help_text='Прикрепите файл договора')
	#content = RichTextField() 
	описание = models.TextField(max_length=500,blank=True, null = True, default= None, help_text='Максимальное кол-во символов 500')
	ед_изм = models.CharField(max_length=10, choices=VALUE, default="шт")
	количество = models.IntegerField(default='',validators=[MaxValueValidator(125), MinValueValidator(0)],help_text='укажите кол-во')
	статус = models.CharField(max_length=125, choices=STATUS)
	created = models.DateTimeField(auto_now_add = True, auto_now=False, verbose_name="дата_создания")
	updated = models.DateTimeField(auto_now=True,verbose_name="дата_обновления")
	списано = models.BooleanField(default=False, db_index=True)
	картридж = models.CharField(max_length=125,blank=True)

	def __str__(self):
		s=self.наименование
		if not self.списано:
			s=s+"(нет в наличии)"
		return s	
	


	def __str__(self):
		return "%s:%s - %s" % (self.barcode, self.наименование, self.модель_устройства) # отображаем в админке атрибут: email

	class Meta:
		ordering = ['-created']
		verbose_name = "компьютерная и оргтехника"
		verbose_name_plural = 'компьютеры и оргтехника' # переименуем название в админке

	def get_is_stock(self):
		if self.списано:
			return"+"
		else:
			return ""		


class Принтер(models.Model):
	printer_id = models.AutoField(primary_key=True, verbose_name='Номер принтера')
	printer_model= models.CharField(max_length= 100, verbose_name='Модель принтера')
	#кол_во = models.IntegerField(default='',validators=[MaxValueValidator(125), MinValueValidator(0)],help_text='укажите кол-во')
	def __str__(self):
		return "%s" % self.printer_model # отображаем в админке атрибут: email

	class Meta:
		verbose_name = "принтер"
		verbose_name_plural = 'принтеры' # переименуем название в админке


class Картридж(models.Model):
	cartridge_id = models.AutoField(primary_key=True, verbose_name='Номер картриджа')
	cartridge_model= models.CharField(max_length= 100, verbose_name='Модель картриджа')
	#кол_во = models.IntegerField(default='',validators=[MaxValueValidator(125), MinValueValidator(0)],help_text='укажите кол-во')
	def __str__(self):
		return "%s" % self.cartridge_model # отображаем в админке атрибут: email

	class Meta:
		verbose_name = "картридж"
		verbose_name_plural = 'картриджи' # переименуем название в админке

class Cartridge_list(models.Model):
	catlis_id = models.AutoField(primary_key=True, verbose_name='Номер списка')
	catlis_printer = models.ForeignKey(Принтер,verbose_name='Модель принтеров')
	catlis_cartridge = models.ForeignKey(Картридж, verbose_name='Модель картриджей')
	address_to_dislacate = models.ForeignKey(Справочник_мест_установки, verbose_name='место установки')
	наименование = models.ForeignKey(Компьютеры_оргтехника)
	модель_картридж = models.ForeignKey(Компьютеры_оргтехника,related_name='model')
	class Meta:
		verbose_name = "cписок - принтер, картридж"
		verbose_name_plural = 'cписок - принтеры, картриджи' # переименуем название в админке


class List_of_printer(models.Model):
	printer_model= models.CharField(max_length= 100, verbose_name='Модель принтера')
	cartridge_model= models.CharField(max_length= 100, verbose_name='Модель картриджа')
	address_to_dislacate = models.ForeignKey(Справочник_мест_установки, verbose_name='место установки')
	created_date=models.DateField(auto_now_add = True, auto_now=False)




# class Перемещение(models.Model):
# 	инвентарный_номер = models.OneToOneField(Уникальный_номер, on_delete=models.CASCADE, unique=True, blank=True, null = True, default= None)
# 	ответственное_лицо = models.ForeignKey(Сотрудники)
# 	наименование = models.ForeignKey(Компьютеры_оргтехника,on_delete=models.CASCADE)
# 	адрес = models.CharField(max_length=125, choices=ADDRES)
# 	кабинет = models.CharField(max_length=4,choices=KABINET, blank=True, null = True, default= None)
# 	created = models.DateTimeField(auto_now_add = True, auto_now=False, verbose_name="дата_создания")
# 	updated = models.DateTimeField(auto_now=True,verbose_name="дата_обновления")


# 	def __str__(self):
# 		#return "%s; %s; %s кабинет" % (self.инвентарный_номер, self.наименование, self.кабинет) # отображаем в админке атрибут: email
# 		return "%s" % (self.кабинет)
# 	class Meta:
# 		verbose_name = "перемещение компьютерной и оргтехники"
# 		verbose_name_plural = 'компьютеры и оргтехника - перемещение' # переименуем название в админке

class Фиксация_перемещения(models.Model):
	инвентарный_номер = models.ForeignKey(Уникальный_номер, on_delete=models.CASCADE,blank=True, null = True, default= None)
	ответственное_лицо = models.ForeignKey(Сотрудники)
	наименование = models.ForeignKey(Компьютеры_оргтехника, on_delete=models.CASCADE)
	причина_перемещения = models.TextField(max_length=250,blank=True, null = True, default= None, help_text='Максимальное кол-во символов 250')
	откуда_переместили = models.ForeignKey(Справочник_мест_установки, on_delete=models.CASCADE)
	куда_переместили = models.CharField(max_length=4,choices=KABINET)
	куда_адрес = models.ForeignKey(Справочник_мест_установки, on_delete=models.CASCADE, related_name= 'adress')
	#адрес_местонахождения = models.CharField(max_length=125, choices=ADDRES)
	created = models.DateTimeField(auto_now_add = True, auto_now=False,verbose_name="дата_перемещения")
	updated = models.DateTimeField(auto_now=True,verbose_name="дата_обновления")

	def __str__(self):
		return "%s; %s" % (self.инвентарный_номер, self.наименование) # отображаем в админке атрибут: email

	class Meta:
		verbose_name = "перемещение компьютерной и оргтехники"
		verbose_name_plural = 'компьютеры и оргтехника - фиксация_перемещения'


class Списанное_оборудование(models.Model):
	инвентарный_номер = models.OneToOneField(Уникальный_номер, on_delete=models.CASCADE, unique=True)
	наименование = models.ForeignKey(Компьютеры_оргтехника,on_delete=models.CASCADE)
	причина_списания = models.CharField(max_length=125, blank=True)
	адрес_местонахождения = models.CharField(max_length=125, choices=ADDRES)
	date_end = models.DateTimeField(auto_now_add = True, auto_now=False,verbose_name="дата_списания")
	
	def __str__(self):
		return "%s; %s" % (self.инвентарный_номер, self.наименование) # отображаем в админке атрибут: email

	class Meta:
		verbose_name = "списанное оборудование"
		verbose_name_plural = 'списанное оборудование'


