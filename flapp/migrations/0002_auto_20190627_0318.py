# Generated by Django 2.2.2 on 2019-06-26 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writer',
            name='designation',
            field=models.CharField(choices=[('A', 'Author'), ('F', 'Founder'), ('CF', 'Co-Founder'), ('GA', 'Guest Author'), ('EC', 'Editor-in-Chief'), ('STE', 'Section Editor: Science & Technology Editor'), ('EFE', 'Section Editor: Economics & Finance Editor'), ('WAE', 'Section Editor: World Affairs Editor'), ('EE', 'Section Editor: Editorial Editor')], default='A', max_length=2),
        ),
    ]