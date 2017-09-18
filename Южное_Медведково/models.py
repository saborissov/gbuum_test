from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
#from sorl.thumbnail import ImageField


# class Status(models.Model):
# 	name = models.CharField(max_length = 25, blank=True, null = True, default= None)
# 	is_active = models.BooleanField(default=True)
# 	created = models.DateTimeField(auto_now_add = True, auto_now=False)
# 	updated = models.DateTimeField(auto_now=True)
	

# 	def __str__(self):   # функция отображает название атрибута из таблицы базы данных
		
# 		return "Статус: %s " % self.name # отображаем в админке атрибут: email

# 	class Meta:
# 		verbose_name = "Статус заявки"
# 		verbose_name_plural = 'Статусы заявок' # переименуем название в админке 


THEMS =(

	('Неисправное освещение в подъезде','Неисправное освещение в подъезде'),
	('Неисправность систем пожаробезопасности','Неисправность систем пожаробезопасности'),
	('Неисправность/недоступность подъемной платформы для инвалидов','Неисправность/недоступность подъемной платформы для инвалидов'),
	('Неисправный мусоропровод','Неисправный мусоропровод'),
	('Неисправный пандус','Неисправный пандус'),
	('Некачественный текущий ремонт','Некачественный текущий ремонт'),
	('Несанкционированные объявления, надписи и рисунки в подъезде','Несанкционированные объявления, надписи и рисунки в подъезде'),
	('Неубранный подъезд','Неубранный подъезд'),
	('Отсутствие/повреждение указателей с наименованием улицы и номером дома','Отсутствие/повреждение указателей с наименованием улицы и номером дома'),
	('Повреждение электропроводки/щитового оборудования','Повреждение электропроводки/щитового оборудования'),
	('Повреждение элементов: продухи, отмостки, фундамент, стены, водостоки','Повреждение элементов: продухи, отмостки, фундамент, стены, водостоки'),
	('Поврежденные лестницы','Поврежденные лестницы'),
	('Поврежденный козырек подъезда','Поврежденный козырек подъезда'),
	('Протечка кровли-крыши','Протечка кровли-крыши'),
	('Сломанные почтовые ящики','Сломанные почтовые ящики'),
	("Брошенный разукомплектованный автомобиль","Брошенный разукомплектованный автомобиль"),
	("Наличие ям и выбоин на внутридворовых проездах и тротуарах","Наличие ям и выбоин на внутридворовых проездах и тротуарах"),
	("Некачественное содержание детской площадки","Некачественное содержание детской площадки"),
	("Некачественное содержание малых архитектурных форм","Некачественное содержание малых архитектурных форм"),
	("Некачественное содержание площадки для выгула собак","Некачественное содержание площадки для выгула собак"),
	("Некачественное содержание спортивной площадки","Некачественное содержание спортивной площадки"),
	("Ненадлежащий уход за зелеными насаждениями","Ненадлежащий уход за зелеными насаждениями"),
	("Несвоевременное восстановление благоустройства территории после разрытий","Несвоевременное восстановление благоустройства территории после разрытий"),
	("Неубранная дворовая территория","Неубранная дворовая территория"),
	("Неубранная контейнерная площадка","Неубранная контейнерная площадка"),
	("Отсутствие песка в песочнице","Отсутствие песка в песочнице"),
	("Отсутствие урн в положенных местах","Отсутствие урн в положенных местах"),
	("Повреждение ограждений газонов","Повреждение ограждений газонов"),
	("Поврежденные искусственные дорожные неровности","Поврежденные искусственные дорожные неровности"),
	("Подтопление придомовой территории","Подтопление придомовой территории"),
	("Размещение мусорных контейнеров с нарушением норм","Размещение мусорных контейнеров с нарушением норм"),

	)


STATUS =(

	("В работе","В работе"),
	("Отправлено на доп. контроль","Отправлено на доп. контроль"),
	("Выполнено","Выполнено"),
	

	)


CATEGORY = (

	("Плиточные работы","Плиточные работы"),
	("Штукатурно-малярные работы","Штукатурно-малярные работы"),
	("Фасадные работы","Фасадные работы"),


	)



MATERIALS = (

	("Плиточный клей","Плиточный клей"),
	("Плитка 40х40","Плитка 40х40"),
	("Штукатурная смесь ротбанд","Штукатурная смесь ротбанд"),
	("Краска белая алкидная","Краска белая алкидная"),



	)



HOMES = (


	("Дежнева пр. д.2","Дежнева пр. д.2"),
	("Дежнева пр. д.2а","Дежнева пр. д.2а"),
	("Дежнева пр. д.5 кор.1","Дежнева пр. д.5 кор.1"),
	("Дежнева пр. д.6 кор.1","Дежнева пр. д.6 кор.1"),
	("Дежнева пр. д.8","Дежнева пр. д.8"),
	("Дежнева пр. д.9 кор.2","Дежнева пр. д.9 кор.2"),
	("Дежнева пр. д.9 кор.3","Дежнева пр. д.9 кор.3"),
	("Дежнева пр. д.10","Дежнева пр. д.10"),
	("Дежнева пр. д.12 кор.1","Дежнева пр. д.12 кор.1"),
	("Дежнева пр. д.14","Дежнева пр. д.14"),
	("Дежнева пр. д.15","Дежнева пр. д.15"),
	("Дежнева пр. д.17 кор.1","Дежнева пр. д.17 кор.1"),
	("Дежнева пр. д.19 кор.1","Дежнева пр. д.19 кор.1"),
	("Дежнева пр. д.19 кор.2","Дежнева пр. д.19 кор.2"),
	("Дежнева пр. д.22 кор.1","Дежнева пр. д.22 кор.1"),
	("Дежнева пр. д.22 кор.2","Дежнева пр. д.22 кор.2"),
	("Дежнева пр. д.22 кор.3","Дежнева пр. д.22 кор.3"),
	("Дежнева пр. д.22 кор.4","Дежнева пр. д.22 кор.4"),
	("Дежнева пр. д.24","Дежнева пр. д.24"),
	("Дежнева пр. д.25 кор.1","Дежнева пр. д.25 кор.1"),
	("Дежнева пр. д.25 кор.2","Дежнева пр. д.25 кор.2"),
	("Дежнева пр. д.25 кор.3","Дежнева пр. д.25 кор.3"),
	("Дежнева пр. д.26 кор.3","Дежнева пр. д.26 кор.3"),
	("Дежнева пр. д.27 кор.1","Дежнева пр. д.27 кор.1"),
	("Дежнева пр. д.27 кор.2","Дежнева пр. д.27 кор.2"),
	("Дежнева пр. д.27 кор.3","Дежнева пр. д.27 кор.3"),
	("Дежнева пр. д.28","Дежнева пр. д.28"),
	("Дежнева пр. д.29 кор.1","Дежнева пр. д.29 кор.1"),
	("Дежнева пр. д.30 кор.3","Дежнева пр. д.30 кор.3"),
	("Дежнева пр. д.32","Дежнева пр. д.32"),
	("Дежнева пр. д.34","Дежнева пр. д.34"),
	("Дежнева пр. д.36","Дежнева пр. д.36"),
	("Дежнева пр. д.38","Дежнева пр. д.38"),
	("Дежнева пр. д.38 кор.а","Дежнева пр. д.38 кор.а"),
	("Заповедная ул. д.2","Заповедная ул. д.2"),
	("Заповедная ул. д.4","Заповедная ул. д.4"),
	("Заповедная ул. д.6","Заповедная ул. д.6"),
	("Заповедная ул. д.8","Заповедная ул. д.8"),
	("Заповедная ул. д.8 кор.1","Заповедная ул. д.8 кор.1"),
	("Заповедная ул. д.10","Заповедная ул. д.10"),
	("Заповедная ул. д.14 кор.1","Заповедная ул. д.14 кор.1"),
	("Заповедная ул. д.16 кор.3","Заповедная ул. д.16 кор.3"),
	("Заповедная ул. д.20","Заповедная ул. д.20"),
	("Заповедная ул. д.20а","Заповедная ул. д.20а"),
	("Заповедная ул. д.24","Заповедная ул. д.24"),
	("Заповедная ул. д.28","Заповедная ул. д.28"),
	("Молодцова ул. д.1в","Молодцова ул. д.1в"),
	("Молодцова ул. д.3","Молодцова ул. д.3"),
	("Молодцова ул. д.5","Молодцова ул. д.5"),
	("Молодцова ул. д.9","Молодцова ул. д.9"),
	("Молодцова ул. д.15 кор.1","Молодцова ул. д.15 кор.1"),
	("Молодцова ул. д.15 кор.2","Молодцова ул. д.15 кор.2"),
	("Молодцова ул. д.17 кор.1","Молодцова ул. д.17 кор.1"),
	("Молодцова ул. д.19 кор.1","Молодцова ул. д.19 кор.1"),
	("Молодцова ул. д.19 кор.2","Молодцова ул. д.19 кор.2"),
	("Молодцова ул. д.23 кор.1","Молодцова ул. д.23 кор.1"),
	("Молодцова ул. д.23 кор.2","Молодцова ул. д.23 кор.2"),
	("Молодцова ул. д.25 кор.1","Молодцова ул. д.25 кор.1"),
	("Молодцова ул. д.25 кор.2","Молодцова ул. д.25 кор.2"),
	("Молодцова ул. д.27 кор.1","Молодцова ул. д.27 кор.1"),
	("Молодцова ул. д.27 кор.2","Молодцова ул. д.27 кор.2"),
	("Молодцова ул. д.27 кор.3","Молодцова ул. д.27 кор.3"),
	("Молодцова ул. д.31 кор.1","Молодцова ул. д.31 кор.1"),
	("Молодцова ул. д.33 кор.1","Молодцова ул. д.33 кор.1"),
	("Полярная ул. д.1","Полярная ул. д.1"),
	("Полярная ул. д.2","Полярная ул. д.2"),
	("Полярная ул. д.2 кор.1","Полярная ул. д.2 кор.1"),
	("Полярная ул. д.3 кор.1","Полярная ул. д.3 кор.1"),
	("Полярная ул. д.3 кор.2","Полярная ул. д.3 кор.2"),
	("Полярная ул. д.4 кор.1","Полярная ул. д.4 кор.1"),
	("Полярная ул. д.4 кор.2","Полярная ул. д.4 кор.2"),
	("Полярная ул. д.5 кор.1","Полярная ул. д.5 кор.1"),
	("Полярная ул. д.5 кор.2","Полярная ул. д.5 кор.2"),
	("Полярная ул. д.6 кор.1","Полярная ул. д.6 кор.1"),
	("Полярная ул. д.7 кор.1","Полярная ул. д.7 кор.1"),
	("Полярная ул. д.8","Полярная ул. д.8"),
	("Полярная ул. д.10","Полярная ул. д.10"),
	("Полярная ул. д.11 кор.2","Полярная ул. д.11 кор.2"),
	("Полярная ул. д.12","Полярная ул. д.12"),
	("Полярная ул. д.13 кор.1","Полярная ул. д.13 кор.1"),
	("Полярная ул. д.13 кор.3","Полярная ул. д.13 кор.3"),
	("Полярная ул. д.13 кор.4","Полярная ул. д.13 кор.4"),
	("Полярная ул. д.14","Полярная ул. д.14"),
	("Полярная ул. д.14 кор.1","Полярная ул. д.14 кор.1"),
	("Полярная ул. д.15 кор.1","Полярная ул. д.15 кор.1"),
	("Полярная ул. д.15 кор.2","Полярная ул. д.15 кор.2"),
	("Полярная ул. д.15 кор.3","Полярная ул. д.15 кор.3"),
	("Полярная ул. д.16 кор.1","Полярная ул. д.16 кор.1"),
	("Полярная ул. д.16 кор.2","Полярная ул. д.16 кор.2"),
	("Полярная ул. д.17 кор.1","Полярная ул. д.17 кор.1"),
	("Полярная ул. д.17 кор.2","Полярная ул. д.17 кор.2"),
	("Полярная ул. д.18","Полярная ул. д.18"),
	("Полярная ул. д.19","Полярная ул. д.19"),
	("Сухонская ул. д.1","Сухонская ул. д.1"),
	("Сухонская ул. д.1а","Сухонская ул. д.1а"),
	("Сухонская ул. д.5","Сухонская ул. д.5"),
	("Сухонская ул. д.5а","Сухонская ул. д.5а"),
	("Сухонская ул. д.7","Сухонская ул. д.7"),
	("Сухонская ул. д.7а","Сухонская ул. д.7а"),
	("Шокальского пр. д.1","Шокальского пр. д.1"),
	("Шокальского пр. д.1 кор.1","Шокальского пр. д.1 кор.1"),
	("Шокальского пр. д.2","Шокальского пр. д.2"),
	("Шокальского пр. д.2а","Шокальского пр. д.2а"),
	("Шокальского пр. д.3 кор.2","Шокальского пр. д.3 кор.2"),
	("Шокальского пр. д.4","Шокальского пр. д.4"),
	("Шокальского пр. д.6","Шокальского пр. д.6"),
	("Шокальского пр. д.6а","Шокальского пр. д.6а"),
	("Шокальского пр. д.7 кор.1","Шокальского пр. д.7 кор.1"),
	("Шокальского пр. д.10","Шокальского пр. д.10"),
	("Шокальского пр. д.11","Шокальского пр. д.11"),
	("Шокальского пр. д.12","Шокальского пр. д.12"),
	("Шокальского пр. д.12б","Шокальского пр. д.12б"),
	("Шокальского пр. д.13","Шокальского пр. д.13"),
	("Шокальского пр. д.13 кор.1","Шокальского пр. д.13 кор.1"),
	("Шокальского пр. д.15","Шокальского пр. д.15"),
	("Ясный пр. д.1","Ясный пр. д.1"),
	("Ясный пр. д.4 кор.3","Ясный пр. д.4 кор.3"),
	("Ясный пр. д.5","Ясный пр. д.5"),
	("Ясный пр. д.5а","Ясный пр. д.5а"),
	("Ясный пр. д.7","Ясный пр. д.7"),
	("Ясный пр. д.8 кор.1","Ясный пр. д.8 кор.1"),
	("Ясный пр. д.8 кор.2","Ясный пр. д.8 кор.2"),
	("Ясный пр. д.8 кор.4","Ясный пр. д.8 кор.4"),
	("Ясный пр. д.9","Ясный пр. д.9"),
	("Ясный пр. д.9а","Ясный пр. д.9а"),
	("Ясный пр. д.11","Ясный пр. д.11"),
	("Ясный пр. д.12 кор.1","Ясный пр. д.12 кор.1"),
	("Ясный пр. д.12 кор.2","Ясный пр. д.12 кор.2"),
	("Ясный пр. д.12 кор.3","Ясный пр. д.12 кор.3"),
	("Ясный пр. д.13","Ясный пр. д.13"),
	("Ясный пр. д.13а","Ясный пр. д.13а"),
	("Ясный пр. д.14","Ясный пр. д.14"),
	("Ясный пр. д.14 кор.1","Ясный пр. д.14 кор.1"),
	("Ясный пр. д.15","Ясный пр. д.15"),
	("Ясный пр. д.15б","Ясный пр. д.15б"),
	("Ясный пр. д.16","Ясный пр. д.16"),
	("Ясный пр. д.16 кор.2","Ясный пр. д.16 кор.2"),
	("Ясный пр. д.18","Ясный пр. д.18"),
	("Ясный пр. д.19","Ясный пр. д.19"),
	("Ясный пр. д.20 кор.2","Ясный пр. д.20 кор.2"),
	("Ясный пр. д.24 кор.1","Ясный пр. д.24 кор.1"),
	("Ясный пр. д.26 кор.3","Ясный пр. д.26 кор.3"),
	("Ясный пр. д.28","Ясный пр. д.28"),
	("Ясный пр. д.34 кор.1","Ясный пр. д.34 кор.1"),
	("Ясный пр. д.34 кор.2","Ясный пр. д.34 кор.2"),
	


	)


NUMBERS = (

	("12901831","12901831"),
	("12997783","12997783"),
	("13010571","13010571"),
	("13040146","13040146"),
	("13017278","13017278"),
	("13100924","13100924"),
	("13099290","13099290"),
	("13039315","13039315"),
	("13123420","13123420"),
	("13275828","13275828"),
	("13210602","13210602"),
	("13231892","13231892"),
	("13328680","13328680"),
	("13316989","13316989"),
	("13347489","13347489"),
	("13332373","13332373"),
	("13219224","13219224"),
	("13289883","13289883"),
	("13305055","13305055"),
	("12915024","12915024"),
	("13249885","13249885"),
	("13000713","13000713"),
	("13338785","13338785"),
	("13347526","13347526"),
	("13334024","13334024"),
	("13314372","13314372"),
	("13287822","13287822"),
	("13603870","13603870"),
	("13287596","13287596"),
	("13315978","13315978"),
	("13286479","13286479"),
	("13305046","13305046"),
	("13289887","13289887"),
	("13284609","13284609"),
	("13319254","13319254"),
	("13287899","13287899"),
	("13302263","13302263"),
	("13410681","13410681"),
	("13613280","13613280"),
	("13612964","13612964"),
	("13347678","13347678"),
	("13347480","13347480"),
	("13369806","13369806"),
	("13330445","13330445"),
	("13308732","13308732"),
	("13759360","13759360"),
	("13846758","13846758"),
	("13901716","13901716"),
	("13881399","13881399"),
	("12922198","12922198"),
	("12678731","12678731"),
	("12678865","12678865"),
	("12832279","12832279"),
	("12678647","12678647"),
	("12833546","12833546"),
	("12882562","12882562"),
	("12676394","12676394"),
	("12882295","12882295"),
	("12899949","12899949"),
	("12758380","12758380"),
	("12779667","12779667"),
	("12885966","12885966"),
	("12882361","12882361"),
	("12851111","12851111"),
	("13189413","13189413"),
	("12831402","12831402"),
	("12822484","12822484"),
	("12824249","12824249"),
	("12706264","12706264"),
	("13358175","13358175"),
	("13369328","13369328"),
	("13921376","13921376"),
	("13923219","13923219"),
	("13962465","13962465"),
	("13786720","13786720"),
	("13845952","13845952"),
	("13870057","13870057"),
	("13881369","13881369"),
	("13763939","13763939"),
	("13839731","13839731"),
	("13871382","13871382"),
	("13874541","13874541"),
	("13968968","13968968"),
	("13965992","13965992"),
	("13968039","13968039"),
	("13937982","13937982"),
	("13930785","13930785"),
	("13934312","13934312"),
	("13965997","13965997"),
	("13969043","13969043"),
	("13968063","13968063"),
	("13943641","13943641"),
	("13966017","13966017"),
	("13943603","13943603"),
	("13287888","13287888"),
	("13971708","13971708"),
	("12882559","12882559"),
	("12910655","12910655"),
	("13959842","13959842"),
	("13948844","13948844"),
	("13955271","13955271"),
	("13955099","13955099"),
	("13978556","13978556"),
	("13958049","13958049"),
	("13955434","13955434"),
	("13964992","13964992"),
	("13948916","13948916"),
	("12882123","12882123"),
	("13952651","13952651"),
	("12910654","12910654"),
	("13952665","13952665"),
	("13958250","13958250"),
	("13196437","13196437"),
	("12680775","12680775"),
	("13198144","13198144"),
	("12930977","12930977"),
	("13931053","13931053"),
	("13947201","13947201"),
	("12911367","12911367"),
	("13946821","13946821"),
	("12918094","12918094"),
	("13976245","13976245"),
	("13394988","13394988"),
	("13964995","13964995"),
	("13955104","13955104"),
	("13029883","13029883"),
	("13964915","13964915"),
	("13965765","13965765"),
	("13930801","13930801"),
	("12924866","12924866"),
	("12917807","12917807"),
	("13301431","13301431"),
	("13923225","13923225"),
	("13754708","13754708"),
	("13952652","13952652"),
	("13946643","13946643"),
	("13985336","13985336"),
	("13006177","13006177"),
	("13754553","13754553"),
	("13992305","13992305"),
	("13958223","13958223"),
	("13985110","13985110"),
	("13962661","13962661"),
	("13937980","13937980"),
	("13983002","13983002"),
	("13964972","13964972"),
	("13895322","13895322"),
	("13983010","13983010"),
	("13997190","13997190"),
	("13985558","13985558"),
	("13978540","13978540"),
	("13939233","13939233"),
	("13988492","13988492"),
	("13936033","13936033"),
	("13921363","13921363"),
	("13931348","13931348"),
	("13952649","13952649"),
	("13961038","13961038"),
	("13992903","13992903"),
	("13955103","13955103"),
	("13992910","13992910"),
	("13891566","13891566"),
	("13931051","13931051"),
	("14041930","14041930"),
	("13926388","13926388"),
	("13888144","13888144"),
	("14027519","14027519"),
	("14009355","14009355"),
	("14043950","14043950"),
	("14001498","14001498"),
	("13952656","13952656"),
	("13932098","13932098"),
	("14030661","14030661"),
	("13898104","13898104"),
	("13938024","13938024"),
	("13932107","13932107"),
	("13999592","13999592"),
	("13997175","13997175"),
	("13997407","13997407"),
	("13926378","13926378"),
	("13898139","13898139"),
	("13948858","13948858"),
	("13733588","13733588"),
	("13934665","13934665"),
	("13946820","13946820"),
	("14034877","14034877"),
	("13997155","13997155"),
	("13952669","13952669"),
	("14043694","14043694"),
	("13955269","13955269"),
	("13961046","13961046"),
	("13930522","13930522"),
	("14018784","14018784"),
	("12912725","12912725"),
	("13959832","13959832"),
	("13964987","13964987"),
	("14027965","14027965"),
	("14019556","14019556"),
	("13995604","13995604"),
	("13895266","13895266"),
	("14000044","14000044"),
	("13988518","13988518"),
	("14017667","14017667"),
	("14000065","14000065"),
	("14013492","14013492"),
	("13997171","13997171"),
	("13939229","13939229"),
	("13959836","13959836"),
	("13921358","13921358"),
	("13982980","13982980"),
	("13999754","13999754"),
	("13988507","13988507"),
	("13292262","13292262"),
	("14013562","14013562"),
	("14027087","14027087"),
	("13985076","13985076"),
	("14001181","14001181"),
	("13997176","13997176"),
	("13939235","13939235"),
	("14041644","14041644"),
	("14017744","14017744"),
	("13776596","13776596"),
	("13932092","13932092"),
	("13982818","13982818"),
	("14009194","14009194"),
	("13958211","13958211"),
	("13997423","13997423"),
	("14010081","14010081"),
	("14013576","14013576"),
	("14013490","14013490"),
	("14013526","14013526"),
	("14018039","14018039"),
	("14018064","14018064"),
	("14034943","14034943"),
	("14027707","14027707"),
	("14018055","14018055"),
	("14042105","14042105"),
	("14019479","14019479"),
	("14026785","14026785"),
	("14018130","14018130"),
	("14018169","14018169"),
	("14018124","14018124"),
	("14070899","14070899"),
	("13965991","13965991"),
	("14057805","14057805"),
	("14058377","14058377"),
	("14055167","14055167"),
	("14050049","14050049"),
	("14047262","14047262"),
	("14058363","14058363"),
	("14067291","14067291"),
	("14038348","14038348"),
	("14049965","14049965"),
	("14054893","14054893"),
	("14058321","14058321"),
	("14058388","14058388"),
	("14047321","14047321"),
	("14047186","14047186"),
	("14030708","14030708"),
	("14047764","14047764"),
	("14058620","14058620"),
	("14047164","14047164"),
	("14047584","14047584"),
	("14055370","14055370"),
	("14058612","14058612"),
	("14047796","14047796"),
	("14058279","14058279"),
	("14057993","14057993"),
	("14047517","14047517"),
	("14030487","14030487"),
	("14063802","14063802"),
	("14047720","14047720"),
	("14058303","14058303"),
	("14047771","14047771"),
	("14027750","14027750"),
	("14063433","14063433"),
	("14073501","14073501"),
	("14073245","14073245"),
	("14070884","14070884"),
	("14067285","14067285"),
	("14067287","14067287"),
	("14070625","14070625"),
	("14067344","14067344"),
	("14073459","14073459"),
	("14070725","14070725"),
	("14066937","14066937"),
	("14073408","14073408"),
	("14070570","14070570"),
	("14073533","14073533"),
	("14073538","14073538"),
	("14073197","14073197"),
	("14070880","14070880"),
	("14070575","14070575"),
	("14063177","14063177"),
	("14055182","14055182"),
	("14066995","14066995"),
	("14067300","14067300"),
	("14070902","14070902"),
	("14073475","14073475"),
	("14179176","14179176"),
	("14190487","14190487"),
	("14193885","14193885"),
	("14190463","14190463"),
	("14267919","14267919"),
	("14294906","14294906"),
	("14305828","14305828"),
	("14374304","14374304"),
	("14374281","14374281"),
	("14374314","14374314"),
	("14397895","14397895"),
	("14384252","14384252"),
	("14379787","14379787"),
	("14397864","14397864"),
	("14417476","14417476"),
	("14435516","14435516"),
	("14454575","14454575"),
	("14450842","14450842"),
	("14437050","14437050"),
	("14447162","14447162"),
	("14476659","14476659"),
	("14460430","14460430"),
	("14469356","14469356"),
	("14466696","14466696"),
	("14473668","14473668"),
	("14473689","14473689"),
	("14476556","14476556"),
	("14466854","14466854"),
	("14473709","14473709"),
	("14476623","14476623"),
	("14473585","14473585"),
	("14475004","14475004"),
	("14480892","14480892"),
	("14495550","14495550"),
	("14491844","14491844"),
	("14506929","14506929"),
	("14522823","14522823"),
	("14527768","14527768"),
	("14512647","14512647"),
	("14526962","14526962"),
	("14558752","14558752"),
	("14537027","14537027"),
	("14542699","14542699"),
	("14506962","14506962"),
	("14512721","14512721"),
	("14506873","14506873"),
	("14558788","14558788"),
	("14506914","14506914"),
	("14558794","14558794"),
	("14546886","14546886"),
	("14532577","14532577"),
	("14522822","14522822"),
	("14522606","14522606"),
	("14522821","14522821"),
	("14506884","14506884"),
	("14558768","14558768"),
	("14542623","14542623"),
	("14522517","14522517"),
	("14512676","14512676"),
	("14537067","14537067"),
	("14522386","14522386"),
	("14516690","14516690"),
	("14516610","14516610"),
	("14516554","14516554"),
	("14565502","14565502"),
	("14565484","14565484"),
	("14565479","14565479"),
	("14621786","14621786"),
	("14573417","14573417"),
	("14640694","14640694"),
	("14641219","14641219"),
	("14522699","14522699"),
	("14558601","14558601"),
	("14522573","14522573"),
	("14677570","14677570"),
	("14697150","14697150"),
	("14710706","14710706"),
	("14697182","14697182"),
	("14712070","14712070"),
	("14710639","14710639"),
	("14718750","14718750"),
	("14705697","14705697"),
	("14705696","14705696"),
	("14703735","14703735"),
	("14706022","14706022"),
	("14705711","14705711"),
	("14734114","14734114"),
	("14734189","14734189"),
	("14742635","14742635"),
	("14782226","14782226"),
	("14737184","14737184"),
	("14785061","14785061"),
	("14790749","14790749"),
	("14819892","14819892"),
	("14835759","14835759"),
	("14805133","14805133"),
	("14819852","14819852"),
	("14819853","14819853"),
	("14819870","14819870"),
	("14819815","14819815"),
	("14805057","14805057"),
	("14819743","14819743"),
	("14823889","14823889"),
	("14814454","14814454"),
	("14819787","14819787"),
	("14819754","14819754"),
	("14819736","14819736"),
	("14823992","14823992"),
	("14819751","14819751"),
	("14830762","14830762"),
	("14824004","14824004"),
	("14814256","14814256"),
	("14819764","14819764"),
	("14823879","14823879"),
	("14819770","14819770"),
	("14823969","14823969"),
	("14819886","14819886"),
	("14819900","14819900"),
	("14823939","14823939"),
	("14819783","14819783"),
	("14824009","14824009"),
	("14824016","14824016"),
	("14823946","14823946"),
	("14819798","14819798"),
	("14895352","14895352"),
	("14824023","14824023"),
	("14830641","14830641"),
	("14835911","14835911"),
	("14835879","14835879"),
	("14843293","14843293"),
	("14830738","14830738"),
	("14857459","14857459"),
	("14865870","14865870"),
	("14857421","14857421"),
	("14886466","14886466"),
	("14857427","14857427"),
	("14875519","14875519"),
	("14857503","14857503"),
	("14891606","14891606"),
	("14881861","14881861"),
	("14875776","14875776"),
	("14896479","14896479"),
	("14891885","14891885"),
	("14896496","14896496"),
	("14889415","14889415"),
	("14904935","14904935"),
	("14908943","14908943"),
	("14903395","14903395"),
	("14903387","14903387"),
	("14933573","14933573"),
	("14903080","14903080"),
	("14903479","14903479"),
	("14933504","14933504"),
	("14939568","14939568"),
	("14915878","14915878"),
	("14931147","14931147"),
	("14939341","14939341"),
	("14951986","14951986"),
	("14959115","14959115"),
	("14965620","14965620"),
	("15011109","15011109"),
	("14986189","14986189"),
	("15049239","15049239"),
	("15039436","15039436"),
	("15062616","15062616"),
	("15038781","15038781"),
	("15049676","15049676"),
	("15080126","15080126"),
	("15079907","15079907"),
	("15132967","15132967"),
	("15104473","15104473"),
	("15132969","15132969"),
	("15132860","15132860"),
	("15097767","15097767"),
	("15097809","15097809"),
	("15118204","15118204"),
	("12909893","12909893"),
	("15132887","15132887"),
	("15294641","15294641"),
	("15302199","15302199"),
	("15168046","15168046"),
	("15200918","15200918"),
	("15170627","15170627"),
	("15183053","15183053"),
	("15206454","15206454"),
	("15200520","15200520"),
	("15214576","15214576"),
	("15200187","15200187"),
	("15200190","15200190"),
	("15234034","15234034"),
	("15200161","15200161"),
	("15200562","15200562"),
	("15214840","15214840"),
	("15206470","15206470"),
	("15221284","15221284"),
	("15214810","15214810"),
	("15232255","15232255"),
	("15222287","15222287"),
	("15365731","15365731"),
	("15232216","15232216"),
	("15222209","15222209"),
	("15222314","15222314"),
	("15256254","15256254"),
	("15325481","15325481"),
	("15336492","15336492"),
	("15287741","15287741"),
	("15302468","15302468"),
	("15302442","15302442"),
	("15294466","15294466"),
	("15294224","15294224"),
	("15338020","15338020"),
	("15343065","15343065"),
	("15334835","15334835"),
	("15333409","15333409"),
	("15374479","15374479"),
	("15350101","15350101"),
	("15448057","15448057"),
	("15350089","15350089"),
	("15369539","15369539"),
	("15362574","15362574"),
	("15350116","15350116"),
	("15369556","15369556"),
	("15374493","15374493"),
	("15387845","15387845"),
	("15387849","15387849"),
	("15383712","15383712"),
	("15374432","15374432"),
	("15383788","15383788"),
	("15378187","15378187"),
	("15390390","15390390"),
	("15383741","15383741"),
	("12899930","12899930"),
	("10890730","10890730"),
	("15393336","15393336"),
	("15424170","15424170"),
	("15424149","15424149"),
	("15411577","15411577"),
	("15415328","15415328"),
	("15415349","15415349"),
	("15550653","15550653"),
	("15424145","15424145"),
	("15420173","15420173"),
	("15424178","15424178"),
	("15433821","15433821"),
	("15424188","15424188"),
	("15420188","15420188"),
	("15498090","15498090"),
	("15441657","15441657"),
	("15437994","15437994"),
	("15481450","15481450"),
	("15486364","15486364"),
	("15468340","15468340"),
	("15481430","15481430"),
	("15510548","15510548"),
	("15514446","15514446"),
	("15510516","15510516"),
	("15474143","15474143"),
	("15510514","15510514"),
	("15538533","15538533"),
	("15538263","15538263"),
	("15257363","15257363"),
	("15302324","15302324"),
	("15257712","15257712"),
	("15383703","15383703"),
	("15302279","15302279"),
	("15268000","15268000"),
	("15277515","15277515"),
	("15556361","15556361"),
	("15257335","15257335"),
	("15533416","15533416"),
	("15257642","15257642"),
	("15257415","15257415"),
	("15239464","15239464"),
	("15238450","15238450"),
	("15267929","15267929"),
	("15315765","15315765"),
	("15522383","15522383"),
	("15277601","15277601"),
	("15268201","15268201"),
	("15239786","15239786"),
	("15268142","15268142"),
	("15257596","15257596"),
	("15239673","15239673"),
	("15257696","15257696"),
	("15257282","15257282"),
	("15316145","15316145"),
	("15308285","15308285"),
	("15302238","15302238"),
	("15268042","15268042"),
	("15257051","15257051"),
	("15249954","15249954"),
	("15268095","15268095"),
	("15552424","15552424"),
	("15556348","15556348"),
	("15558472","15558472"),
	("15545847","15545847"),
	("15552413","15552413"),
	("15565191","15565191"),
	("15562350","15562350"),
	("15565140","15565140"),
	("15565116","15565116"),
	("15583921","15583921"),
	("15579579","15579579"),
	("15579373","15579373"),
	("15628570","15628570"),
	("15621652","15621652"),
	("15622432","15622432"),
	("15579362","15579362"),
	("15621469","15621469"),
	("15701447","15701447"),
	("15655603","15655603"),
	("15698098","15698098"),
	("15628445","15628445"),
	("15594826","15594826"),
	("15689813","15689813"),
	("15817059","15817059"),
	("15710813","15710813"),
	("15704387","15704387"),
	("16012722","16012722"),
	("15754748","15754748"),
	("15817057","15817057"),
	("15817061","15817061"),
	("15257099","15257099"),
	("15257093","15257093"),
	("15257227","15257227"),
	("15831093","15831093"),
	("15257151","15257151"),
	("15846759","15846759"),
	("16055778","16055778"),
	("16013615","16013615"),
	("16034743","16034743"),
	("16043309","16043309"),
	("16043435","16043435"),
	("16792055","16792055"),
	("16845046","16845046"),
	("16833882","16833882"),
	("16862298","16862298"),
	("16862370","16862370"),
	("16862313","16862313"),
	("16896105","16896105"),
	("16892458","16892458"),
	("16913763","16913763"),
	("16935255","16935255"),
	("16998705","16998705"),
	("17027819","17027819"),
	("17077850","17077850"),
	("17080767","17080767"),
	("17136929","17136929"),
	("17163086","17163086"),
	("17173203","17173203"),
	("17202332","17202332"),
	("17242537","17242537"),
	("17242824","17242824"),
	("17242954","17242954"),
	("17242650","17242650"),
	("17242925","17242925"),
	("17242785","17242785"),
	("17242989","17242989"),
	("17242772","17242772"),
	("17243233","17243233"),
	("13761517","13761517"),

	)

VALUE = (


	("кг","кг"),
	("шт","шт"),
	("п.м.","п.м."),
	("см","см"),

	)	
	

CATEGORYS = [

	("Дома","Дома"),
	("Дворы","Дворы"),
	("Дороги","Дороги"),
	("Парки-скверы","Парки-скверы"),

]

####################################Информация о заявке по заданному мкд#####################

class Южное_Медведково (models.Model):
	user = models.ForeignKey(User,related_name='Южное_Медведково')
	#cтатус = models.ForeignKey(Status)
	Статус = models.CharField(max_length=30, choices=STATUS)
	номер_заявки = models.CharField(max_length=30, choices=NUMBERS)
	#номер_заявки = models.DecimalField(max_digits = 8,help_text='Минимальное кол-во символов 8, пример:12345678', decimal_places = 0, default = None)
	адрес = models.CharField(max_length=30, choices=HOMES)
	проблемная_тема = models.CharField(max_length=128,choices=THEMS)
	примечание =models.TextField(max_length=750,blank=True, null = True, default= None,help_text='Максимальное кол-во символов 750')
	фото = models.ImageField(upload_to = 'user_media/акты', blank=True)
	Файл = models.FileField(upload_to='user_media/files', blank =True)
	добавлено = models.DateTimeField(auto_now_add = True, auto_now=False,)
	обновлено = models.DateTimeField(auto_now=True)

	
	def __str__(self):
		return "%s; %s" % (self.адрес,self.номер_заявки) # отображаем в админке атрибут: email

	class Meta:
		verbose_name = " - Информация о заявке"
		verbose_name_plural = 'Информация о заявках' # переименуем название в админке 	 	


class справочник_материалов(models.Model):
	id_материала = models.AutoField(primary_key=True)
	категория = models.CharField(max_length=100, choices=CATEGORY)
	наименование_материала = models.CharField(max_length=150, choices=MATERIALS)
	кол_во = models.IntegerField(default=0, validators=[MaxValueValidator(99), MinValueValidator(1)],help_text='значение не может быть раным: 0')
	единица_измерения = models.CharField(max_length=10, choices=VALUE) 
	примечание = models.TextField(max_length=650, blank=True)
	

	def __str__(self):
		return "%s; %s" % (self.категория,self.наименование_материала) # отображаем в админке атрибут: email

	class Meta:
		verbose_name = " справочник материал"
		verbose_name_plural = 'справочник материалов' # пер


################## Обращение гражданина-пользователя о проблеме в его доме############################

class  мкд(models.Model): # мкд (многоквартирный дом)
	вид_работ	 = models.CharField(max_length=60, choices=CATEGORYS)
	адрес = models.CharField(max_length=60, choices=HOMES)
	номер_подъезда = models.IntegerField(default=0,validators=[MaxValueValidator(10), MinValueValidator(1)],help_text='значение не может быть раным: 0')
	этаж = models.IntegerField(default='',validators=[MaxValueValidator(25), MinValueValidator(0)],help_text='укажите этаж, если требуется')
	#num = models.PositiveIntegerField(validators=[MinValueValidator(1)])
	проблемная_тема = models.CharField(max_length=128,choices=THEMS)
	сообщение = models.TextField(max_length=1250,blank=True, null = True, default= None,help_text='Максимальное кол-во символов: 1250')
	фотоматериал = models.ImageField(upload_to = 'users_photo/%d.%m.%Y/', null=False,blank=True)
	#файл = models.FileField(upload_to='user_media/files', blank =True)
	добавлено = models.DateTimeField(auto_now_add = True, auto_now=False,)
	обновлено = models.DateTimeField(auto_now=True)
	требуемый_материал = models.ForeignKey(справочник_материалов)


	def bit(self):
		if self.фотоматериал:
			return u'<a href="{0}" target="_blank"><img src="{0}" width="150"/></a>'.format(self.фотоматериал.url)
		else:
			return '(Нет изображения)'
	bit.short_description = 'Фотоматериал'
	bit.allow_tags = True


	def __str__(self):
		return "%s; %s" % (self.адрес,self.сообщение) # отображаем в админке атрибут: email

	class Meta:
		verbose_name = " - Информация о многоквартирном доме"
		verbose_name_plural = 'Информация о многоквартирных домах' # переименуем название в админке 




# class user(models.Model):
# 	name =
# 	email =




# Create your models here.
