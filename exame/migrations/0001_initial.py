# Generated by Django 3.2.6 on 2023-02-14 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_questao', models.CharField(max_length=25)),
                ('pergunta', models.CharField(max_length=500, verbose_name='Pergunta')),
                ('alternativa1', models.CharField(max_length=500)),
                ('alternativa2', models.CharField(max_length=500)),
                ('alternativa3', models.CharField(max_length=500)),
                ('alternativa4', models.CharField(max_length=500)),
                ('alternativa5', models.CharField(max_length=500)),
                ('resposta', models.CharField(max_length=500)),
                ('area', models.CharField(max_length=100)),
            ],
        ),
    ]
