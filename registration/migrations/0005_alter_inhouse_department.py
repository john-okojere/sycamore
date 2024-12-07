# Generated by Django 5.1.3 on 2024-12-02 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0004_inhouse_volunteer_role_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inhouse",
            name="department",
            field=models.CharField(
                choices=[
                    ("ushering", "Ushering"),
                    ("sanctuary", "Sanctuary"),
                    ("spirit & Truth", "Spirit & Truth"),
                    ("technical", "Technical"),
                    ("Light & Power", "Light & Power"),
                    ("media", "New Wine Media"),
                    ("follow up", "Labour Room (follow_up)"),
                    ("decoration", "Decoration"),
                    ("welfare", "Taste & See"),
                    ("pastoral", "Pastoral Care"),
                ],
                max_length=25,
            ),
        ),
    ]
