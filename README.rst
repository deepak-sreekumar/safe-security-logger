.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/safe-security-logger.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/safe-security-logger
    .. image:: https://readthedocs.org/projects/safe-security-logger/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://safe-security-logger.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/pypi/v/safe-security-logger.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/safe-security-logger/

|

====================
safe-security-logger
====================


    Structured JSON logger package from Safe Security



============
Installation
============

::

    pip install -i https://test.pypi.org/simple/ safe-security-logger


============
Usage
============

::

    import safe_security_logger as logging

    logger = logging.getLogger("awesome-logger")

    def test():
        logger.info("Hello world")

    test()
