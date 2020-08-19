import pytest

from calc import Calc


class Test_calc():
    def setup_class(self):
        self.calc = Calc()

    @pytest.mark.parametrize('a,b,c',
                             [(1, 2, 3), (0.1, 0.2, 0.3), (1, 0.1, 1.1), (-1, -2, -3), (1, -2, -1), (-2, 1, -1),
                              (-1, 0.2, -0.8)]
                             )
    def test_add(self, a, b, c):
        assert self.calc.add(a, b) == c

    @pytest.mark.parametrize('a,b,c', [(6, 2, 3), (6, -2, -3), (-6, 2, -3), (-6, -2, 3), (6, 0.5, 12),
                                       (0.6, 2, 0.3), (0.6, 0.2, 3), (6, 0, 0)])
    def test_div(self, a, b, c):
        assert self.calc.div(a, b) == c
