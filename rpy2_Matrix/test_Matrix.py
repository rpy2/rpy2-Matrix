import pytest

from rpy2 import robjects
from rpy2.robjects.vectors import IntVector
from . import Matrix
from . import conversion


@pytest.mark.parametrize(
    'args,expected_cls',
<<<<<<< Updated upstream
    [((0, 2, 3), Matrix.generalMatrix),
     ((0, 2, 2), Matrix.ddiMatrix),
     ((IntVector([0, 1, 2, 3]), 2, 2), Matrix.dgeMatrix)]
=======
    [(((0, ), 2, 3), Matrix.generalMatrix),
     (((0, 1, 1, 0), 2, 2), Matrix.symmetricMatrix)]
>>>>>>> Stashed changes
)
def test_Matrix(args, expected_cls):
    final_args = (robjects.baseenv['c'](*(args[0])),
                  args[1], args[2])
    m = Matrix.Matrix.new(*final_args)
    assert isinstance(m, expected_cls)


@pytest.mark.parametrize(
    'args,kwargs,expected_cls',
    [((IntVector([1, 3, 4]), IntVector([2, 3, 5])),
<<<<<<< Updated upstream
      {'x': IntVector([3, 9, 21])},
      Matrix.dgCMatrix),
     ((IntVector([1, 2, 3]), IntVector([2, 3, 4])),
      {'x': True},
      Matrix.lgCMatrix),
     ((IntVector([1, 2, 3, 4, 5, 6]),
       IntVector([7, 6, 5, 4, 3, 2])),
      {},
      Matrix.ngCMatrix)]
=======
      {'x': IntVector([3, 9, 21]), 'repr': 'C'},
      Matrix.sparseMatrix),
     ((IntVector([1, 3, 4]), IntVector([2, 3, 5])),
      {'x': IntVector([3, 9, 21]), 'repr': 'T'},
      Matrix.sparseMatrix)]
>>>>>>> Stashed changes
)
def test_sparseMatrix(args, kwargs, expected_cls):
    m = Matrix.sparseMatrix.new(*args, **kwargs)
    assert isinstance(m, expected_cls)


def test_conversion_wrap():
    with conversion.rs4map_context:
        # The package Matrix is already imported in the embedded R
        # (implicit when importing our Python package Matrix).
        m = robjects.r('Matrix(c(0,1,0,0), 6, 4)')
    assert isinstance(m, Matrix.Matrix)
