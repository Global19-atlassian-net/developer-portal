# Generated by Django 2.2.1 on 2019-06-19 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("topics", "0015_merge_20190619_1437")]

    operations = [
        migrations.AlterField(
            model_name="topic",
            name="icon",
            field=models.FileField(blank=True, default="", upload_to="topics/icons"),
        )
    ]
