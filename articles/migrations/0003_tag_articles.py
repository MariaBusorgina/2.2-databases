# Generated by Django 4.1.3 on 2022-12-11 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='articles',
            field=models.ManyToManyField(related_name='tags', to='articles.article'),
        ),
    ]
