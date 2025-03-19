=================
atsphinx-pagefind
=================

Pagefind search component for Sphinx.

Overview
========

This is Sphinx extension to use Pagefind for searching documentation.

Pagefind is website search library for static site.It can indexes from published website.
Please see `official website <https://pagefind.app/>`_ if you want to know more information.

You can see `own document <https://atsphinx.github.io/pagefind/>`_ to know behavior of this.

Getting started
===============

Installation
------------

This publishes on PyPI. You can install by ``pip`` and other package managers.

.. code:: console

   pip install atsphinx-pagefind

Configuration
-------------

Register this into your ``conf.py`` of document.

.. code:: python

   extensions = [
       ...,  # Your extensions
       "atsphinx.pagefind",
   ]
