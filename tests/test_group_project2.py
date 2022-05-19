from jinja2 import TemplateNotFound, TemplateSyntaxError

import flask


def test_render_template_TFTFT(app, client):
    """
    if dictionary is not empty
    if templates found
    if template is malformed (invalid jinja2 syntax)
    if template conatins jinja syntax
    if template variable don't match dictionary
    """
    @app.route("/")
    def index():
        return flask.render_template(
            "template_invalid_syntax_mismatch.html",
            var=1
        )

    try:
        rv = client.get("/")
        assert False
    except TemplateSyntaxError:
        assert True
    

def test_render_template_FFTFT(app, client):
    """
    if dictionary is empty
    if templates found
    if template is malformed (invalid jinja2 syntax)
    if template conatins jinja syntax
    if template variable don't match dictionary
    """
    @app.route("/")
    def index():
        return flask.render_template(
            "template_invalid_syntax_mismatch.html"
        )

    try:
        rv = client.get("/")
        assert False
    except TemplateSyntaxError:
        assert True
    


def test_render_template_TFFFT(app, client):
    """
    if dictionary is not empty
    if templates found
    if template is not malformed (invalid jinja2 syntax)
    if template conatins jinja syntax
    if template variable don't match dictionary
    """
    @app.route("/")
    def index():
        return flask.render_template(
            "template_mismatch.html",
            var=1
        )

    
    rv = client.get("/")
    assert rv.data == b''
    
    


def test_render_template_TFTFF(app, client):
    """
    if dictionary is not empty
    if templates found
    if template is malformed (invalid jinja2 syntax)
    if template conatins jinja syntax
    if template variable match dictionary
    """
    @app.route("/")
    def index():
        return flask.render_template(
            "template_invalid_syntax_match.html",
            match=1
        )

    try:
        rv = client.get("/")
        assert False
    except TemplateSyntaxError:
        assert True
    


def test_render_template_TTFTF(app, client):
    """
    if dictionary is not empty
    if templates not found
    if template is not malformed (invalid jinja2 syntax) (no actual template)
    if template conatins not jinja syntax (no actual template)
    if template variable match dictionary (no actual template)
    """
    @app.route("/")
    def index():
        return flask.render_template(
            "not_found.html",
            var=1
        )

    try:
        rv = client.get("/")
        assert False
    except TemplateNotFound:
        assert True
    


def test_render_template_string_TFTFT(app, client):
    """
    if dictionary is not empty
    if string is not None
    if string is malformed (invalid jinja2 syntax)
    if string conatins jinja syntax
    if string's variable don't match dictionary
    """
    @app.route("/")
    def index():
        return flask.render_template_string(
            "{% if true }"
            "haha"
            "{{ mismatch }}",
            var=1
        )

    try:
        rv = client.get("/")
        assert False
    except TemplateSyntaxError:
        assert True
    


def test_render_template_string_FFTFT(app, client):
    """
    if dictionary is empty
    if string is not None
    if string is malformed (invalid jinja2 syntax)
    if string conatins jinja syntax
    if string's variable don't match dictionary
    """
    @app.route("/")
    def index():
        return flask.render_template_string(
            "{% if true }"
            "haha"
            "{{ mismatch }}"
        )

    try:
        rv = client.get("/")
        assert False
    except TemplateSyntaxError:
        assert True
    


def test_render_template_string_TFFFT(app, client):
    """
    if dictionary is not empty
    if string is not None
    if string  is not malformed (invalid jinja2 syntax)
    if string  conatins jinja syntax
    if string's variable don't match dictionary
    """
    @app.route("/")
    def index():
        return flask.render_template_string(
            "{{ mismatch }}",
            var=1
        )

    
    rv = client.get("/")
    assert rv.data == b''


def test_render_template_string_TFTFF(app, client):
    """
    if dictionary is not empty
    if string is not None
    if string is malformed (invalid jinja2 syntax)
    if string conatins jinja syntax
    if string's variable match dictionary
    """
    @app.route("/")
    def index():
        return flask.render_template_string(
            "{{ match }}"
            "{% if true }"
            "haha",
            match=1
        )

    try:
        rv = client.get("/")
        assert False
    except TemplateSyntaxError:
        assert True
    


def test_render_template_string_TTFTF(app, client):
    """
    if dictionary is not empty
    if string is None
    if string is not malformed (invalid jinja2 syntax) (no actual string)
    if string conatins no jinja syntax (no actual string)
    if string variable match dictionary (no actual string)
    """
    @app.route("/")
    def index():
        return flask.render_template_string(
            None,
            var=1
        )

    try:
        rv = client.get("/")
        assert False
    except TypeError:
        assert True
    
