ST-2022 Group Project
========================

- v2.0

  - `spec <https://docs.google.com/spreadsheets/d/1QADsETXS6YzqMmRBtplheqgtbMsZcRDUV6zPW56OfkM/edit?usp=sharing>`_
  - group project3, using PC, CC, CACC
  - API: ``get_root_path()``


- v1.0

  - `spec <https://docs.google.com/spreadsheets/d/1CWzXtN7biDFjhNZDuiSEettylRWZJQOEwtPNYqtCsYQ/edit?usp=sharing>`_
  - group project2, using ISP
  - API: ``render_template()``



Usage

.. code:: sh

  python3 -m venv flask
  pip3 install <packages>

  source bin/activate

  coverage run -m pytest > output

  coverage html #generage htmlcov/index.html
