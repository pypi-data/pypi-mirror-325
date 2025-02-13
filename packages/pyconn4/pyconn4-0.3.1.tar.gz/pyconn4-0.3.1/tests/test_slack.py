from pyconn.slack import SlackAgent
from nose.tools import assert_true

MY_TOKEN = ""


def test_post_message():
    slack_agent = SlackAgent(MY_TOKEN)
    response = slack_agent.send_text("@test", "hello world")
    assert_true(response["ok"])


def test_post_file():
    slack_agent = SlackAgent(MY_TOKEN)
    response = slack_agent.send_file("#test", "__init__.py", "hello world")
    assert_true(response["ok"])
