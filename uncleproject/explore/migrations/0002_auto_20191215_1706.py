# Generated by Django 2.2.1 on 2019-12-15 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='big5_agreeableness',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='big5_conscientiousness',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='big5_extraversion',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='big5_neuroticism',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='big5_openness',
            field=models.FloatField(),
        ),
    ]
