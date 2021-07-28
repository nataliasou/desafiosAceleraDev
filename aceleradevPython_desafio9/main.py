# .travis.yml
config = """
language: python
python:
  - "2.7"
  - "3.7"
  - "pypy"   # currently Python 2.7.13, PyPy 7.1.1
  - "pypy3"  # currently Python 3.6.1,  PyPy 7.1.1-beta0

install:
  - pip install -r requirements.txt

script: pytest
"""
