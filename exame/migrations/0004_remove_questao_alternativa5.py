# Generated by Django 3.2.6 on 2023-02-23 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exame', '0003_alter_exame_cod_exame'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questao',
            name='alternativa5',
        ),
    ]
