# Generated by Django 4.2.2 on 2024-07-12 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('quantity', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='items/')),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='inventory.bin')),
            ],
        ),
    ]
