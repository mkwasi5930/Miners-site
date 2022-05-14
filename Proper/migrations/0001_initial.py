# Generated by Django 3.2.12 on 2022-05-11 18:00

from django.db import migrations, models
import django.db.models.deletion
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(blank=sqlalchemy.sql.expression.true, max_length=500, null=sqlalchemy.sql.expression.true)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField(max_length=20)),
                ('mineral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Proper.mineral')),
            ],
        ),
    ]