from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from primer.forms import FeedbackForm
from primer.models import Feedback
from primer.models import Feedback_done
from Computers_and_other_equipment.models import Компьютеры_оргтехника
from Computers_and_other_equipment.models import Уникальный_номер
from Computers_and_other_equipment.models import Справочник_мест_установки
from Сотрудники.models import Сотрудники
from django.db.models import Count
from .models import *
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage    
from django.core.mail import EmailMultiAlternatives
from django.core import mail
from django.template.loader import render_to_string, get_template
from django.forms.models import model_to_dict
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
#from Computers_and_other_equipment.models import Принтеры_картриджи
from django.contrib.auth.models import User
from django.contrib import auth 
import csv   
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
 
def index (request):
	if request.POST:
		data = Feedback(name=request.POST.get('data_name'))
		data.save()
	form = FeedbackForm()
	data = { "form": form }
	return render(request,'base.html', data)
 
 
# Create your views here.
 
def index2 (request):
	person = Feedback.objects.all()
	context = {'person': person}
	return render(request, 'primer/list.html',context)
 
def thanks (request):
	return render_to_response('primer/thanks.html',{'zayavka':Feedback.objects.all()}) 
	#return render(request,'primer/thanks.html') 

def login (request):
	return render_to_response('primer/login.html',{'zayavka':Feedback.objects.all()})

def comments (request):
	return render_to_response('primer/comments.html',{'zayavka':Feedback.objects.all()})    




# def test (request):
#     return render_to_response('primer/zayavki.html',{'zayavka':Feedback_done.objects.all()})



# def test (request):
# 	return render_to_response('primer/zayavki.html',  {'zayavka':Feedback.objects.all(),
# 			'zayavka_done':Feedback_done.objects.all()
# 		})


def test (request):
	zayavki = Feedback.objects.all()
	paginator = Paginator(zayavki, 1)
	page = request.GET.get('page')
	try:
			zayavki = paginator.page(page)
	except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			zayavki = paginator.page(1)
	except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			zayavki = paginator.page(paginator.num_pages)
	

	# category = Компьютеры_оргтехника.objects.filter('') 
	# context2 = {'category': category}   
	 
	return render_to_response('primer/zayavki.html',  {'zayavka':Feedback.objects.all(),
			'zayavka_done':Feedback_done.objects.all()
		})  

# def computers_and_other (request):
# 	person = Компьютеры_оргтехника.objects.all()
# 	# page = request.GET.get('page')
# 	# try:
# 	# 		person = paginator.page(page)
# 	# except PageNotAnInteger:
# 	# 		# If page is not an integer, deliver first page.
# 	# 		person = paginator.page(1)
# 	# except EmptyPage:
# 	# 		# If page is out of range (e.g. 9999), deliver last page of results.
# 	# 		person = paginator.page(paginator.num_pages)
	

# 	# category = Компьютеры_оргтехника.objects.filter('') 
# 	# context2 = {'category': category}   
	
# 	return render(request, 'primer/computers_and_other.html',{"person": person})


def computers_and_other (request):
	person = Компьютеры_оргтехника.objects.all()
	#args['username']=auth.get_user(request).username

	# paginator = Paginator(person, 10)
	# page = request.GET.get('page')

	# try:
	# 		person = paginator.page(page)
	# except PageNotAnInteger:
	# 		# If page is not an integer, deliver first page.
	# 		person = paginator.page(1)
	# except EmptyPage:
	# 		# If page is out of range (e.g. 9999), deliver last page of results.
	# 		person = paginator.page(paginator.num_pages)
	

	# category = Компьютеры_оргтехника.objects.filter('') 
	# context2 = {'category': category}   

	return render_to_response('primer/computers_and_other.html',  {'person':Компьютеры_оргтехника.objects.all(),'username': auth.get_user(request).username })  
	#return render(request, 'primer/computers_and_other.html',{"person": person})

   
def printers_cartridge (request):

	printer = Принтеры_картриджи.objects.all()
	# paginator = Paginator(person, 10)
	# page = request.GET.get('page')

	# try:
	# 		person = paginator.page(page)
	# except PageNotAnInteger:
	# 		# If page is not an integer, deliver first page.
	# 		person = paginator.page(1)
	# except EmptyPage:
	# 		# If page is out of range (e.g. 9999), deliver last page of results.
	# 		person = paginator.page(paginator.num_pages,count)
	

	# category = Компьютеры_оргтехника.objects.filter('') 
	# context2 = {'category': category}   
	
	return render(request, 'primer/computers_and_other.html', {"person": person})

# def computers_and_other (request):
#     return render_to_response('primer/computers_and_other.html',{'computers':Компьютеры_оргтехника.objects('категория', 'наименование')})


 
# def add_list(request):
#     if request.method == "POST":
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['name']
#             address = form.cleaned_data['address']
#             cabinet = form.cleaned_data['cabinet']
#             message = form.cleaned_data['address']
#             recipients = ['saborissov@mail.ru']
#             try:
#                 send_mail(subject, message, 'saborissov@mail.ru', recipients)
#             except BadHeaderError: #Защита от уязвимости
#                 return HttpResponse('Invalid header found')
#             post = form.save()
#             post.save()
#             return render(request, 'contactform/thank.html')                    
#     else:
#             form = FeedbackForm()
#     return render(request, 'primer/add_list.html',{'form':form})
 
 
 
 
 
def add_list (request):
	form = FeedbackForm(request.POST or None)
	if form.is_valid():
		new_feedback = form.save()        
		subject = request.POST.get('Проблема')
		from_email = request.POST.get('email')    
		receiver = ['saborissov@mail.ru','portalgbuum@gmail.com']

		feedback_item_data = model_to_dict( new_feedback )
		print (feedback_item_data)
		vars = {
			'data':feedback_item_data,
		}
 
 
		message = get_template('primer/add_list.html').render(vars)
 
		msg = EmailMessage(
						subject, message, from_email=from_email,
						to=receiver
						)
		msg.content_subtype = 'html'
		msg.mixed_subtype = 'related'
		msg.send()
		

		#send_mail(subject, message, from_email,['saborissov@mail.ru,','portal-gbuum@mail.ru'], fail_silently=False)
		#return HttpResponse('/thanks/')
		return HttpResponseRedirect('/thanks/')   
		
		#send_mail('ГБУ "Жилижник района Южное Медведково', request.POST.get('text'),  'saborissov@mail.ru',['saborissov@mail.ru','portal-gbuum@mail.ru'], fail_silently=False)
		#send_mail('ГБУ "Жилижник района Южное Медведково', ' Сообщение о проблемной теме: datasent: %s %s %s'%(name,text,email), 'saborissov@mail.ru',   ['saborissov@mail.ru','portal-gbuum@mail.ru'], fail_silently=False)
		return HttpResponseRedirect('/index2/')
	return render(request, 'primer/add_list.html',{'form':form})



############# Выгрузка данных о пользователях ############  
 
# def export_users_csv (request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="users.csv"'

#     writer = csv.writer(response)
#     writer.writerow(['Username', 'First name', 'Last name', 'Email address'])

#     users = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
#     for user in users:
#         writer.writerow(user)

#     return response


########## ВЫГРУЗКА ДАННЫХ О ЗАЯВКАХ ######################

def export_users_csv (request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="zayavki.csv"'

	writer = csv.writer(response)
	writer.writerow(['ФИО', 'Проблема', 'Отдел', 'Адрес', 'статус'])

	users = Feedback.objects.all().values_list('ФИО', 'Проблема', 'Отдел', 'Адрес','статус')
	for user in users:
		writer.writerow(user)

	return response    
 
def export_comps_csv (request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="comps.csv"'

	writer = csv.writer(response)
	writer.writerow(['Мол','Инвентарный номер','наименование', 'категория', 'модель_устройства', 'Место установки/Адрес','Место установки/кабинет', 'статус'])

	users = Компьютеры_оргтехника.objects.all().values_list('материально_ответственный__фио','barcode__инвентарный_номер','наименование', 'категория', 'модель_устройства','id_места_установки__адрес','id_места_установки__кабинет', 'статус')
	for user in users:
		writer.writerow(user)

	return response   
 
 
 
# def add_list (request):
#     form = FeedbackForm(request.POST or None)
#     if request.POST:
#         person = Feedback(name=request.POST.get('person_name'))
#         person.save()
#         return HttpResponseRedirect('/index2/')
#     return render(request, 'primer/add_list.html')