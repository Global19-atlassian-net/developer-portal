# Generated by Django 2.2.1 on 2019-07-02 10:59

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [("people", "0011_merge_20190627_1428")]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="intro",
            field=wagtail.core.fields.RichTextField(blank=True, default=""),
        )
    ]
