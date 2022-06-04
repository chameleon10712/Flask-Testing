import io
import os

import pytest

import flask
from flask.helpers import get_debug_flag
from flask.helpers import get_env
from flask.helpers import is_ip


class TestIsIp:
    def test_FTF(self):
        """
        if ip is in valid format
        if ip is in valid ipv4 format
        if ip is not in valid ipv6 format
        """
        assert is_ip("127.0.0.1") == True

    def test_FFT(self):
        """
        if ip is in valid format
        if ip is not in valid ipv4 format
        if ip is in valid ipv6 format
        """
        assert is_ip("2001:db8:3333:4444:5555:6666:7777:8888") == True

    def test_TFF(self):
        """
        if ip is in invalid format
        if ip is not in valid ipv4 format
        if ip is not in valid ipv6 format
        """
        assert is_ip("256.0.0.0") == False
        assert is_ip("56FE::2159:5BBC::6594") == False
        assert is_ip("123:0.1:500") == False


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

        # testcase 6 - .jpeg
        rv = flask.send_file("static/test.jpeg")
        assert rv.direct_passthrough
        assert rv.mimetype == "image/jpeg"
        rv.close()

        # testcase 7 - .png
        rv = flask.send_file("static/test.png")
        assert rv.direct_passthrough
        assert rv.mimetype == "image/png"
        rv.close()

        # testcase 8 - .svg
        rv = flask.send_file("static/test.svg")
        assert rv.direct_passthrough
        assert rv.mimetype == "image/svg+xml"
        rv.close()

        # testcase 9 - .js
        rv = flask.send_file("static/test.js")
        assert rv.direct_passthrough
        assert rv.mimetype == "application/javascript"
        rv.close()

        # testcase 10 - .mp3
        rv = flask.send_file("static/test.mp3")
        assert rv.direct_passthrough
        assert rv.mimetype == "audio/mpeg"
        rv.close()

        # testcase 11 - .pdf
        rv = flask.send_file("static/test.pdf")
        assert rv.direct_passthrough
        assert rv.mimetype == "application/pdf"
        rv.close()

        # testcase 12 - .mp4
        rv = flask.send_file("static/test.mp4")
        assert rv.direct_passthrough
        assert rv.mimetype == "video/mp4"
        rv.close()

        # testcase 13 - .tar
        rv = flask.send_file("static/test.tar")
        assert rv.direct_passthrough
        assert rv.mimetype == "application/x-tar"
        rv.close()

        # testcase 14 - .xml
        rv = flask.send_file("static/test.xml")
        assert rv.direct_passthrough
        assert rv.mimetype == "application/xml"
        rv.close()

        # testcase 15 - .zip
        rv = flask.send_file("static/test.zip")
        assert rv.direct_passthrough
        assert rv.mimetype == "application/zip"
        rv.close()

        # testcase 16 - .rar
        rv = flask.send_file("static/test.rar")
        assert rv.direct_passthrough
        assert rv.mimetype == "application/rar"
        rv.close()

        # testcase 17 - .bin
        rv = flask.send_file("static/test.bin")
        assert rv.direct_passthrough
        assert rv.mimetype == "application/octet-stream"
        rv.close()

        # testcase 18 - .doc
        rv = flask.send_file("static/test.doc")
        assert rv.direct_passthrough
        assert rv.mimetype == "application/msword"
        rv.close()

        # testcase 19 - .ppt
        rv = flask.send_file("static/test.ppt")
        assert rv.direct_passthrough
        assert rv.mimetype == "application/vnd.ms-powerpoint"
        rv.close()

    def test_send_file(self, app, req_ctx):
        rv = flask.send_file("static/index.html")
        assert rv.direct_passthrough
        assert rv.mimetype == "text/html"

        with app.open_resource("static/index.html") as f:
            rv.direct_passthrough = False
            assert rv.data == f.read()
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


    def test_make_response(self):
        app = flask.Flask(__name__)
        with app.test_request_context():
            # FFTT
            data = {"a":1}
            rv = flask.helpers.make_response(data, 400)
            assert rv.status_code == 400
            assert rv.mimetype == "application/json"

            # FTFT
            rv = flask.helpers.make_response("Internal Server Error", 500)
            assert rv.status_code == 500
            assert rv.data == b"Internal Server Error"
            assert rv.mimetype == "text/html"

            # FFTF
            data = {"a":1}
            rv = flask.helpers.make_response(data, 200)
            assert rv.status_code == 200
            assert rv.mimetype == "application/json"

            # FTFF
            rv = flask.helpers.make_response("Hello", 200)
            assert rv.status_code == 200
            assert rv.data == b"Hello"
            assert rv.mimetype == "text/html"

            # TFFF
            rv = flask.helpers.make_response()
            assert rv.status_code == 200
            assert rv.mimetype == "text/html"


