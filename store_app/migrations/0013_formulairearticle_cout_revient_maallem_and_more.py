# Generated by Django 5.0.7 on 2024-08-17 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0012_alter_formulairearticle_ref_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulairearticle',
            name='cout_revient_maallem',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Coût revient Maallem'),
        ),
        migrations.AddField(
            model_name='formulairearticle',
            name='cout_revient_ozaz',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Coût revient Ozaz'),
        ),
        migrations.AddField(
            model_name='formulairearticle',
            name='cout_revient_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Coût revient Total'),
        ),
        migrations.AlterField(
            model_name='formulairearticle',
            name='prix',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Prix Estimé'),
        ),
    ]