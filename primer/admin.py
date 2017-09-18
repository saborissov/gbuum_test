from django.contrib import admin
from primer.models import Feedback, Feedback_done


class FeedbackAdmin (admin.ModelAdmin):
	#list_display = ['name','email']
	list_display = [field.name for field in Feedback._meta.fields]
	list_filter = ['Отдел','Адрес'] # выводим фильтр по атрибуту - name
	search_fields = ['ФИО'] #Возможность поиска по указанному атрибуту
	#exclude = ['email'] # исключаем из показа атрибут - email
	class Meta:
		model = Feedback

admin.site.register(Feedback, FeedbackAdmin)


class Feedback_doneAdmin (admin.ModelAdmin):
	#list_display = ['name','email']
	list_display = [field.name for field in Feedback_done._meta.fields]
	#list_filter = ['Отдел','Адрес'] # выводим фильтр по атрибуту - name
	#search_fields = ['ФИО'] #Возможность поиска по указанному атрибуту
	#exclude = ['email'] # исключаем из показа атрибут - email
	class Meta:
		model = Feedback_done

admin.site.register(Feedback_done, Feedback_doneAdmin)


# Register your models here.
