"""This module handles the conversion of data structures
between R objects from the package Matrix and scipy sparse matrices."""

import rpy2.robjects.conversion as conversion
from rpy2.rinterface import SexpS4

try:
    import scipy.sparse
    has_scipy = True
except ImportError:
    has_scipy = False
from . import Matrix


rs4_map = conversion.converter.rpy2py_nc_name[SexpS4]
rs4map_context = conversion.NameClassMapContext(rs4_map, Matrix._classmap)

cast = conversion.Converter('Cast R objects into scipy objects')


if has_scipy:

    def py2rpy_csc_matrix(obj) -> Matrix.Matrix:
        # TODO: implement how to populate an R compressed sparse column matrix
        # from the scipy object.
        # res = Matrix.sparseMatrix(giveCsparse=True)
        raise NotImplementedError()

    cast.py2rpy.register(scipy.sparse.csc_matrix, py2rpy_csc_matrix)
