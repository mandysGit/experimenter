# Generated by Django 3.2.5 on 2021-10-22 21:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experiments", "0188_auto_20210930_1549"),
    ]

    operations = [
        migrations.AddField(
            model_name="nimbusexperiment",
            name="conclusion_recommendation",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="nimbusexperiment",
            name="takeaways_summary",
            field=models.TextField(blank=True, null=True),
        ),
    ]
