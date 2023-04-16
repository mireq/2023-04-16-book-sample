# Generated by Django 4.2 on 2023-04-16 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

	initial = True

	dependencies = [
	]

	operations = [
		migrations.CreateModel(
			name='Book',
			fields=[
				('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('name', models.CharField(max_length=100)),
				('year', models.SmallIntegerField(db_index=True)),
			],
			options={
				'db_table': 'book',
			},
		),
		migrations.CreateModel(
			name='BookRating',
			fields=[
				('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('rating', models.SmallIntegerField()),
				('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.book')),
			],
			options={
				'db_table': 'book_rating',
			},
		),
		migrations.CreateModel(
			name='BookOrder',
			fields=[
				('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
				('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.book')),
			],
			options={
				'db_table': 'book_order',
			},
		),
	]
