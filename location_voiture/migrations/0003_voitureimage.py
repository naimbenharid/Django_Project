# Generated by Django 4.2.7 on 2023-11-25 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location_voiture', '0002_alter_location_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoitureImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('voiture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location_voiture.voiture')),
            ],
        ),
    ]
