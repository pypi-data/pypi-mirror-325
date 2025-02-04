from datetime import datetime

from django.core.exceptions import ImproperlyConfigured

from actstream.signals import action
from actstream.registry import register, unregister
from actstream.models import Action, actor_stream, model_stream, ActionEvent
from actstream.tests.base import render, ActivityBaseTestCase
from actstream.settings import USE_JSONFIELD

from testapp.models import Abstract, Unregistered


class TestAppTests(ActivityBaseTestCase):
    def setUp(self):
        super(TestAppTests, self).setUp()
        self.user = self.User.objects.create(username='test')
        self.action_event_created = ActionEvent.objects.create(
            entity_name='testbar',
            message='was created'
        )
        self.action_event_said = ActionEvent.objects.create(
            entity_name='testbar',
            message='said'
        )
        action.send(self.user, verb=self.action_event_created)

    def test_accessor(self):
        self.assertEqual(len(Action.objects.testfoo(self.user)), 1)
        self.assertEqual(
            len(Action.objects.testfoo(self.user, datetime(1970, 1, 1))),
            0
        )

    def test_mystream(self):
        self.assertEqual(
            len(self.user.actor_actions.testbar(self.action_event_created)),
            1
        )
        self.assertEqual(
            len(self.user.action_object_actions.testbar(self.action_event_created)),
            0
        )

    def test_registration(self):
        instance = Unregistered.objects.create(name='fubar')
        self.assertRaises(ImproperlyConfigured, actor_stream, instance)
        register(Unregistered)
        self.assertEqual(actor_stream(instance).count(), 0)

        self.assertRaises(RuntimeError, model_stream, Abstract)
        self.assertRaises(ImproperlyConfigured, register, Abstract)
        unregister(Unregistered)

    def test_tag_custom_activity_stream(self):
        stream = self.user.actor_actions.testbar(self.action_event_created)
        output = render('''{% activity_stream 'testbar' 1 %}
        {% for action in stream %}
            {{ action }}
        {% endfor %}
        ''', user=self.user)
        self.assertAllIn([str(action) for action in stream], output)

        self.assertEqual(
            self.capture(
                'testapp_custom_feed',
                self.action_event_created.id)['totalItems'],
            1
        )

    def test_customuser(self):
        from testapp.models import MyUser

        self.assertEqual(self.User, MyUser)
        self.assertEqual(self.user.get_full_name(), 'test')

    if USE_JSONFIELD:
        def test_jsonfield(self):
            action.send(
                self.user, verb=self.action_event_said, text='foobar',
                tags=['sayings'],
                more_data={'pk': self.user.pk}
            )
            newaction = Action.objects.filter(verb=self.action_event_said)[0]
            self.assertEqual(newaction.data['text'], 'foobar')
            self.assertEqual(newaction.data['tags'], ['sayings'])
            self.assertEqual(newaction.data['more_data'], {'pk': self.user.pk})
