# Generated by Django 3.1.1 on 2020-11-02 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('square', models.DecimalField(decimal_places=2, max_digits=19)),
                ('windows_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('style', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('price_for_which_was_purchased', models.IntegerField()),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pictures.hall')),
            ],
        ),
    ]
