# -*- coding: utf-8 -*-
from django.db.models import F, Sum, Subquery, OuterRef
from django.views.generic import ListView
from django_universal_paginator.cursor import CursorPaginateMixin

from .models import BookRating, BookOrder


# simple query
LIST_QUERY = (BookRating.objects
	.annotate(name=F('book__name'))
	.values('id', 'rating', 'name')
	.order_by('id'))

# not optimalized query
LIST_QUERY = (BookRating.objects
	.annotate(name=F('book__name'), total_revenue=Sum('book__bookorder__total_price'))
	.values('id', 'rating', 'name', 'total_revenue')
	.order_by('id'))

# optimized using subquery
REVENUE_QUERY = Subquery(BookOrder.objects
	.filter(book_id=OuterRef('book_id'))
	.values('book_id')
	.annotate(total=Sum('total_price'))
	.values('total')[:1])
LIST_QUERY = (BookRating.objects
	.annotate(name=F('book__name'), total_revenue=REVENUE_QUERY)
	.values('id', 'rating', 'name', 'total_revenue')
	.order_by('id'))


class RatingStandardView(ListView):
	paginate_by = 10

	def get_queryset(self):
		return LIST_QUERY


class RatingCursorView(CursorPaginateMixin, RatingStandardView):
	pass
