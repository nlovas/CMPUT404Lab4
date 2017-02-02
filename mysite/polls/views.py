from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
# Create your views here.

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {
	'latest_question_list':latest_question_list}
	return render(request, 'polls/index.html',context)

def detail(request, question_id):
	question= get_object_or_404(Question,pk=question_id)
	return render(request,'polls/details.html', {'question':question})
	#return HttpResponse("Hello you're at the detail page for poll " + question_id)
def vote(request,question_id):
	p = get_object_or_404(Question,pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/details.html', {'question': p,'error_message': "You didn't select a choice.",})
	else:
		selected_choice.votes += 1
		selected_choice.save()
	return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
def results(request, question_id):
	question= get_object_or_404(Question,pk=question_id)
	return HttpResponse("This page will show us wich one is most popular")
