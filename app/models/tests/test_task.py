import pytest

from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db  # This is put here so that we can save to the database otherwise it will fail because tests are not written to the database.


class TestTask:

    def test_create_task(self):
        obj = mixer.blend('app.Task')
        assert obj.pk is not None, 'Should create a Task instance'

    def test_string(self):
        obj = mixer.blend('app.Task')
        assert str(obj) == obj.title, 'Task string should be its title'

    def test_representation(self):
        obj = mixer.blend('app.Task')
        assert repr(obj) == 'Task<{}>'.format(obj.title), 'Task representation should be its class name with title'
