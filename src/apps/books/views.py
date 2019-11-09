from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from books.permissions import IsValidUserBookService


class Books(APIView):
	""" API For Mantaining Book Details"""

	# Appliying basic permission for book service users
	permission_classes = (IsValidUserBookService,)

	def get(self, request):
		"""
		Fethcing all book details available in the system
		"""
		books = [
			{'name': 'ABC', 'category': 'Drama'},
			{'name': 'Rich Dad Poor Dad', 'category': 'Inspiration'},
		]
		return Response(data=books, status=status.HTTP_200_OK)

