# Generated by Django 2.2.6 on 2019-10-24 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doacao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doacao',
            name='linkImg',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
