# Generated by Django 2.2.1 on 2019-05-16 09:06

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [("articles", "0002_article_date")]

    operations = [
        migrations.AddField(
            model_name="article",
            name="intro",
            field=wagtail.core.fields.RichTextField(default=None, verbose_name="Intro"),
        )
    ]
