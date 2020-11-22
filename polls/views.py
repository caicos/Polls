from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic    # Nous utlisions ici 2 vues génériques : ListView et DetailView.Respectivement, ces deux vues permettent l’abstraction des concepts « afficher une liste d’objets » et « afficher une page détaillée pour un type particulier d’objet ».

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

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
