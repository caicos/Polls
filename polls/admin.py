from django.contrib import admin

from .models import Question, Choice

# les objets Choice sont édités dans la page d’administration de Question. Par défaut, fournir assez de place pour 3 choix
# Avec tabular, les objets sont affichés sous forme de tableau
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')      # Par défaut, Django affiche le str() de chaque objet. L’option list_display est un tuple de noms de champs particuliers à afficher en colonnes.
    list_filter = ['pub_date']                                                  # ajoute une barre latérale "Filter" pour filtrer la liste selon le champ "pub_date"
    search_fields = ['question_text']                                           # ajoute une fonction (boîte) de recherche

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)
