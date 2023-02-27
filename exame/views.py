from django.shortcuts import render

from exame.models import Questao, Exame
#import openai
import string
import random

def random_generator(size=10, chars=string.ascii_uppercase + string.digits):
 return ''.join(random.choice(chars) for _ in range(size))

def index(request):

    return render(request, 'index.html')

#def exame(request):

    context = {}

    #inicializar o cod_exame quando a chamada ao método não for via POST
    cod_exame = ""

    if request.method == "POST":

        cod_exame = request.POST["cod_exame"]

    context = { 
        'qtd_questoes': qtd_questoes(cod_exame),
        'questoes': dados_questoes(cod_exame)
    }

    return render(request, 'exame.html', context)

#def exame_via_link(request, cod_exame):

    context = {}

    print(cod_exame)

    context = { 
        'qtd_questoes': qtd_questoes(cod_exame),
        'questoes': dados_questoes(cod_exame)
    }

    return render(request, 'exame.html', context)

#def gerar_exame(request):

    context = {}

    if request.method == "POST":

        tema = request.POST["tema"]
        qtd_questoes = request.POST["qtd_questoes"]

        exame = Exame(cod_exame=random_generator(), qtd_questoes=int(qtd_questoes))
        exame.save()

        obj_exame = Exame.objects.get(cod_exame=exame)

        try:
            context['response'] = gerador_chatGPT(obj_exame, int(qtd_questoes), tema)
            context['cod_exame'] = exame
        except:
            context['erro'] = 'Servidor do ChatGPT está indisponível no momento.\nGere o teste de forma manual.'


    return render(request, 'gerar_exame.html', context)

#def acessar_exame(request):

    context = { 
        'template': 'acessar_exame'
    }

    return render(request, 'acessar_exame.html', context)

#def qtd_questoes(cod_exame):

    exame = Exame.objects.filter(cod_exame=cod_exame).values('qtd_questoes')

    return exame

#def dados_questoes(cod_exame):

    questoes = Questao.objects.filter(cod_exame=cod_exame).values('pergunta',
                                                                    'alternativa1',
                                                                    'alternativa2',
                                                                    'alternativa3',
                                                                    'alternativa4',
                                                                    'resposta')

    return questoes

#def gerador_chatGPT(cod_exame, qtd_questoes, tema):

    openai.api_key = "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"

    loop = 1
    while loop <= qtd_questoes:
        prompt = f"Gere uma questão sobre {tema} com 4 alternativas e a resposta."
        completions = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500
        )

        message = completions.choices[0].text
        message = message.split('\n')

        itens = []
        for elem in message:
            if len(elem) > 2:
                itens.append(elem)

        pergunta = itens[0]
        alternativa1 = itens[1]
        alternativa2 = itens[2]
        alternativa3 = itens[3]
        alternativa4 = itens[4]
        resposta = itens[5]

        alternativas = [itens[n] for n in range(1, len(itens)-1)]

        if resposta[10:] in alternativas and len(pergunta) > 20:

            try:
                gravar_questao = Questao(cod_exame=cod_exame, pergunta=pergunta, alternativa1=alternativa1[3:], alternativa2=alternativa2[3:], alternativa3=alternativa3[3:], alternativa4=alternativa4[3:], resposta=resposta[13:], area=tema)
                gravar_questao.save()
                loop+=1
            except:
                pass

    return 'Sucesso na geração de todas as questões pelo chatGPT.'

