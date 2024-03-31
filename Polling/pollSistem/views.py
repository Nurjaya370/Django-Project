from django.template import loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice

# mengambil data pertanyaan daan menampilkannya


def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'pollSistem/index.html', context)

# menampilkan detail pertanyaan dan pilihan jawaban


def detail(request, question_id):
	try:
		question = Question.objects.get(pk = question_id)
	except Question.DoesNotExist:
		raise Http404("Tidak ada Data Pertanyaan")
	return render(request, 'pollSistem/detail.html', {'question': question})

# mengambil pertnyaan dan menampilkannya


def results(request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	return render(request, 'pollSistem/results.html', {'question': question})

# menampilkan pilihan jawban dari setiap pertanyaan


def vote(request, question_id):
	# menampilkan request
	question = get_object_or_404(Question, pk = question_id)
	try:
		selected_choice = question.choice_set.get(pk = request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Menampilkan kembali form Pertanyaan.
		return render(request, 'pollSistem/detail.html', {
			'question': question,
			'error_message': "Anda Belum Memilih Jawaban",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
        # HttpResponseRedirect mengembalikan respon setelah request berhasil ditangani
		return HttpResponseRedirect(reverse('pollSistem:results', args =(question.id, )))
