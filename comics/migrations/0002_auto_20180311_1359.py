# Generated by Django 2.0.2 on 2018-03-11 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='arc',
            options={'ordering': ('sort_order',)},
        ),
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ('sort_order',)},
        ),
        migrations.AlterField(
            model_name='issue',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterUniqueTogether(
            name='issue',
            unique_together={('arc', 'slug')},
        ),
    ]
