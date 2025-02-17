# Generated by Django 5.1.5 on 2025-01-17 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attacker_card', models.IntegerField()),
                ('defender_card', models.IntegerField(blank=True, null=True)),
                ('result', models.CharField(blank=True, max_length=10, null=True)),
                ('is_greater_wins', models.BooleanField()),
            ],
        ),
    ]
