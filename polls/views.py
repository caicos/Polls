from django.shortcuts import render
from django.http import HttpResponse # uniquement utile pour les vues détails, résults et vote qui n'ont pas la fonction render()
# from django.template import loader

from .models import Question

# Ancienne fonction
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list' : latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))
#
# Ce code charge le gabarit appelé polls/index.html et lui fournit un contexte.
# Ce contexte est un dictionnaire qui fait correspondre des objets Python à des noms de variables de gabarit.

# Nouvelle fonction
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list' : latest_question_list,
    }
    return render(request, 'polls/index.html', context)
# Il est très courant de charger un gabarit, remplir un contexte et renvoyer un objet HttpResponse avec le résultat du gabarit interprété.
# Django fournit la fonction raccourci render()
# La fonction render() prend comme premier paramètre l’objet requête, un nom de gabarit comme deuxième paramètre et un dictionnaire comme troisième paramètre facultatif. Elle retourne un objet HttpResponse composé par le gabarit interprété avec le contexte donné.

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "Your're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
