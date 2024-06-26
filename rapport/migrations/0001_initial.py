# Generated by Django 5.0.4 on 2024-05-05 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utilisateurs', '0002_alter_membre_compte'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rapport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_ev', models.CharField(max_length=25, unique=True)),
                ('titre', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('membre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='utilisateurs.membre')),
            ],
        ),
    ]
