# Generated by Django 4.1.1 on 2022-10-10 04:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSeries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disney',
            name='qualification',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='hbo',
            name='qualification',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='netflix',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='netflix',
            name='qualification',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='prime',
            name='qualification',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]