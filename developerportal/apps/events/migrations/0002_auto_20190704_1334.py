# Generated by Django 2.2.1 on 2019-07-04 13:34

import datetime
import developerportal.apps.common.fields
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("topics", "0021_auto_20190702_1402"),
        ("people", "0013_merge_20190702_1300"),
        ("wagtailcore", "0041_group_collection_permissions_verbose_name_plural"),
        ("mozimages", "0001_initial"),
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Events",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                )
            ],
            options={"abstract": False},
            bases=("wagtailcore.page",),
        ),
        migrations.AlterModelOptions(
            name="event", options={"ordering": ["-start_date"]}
        ),
        migrations.AddField(
            model_name="event",
            name="agenda",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "agenda_item",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("start_time", wagtail.core.blocks.TimeBlock()),
                                (
                                    "end_time",
                                    wagtail.core.blocks.TimeBlock(required=False),
                                ),
                                ("title", wagtail.core.blocks.CharBlock()),
                                (
                                    "speaker",
                                    wagtail.core.blocks.PageChooserBlock(
                                        page_type=["people.Person"], required=False
                                    ),
                                ),
                                (
                                    "external_speaker",
                                    wagtail.core.blocks.StructBlock(
                                        [
                                            (
                                                "name",
                                                wagtail.core.blocks.CharBlock(
                                                    required=False
                                                ),
                                            ),
                                            (
                                                "url",
                                                wagtail.core.blocks.URLBlock(
                                                    label="URL", required=False
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    )
                ],
                blank=True,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="body",
            field=developerportal.apps.common.fields.CustomStreamField(
                [
                    (
                        "paragraph",
                        wagtail.core.blocks.RichTextBlock(
                            features=(
                                "h2",
                                "h3",
                                "h4",
                                "bold",
                                "italic",
                                "link",
                                "ol",
                                "ul",
                                "blockquote",
                                "code",
                                "hr",
                            )
                        ),
                    ),
                    ("image", wagtail.images.blocks.ImageChooserBlock()),
                    ("embed", wagtail.embeds.blocks.EmbedBlock()),
                    (
                        "embed_html",
                        wagtail.core.blocks.RawHTMLBlock(
                            help_text="Warning: be careful what you paste here, since\n                          this field could introduce XSS (or similar) bugs.\n                          This field is meant solely for third-party embeds."
                        ),
                    ),
                    (
                        "code_snippet",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "language",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("css", "CSS"),
                                            ("go", "Go"),
                                            ("html", "HTML"),
                                            ("js", "JavaScript"),
                                            ("python", "Python"),
                                            ("rust", "Rust"),
                                            ("ts", "TypeScript"),
                                        ]
                                    ),
                                ),
                                ("code", wagtail.core.blocks.TextBlock()),
                            ]
                        ),
                    ),
                ],
                blank=True,
                default=None,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="description",
            field=models.TextField(blank=True, default="", max_length=250),
        ),
        migrations.AddField(
            model_name="event",
            name="end_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="header_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="mozimages.MozImage",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="register_url",
            field=models.URLField(blank=True, null=True, verbose_name="Register URL"),
        ),
        migrations.AddField(
            model_name="event",
            name="speakers",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "speaker",
                        wagtail.core.blocks.PageChooserBlock(
                            page_type=["people.Person"], required=False
                        ),
                    ),
                    (
                        "external_speaker",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("name", wagtail.core.blocks.CharBlock()),
                                ("job_title", wagtail.core.blocks.CharBlock()),
                                (
                                    "profile_picture",
                                    wagtail.images.blocks.ImageChooserBlock(),
                                ),
                            ],
                            required=False,
                        ),
                    ),
                ],
                blank=True,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="start_date",
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name="event",
            name="venue",
            field=models.TextField(blank=True, default="", max_length=250),
        ),
        migrations.CreateModel(
            name="EventTopic",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "event",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="topics",
                        to="events.Event",
                    ),
                ),
                (
                    "topic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="topics.Topic",
                    ),
                ),
            ],
            options={"ordering": ["sort_order"], "abstract": False},
        ),
        migrations.CreateModel(
            name="EventSpeaker",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "event",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="speaker",
                        to="events.Event",
                    ),
                ),
                (
                    "speaker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="people.Person",
                    ),
                ),
            ],
            options={"ordering": ["sort_order"], "abstract": False},
        ),
    ]
