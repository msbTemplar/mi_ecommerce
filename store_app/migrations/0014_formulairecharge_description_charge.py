# Generated by Django 5.0.7 on 2024-08-17 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0013_formulairearticle_cout_revient_maallem_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulairecharge',
            name='description_charge',
            field=models.TextField(blank=True, max_length=15000, null=True, verbose_name='Description Charge'),
        ),
    ]
