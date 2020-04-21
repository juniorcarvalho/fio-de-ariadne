# Generated by Django 3.0.5 on 2020-04-21 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_add_age_at_occurrence_to_kid_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="kid",
            name="eyes",
            field=models.CharField(
                blank=True,
                choices=[
                    (1, "Preto"),
                    (2, "Castanhos"),
                    (3, "Loiro"),
                    (4, "Ruivo"),
                    (5, "Azul"),
                    (6, "Morena"),
                    (7, "Branca"),
                ],
                db_index=True,
                max_length=50,
                null=True,
                verbose_name="Cor dos olhos",
            ),
        ),
        migrations.AlterField(
            model_name="kid",
            name="hair",
            field=models.CharField(
                blank=True,
                choices=[
                    (1, "Preto"),
                    (2, "Castanhos"),
                    (3, "Loiro"),
                    (4, "Ruivo"),
                    (5, "Azul"),
                    (6, "Morena"),
                    (7, "Branca"),
                ],
                db_index=True,
                max_length=50,
                null=True,
                verbose_name="Cor dos cabelos",
            ),
        ),
        migrations.AlterField(
            model_name="kid",
            name="skin",
            field=models.CharField(
                blank=True,
                choices=[
                    (1, "Preto"),
                    (2, "Castanhos"),
                    (3, "Loiro"),
                    (4, "Ruivo"),
                    (5, "Azul"),
                    (6, "Morena"),
                    (7, "Branca"),
                ],
                db_index=True,
                max_length=50,
                null=True,
                verbose_name="Cor da pele",
            ),
        ),
    ]
