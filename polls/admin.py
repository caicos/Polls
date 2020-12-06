from django.contrib import admin

from .models import Question, Choice

# Personnalisation de l'affichage et du comportement du formulaire pour le modèle "Question"
# on partage le formulaire en plusieurs sous-ensembles (fieldsets). (Le premier élément de chaque tuple dans fieldsets est le titre du groupe de champs.)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)
