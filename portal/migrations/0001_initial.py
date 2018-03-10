# Generated by Django 2.0.2 on 2018-03-09 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BestellPositionen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menge', models.PositiveIntegerField()),
                ('alsTeig', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Bestellung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bestellDatum', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Rechnung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rechnungsDatum', models.DateField()),
                ('bezahlStatus', models.PositiveIntegerField()),
                ('bestellung', models.ForeignKey(on_delete=False, to='portal.Bestellung')),
            ],
        ),
        migrations.CreateModel(
            name='Rezept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rezeptBez', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('prename', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('bakeryName', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=200)),
                ('plz', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Zutaten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zutatenBez', models.CharField(max_length=100)),
                ('einheit', models.PositiveIntegerField()),
                ('pricePerUnit', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Zutatenliste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rezept', models.ForeignKey(on_delete=False, to='portal.Rezept')),
                ('zutat', models.ForeignKey(on_delete=False, to='portal.Zutaten')),
            ],
        ),
        migrations.AddField(
            model_name='bestellung',
            name='user',
            field=models.ForeignKey(on_delete=False, to='portal.User'),
        ),
        migrations.AddField(
            model_name='bestellpositionen',
            name='bestellung',
            field=models.ForeignKey(on_delete=False, to='portal.Bestellung'),
        ),
        migrations.AddField(
            model_name='bestellpositionen',
            name='rezept',
            field=models.ForeignKey(on_delete=False, to='portal.Rezept'),
        ),
    ]
