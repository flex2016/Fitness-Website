from fitness.extensions import mail
from fitness.blueprints.feedback.tasks import deliver_feedback_email


class TestTasks(object):
    def test_deliver_support_email(self):
        """ Deliver a feedback email. """
        form = {
            'name': 'flex',
            'email': 'foo@bar.com',
            'feedback': 'Test feedback from Fitness.'
        }

        with mail.record_messages() as outbox:
            deliver_feedback_email(form.get('name'), form.get('email'),
                                   form.get('message'))

            assert len(outbox) == 1
            assert form.get('email') in outbox[0].body
