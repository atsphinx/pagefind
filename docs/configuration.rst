=============
Configuration
=============

Generic options
===============

.. confval:: pagefind_directory
   :type: string
   :default: ``"_pagefind"``
   :required: False

   Directory name that is generated indexes by pagefind.
   This is handled as relative path from output directory.

Indexing options
================

.. confval:: pagefind_root_selector
   :type: string
   :default: ``".body"``
   :required: False

   Query selector of content in html page.
   Default value ``".body"`` is selector that write :data:`body` in ``basic`` theme.

   Please change value when you use custom theme and theme write :data:`body` into other selector.
