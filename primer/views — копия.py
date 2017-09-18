from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from primer.forms import FeedbackForm
from primer.models import Feedback
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMessage	
from django.core.mail import EmailMultiAlternatives
from django.core import mail
from django.template.loader import render_to_string, get_template





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



# def add_list(request):
# 	if request.method == "POST":
# 		form = FeedbackForm(request.POST)
# 		if form.is_valid():
# 			subject = form.cleaned_data['name']
# 			address = form.cleaned_data['address']
# 			cabinet = form.cleaned_data['cabinet']
# 			message = form.cleaned_data['address']
# 			recipients = ['saborissov@mail.ru']
# 			try:
# 				send_mail(subject, message, 'saborissov@mail.ru', recipients)
# 			except BadHeaderError: #Защита от уязвимости
# 				return HttpResponse('Invalid header found')
# 			post = form.save()
# 			post.save()
# 			return render(request, 'contactform/thank.html')					
# 	else:
# 			form = FeedbackForm()
# 	return render(request, 'primer/add_list.html',{'form':form})





def add_list (request):
	form = FeedbackForm(request.POST or None)
	if form.is_valid():
		vars = {
			'message': self.message,
		}

		message = get_template('primer/add_list.html').render(vars)

		receiver = 'saborissov@mail.ru'
		msg = EmailMessage(subject, message, from_email, [receiver])
		msg.content_subtype = 'primer/add_list.html'
		msg.send()

		#send_mail(subject, message, from_email,['saborissov@mail.ru,','portal-gbuum@mail.ru'], fail_silently=False)
		return HttpResponse('Спасибо уважаемый пользователь! Ваше сообщение отправлено!')

		
		#send_mail('ГБУ "Жилижник района Южное Медведково', request.POST.get('text'),  'saborissov@mail.ru',['saborissov@mail.ru','portal-gbuum@mail.ru'], fail_silently=False)
		form.save()
		#send_mail('ГБУ "Жилижник района Южное Медведково', ' Сообщение о проблемной теме: datasent: %s %s %s'%(name,text,email), 'saborissov@mail.ru',   ['saborissov@mail.ru','portal-gbuum@mail.ru'], fail_silently=False)
		return HttpResponseRedirect('/index2/')
	return render(request, 'primer/add_list.html',{'form':form})






# def add_list (request):
# 	form = FeedbackForm(request.POST or None)
# 	if request.POST:
# 		person = Feedback(name=request.POST.get('person_name'))
# 		person.save()
# 		return HttpResponseRedirect('/index2/')
# 	return render(request, 'primer/add_list.html')







