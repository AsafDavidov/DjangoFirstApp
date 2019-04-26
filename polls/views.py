from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from polls.models import Question
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    questions = Question.objects.all().values('question_text', 'pub_date')
    questions_list = list(questions)
    return JsonResponse(questions_list, safe=False)
# Create your views here.
