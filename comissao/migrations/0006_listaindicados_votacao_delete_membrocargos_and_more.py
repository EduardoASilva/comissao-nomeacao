# Generated by Django 4.2.2 on 2023-10-04 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comissao', '0005_remove_membrocargos_anciao_jovem_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListaIndicados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_membro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comissao.membros')),
            ],
        ),
        migrations.CreateModel(
            name='Votacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('votado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='comissao.membros')),
            ],
        ),
        migrations.DeleteModel(
            name='MembroCargos',
        ),
        migrations.AddField(
            model_name='listaindicados',
            name='id_votacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comissao.votacao'),
        ),
    ]