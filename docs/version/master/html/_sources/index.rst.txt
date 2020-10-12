.. rpy2-Matrix documentation master file, created by
   sphinx-quickstart on Sat Nov 16 22:52:31 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

rpy2-Matrix: mapping R's package Matrix for rpy2
================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Installation
------------

.. code-block:: python

   pip install git+https://github.com/rpy2/rpy2-Matrix.git#egg=rpy2_Matrix


Usage
-----

This package is a wrapper for the R package `Matrix`.


Create R Matrix object with Python
..................................

.. code-block:: python

   from rpy2_Matrix import Matrix
   from rpy2.robjects.vectors import IntVector

   m = Matrix.sparseMatrix.new(
       IntVector([1, 3, 4]), IntVector([2, 3, 5]),
       x=IntVector([3, 9, 21]), giveCsparse=True)

`m` is a Python object acting as a proxy to interact
with an R object in the R memory space.


Map R Matrix object creating in R
.................................

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

`m` was automatically mapped to one of the matrix classes defined in this package.


Using matrix objects
....................

Objects can be passed to R functions compatible with `Matrix` objects.
The R package `Matrix` contains such functions. 

We create a matrix to run our examples:

.. code-block:: python

   m = Matrix.sparseMatrix.new(
           IntVector([1, 3, 4]), IntVector([2, 3, 5]),
           x=IntVector([3, 9, 21]), giveCsparse=True)


.. code-block:: python

   >>> print(m)
   4 x 5 sparse Matrix of class "dgCMatrix"
               
   [1,] . 3 . .  .
   [2,] . . . .  .
   [3,] . . 9 .  .
   [4,] . . . . 21


To get the diagonal of our matrix:


.. code-block:: python

   >>> Matrix.Matrix_pack.diag(m)
   R object with classes: ('numeric',) mapped to:
   [0.000000, 0.000000, 9.000000, 0.000000]

Values in the matrix can also be accessed through R's own subsetting system

.. note::

   See the :mod:`rpy2` documentation for more information it in the section about
   the method `rx()`.


For example, to get the values in the first row and second column (remember: R
arrays are one-indexed, not zero-indexed)

.. code-block:: python
		
   >>> m.rx(1, 2)
   R object with classes: ('numeric',) mapped to:
   [3.000000]

To get the complete second column:

.. code-block:: python

   >>>  m.rx(True, 2)
   R object with classes: ('numeric',) mapped to:
   [3.000000, 0.000000, 0.000000, 0.000000]

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
