import datetime

from django.test import TestCase
from django.test.client import RequestFactory
from django.urls.base import reverse

from core.models import Movie, Person
from core.views import MovieListView, PersonListView

# debug pagination


class TestMoviewListPagination(TestCase):
    ACTIVE_PAGINATION_HTML = """
    <li class="page-item active">
        <a href="{}?page={}" class="page-link">{}</a>
    </li>
    """

    def setUp(self):
        for n in range(15):
            Movie.objects.create(
                title='Title {}'.format(n),
                year=1990 + n,
                runtime=100,
            )

    def test_first_page(self):
        movie_list_path = reverse('core:movie-list')
        request = RequestFactory().get(path=movie_list_path)
        response = MovieListView.as_view()(request)

        self.assertEqual(200, response.status_code)
        self.assertTrue(response.context_data['is_paginated'])
        self.assertInHTML(
            self.ACTIVE_PAGINATION_HTML.format(movie_list_path, 1, 1),
            response.rendered_content)


class TestPersonListView(TestCase):
    ACTIVE_PAGINATION_HTML = """
    <li class="page-item active">
        <a href="{}?page={}" class="page-link">{}</a>
    </li>
    """

    def setUp(self):
        for n in range(15):
            Person.objects.create(
                first_name='first_name {}'.format(n),
                last_name='last_name {}'.format(n),
                born=datetime.datetime.now().date()
            )

    def test_first_page(self):
        person_list_path = reverse('core:person-list')
        request = RequestFactory().get(path=person_list_path)
        response = PersonListView.as_view()(request)

        self.assertEqual(200, response.status_code)
        self.assertTrue(response.context_data['is_paginated'])
        self.assertInHTML(
            self.ACTIVE_PAGINATION_HTML.format(person_list_path, 1, 1),
            response.rendered_content)
