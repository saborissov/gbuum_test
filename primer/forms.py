from django import forms
from django .forms import ModelForm
from primer.models import Feedback
from django.core.mail import send_mail



class FeedbackForm(ModelForm):

	class Meta:
		model = Feedback
		fields = '__all__'		
		widgets = {
			'ФИО':forms.TextInput(attrs={'placeholder':'Введите ваше Ф.И.О.', 'class':'form-control' }),
			'Email':forms.EmailInput(attrs={'placeholder':'Почта', 'class':'form-control' }),
			'Проблема':forms.Textarea(attrs={'placeholder':'Опишите проблему', 'class':'form-control' }),
			#'address':forms.Select(attrs={'placeholder':'Сообщение', 'class':'form-control' }),

			#'date_create':forms.DateTimeWidget(attrs={'placeholder':'Сообщение', 'class':'form-control' }),
			
		}	
		# labels = {
		# 	'фио': 'ФИО',
		# 	'email':'Электронная почта',
		# 	'проблема': 'Проблема'

		# }



# class FeedbackForm(forms.ModelForm):
# 	class Meta:
# 		model=Feedback
# 		fields = [
# 			'name',
# 			'email',
# 			'text'
# 		]
# 		widgets = {
# 			'name':forms.TextInput(attrs={'placeholder':'Имя', 'class':'form-control' }),
# 			'email':forms.EmailInput(attrs={'placeholder':'Почта', 'class':'form-control' }),
# 			'text':forms.Textarea(attrs={'placeholder':'Сообщение', 'class':'form-control' }),


# 		}	

		