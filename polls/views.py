from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic    # Nous utlisions ici 2 vues génériques : ListView et DetailView.Respectivement, ces deux vues permettent l’abstraction des concepts « afficher une liste d’objets » et « afficher une page détaillée pour un type particulier d’objet ».
from django.utils import timezone
from django.utils.translation import gettext as _
from django.utils.translation import gettext_noop

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions (not including those set to be published in the future)."""
        return Question.objects.filter(pub_date__lte = timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Esclue toutes questions n'étant pas encore publiées
        """
        return Question.objects.filter(pub_date__lte = timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])  # request.POST est similaire à un dictionnaire dont les valeurs sont tjrs des chaines de caractères
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message' : "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1 # Il peut y avoir une "situation de compétition" entre 2 utilisateurs qui voterait en même temps. Lire "Prévention des conflits de concurrence avec F()"
        selected_choice.save()
        # always return an HttpResponseRedirect after successfully dealing with POST data.
        # This prevents data from being posted twice if a user hits the back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def mytranslateview(request):
    context = {
        'static_string_1' : gettext_noop('Première phrase statique à traduire'),
        'static_string_2' : gettext_noop('Seconde phrase statique à traduire'),
        'second_paragraph' : _('Ceci est le second paragraphe à traduire'),      # la traduction s'effectue directement dans le code python
    }
    return render(request, 'polls/my_translate_template.html', context)
    # On utilise la fonction "gettext_lazy()" dans une définition de modèle ou de formulaire et "gettext()" dans une vue
    # En règle générale : Si vous devez appeler la fonction sur une chaîne à un moment où Django ne sait pas encore quelle langue utiliser, utilisez gettext_lazy(). La chaîne ne sera traduite qu’au dernier moment (au moment de son rendu).

def matraduc(request):
    context = {
        'static_string_1' : gettext_noop('Première phrase statique à traduire'),
        'static_string_2' : gettext_noop('Seconde phrase statique à traduire'),
        'second_paragraph' : _('Ceci est le second paragraphe à traduire'),      # la traduction s'effectue directement dans le code python
    }
    return render(request, 'polls/Page_essai_traduction.html', context)
