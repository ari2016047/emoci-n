from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.urls import reverse
from googletrans import Translator
import json
import speech_recognition as sr

translator = Translator(service_urls=[
			'translate.google.com',
			'translate.google.co.kr',
		])


def MainPage(request):
	context = {}
	
	return render(request, 'blog/MainPage.html', context)

# def SpeechToText(request):
# 	context = {}
# 	r = sr.Recognizer()
# 	with sr.Microphone() as source:
# 		r.adjust_for_ambient_noise(source)
# 		print("Say something!")
# 		audio = r.listen(source)
# 		print("Done!")

# 	try:
# 		context = {
# 			"result": r.recognize_google(audio)
# 		}
# 		print("You said: " + r.recognize_google(audio))
# 	except Exception as e:
# 		print (e)

# 	return render(request, 'blog/Python.html', context)


def Translate(request):
	username = " "
	context={}
	result_text = " "
	print(1)
	print("inside translations before ",username)

	if request.method == 'GET':
		username = request.GET.get('username', None)
			# data = {
			# 	'is_taken': objects.filter(username__iexact=username).exists()
			# }
			# if data['is_taken']:
			# 	data['error_message'] = 'A user with this username already exists.'
		print("thsi is in translate after ",username)
		# if username == None:
		# 	username = "1"

		translations = translator.translate([username], dest='en')
		
		for translation in translations:
		# print(translation.origin, ' -> ', translation.text)
			result_text += translation.text

		print("Result = "  +result_text)

		context = {
			"result": result_text
		}

		print("before render ")

		# def get_object(self, queryset=None, *args, **kwargs):
		# 	title = self.kwargs.get("title")
		# 	self.model.objects.get('title')=result_text
		# 	print(self.model.objects.get('title'))

		obj = json.dumps(context)
		print("oo")
		return HttpResponse(obj, content_type='application/json')
