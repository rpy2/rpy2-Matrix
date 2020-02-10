"""This module handles the conversion of data structures
between R objects from the package Matrix and scipy sparse matrices."""

from functools import partial
import rpy2.robjects
import rpy2.robjects.conversion as conversion
from rpy2.rinterface import SexpS4
from rpy2.robjects.methods import RS4

try:
    import scipy.sparse
    has_scipy = True
except ImportError:
    has_scipy = False
import typing
from . import Matrix


rs4map_context = partial(rpy2.robjects.rs4map_context, Matrix._classmap)

cast = conversion.Converter('Cast R objects into scipy objects')


if has_scipy:
    def rpy2py_sexps4_scipy(
            obj: SexpS4
    ) -> typing.Union[RS4, scipy.sparse.spmatrix]:

        cls = Matrix.nameclassmap.find(obj.extends())
        if cls is RS4:
            return cls(obj)
        else:
            # TODO: implement how to populate a scipy sparse column matrix
            # from an R object.
            # 1. identify the best matching scipy class
            # 2. create an instance populated with data
            raise NotImplementedError()

    def py2rpy_csc_matrix(obj) -> Matrix.Matrix:
        # TODO: implement how to populate an R compressed sparse column matrix
        # from the scipy object.
        # res = Matrix.sparseMatrix(giveCsparse=True)
        raise NotImplementedError()

    cast.rpy2py.register(SexpS4, rpy2py_sexps4_scipy)
    cast.py2rpy.register(scipy.sparse.csc_matrix, py2rpy_csc_matrix)
