import pytest

from api.factories import PostFactory


@pytest.fixture
def post_published():
    return PostFactory(title='Pytest with Factory')


@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'Pytest with Factory'
