# Generated by Django 3.0.5 on 2020-07-14 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plume', '0002_choice_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='legume',
            name='image',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='legume',
            name='variete',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
