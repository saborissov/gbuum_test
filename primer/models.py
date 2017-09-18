from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


OTDEL = [



	('нет','нет'),
	('Диспетчерская служба','Диспетчерская служба'),
	("Общий отдел","Общий отдел"),
	("Юридический отдел","Юридический отдел"),
	("Бухгалтерия","Бухгалтерия"),
	("Кадры","Кадры"),
	("Сектор по работе с порталами","Сектор по работе с порталами"),
	("Технический отдел","Технический отдел"),
	("Благоустройство","Благоустройство"),
	("Отдел материально-технического обеспечения","Отдел материально-технического обеспечения"),
	("Контрактный отдел","Контрактный отдел"),
	("Отдел по работе с энергоснабжающими организациями","Отдел по работе с энергоснабжающими организациями"),

	
	
]


ADDRES = [

	

	("Молодцова 9","Молодцова 9"),
	("Дежнева 22к4","Дежнева 22к4"),
	("Дежнева 9к2","Дежнева 9к2"),
	("Дежнева 34 - склад","Дежнева 34 - склад"),
	("ОДС-1 ул. - Полярная 15к3","ОДС-1 ул. - Полярная 15к3"),
	("ОДС-2 ул. - Полярная 15к3","ОДС-2 ул. - Полярная 15к3"),
	("ОДС-3 ул. - Полярная 15к3","ОДС-3 ул. - Полярная 15к3"),
	("ОДС-4 ул. - Шокальского 3к1","ОДС-4 ул. - Шокальского 3к1"),
	("ОДС-5 ул. - Шокальского 3к1","ОДС-5 ул. - Шокальского 3к1"),
	("ОДС-6 ул. - Дежнева 9к2","ОДС-6 ул. - Дежнева 9к2"),
	("ОДС-7 ул. - Полярная 9к2","ОДС-7 ул. - Полярная 9к2"),
	("Вилюйская ул. строение5","Вилюйская ул. строение5"),

]

KABINET = [

	("нет","нет"),
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


STATUS_IN_WORK = [
	
	("В работе","В работе"),
	("Выполнено","Выполнено")

]

STATUS_DONE =[
	
	("Выполнено","Выполнено")

]


class Feedback(models.Model):
	
	Номер_заявки = models.AutoField(primary_key=True)
	ФИО = models.CharField(max_length=200, blank=True, null=True, verbose_name='ФИО')
	#Email = models.EmailField(max_length=200, blank=True)
	Проблема = models.TextField(verbose_name='Проблема')
	Адрес = models.CharField(max_length=250, choices=ADDRES, verbose_name='Адрес')
	Кабинет = models.CharField(max_length=250, choices=KABINET, verbose_name='Кабинет')
	Отдел = models.CharField(max_length=250, choices=OTDEL, verbose_name='Отдел')
	статус = models.CharField(max_length=125, choices=STATUS_IN_WORK, default='В работе')
	create=models.DateTimeField(auto_now_add = True, null = True)
	class Meta():
		ordering = ['-create']
		db_table='user_story'
		verbose_name = u'Заявки'

		def __str__(self):
			return "Номер заявки:%s; Заявитель:%s; Проблема:%s; Адрес:%s; Кабинет:%s" % (self.Номер_заявки, self.ФИО, self.Проблема, self.Адрес, self.Кабинет)



class Feedback_done(models.Model):
	Атрибуты_заявки = models.ForeignKey(Feedback)
	cтатус = models.CharField(max_length=125, choices= STATUS_DONE, default='Выполнено')
	done_time = models.DateTimeField(auto_now_add = True, null = True, verbose_name='Дата закрытия')

	class Meta():
		#ordering = ['-create']
		db_table='zayavki_done'
		verbose_name = u'Выполненые заявки'

	def __str__(self):
		return str (self.Атрибуты_заявки)



# Create your models here.
