import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def url_list():
    return reverse('courses-list')


@pytest.mark.django_db
def test_get_course(client, course_factory):
    courses = course_factory(_quantity=1)
    id_ = courses[0].id
    name = courses[0].name
    url = reverse('courses-detail', args=[id_])
    response = client.get(url)
    assert response.status_code == 200
    assert response.data['name'] == name


@pytest.mark.django_db
def test_get_courses_list(client, course_factory, url_list):
    courses = course_factory(_quantity=10)
    response = client.get(url_list)
    assert response.status_code == 200
    for i, course in enumerate(courses):
        assert course.name == response.data[i]['name']


@pytest.mark.django_db
def test_filter_course_id(client, course_factory, url_list):
    courses = course_factory(_quantity=5)
    id_ = courses[3].id
    response = client.get(url_list, data={'id': id_})
    assert response.status_code == 200
    assert response.data[0]['id'] == id_


@pytest.mark.django_db
def test_filter_course_name(client, course_factory, url_list):
    courses = course_factory(_quantity=3)
    name_ = courses[2].name
    response = client.get(url_list, data={'name': name_})
    assert response.status_code == 200
    assert response.data[0]['name'] == name_


@pytest.mark.django_db
def test_create_course(client, url_list):
    data = {'name': 'test_course'}
    response = client.post(url_list, data=data)
    assert response.status_code == 201
    assert response.data.get('name') == data.get('name')


@pytest.mark.django_db
def test_update_course(client, course_factory):
    course = course_factory(_quantity=1)
    id_ = course[0].id
    data = {'name': 'test_course'}
    url = reverse('courses-detail', args=[id_])
    response = client.patch(url, data=data)
    assert response.status_code == 200
    assert response.data.get('name') == data.get('name')


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    courses = course_factory(_quantity=5)
    count = Course.objects.count()
    id_ = courses[2].id
    url = reverse('courses-detail', args=[id_])
    response = client.delete(url)
    assert response.status_code == 204
    assert Course.objects.count() == count - 1
    assert len(Course.objects.filter(pk=id_)) == 0


data_ = [(20, True), (21, False), (-1, False)]


@pytest.mark.parametrize(['students_per_course', 'expected_value'], data_)
def test_with_specific_settings(settings, students_per_course, expected_value):
    res = 0 < students_per_course <= settings.MAX_STUDENTS_PER_COURSE
    assert res == expected_value
