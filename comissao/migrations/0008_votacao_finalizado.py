# Generated by Django 4.2.2 on 2023-10-05 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comissao', '0007_votacao_id_cargo'),
    ]

    operations = [
        migrations.AddField(
            model_name='votacao',
            name='finalizado',
            field=models.BooleanField(default=0, null=True),
        ),
    ]
