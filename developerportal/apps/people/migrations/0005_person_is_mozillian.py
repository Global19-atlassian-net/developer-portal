# Generated by Django 2.2.1 on 2019-05-31 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("people", "0004_auto_20190530_1441")]

    operations = [
        migrations.AddField(
            model_name="person",
            name="is_mozillian",
            field=models.BooleanField(default=True),
        )
    ]
