# Generated by Django 5.1.4 on 2025-01-06 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_posts_clicks_alter_posts_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='experiences',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='posts',
            name='skills',
            field=models.JSONField(default=list),
        ),
    ]
