"""Map the R package Matrix for rpy2.

This module maps some of the classes defined by the R
package Matrix.
"""

from rpy2.rinterface import MissingArg
import rpy2.robjects
import rpy2.robjects.methods
from rpy2.robjects import vectors
from rpy2.robjects.packages import (importr,
                                    WeakPackage)
import typing
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    Matrix_pack = importr('Matrix', on_conflict="warn")

TARGET_VERSION = '1.4-'

if not Matrix_pack.__version__.startswith(TARGET_VERSION):
    warnings.warn(
        'This was designed to match Matrix version starting with %s '
        'but you have %s' % (TARGET_VERSION, Matrix_pack.__version__)
    )

MissingOrInt = typing.Union[typing.Literal[MissingArg], int]

Matrix_weakpack = WeakPackage(Matrix_pack._env,
                              Matrix_pack.__rname__,
                              translation=Matrix_pack._translation,
                              exported_names=Matrix_pack._exported_names,
                              on_conflict="warn",
                              version=Matrix_pack.__version__,
                              symbol_r2python=Matrix_pack._symbol_r2python,
                              symbol_resolve=Matrix_pack._symbol_resolve)


class RS4Vector(rpy2.robjects.methods.RS4):
    """Base class for RS4 objects with the behavior of base R vectors."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ro = vectors.VectorOperationsDelegator(self)
        self.rx = vectors.ExtractDelegator(self)


def _setExtractDelegators(self):
    self.rx = vectors.ExtractDelegator(self)
    self.rx2 = vectors.DoubleExtractDelegator(self)


class mMatrix(metaclass=rpy2.robjects.methods.RS4Auto_Type):
    """Mapping for the RS4 class Matrix::mMatrix."""
    __rname__ = 'mMatrix'
    __rpackagename__ = 'Matrix'


class replValueSp(metaclass=rpy2.robjects.methods.RS4Auto_Type):
    """Mapping for the RS4 class Matrix::replValueSp."""
    __rname__ = 'replValueSp'
    __rpackagename__ = 'Matrix'


class Matrix(mMatrix, replValueSp):
    """Mapping for the RS4 class Matrix::Matrix."""
    __rname__ = 'Matrix'
    __rpackagename__ = 'Matrix'

    @classmethod
    def new(cls,
            data=rpy2.robjects.NA_Logical,
            nrow: MissingOrInt = MissingArg,
            ncol: MissingOrInt = MissingArg,
            byrow: bool = False,
            dimnames = rpy2.robjects.NULL,
            sparse = rpy2.robjects.NULL,
            doDiag: bool = True,
            forceCheck: bool = False):

        unclassed_obj = Matrix_pack.Matrix(
            data=data,
            nrow=nrow, ncol=ncol, byrow=byrow,
            dimnames=dimnames,
            sparse=sparse, doDiag=doDiag, forceCheck=forceCheck)
        wrapcls = _classmap.get(unclassed_obj.rclass[0])
        if wrapcls is None:
            # TODO: issue a warning if no class map ?
            obj = unclassed_obj
        else:
            obj = wrapcls(unclassed_obj)
        return obj


class compMatrix(Matrix):
    __rname__ = 'compMatrix'


class triangularMatrix(Matrix):
    __rname__ = 'triangularMatrix'


class dMatrix(Matrix):
    __rname__ = 'dMatrix'


class iMatrix(Matrix):
    __rname__ = 'iMatrix'


class lMatrix(Matrix):
    __rname__ = 'lMatrix'


class nMatrix(Matrix):
    __rname__ = 'nMatrix'


class zMatrix(Matrix):
    __rname__ = 'zMatrix'


class denseMatrix(Matrix):
    __rname__ = 'denseMatrix'


class ddenseMatrix(dMatrix):
    __rname__ = 'ddenseMatrix'


class ldenseMatrix(lMatrix):
    __rname__ = 'ldenseMatrix'


class ndenseMatrix(Matrix):
    __rname__ = 'ndenseMatrix'


class sparseMatrix(Matrix):
    """Mapping for the RS4 class Matrix::sparseMatrix."""

    __rname__ = 'sparseMatrix'

    @staticmethod
    def new(i=vectors.MissingArg, j=vectors.MissingArg,
            p=vectors.MissingArg, x=vectors.MissingArg,
            dims=vectors.MissingArg, dimnames=vectors.MissingArg,
            symmetric: bool = False, triangular: bool = False,
            index1: bool = True,
            giveCsparse: bool = True, check: bool = True,
            use_last_ij: bool = False):
        unclassed_obj = Matrix_pack.sparseMatrix(
            i=i, j=j, p=p, x=x, dims=dims, dimnames=dimnames,
            symmetric=symmetric, triangular=triangular, index1=index1,
            giveCsparse=giveCsparse, check=check, use_last_ij=use_last_ij)
        wrapcls = _classmap.get(unclassed_obj.rclass[0])
        if wrapcls is None:
            # TODO: issue a warning if no class map ?
            obj = unclassed_obj
        else:
            obj = wrapcls(unclassed_obj)
        return obj


class diagonalMatrix(sparseMatrix):
    __rname__ = "diagonalMatrix"


class ddiMatrix(diagonalMatrix, RS4Vector):
    __rname__ = "ddiMatrix"


class ldiMatrix(diagonalMatrix, RS4Vector):
    __rname__ = "ldiMatrix"


class dgeMatrix(ddenseMatrix, RS4Vector):
    __rname__ = "dgeMatrix"


class dtrMatrix(ddenseMatrix, RS4Vector):
    __rname__ = "dtrMatrix"


class dtpMatrix(ddenseMatrix, RS4Vector):
    __rname__ = "dtpMatrix"


class dsyMatrix(ddenseMatrix):
    __rname__ = "dsyMatrix"


class dspMatrix(ddenseMatrix):
    __rname__ = "dspMatrix"


class generalMatrix(compMatrix):
    """Mapping for the RS4 class Matrix::generalMatrix."""
    __rname__ = 'generalMatrix'


class symmetricMatrix(compMatrix):
    """Mapping for the RS4 class Matrix::symmetricMatrix."""
    __rname__ = 'symmetricMatrix'


class dsparseMatrix(dMatrix, sparseMatrix):
    """Mapping for the RS4 class Matrix::dsparseMatrix."""
    __rname__ = 'dsparseMatrix'


class dgCMatrix(dsparseMatrix, generalMatrix,
                RS4Vector):
    """Mapping for the RS4 class Matrix::dcgMatrix."""
    __rname__ = 'dgCMatrix'


class CsparseMatrix(sparseMatrix):
    """Mapping for the RS4 class Matrix::CsparseMatrix."""
    __rname__ = 'CsparseMatrix'


class dCsparseMatrix(sparseMatrix):
    """Mapping for the RS4 class Matrix::dCsparseMatrix."""
    __rname__ = 'dCsparseMatrix'


class dsCMatrix(CsparseMatrix, dsparseMatrix, symmetricMatrix,
                dCsparseMatrix,
                RS4Vector):
    """Mapping for the RS4 class Matrix::dsCMatrix."""
    __rname__ = 'dsCMatrix'


class TsparseMatrix(sparseMatrix):
    """Mapping for the RS4 class Matrix::TsparseMatrix."""
    __rname__ = 'TsparseMatrix'


class dgTMatrix(TsparseMatrix, dsparseMatrix, generalMatrix,
                RS4Vector):
    """Mapping for the RS4 class Matrix::dgTMatrix."""
    __rname__ = 'dgTMatrix'


_classmap = {
    'ddiMatrix': ddiMatrix,
    'dgeMatrix': dgeMatrix,
    'dtrMatrix': dtrMatrix,
    'dtpMatrix': dtpMatrix,
    'dgCMatrix': dgCMatrix,
    'dsCMatrix': dsCMatrix,
    'dgTMatrix': dgTMatrix
}

nameclassmap = (rpy2.robjects
                .conversion.NameClassMap(rpy2.robjects.methods.RS4))
for k, v in _classmap.items():
    nameclassmap[k] = v
