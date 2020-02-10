from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Books
from .serializers import BookSerializer

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_book(title="", author=""):
        if title != "" and artist != "":
            Books.objects.create(title=title, author=author)

    def setUp(self):
        # add test data
        self.create_book("Harry Potter", "JK Rownling")
        self.create_book("Kafka on the Shore", "Haruki Murakami")
        self.create_book("let it be", "Kazuo Iziguro")
        self.assertEqual(1,1)


# class GetAllSongsTest(BaseViewTest):

#     def test_get_all_songs(self):
#         """
#         This test ensures that all songs added in the setUp method
#         exist when we make a GET request to the songs/ endpoint
#         """
#         # hit the API endpoint
#         response = self.client.get(
#             reverse("songs-all", kwargs={"version": "v1"})
#         )
#         # fetch the data from db
#         expected = Songs.objects.all()
#         serialized = SongsSerializer(expected, many=True)
#         self.assertEqual(response.data, serialized.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
# view rawdrf_tut_tests.py hosted with ❤ by GitHub