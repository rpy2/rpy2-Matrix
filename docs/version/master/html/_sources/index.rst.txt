.. rpy2-Matrix documentation master file, created by
   sphinx-quickstart on Sat Nov 16 22:52:31 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

rpy2-Matrix: mapping R's package Matrix for rpy2
================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Overview
--------

This package is a wrapper for the R package `Matrix`.

.. code-block:: python

   from rpy2_Matrix import Matrix
   from rpy2.robjects.vectors import IntVector

   m = Matrix.sparseMatrix.new(
       IntVector([1, 3, 4]), IntVector([2, 3, 5]),
       x=IntVector([3, 9, 21]), giveCsparse=True)

An extension for the :mod:`rpy2` conversion system is provided, allowing to
map R objects resulting from the evaluation of R code to the wrapping classes
defined in this package:

.. code-block:: python

   import rpy2_Matrix.conversion as matrix_conversion
   from rpy2 import robjects

   with conversion.rs4map_context:
        # The package Matrix is already imported in the embedded R
        # (implicit when importing our Python package Matrix).
        m = robjects.r('Matrix(c(0,1,0,0), 6, 4)')

	     

Inheritance Diagram
-------------------

.. inheritance-diagram:: rpy2_Matrix.Matrix
   :parts: 1


module `Matrix`
---------------

.. automodule:: rpy2_Matrix.Matrix


module `conversion`
-------------------

.. automodule:: rpy2_Matrix.conversion

	   
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
