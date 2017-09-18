from django.contrib import admin
from Южное_Медведково.models import Южное_Медведково, мкд, справочник_материалов #Status




class Южное_МедведковоAdmin (admin.ModelAdmin):
	#list_display = ['name','email']
	list_display = [field.name for field in Южное_Медведково._meta.fields]
	list_filter = ['Статус','проблемная_тема'] # выводим фильтр по атрибуту - name
	search_fields = ['мкд', 'проблемная_тема', 'номер_заявки'] #Возможность поиска по указанному атрибуту
	#exclude = ['email'] # исключаем из показа атрибут - email
	class Meta:
		model = Южное_Медведково


admin.site.register(Южное_Медведково, Южное_МедведковоAdmin)


class мкдAdmin (admin.ModelAdmin):
	list_display = ['адрес','вид_работ','проблемная_тема','требуемый_материал', 'bit']
	#list_display = [field.name for field in мкд._meta.fields]
	#list_filter = ['Статус','проблемная_тема'] # выводим фильтр по атрибуту - name
	#search_fields = ['мкд', 'проблемная_тема', 'номер_заявки'] #Возможность поиска по указанному атрибуту
	#exclude = ['email'] # исключаем из показа атрибут - email
	class Meta:
		model = мкд


admin.site.register(мкд, мкдAdmin)






class справочник_материаловAdmin (admin.ModelAdmin):
	#list_display = ['name','email']
	list_display = [field.name for field in справочник_материалов._meta.fields]
	#list_filter = ['Статус','проблемная_тема'] # выводим фильтр по атрибуту - name
	#search_fields = ['мкд', 'проблемная_тема', 'номер_заявки'] #Возможность поиска по указанному атрибуту
	#exclude = ['email'] # исключаем из показа атрибут - email
	class Meta:
		model = справочник_материалов


admin.site.register(справочник_материалов, справочник_материаловAdmin)

# class StatusAdmin (admin.ModelAdmin):
# 	#list_display = ['name','email']
# 	list_display = [field.name for field in Status._meta.fields]
	
# 	#list_filter = ['мкд'] # выводим фильтр по атрибуту - name
# 	#search_fields = ['мкд', 'номер_заявки'] #Возможность поиска по указанному атрибуту
# 	#exclude = ['email'] # исключаем из показа атрибут - email
# 	class Meta:
# 		model = Status


# admin.site.register(Status, StatusAdmin)

