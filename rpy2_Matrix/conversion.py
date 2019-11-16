"""This module handles the conversion of data structures
between R objects from the package Matrix and scipy sparse matrices."""

import rpy2.robjects.conversion as conversion
import rpy2.rinterface as rinterface
from rpy2.rinterface import SexpS4
from rpy2.robjects.methods import RS4

try:
    import scipy.sparse
    has_scipy = True
except ImportError:
    has_scipy = False
import typing
import warnings

from . import Matrix


def rpy2py_sexps4_wrap(obj: SexpS4) -> RS4:
    """Wrap an R S4 object into a Matrix class, if possible.

    If there is no matching Matrix class, this returns an
    robjects-level RS4 instance."""

    for x in obj.rclass:
        cls = Matrix._classmap.get(x)
        if cls is not None:
            return cls(obj)
    return RS4(obj)


wrap = conversion.Converter('Wrap R objects')
wrap.rpy2py.register(SexpS4, rpy2py_sexps4_wrap)

cast = conversion.Converter('Cast R objects into scipy objects')


if has_scipy:
    def rpy2py_sexps4_scipy(
            obj: SexpS4
    ) -> typing.Union[RS4, scipy.sparse.spmatrix]:

        res = rpy2py_sexps4_wrap(obj)
        if type(res) is RS4:
            return res
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

    wrap.py2rpy.register(scipy.sparse.csc_matrix, py2rpy_csc_matrix)

    cast.rpy2py.register(SexpS4, rpy2py_sexps4_scipy)
    cast.py2rpy.register(scipy.sparse.csc_matrix, py2rpy_csc_matrix)
