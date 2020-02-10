import pytest

from rpy2 import robjects
from rpy2.robjects.vectors import IntVector
from . import Matrix
from . import conversion


@pytest.mark.parametrize(
    'args,expected_cls',
    [((0, 2, 3), Matrix.generalMatrix),
     ((0, 2, 2), Matrix.symmetricMatrix)]
)
def test_Matrix(args, expected_cls):
    m = Matrix.Matrix.new(*args)
    assert isinstance(m, expected_cls)


@pytest.mark.parametrize(
    'args,kwargs,expected_cls',
    [((IntVector([1, 3, 4]), IntVector([2, 3, 5])),
      {'x': IntVector([3, 9, 21]), 'giveCsparse': True},
      Matrix.sparseMatrix),
     ((IntVector([1, 3, 4]), IntVector([2, 3, 5])),
      {'x': IntVector([3, 9, 21]), 'giveCsparse': False},
      Matrix.sparseMatrix)]
)
def test_sparseMatrix(args, kwargs, expected_cls):
    m = Matrix.sparseMatrix.new(*args, **kwargs)
    assert isinstance(m, expected_cls)


def test_conversion_wrap():
    with conversion.rs4map_context():
        # The package Matrix is already imported in the embedded R
        # (implicit when importing our Python package Matrix).
        m = robjects.r('Matrix(c(0,1,0,0), 6, 4)')
    assert isinstance(m, Matrix.Matrix)
