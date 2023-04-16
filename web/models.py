# -*- coding: utf-8 -*-
from django.db import models


class Book(models.Model):
	name = models.CharField(max_length=100)
	year = models.SmallIntegerField(db_index=True)

	class Meta:
		db_table = 'book'


class BookRating(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	rating = models.SmallIntegerField()

	class Meta:
		db_table = 'book_rating'


class BookOrder(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	total_price = models.DecimalField(decimal_places=2, max_digits=10)

	class Meta:
		db_table = 'book_order'
