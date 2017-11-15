from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response


# Create your views here.
def index(request):
    content = {}
    return render_to_response('index.html',content)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def login(request):
    print(request.post)
    return {}
