# Generated by Django 3.1.2 on 2020-11-02 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
        ('core', '0004_pontoturistico_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='avaliacoes',
            field=models.ManyToManyField(to='avaliacoes.Avaliacao'),
        ),
    ]
