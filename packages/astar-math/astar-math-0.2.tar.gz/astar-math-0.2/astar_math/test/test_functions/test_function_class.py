import unittest

import numpy as np

from astar_math.functions import polynomial, fourier, gaussian, Abs, Arcsin, Arctan, Const, Cos, Cot, Csc, Exp, Power, Ln, Log, Sin, Sec, Function
from astar_math.functions import Arccos

npa = np.array


class TestAbs(unittest.TestCase):
    def setUp(self) -> None:
        self.abs = Abs()

    def test_abs_get(self):
        y = lambda x: np.abs(x)
        t = np.linspace(-1, 1, 100)
        yt = y(t)
        y_abs = self.abs.get(t)
        self.assertTrue(np.allclose(yt, y_abs))

    def test_abs_integral(self):
        y = self.abs.integral(-1, 1)
        self.assertTrue(np.isclose(y, 1))


class TestArccos(unittest.TestCase):
    def setUp(self) -> None:
        self.arccos = Arccos()

    def test_arccos_get(self):
        y = lambda x: np.arccos(x)
        t = np.linspace(-1, 1, 100)
        t = t[1:-1]
        yt = y(t)
        y_arccos = self.arccos.get(t)
        self.assertTrue(np.allclose(yt, y_arccos))

    def test_arccos_derivative(self):
        y = lambda x: -1 / np.sqrt(1 - x * x)
        diff = self.arccos.derivative()
        t = np.linspace(-1, 1, 100)
        t = t[1:-1]
        yt = y(t)
        diff_t = diff(t)
        self.assertTrue(np.allclose(yt, diff_t))


class TestArcsin(unittest.TestCase):
    def setUp(self) -> None:
        self.arcsin = Arcsin()

    def test_arcsin_get(self):
        y = lambda x: np.arcsin(x)
        t = np.linspace(-1, 1, 100)
        yt = y(t)
        y_arcsin = self.arcsin.get(t)
        self.assertTrue(np.allclose(yt, y_arcsin))

    def test_arcsin_derivative(self):
        y = lambda x: 1 / np.sqrt(1 - x * x)
        diff = self.arcsin.derivative()
        t = np.linspace(-1, 1, 100)
        t = t[1:-1]
        yt = y(t)
        diff_t = diff(t)
        self.assertTrue(np.allclose(yt, diff_t))

    def test_arcsin_integral(self):
        arcsin_integral = self.arcsin.indefinite_integral(inplace=False)
        t = np.linspace(-1, 1, 100)
        y = lambda xx: np.sqrt(1-xx*xx) + xx*np.arcsin(xx)
        yt = y(t)
        yint = arcsin_integral(t)
        self.assertTrue(np.allclose(yt, yint))


class TestArctan(unittest.TestCase):
    def setUp(self) -> None:
        self.arctan = Arctan()

    def test_arctan_get(self):
        y = lambda x: np.arctan(x)
        t = np.linspace(-1, 1, 100)
        yt = y(t)
        y_arctan = self.arctan.get(t)
        self.assertTrue(np.allclose(yt, y_arctan))

    def test_arctan_derivative(self):
        y = lambda x: 1 / (1 + x * x)
        diff = self.arctan.derivative()
        t = np.linspace(-1, 1, 100)
        yt = y(t)
        diff_t = diff(t)
        self.assertTrue(np.allclose(yt, diff_t))


class TestConst(unittest.TestCase):
    def setUp(self) -> None:
        self.const = Const(8)

    def test_const_get(self):
        t = np.linspace(-1, 1, 100)
        yt = np.ones_like(t) * 8
        y_const = self.const.get(t)
        self.assertTrue(np.allclose(yt, y_const))

    def test_const_derivative(self):
        diff = self.const.derivative()
        t = np.linspace(-1, 1, 100)
        yt = np.zeros_like(t)
        diff_t = diff(t)
        self.assertTrue(np.allclose(yt, diff_t))


class TestCos(unittest.TestCase):
    def setUp(self) -> None:
        self.cos = Cos()

    def test_cos_get(self):
        t = np.linspace(-1, 1, 100)
        yt = np.cos(t)
        y_cos = self.cos.get(t)
        self.assertTrue(np.allclose(yt, y_cos))

    def test_cos_derivative(self):
        diff = self.cos.derivative()
        t = np.linspace(-1, 1, 100)
        yt = -np.sin(t)
        diff_t = diff(t)
        self.assertTrue(np.allclose(yt, diff_t))

    def test_cos_integral(self):
        y = self.cos.integral(-1, 1)
        sin = self.cos.indefinite_integral(inplace=False)
        self.assertTrue(np.isclose(y, sin(1) - sin(-1)))


class TestCot(unittest.TestCase):
    def setUp(self) -> None:
        self.cot = Cot()

    def test_cot_get(self):
        t = np.linspace(-1, 1, 100)
        yt = 1 / np.tan(t)
        y_cos = self.cot.get(t)
        self.assertTrue(np.allclose(yt, y_cos))

    def test_cot_derivative(self):
        diff = self.cot.derivative()
        t = np.linspace(-1, 1, 100)
        func = - Csc() * Csc()
        yt = func.get(t)
        diff_t = diff(t)
        self.assertTrue(np.allclose(yt, diff_t))

    def test_cot_integral(self):
        y = self.cot.integral(-1, 1)
        sin = self.cot.indefinite_integral(inplace=False)
        self.assertTrue(np.isclose(y, np.log(np.abs(sin(1))) - np.log(np.abs(sin(-1)))))


class TestCsc(unittest.TestCase):
    def setUp(self) -> None:
        self.csc = Csc()

    def test_csc_get(self):
        t = np.linspace(-1, 1, 100)
        yt = 1 / np.sin(t)
        y_csc = self.csc.get(t)
        self.assertTrue(np.allclose(yt, y_csc))

    def test_csc_derivative(self):
        diff = self.csc.derivative()
        t = np.linspace(-1, 1, 100)
        yt = -1 / (np.tan(t) * np.sin(t))
        diff_t = diff(t)
        self.assertTrue(np.allclose(yt, diff_t))

    def test_csc_integral(self):
        y = self.csc.integral(-1, 1)
        csc_int = self.csc.indefinite_integral(inplace=False)
        csc_int_derivative = csc_int.derivative()
        t = np.linspace(-1, 1, 100)
        y1 = self.csc(t)
        y2 = csc_int_derivative(t)
        self.assertTrue(np.allclose(y1, y2))


class TestExp(unittest.TestCase):
    def setUp(self) -> None:
        self.exp = Exp()

    def test_exp_get(self):
        t = np.linspace(-1, 1, 100)
        yt = np.exp(t)
        y_exp = self.exp.get(t)
        self.assertTrue(np.allclose(yt, y_exp))

    def test_exp_derivative(self):
        diff = self.exp.derivative()
        t = np.linspace(-1, 1, 100)
        yt = np.exp(t)
        diff_t = diff(t)
        self.assertTrue(np.allclose(yt, diff_t))

    def test_exp_integral(self):
        y = self.exp.integral(-1, 1)
        exp_int = self.exp.indefinite_integral(inplace=False)
        exp_int_derivative = exp_int.derivative()
        t = np.linspace(-1, 1, 100)
        y1 = self.exp(t)
        y2 = exp_int_derivative(t)
        self.assertTrue(np.allclose(y1, y2))
        self.assertAlmostEqual(y, np.exp(1) - np.exp(-1))


class TestPower(unittest.TestCase):
    def setUp(self) -> None:
        self.a = 4.
        self.power = Power(self.a)
        self.a2 = 2.
        self.power2 = Power(self.a2)
        self.a3 = -2.
        self.power3 = Power(self.a3)

    def test_exp_get(self):
        t = np.linspace(-1, 1, 100)
        yt = self.a ** t
        y_exp = self.power.get(t)
        self.assertTrue(np.allclose(yt, y_exp))

    def test_power_derivative(self):
        diff = self.power.derivative()
        t = np.linspace(-1, 1, 100)
        yt = np.log(self.a) * self.a ** t
        diff_t = diff(t)
        self.assertTrue(np.allclose(yt, diff_t))

    def test_mul1(self):
        power_8x = self.power * self.power2
        t = np.linspace(-1, 1, 100)
        yt = 8. ** t
        y_exp = power_8x.get(t)
        self.assertTrue(np.allclose(yt, y_exp))

    def test_mul2(self):
        power_p4x = self.power2 * self.power3
        t = np.linspace(-1, 1, 100)
        yt = (-4.) ** t
        y_exp = power_p4x.get(t)
        self.assertTrue(np.allclose(yt[~np.isnan(yt)], y_exp[~np.isnan(y_exp)]))


class TestLn(unittest.TestCase):
    def setUp(self) -> None:
        self.a = 4.
        self.ln = Ln()

    def test_ln_get(self):
        t = np.linspace(0, 2, 100)
        t = t[1:]
        yt = np.log(t)
        y_ln = self.ln.get(t)
        self.assertTrue(np.allclose(yt, y_ln))

    def test_ln_derivative(self):
        diff = self.ln.derivative()
        t = np.linspace(0, 2, 100)
        t = t[1:]
        yt = 1 / t
        diff_t = diff(t)
        self.assertTrue(np.allclose(yt, diff_t))


class TestLog(unittest.TestCase):
    def setUp(self) -> None:
        self.a = 4.
        self.log = Log(self.a)

    def test_log_get(self):
        t = np.linspace(0, 2, 100)
        t = t[1:]
        yt = np.log(t) / np.log(self.a)
        y_log = self.log.get(t)
        self.assertTrue(np.allclose(yt, y_log))

    def test_ln_derivative(self):
        diff = self.log.derivative()
        t = np.linspace(0, 2, 100)
        t = t[1:]
        yt = 1 / (t * np.log(self.a))
        diff_t = diff(t)
        self.assertTrue(np.allclose(yt, diff_t))


class TestSin(unittest.TestCase):
    def setUp(self) -> None:
        self.sin = Sin()

    def test_sin_get(self):
        t = np.linspace(-1, 1, 100)
        yt = np.sin(t)
        y_sin = self.sin.get(t)
        self.assertTrue(np.allclose(yt, y_sin))

    def test_sin_derivative(self):
        diff = self.sin.derivative()
        t = np.linspace(-1, 1, 100)
        yt = np.cos(t)
        diff_t = diff(t)
        self.assertTrue(np.allclose(yt, diff_t))


class TestSec(unittest.TestCase):
    def setUp(self) -> None:
        self.sec = Sec()

    def test_sec_get(self):
        t = np.linspace(-1, 1, 100)
        yt = 1 / np.cos(t)
        y_csc = self.sec.get(t)
        self.assertTrue(np.allclose(yt, y_csc))

    def test_sec_derivative(self):
        diff = self.sec.derivative()
        t = np.linspace(-1, 1, 100)
        yt = np.tan(t) * self.sec.get(t)
        diff_t = diff(t)
        self.assertTrue(np.allclose(yt, diff_t))
