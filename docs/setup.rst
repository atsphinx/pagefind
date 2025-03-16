===============
Getting started
===============

Installation
============

This is published on PyPI.
You can isntall by pip or other package managers.

.. code-block:: console

   pip install atsphinx-pagefind

Set up
======

.. code-block:: python
   :name: conf.py

   extensions = [
       # Other extensions
       ...,
       "atsphinx.pagefind",  # Add it!
   ]

Runs
====

When you run sphinx-build with html format builders after register this into extensions,
it generates search page [#]_ with pagefind.

.. [#] ``/search.html`` ( ``html`` builder) or ``/search/index.html`` ( ``dirhtml`` builder )
