ST-2022 Group Project
========================

- Final Report

  - `ppt <https://docs.google.com/presentation/d/1act51bX2gQ-bNKYqgmIFuGl47beOGu3GlYtnj_Uegro/edit?usp=sharing>`_

- v3.0

  - refer to final
  - `spec <https://docs.google.com/spreadsheets/d/1BK3O25pRYLnXxNRhNQnu9dPVlXgKkTXmDsPhYlAuALw/edit?usp=sharing>`_
  - ``tests/test_final.py``, using ISP
  - API: ``url_for()``, ``send_file()``, ``is_ip()``, ``make_response()``, ``get_env()``, ``get_debug_flag()``


- v2.0

  - refer to group work 3
  - `spec <https://docs.google.com/spreadsheets/d/1QADsETXS6YzqMmRBtplheqgtbMsZcRDUV6zPW56OfkM/edit?usp=sharing>`_
  - ``tests/test_group_project3.py``, using PC, CC, CACC
  - API: `get_root_path() <https://github.com/chameleon10712/Flask-Testing/blob/main/src/flask/helpers.py#L680>`_


- v1.0

  - refer to group work 2
  - `spec <https://docs.google.com/spreadsheets/d/1CWzXtN7biDFjhNZDuiSEettylRWZJQOEwtPNYqtCsYQ/edit?usp=sharing>`_
  - ``tests/test_group_project2.py``, using ISP
  - API: ``render_template()``



Usage

.. code:: sh

  python3 -m venv flask
  pip3 install <packages>

  source bin/activate

  coverage run -m pytest > output

  coverage html #generage htmlcov/index.html
