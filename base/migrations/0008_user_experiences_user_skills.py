# Generated by Django 5.1.4 on 2025-01-06 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_posts_experiences_posts_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='experiences',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='user',
            name='skills',
            field=models.JSONField(default=list),
        ),
    ]
