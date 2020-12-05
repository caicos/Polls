from django.contrib import admin

from .models import Question

# Personnalisation de l'affichage et du comportement du formulaire pour le modèle "Question"
# Cette méthode (de  créer une classe d’administration de modèle, puis le transmettre en tant que deuxième paramètre de admin.site.register())
# permet de modifier les options d’administration pour un modèle.
# Le champ « Date de publication » est maintenant affiché avant le champ « Question »
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
