import pytest

from . import Matrix


@pytest.mark.parametrize(
    'args,expected_cls',
    [((0, 2, 3), Matrix.generalMatrix),
     ((0, 2, 2), Matrix.symmetricMatrix)]
)
def test_Matrix(args, expected_cls):
    m = Matrix.Matrix.new(*args)
    assert isinstance(m, expected_cls)
