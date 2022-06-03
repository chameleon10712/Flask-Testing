import io
import os

import pytest

import flask
from flask.helpers import get_debug_flag
from flask.helpers import get_env


class TestSendfile:
    def test_my_send_file(self, app, req_ctx):
        # testcase 1 - .html
        rv = flask.send_file("static/test.html")
        assert rv.direct_passthrough
        assert rv.mimetype == "text/html"
        rv.close()

        # testcase 2 - .css
        rv = flask.send_file("static/test.css")
        assert rv.direct_passthrough
        assert rv.mimetype == "text/css"
        rv.close()

        # testcase 3 - .json
        rv = flask.send_file("static/test.json")
        assert rv.direct_passthrough
        assert rv.mimetype == "application/json"
        rv.close()

        # testcase 4 - .ico
        rv = flask.send_file("static/test.ico")
        assert rv.direct_passthrough
        assert rv.mimetype == "image/x-icon"
        rv.close()

        # testcase 5 - .gif
        rv = flask.send_file("static/test.gif")
        assert rv.direct_passthrough
        assert rv.mimetype == "image/gif"
        rv.close()


class TestHelpers:
    @pytest.mark.parametrize(
        "debug, expected_flag, expected_default_flag",
        [
            ("", False, False),
            ("0", False, False),#FT
            ("False", False, False),#FT
            ("No", False, False),#FT
            ("True", True, True),#TF
        ],
    )
    def test_get_debug_flag(
        self, monkeypatch, debug, expected_flag, expected_default_flag
    ):
        monkeypatch.setenv("FLASK_DEBUG", debug)
        if expected_flag is None:
            assert get_debug_flag() is None
        else:
            assert get_debug_flag() == expected_flag
        assert get_debug_flag() == expected_default_flag

    @pytest.mark.parametrize(
        "env, ref_env, debug",
        [
            ("", "production", False),
            ("production", "production", False),#TFF
            ("development", "development", True),#FFT
            ("other", "other", False),#FTF
        ],
    )
    def test_get_env(self, monkeypatch, env, ref_env, debug):
        monkeypatch.setenv("FLASK_ENV", env)
        assert get_debug_flag() == debug
        assert get_env() == ref_env
