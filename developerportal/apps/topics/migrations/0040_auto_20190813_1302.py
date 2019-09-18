# Generated by Django 2.2.4 on 2019-08-13 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("topics", "0039_auto_20190805_0806")]

    operations = [
        migrations.AlterField(
            model_name="topic",
            name="card_description",
            field=models.TextField(
                blank=True, default="", max_length=400, verbose_name="Description"
            ),
        ),
        migrations.AlterField(
            model_name="topic",
            name="description",
            field=models.TextField(blank=True, default="", max_length=400),
        ),
    ]
