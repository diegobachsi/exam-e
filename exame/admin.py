from django.contrib import admin

from .models import Questao, Exame

class QuestaoAdmin(admin.ModelAdmin):

    list_display = ['cod_exame', 'pergunta', 'resposta']
    search_fields = ['cod_exame']

admin.site.register(Questao, QuestaoAdmin)

class ExameAdmin(admin.ModelAdmin):

    list_display = ['cod_exame']
    search_fields = ['cod_exame']

admin.site.register(Exame, ExameAdmin)
