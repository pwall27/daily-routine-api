import pytest
from django.test import RequestFactory
from faker import Faker
from mixer.backend.django import mixer
from rest_framework.exceptions import ValidationError

from app.models import Task
from app.serializers.task import TaskSerializer

fake = Faker()


@pytest.mark.django_db
class TestTaskSerializer:
    def test_task_serializer(self):
        owner = mixer.blend('app.User')

        data = {
            'title': fake.sentence(nb_words=4, variable_nb_words=True, ext_word_list=None),
            'description': fake.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None),
            'is_active': fake.pybool(),
            'owner': owner.uuid
        }

        serializer = TaskSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        assert isinstance(instance, Task)
        assert instance.title == data['title']
        assert instance.description == data['description']
        assert instance.is_active == data['is_active']
        assert instance.owner == owner

    def test_task_serializer_getting_owner_from_request(self):

        owner = mixer.blend('app.User')

        data = {
            'title': fake.sentence(nb_words=4, variable_nb_words=True, ext_word_list=None),
            'description': fake.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None),
            'is_active': fake.pybool()
        }

        factory = RequestFactory()

        context = {
            'request': factory.post('/v1/tasks/')
        }

        context['request'].user = owner

        serializer = TaskSerializer(data=data, context=context)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        assert instance.owner == owner

    def test_task_serializer_without_owner(self):
        data = {
            'title': fake.sentence(nb_words=4, variable_nb_words=True, ext_word_list=None),
            'description': fake.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None),
            'is_active': fake.pybool()
        }

        serializer = TaskSerializer(data=data)
        with pytest.raises(ValidationError) as e:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        assert str(e.value.args[0]['message'][0]) == 'Field owner not informed.'
