# Generated by Django 2.2.1 on 2019-06-18 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("topics", "0009_topic_color")]

    operations = [
        migrations.AlterField(
            model_name="topic",
            name="intro",
            field=models.TextField(blank=True, default="", max_length=250),
        )
    ]
