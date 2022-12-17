# Generated by Django 4.1.4 on 2022-12-17 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MedicineDetails',
        ),
        migrations.AlterModelOptions(
            name='medicinerecord',
            options={'verbose_name_plural': 'Medicine Details'},
        ),
        migrations.AddField(
            model_name='medicinerecord',
            name='medicine_details',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
