from flask import url_for

from lib.tests import assert_status_with_message


class TestFeedback(object):
    def test_feedback_page(self, client):
        """ Feedback page should respond with a success 200. """
        response = client.get(url_for('feedback.index'))
        assert response.status_code == 200

    def test_feedback_form(self, client):
        """ Feedback form should redirect with a message. """
        form = {
            'name': 'flex',
            'email': 'foo@bar.com',
            'feedback': 'Test Feedback from Fitness.'
        }

        response = client.post(url_for('feedback.index'), data=form,
                               follow_redirects=True)
        assert_status_with_message(200, response, 'Thanks')
