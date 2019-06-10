# Generated by Django 2.2.1 on 2019-06-05 14:04

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0016_auto_20190604_1317'),
        ('topics', '0003_subtopic'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicFeaturedArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
                ('topic', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured_articles', to='topics.Topic')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
