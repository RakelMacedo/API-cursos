# Generated by Django 4.1 on 2022-08-14 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cursos", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="avaliacao",
            options={
                "ordering": ["id"],
                "verbose_name": "Avaliação",
                "verbose_name_plural": "Avaliações",
            },
        ),
        migrations.AlterModelOptions(
            name="curso",
            options={
                "ordering": ["id"],
                "verbose_name": "Curso",
                "verbose_name_plural": "Cursos",
            },
        ),
    ]
