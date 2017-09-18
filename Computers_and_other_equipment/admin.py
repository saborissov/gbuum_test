from django.contrib import admin
from Computers_and_other_equipment.models import Компьютеры_оргтехника, Уникальный_номер, Фиксация_перемещения,Списанное_оборудование, Справочник_мест_установки, Принтер, Картридж, Cartridge_list, List_of_printer

class Уникальный_номерAdmin (admin.ModelAdmin):
	#list_display = ['name','email']
	list_display = [field.name for field in Уникальный_номер._meta.fields]
	#list_filter = ['наименование'] # выводим фильтр по атрибуту - name
	#search_fields = ['наименование'] #Возможность поиска по указанному атрибуту
	#exclude = ['email'] # исключаем из показа атрибут - email
	class Meta:
		model = Уникальный_номер

admin.site.register(Уникальный_номер, Уникальный_номерAdmin)


class ПринтерAdmin (admin.ModelAdmin):
	#list_display = ['name','email']
	list_display = [field.name for field in Принтер._meta.fields]
	#list_filter = ['наименование'] # выводим фильтр по атрибуту - name
	#search_fields = ['наименование'] #Возможность поиска по указанному атрибуту
	#exclude = ['email'] # исключаем из показа атрибут - email
	class Meta:
		model = Принтер

admin.site.register(Принтер, ПринтерAdmin)


class КартриджAdmin (admin.ModelAdmin):
	#list_display = ['name','email']
	list_display = [field.name for field in Картридж._meta.fields]
	#list_filter = ['наименование'] # выводим фильтр по атрибуту - name
	#search_fields = ['наименование'] #Возможность поиска по указанному атрибуту
	#exclude = ['email'] # исключаем из показа атрибут - email
	class Meta:
		model = Картридж

admin.site.register(Картридж, КартриджAdmin)


class Cartridge_listAdmin (admin.ModelAdmin):
	#list_display = ['name','email']
	list_display = [field.name for field in Cartridge_list._meta.fields]
	#list_filter = ['наименование'] # выводим фильтр по атрибуту - name
	#search_fields = ['наименование'] #Возможность поиска по указанному атрибуту
	#exclude = ['email'] # исключаем из показа атрибут - email
	class Meta:
		model = Cartridge_list

admin.site.register(Cartridge_list, Cartridge_listAdmin)


class List_of_printerAdmin (admin.ModelAdmin):
	#list_display = ['name','email']
	list_display = [field.name for field in List_of_printer._meta.fields]
	#list_filter = ['наименование'] # выводим фильтр по атрибуту - name
	#search_fields = ['наименование'] #Возможность поиска по указанному атрибуту
	#exclude = ['email'] # исключаем из показа атрибут - email
	class Meta:
		model = List_of_printer

admin.site.register(List_of_printer, List_of_printerAdmin)

class Компьютеры_оргтехникаAdmin (admin.ModelAdmin):
	#list_display = ['name','email']
	list_display = [field.name for field in Компьютеры_оргтехника._meta.fields]
	list_filter = ['категория','статус','наименование','картридж','id_места_установки__адрес'] # выводим фильтр по атрибуту - name
	search_fields = ['barcode__инвентарный_номер', 'id_места_установки__адрес',] #Возможность поиска по указанному атрибуту
	#exclude = ['email'] # исключаем из показа атрибут - email
	class Meta:
		model = Компьютеры_оргтехника

admin.site.register(Компьютеры_оргтехника, Компьютеры_оргтехникаAdmin)
# Register your models here.


class Справочник_мест_установкиAdmin (admin.ModelAdmin):
	#list_display = ['name','email']
	list_display = [field.name for field in Справочник_мест_установки._meta.fields]
	#list_filter = ['фамилия'] # выводим фильтр по атрибуту - name
	#search_fields = ['фамилия',] #Возможность поиска по указанному атрибуту
	#exclude = ['email'] # исключаем из показа атрибут - email
	class Meta:
		model = Справочник_мест_установки

admin.site.register(Справочник_мест_установки, Справочник_мест_установкиAdmin)


# class ПеремещениеAdmin (admin.ModelAdmin):
# 	#list_display = ['name','email']
# 	list_display = [field.name for field in Перемещение._meta.fields]
# 	list_filter = ['адрес','кабинет'] # выводим фильтр по атрибуту - name
# 	#raw_id_fields = ['инвентарный_номер',] #поиск по id
# 	#search_fields = ['наименование'] #Возможность поиска по указанному атрибуту
# 	#exclude = ['email'] # исключаем из показа атрибут - email
# 	class Meta:
# 		model = Перемещение

# admin.site.register(Перемещение, ПеремещениеAdmin)


class Фиксация_перемещенияAdmin (admin.ModelAdmin):
	#list_display = ['name','email']
	list_display = [field.name for field in Фиксация_перемещения._meta.fields]
	#list_filter = ['наименование','адрес_местонахождения'] # выводим фильтр по атрибуту - name
	search_fields = ['наименование'] #Возможность поиска по указанному атрибуту
	#exclude = ['email'] # исключаем из показа атрибут - email
	class Meta:
		model = Фиксация_перемещения

admin.site.register(Фиксация_перемещения, Фиксация_перемещенияAdmin)


class Списанное_оборудованиеAdmin (admin.ModelAdmin):
	#list_display = ['name','email']
	list_display = [field.name for field in Списанное_оборудование._meta.fields]
	list_filter = ['наименование','адрес_местонахождения'] # выводим фильтр по атрибуту - name
	#search_fields = ['наименование'] #Возможность поиска по указанному атрибуту
	#exclude = ['email'] # исключаем из показа атрибут - email
	class Meta:
		model = Списанное_оборудование

admin.site.register(Списанное_оборудование, Списанное_оборудованиеAdmin)

