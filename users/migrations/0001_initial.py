<<<<<<< HEAD
# Generated by Django 4.2.2 on 2025-01-16 15:43
=======
# Generated by Django 5.1.5 on 2025-01-16 15:23
>>>>>>> cd2a166e6f860be504767ef9f05b4b48694ba451

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, unique=True)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
    ]
