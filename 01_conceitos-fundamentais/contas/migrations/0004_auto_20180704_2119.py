# Generated by Django 2.0.7 on 2018-07-04 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0003_auto_20180704_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(),
        ),
    ]
