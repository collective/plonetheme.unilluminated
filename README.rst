
Introduction
============

The ``plonetheme.unilluminated`` package uses the **theming** and **packaging** features
available in `plone.app.theming`_ to make the `CSS Templates`_ theme `Unilluminated`_ easily
available in `Plone 4.1`_.

Installation
------------

Add Plone site
~~~~~~~~~~~~~~

Install Plone 4.1 with `plone.app.theming`_ and create a Plone site (if you have not already)
with Diazo theming configured.

.. image:: https://github.com/collective/plonetheme.unilluminated/raw/master/screenshot2.png


Zip file
~~~~~~~~

If you are an end user, you might enjoy installation via zip file import.

1. Download the zip file: http://plone.org/products/plonetheme.unilluminated/releases/0.1.2/unilluminated.zip
2. Import the theme from the Diazo theme control panel.

.. image:: https://github.com/collective/plonetheme.unilluminated/raw/master/screenshot4.png

Buildout
~~~~~~~~

If you are a developer, you might enjoy installation via buildout.

Add ``plonetheme.unilluminated`` to your ``plone.recipe.zope2instance`` section's *eggs* parameter e.g.::

    [instance]
    eggs =
        Plone
        …
        plonetheme.unilluminated

Select theme
~~~~~~~~~~~~

Select and enable the theme from the Diazo control panel.

.. image:: https://github.com/collective/plonetheme.unilluminated/raw/master/screenshot3.png

That's it!

You should see (without the calendar):

.. image:: https://github.com/collective/plonetheme.unilluminated/raw/master/plonetheme/unilluminated/theme/unilluminated/preview.png

Help
----

Obviously there is more work to be done. If you want to help, pull requests accepted! Some ideas:

* Add a diazo rule to import Plone editing styles
* Configure styles to use portal_css
* Add quick installer support
* Improve styles 

License
-------

The author is not a "license guy", but the Unilluminated theme is distributed via CC 3.0 license [1]_ and this package is GPL version 2 (assuming that makes sense).

.. _`Unilluminated`: http://www.freecsstemplates.org/preview/unilluminated/
.. _`plone.app.theming`: http://pypi.python.org/pypi/plone.app.theming
.. _`Plone 4.1`: http://pypi.python.org/pypi/Plone/4.1rc2
.. _`CSS Templates`: http://www.freecsstemplates.org/

.. [1] http://www.freecsstemplates.org/license/
