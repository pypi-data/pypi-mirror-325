import collections
import enum
import itertools
from copy import deepcopy
from functools import reduce
from numbers import Number
from typing import Iterable

import numpy as np
from astartool.number import equals_zero
from astartool.error import ParameterTypeError, MethodNotFoundError
from scipy.special import factorial

from astar_math.functions._functions import fourier
from astar_math.functions._intervals import ContinuousBaseIntervals
from astar_math.functions._intervals import R, ListIntervals, BaseIntervals, IntervalType

__all__ = [
    'Abs',
    'Arccos',
    'Arcsin',
    'Arctan',
    'Const',
    'Cos',
    'Cot',
    'Csc',
    'CompositeFunction',
    'CumulativeAreaFunction',
    'Exp',
    'Function',
    'Fourier',
    'IntegralMethod',
    'Ln',
    'Log',
    'MulFunction',
    'Mod',
    'Neq',
    'Polynomial',
    'Power',
    'Sec',
    'Sin',
    'Tan',
    'TrigonometricFunction',
    'self'
]


class IntegralMethod(enum.Enum):
    Rectangle = 0
    Trapezoid = 1


class Function:
    def __init__(self, function=None, *, expression='', name='', domain_of_definition=R):
        if function is None:
            self.functions = []
            self.expression = expression
            self.name = name
        elif isinstance(function, Function):
            self.functions = function.functions
            self.expression = function.expression
            self.name = function.name
        elif callable(function):
            self.functions = [function]
            self.expression = expression
            self.name = name
        elif isinstance(function, Iterable):
            self.functions = list(function)
            self.expression = expression
            self.name = name
        else:
            self.functions = [function]
            self.expression = expression
            self.name = name
        self.domain_of_definition = domain_of_definition

    def add_by_intervals(self, a, b):
        fa = isinstance(a, Number)
        fb = isinstance(b, Number)
        if fa and fb:
            return a + b
        if fa:
            a = np.ones_like(b) * a
        if fb:
            b = np.ones_like(a) * b

        a_nan_ind = np.isnan(a)
        not_b_nan_ind = ~np.isnan(b)
        avi_b_ind = a_nan_ind & not_b_nan_ind
        avi_ab_ind = ~a_nan_ind & not_b_nan_ind
        c = a[:]
        c[avi_b_ind] = b[avi_b_ind]
        c[avi_ab_ind] += b[avi_ab_ind]
        return c

    def taylor(self, x0, n=2, eps=1e-10):
        """
        泰勒展开
        :param x0:
        :param n:
        :return:
        """
        res = []
        diff_func = [self]
        poly = Polynomial({1: 1, 0: -x0}, domain_of_definition=self.domain_of_definition)
        poly_item = 1
        for i in range(n):
            diff_func_item = diff_func[-1]
            item = poly_item * (diff_func_item.get(x0) / factorial(i, True))
            poly_item = poly * poly_item
            diff_func_item = diff_func[-1].derivative()
            diff_func.append(diff_func_item)
            res.append(item)
        return sum(res, Polynomial({}, domain_of_definition=self.domain_of_definition))

    def maclaurin(self, n=2, eps=1e-10):
        """
        麦克劳林展开
        :param n:
        :param eps:
        :return:
        """
        return self.taylor(0, n, eps)

    def tangent_line(self, x, delta_t=1e-8, eps=1e-10, *args, inplace=False, **kwargs):
        """
        切线方程
        :param x:
        :param delta_t:
        :param eps:
        :param args:
        :param inplace:
        :param kwargs:
        :return:
        """
        derivative_function = self.derivative(delta_t=delta_t, eps=eps, *args, inplace=inplace, **kwargs)
        df = derivative_function.get(x)
        if isinstance(x, Number):
            return Polynomial({1: df, 0: self.get(x) - df * x})
        else:
            ks = df
            bs = self.get(x) - df * x
            return [Polynomial({1: k, 0: y - k * xi}) for k, b, xi, y in zip(ks, bs, x, self.get(x))]

    def get(self, x, *args, **kwargs):
        if isinstance(x, Function):
            expression = self.to_string("(" + x.expression + ")")
            f = deepcopy(self)
            return CompositeFunction(f, x, expression=expression)
        elif isinstance(x, Number):
            if x in self.domain_of_definition:
                return reduce(lambda a, b: self.add_by_intervals(a, b), map(lambda f: f(x) if callable(f) else f, self.functions))
            else:
                return np.nan
        elif isinstance(x, np.ndarray):
            obj = deepcopy(self)
            xind_self = self.domain_of_definition.contains(x)
            new_x_self = x.copy()
            new_x_self[~xind_self] = np.nan
            if len(obj.functions) == 1:
                if callable(obj.functions[0]):
                    return obj.functions[0](new_x_self)
                else:
                    y = np.ones_like(x) * obj.functions[0]
                    y[~xind_self] = np.nan
                    return y
            res = np.zeros_like(x, dtype=float)
            res[~xind_self] = np.nan
            for f in obj.functions:
                if isinstance(f, Function):
                    xind = f.domain_of_definition.contains(x)
                    new_x = x.copy()
                    new_x[~xind] = np.nan
                    res = obj.add_by_intervals(res, f(new_x))
                elif callable(f):
                    res = obj.add_by_intervals(res, f(new_x_self))
                else:
                    res = obj.add_by_intervals(res, f)

            xind = self.domain_of_definition.contains(x)
            res[~xind] = np.nan
            return res
        elif callable(x):
            obj = deepcopy(self)
            return CompositeFunction(obj, Function(x))
        else:
            raise ParameterTypeError("x type error")

    def __call__(self, x, *args, **kwargs):
        return self.get(x, *args, **kwargs)

    def __copy__(self):
        return self.copy()

    def __add__(self, other):
        return self.add(other, inplace=False)

    def __iadd__(self, other):
        return self.add(other, inplace=True)

    def __neg__(self):
        return self.neg(inplace=False)

    def __sub__(self, other):
        return self.sub(other, inplace=False)

    def __isub__(self, other):
        return self.sub(other, inplace=True)

    def __mul__(self, other):
        return self.mul(other, inplace=False)

    def __imul__(self, other):
        return self.mul(other, inplace=True)

    def __truediv__(self, other):
        return self.div(other, inplace=False)

    def __idiv__(self, other):
        return self.div(other, inplace=True)

    def __pow__(self, power, modulo=None):
        return self.pow(power, modulo, inplace=False)

    def __rpow__(self, other):
        return self.rpow(other, inplace=False)

    def __radd__(self, other):
        return self.add(other, inplace=False)

    def __rsub__(self, other):
        return self.rsub(other, inplace=False)

    def __rdiv__(self, other):
        return self.rdiv(other, inplace=False)

    def __rtruediv__(self, other):
        poly = Polynomial({-1: 1}, domain_of_definition=self.domain_of_definition)
        return poly.get(self).mul(other)

    def __rmul__(self, other):
        return self.mul(other, inplace=False)

    def add(self, other, *args, inplace=False, eps=1e-10, **kwargs):
        if isinstance(other, (Number, np.ndarray)) or callable(other):
            if inplace:
                if isinstance(other, Function):
                    self.functions.extend(other.functions)
                    self.expression = self.expression + "+(" + other.expression + ")"
                    self.domain_of_definition = self.domain_of_definition.intersection(other.domain_of_definition)
                elif isinstance(other, (Number, np.ndarray)):
                    if other > 0:
                        self.expression = self.expression + "+{other}".format(other=other)
                    else:
                        self.expression = self.expression + "-{other}".format(other=-other)
                    self.functions.append(other)
                else:
                    self.functions.append(other)
                    self.expression = ""
                return self
            else:
                domain_of_definition = self.domain_of_definition
                if isinstance(other, Function):
                    domain_of_definition = self.domain_of_definition.intersection(other.domain_of_definition)
                    new_func = self.functions + other.functions
                    expression = "{}+{}".format(self.expression, other.expression)
                elif isinstance(other, (Number, np.ndarray)):
                    if other > 0:
                        expression = self.expression + "+{other}".format(other=other)
                    else:
                        expression = self.expression + "-{other}".format(other=-other)
                    new_func = self.functions + [other]
                else:
                    new_func = self.functions + [other]
                    expression = ""
                return Function(new_func, expression=expression, domain_of_definition=domain_of_definition)
        else:
            raise ParameterTypeError("错误的数据类型, 加数应该是callable类型或者数字类型")

    def copy(self):
        return Function(self.functions, expression=self.expression, name=self.name, domain_of_definition=self.domain_of_definition)

    def sub(self, other, *, inplace=False):
        if isinstance(other, (np.ndarray, Number)):
            return self.add(-other, inplace=inplace)
        elif isinstance(other, Function):
            return self.add(-other, inplace=inplace)
        elif callable(other):
            return self.add(lambda x: -other(x), inplace=inplace)
        else:
            raise ParameterTypeError("错误的数据类型, 减数应该是callable类型或者数字类型")

    def rsub(self, other, *, inplace=False):
        return -self.sub(other, inplace=inplace)

    def neg(self, *, inplace=False):
        li = []
        for other in self.functions:
            # print("other:", other, f"{type(other)}", isinstance(other, Number))
            if isinstance(other, (Number, np.ndarray)):
                li.append(-other)
            elif isinstance(other, Function):
                neq = Neq()
                li.append(neq.get(other))
            elif callable(other):
                neq = Neq()
                li.append(neq.get(other))
            else:
                raise ParameterTypeError("错误的数据类型, 负数应该是callable类型或者数字类型")
        if inplace:
            self.functions = li
            self.expression = "-({})".format(self.expression)
            return self
        else:
            return Function(li, expression="-({})".format(self.expression))

    def mul(self, other, *args, inplace=False, unfolding='false', max_term=10, **kwargs):
        if isinstance(other, Function):
            if unfolding == 'auto':
                if len(self.functions) * len(other.functions) <= max_term:
                    unfolding = 'true'
                else:
                    unfolding = 'false'
            if unfolding == 'true':
                li = []
                for a, b in itertools.product(self.functions, other.functions):
                    fa_isnumber = isinstance(a, Number)
                    fa_ispolynomial = isinstance(a, Polynomial)
                    fb_isnumber = isinstance(b, Number)
                    fb_ispolynomial = isinstance(b, Polynomial)
                    if (fa_isnumber or fa_ispolynomial) and (fb_isnumber or fb_ispolynomial):
                        li.append(a * b)
                    elif fb_isnumber and not fa_isnumber:
                        li.append(MulFunction(b, a))
                    else:
                        li.append(MulFunction(a, b))
            else:
                li = []
                obj = deepcopy(self)
                for f in other.functions:
                    if isinstance(f, (Number, np.ndarray)):
                        li.append(obj * f)
                    else:
                        li.append(MulFunction(obj, f))

        elif callable(other):
            li = []
            if len(self.functions) == 1:
                li.append(MulFunction(self, other))
            else:
                obj = deepcopy(self)
                for each in obj.functions:
                    if isinstance(each, Function):
                        func = MulFunction(each, other)
                        li.append(func)
                    elif callable(each):
                        func = MulFunction(each, Function(other))
                        li.append(func)
                    else:
                        func2 = MulFunction(each, other)
                        li.append(func2)
        elif isinstance(other, Number) or isinstance(other, np.ndarray):
            li = []
            obj = deepcopy(self)
            for each in obj.functions:
                if callable(each):
                    func = MulFunction(each, other)
                    li.append(func)
                else:
                    li.append(each * other)
        else:
            raise ParameterTypeError("错误的数据类型, 乘数应该是callable类型或者数字类型")

        if inplace:
            self.functions = li
            if isinstance(other, Function):
                self.expression = "({expression})*({other})".format(expression=self.expression, other=other.expression)
                self.domain_of_definition = self.domain_of_definition.intersection(other.domain_of_definition)
            elif isinstance(other, Number):
                self.expression = "({other})*({expression})".format(expression=self.expression, other=other)
            else:
                self.expression = ''
            return self
        else:
            expression = self.expression
            domain_of_definition = self.domain_of_definition
            if isinstance(other, Function):
                expression = "({expression})*({other})".format(expression=expression, other=other.expression)
                domain_of_definition = self.domain_of_definition.intersection(other.domain_of_definition)
            elif isinstance(other, Number):
                expression = "({other})*({expression})".format(expression=expression, other=other)
            else:
                expression = ''
            return Function(li, expression=expression, domain_of_definition=domain_of_definition)

    def pow(self, power, modulo=None, *, inplace=False):
        if modulo is None:
            expression = "({})^({})".format(self.expression, power)
        else:
            expression = "(({})^({}))%({})".format(self.expression, power, modulo)
        if inplace:
            if isinstance(power, (Number, np.ndarray)):
                obj = deepcopy(self)
                self.functions = [lambda x: pow(obj.get(x), power, modulo)]
                self.expression = expression
                return self
            else:
                power_result = Power(self, domain_of_definition=self.domain_of_definition)
                if modulo is None:
                    res = power_result.get(power)
                else:
                    mod_result = Mod(modulo, domain_of_definition=self.domain_of_definition)
                    res = mod_result.get(power_result)

                self.functions = res.functions
                self.expression = res.expression
                return self
        else:
            if isinstance(power, (Number, np.ndarray)):
                return Function([lambda x: pow(self.get(x), power, modulo)], expression=expression)
            else:
                power_result = Power(power, domain_of_definition=self.domain_of_definition)
                if modulo is None:
                    power_result.expression = expression
                    return power_result.get(power)
                else:
                    mod_result = Mod(modulo, domain_of_definition=self.domain_of_definition)
                    return mod_result.get(power_result)

    def rpow(self, other, *, inplace=False):
        expression = "({})^({})".format(other, self.expression)

        if inplace:
            obj = deepcopy(self)
            self.functions = Power(other, domain_of_definition=self.domain_of_definition).get(obj).functions
            self.expression = expression
            return self
        else:
            p = Power(other, domain_of_definition=self.domain_of_definition).get(self)
            p.expression = expression
            return p

    def div(self, other, *, inplace=False):
        if isinstance(other, Function):
            poly = Polynomial({-1: 1}, domain_of_definition=other.domain_of_definition)
            x_1 = poly.get(other)
        elif callable(other):
            poly = Polynomial({-1: 1})
            x_1 = poly.get(other)
        elif isinstance(other, (np.ndarray, Number)):
            x_1 = 1 / other
        else:
            raise ParameterTypeError("错误的数据类型, 除数应该是callable类型或者数字类型")
        return self.mul(x_1, inplace=inplace)

    def rdiv(self, other, *, inplace=False):
        if isinstance(other, (Number, np.ndarray)):
            poly = Polynomial({-1: other}, domain_of_definition=self.domain_of_definition)
            return poly.get(self)
        elif isinstance(other, Const):
            poly = Polynomial({-1: other.number}, domain_of_definition=self.domain_of_definition & other.domain_of_definition)
            return poly.get(self)
        else:
            poly = Polynomial({-1: 1}, domain_of_definition=self.domain_of_definition)
            return poly.get(self).mul(other)

    def derivative(self, delta_t=1e-8, eps=1e-10, *args, inplace=False, **kwargs):
        functions = []
        for item in self.functions:
            if isinstance(item, Function):
                functions.append(item.derivative(delta_t, eps, inplace=False))
            elif callable(item):
                functions.append(lambda x: (item(x + delta_t) - item(x)) / delta_t)
            elif isinstance(item, (np.ndarray, Number)):
                pass
            else:
                raise ParameterTypeError("错误的数据类型")
        if inplace:
            self.functions = functions
            return self
        else:
            return Function(functions, domain_of_definition=self.domain_of_definition)

    def indefinite_integral(self, *args, inplace=False, **kwargs):
        if inplace:
            raise NotImplemented
        return CumulativeAreaFunction(self, domain_of_definition=self.domain_of_definition)

    def integral(self, lower_limit=0, upper_limit=1, delta_t=1e-8, eps=1e-10, *args, method=IntegralMethod.Rectangle, **kwargs):
        """
        积分
        :param delta_t:
        :param eps:
        :param args:
        :param inplace:
        :param kwargs:
        :return:
        """
        try:
            func = self.indefinite_integral(inplace=False)
            if isinstance(func, CumulativeAreaFunction):
                if np.isinf(upper_limit) or np.isinf(lower_limit):
                    raise NotImplemented
                if method == IntegralMethod.Rectangle:
                    if upper_limit > lower_limit:
                        flag = 1
                    else:
                        flag = -1
                        lower_limit, upper_limit = upper_limit, lower_limit
                    xi = np.arange(lower_limit, upper_limit, delta_t)
                    return flag * np.sum(self.get(xi) * delta_t)
                elif method == IntegralMethod.Trapezoid:
                    if upper_limit > lower_limit:
                        flag = 1
                    else:
                        flag = -1
                        lower_limit, upper_limit = upper_limit, lower_limit
                    xi = np.arange(lower_limit, upper_limit + delta_t, delta_t)
                    yi = self.get(xi)
                    return flag * np.sum((yi[:-1] + yi[1:]) * delta_t / 2)
                else:
                    raise NotImplemented
            else:
                return func(upper_limit) - func(lower_limit)
        except NotImplemented:
            if np.isinf(upper_limit) or np.isinf(lower_limit):
                raise NotImplemented
            if method == IntegralMethod.Rectangle:
                if upper_limit > lower_limit:
                    flag = 1
                else:
                    flag = -1
                    lower_limit, upper_limit = upper_limit, lower_limit
                xi = np.arange(lower_limit, upper_limit, delta_t)
                return flag * np.sum(self.get(xi) * delta_t)
            elif method == IntegralMethod.Trapezoid:
                if upper_limit > lower_limit:
                    flag = 1
                else:
                    flag = -1
                    lower_limit, upper_limit = upper_limit, lower_limit
                xi = np.arange(lower_limit, upper_limit + delta_t, delta_t)
                yi = self.get(xi)
                return flag * np.sum((yi[:-1] + yi[1:]) * delta_t / 2)
            else:
                raise NotImplemented

    def to_string(self, symbol='x', *args, **kwargs) -> str:
        return self.expression

    def __str__(self):
        return self.to_string('x')

    def __repr__(self):
        return str(self)


class Const(Function):
    def __init__(self, number: Number = 0, *, expression='', name='', domain_of_definition=R):
        if callable(number):
            number = number(0)
        if expression is None or expression == '':
            expression = str(number)
        super().__init__([number], expression=expression, name=name, domain_of_definition=domain_of_definition)
        self.number = number

    def add(self, other, *args, inplace=False, eps=1e-10, **kwargs):
        if inplace:
            if isinstance(other, Const):
                self.number += other.number
                self.domain_of_definition.intersection(other.domain_of_definition, inplace=inplace)
            elif isinstance(other, (Number, np.ndarray)):
                self.number += other
            else:
                raise ParameterTypeError("错误的数据类型")
            return self
        else:
            if np.isclose(self.number, 0):
                if isinstance(other, Function):
                    new_result = other.copy()
                    new_result.domain_of_definition = new_result.domain_of_definition.intersection(self.domain_of_definition)
                    return new_result
                elif callable(other):
                    return Function(other, domain_of_definition=self.domain_of_definition)

            if isinstance(other, Polynomial):
                poly = other.polynomial_dict.copy()
                for k, v in other.polynomial_dict.items():
                    if k in poly:
                        poly[k] += v
                    else:
                        poly[k] = v
                return Polynomial(poly, domain_of_definition=self.domain_of_definition.intersection(other.domain_of_definition))
            elif isinstance(other, Const):
                return Const(other.number + self.number, domain_of_definition=self.domain_of_definition.intersection(other.domain_of_definition))
            elif isinstance(other, (np.ndarray, Number)):
                return Const(other + self.number, domain_of_definition=self.domain_of_definition)
            elif isinstance(other, Function) or callable(other):
                return super().add(other)
            else:
                raise ParameterTypeError("错误的数据类型")

    def sub(self, other, *, inplace=False):
        if inplace:
            if isinstance(other, Const):
                self.number -= other.number
                self.domain_of_definition.intersection(other.domain_of_definition, inplace=True)
            elif isinstance(other, (np.ndarray, Number)):
                self.number -= other
            else:
                raise ParameterTypeError("错误的数据类型")
            return self
        else:
            if equals_zero(self.number):
                if isinstance(other, Function):
                    new_result = -other
                    new_result.domain_of_definition = new_result.domain_of_definition.intersection(self.domain_of_definition)
                    return new_result
                elif callable(other):
                    return -Function(other, domain_of_definition=self.domain_of_definition)

            if isinstance(other, Polynomial):
                poly = other.polynomial_dict.copy()
                for k, v in other.polynomial_dict.items():
                    poly[k] = -v
                poly[0] += self.number
                return Polynomial(poly, domain_of_definition=self.domain_of_definition.intersection(other.domain_of_definition))
            elif isinstance(other, Const):
                return Const(self.number - other.number, domain_of_definition=self.domain_of_definition.intersection(other.domain_of_definition))
            elif isinstance(other, (np.ndarray, Number)):
                return Const(self.number - other, domain_of_definition=self.domain_of_definition)
            else:
                return super().sub(other, inplace=False)

    def mul(self, other, *args, inplace=False, unfolding='false', max_term=10, eps=1e-10, **kwargs):
        if inplace:
            if isinstance(other, Const):
                self.number *= other.number
                self.domain_of_definition.intersection(other.domain_of_definition, inplace=inplace)
            elif isinstance(other, (Number, np.ndarray)):
                self.number *= other
            else:
                raise ParameterTypeError("错误的数据类型")
            return self
        else:
            if np.isclose(self.number, 0):
                if isinstance(other, Function):
                    return Const(0, domain_of_definition=self.domain_of_definition.intersection(other.domain_of_definition))
                elif callable(other):
                    return Const(0, domain_of_definition=self.domain_of_definition)
            elif np.isclose(self.number, 1):
                if isinstance(other, Function):
                    new_result = other.copy()
                    new_result.domain_of_definition = new_result.domain_of_definition.intersection(self.domain_of_definition)
                    return new_result
                elif callable(other):
                    return Function(other, domain_of_definition=self.domain_of_definition)
            if isinstance(other, Polynomial):
                poly = other.polynomial_dict.copy()
                for k, v in other.polynomial_dict.items():
                    poly[k] *= v
                return Polynomial(poly, domain_of_definition=self.domain_of_definition.intersection(other.domain_of_definition))
            elif isinstance(other, Const):
                return Const(self.number - other.number, domain_of_definition=self.domain_of_definition.intersection(other.domain_of_definition))
            elif isinstance(other, (np.ndarray, Number)):
                return Const(self.number - other, domain_of_definition=self.domain_of_definition)
            else:
                return super().mul(other, inplace=inplace, unfolding=unfolding, max_term=max_term)

    def derivative(self, delta_t=1e-8, eps=1e-10, *args, inplace=False, **kwargs):
        return Const(0, domain_of_definition=self.domain_of_definition)

    def indefinite_integral(self, *args, inplace=False, **kwargs):
        if inplace:
            poly = Polynomial({1: self.number})
            self.functions = poly.functions
            self.expression = f"{self.number}x"
        else:
            return Polynomial({1: self.number}, expression=f"{self.number}x", domain_of_definition=self.domain_of_definition)

    def to_string(self, symbol='x', *args, **kwargs):
        return "{}".format(self.number)

    def __str__(self):
        return self.to_string('x')


class Polynomial(Function):
    """
    多项式
    """

    def __init__(self, polynomial=None, coefficient=None, exponent=None, *, expression='', name='', domain_of_definition=R):
        """
        coefficient: 系数
        exponent: 指数
        """
        self.polynomial_dict = collections.defaultdict(float)
        if polynomial is not None:
            if isinstance(polynomial, Polynomial):
                self.polynomial_dict = polynomial.polynomial_dict.copy()
            elif isinstance(polynomial, dict):
                self.polynomial_dict.update(polynomial)
            else:
                raise ParameterTypeError("参数类型错误")
        elif coefficient is not None:
            if exponent is not None:
                self.polynomial_dict.update(dict(zip(exponent, coefficient)))
            else:
                self.polynomial_dict.update(zip(range(len(coefficient)), coefficient))
        super().__init__([self], expression=self.to_string('x'), domain_of_definition=domain_of_definition)

    @property
    def coefficient(self):
        return list(self.polynomial_dict.values())

    @property
    def exponent(self):
        return list(self.polynomial_dict.keys())

    def add(self, other, *args, inplace=False, eps=1e-10, **kwargs):
        if inplace:
            if isinstance(other, Polynomial):
                for k, v in other.polynomial_dict.items():
                    self.polynomial_dict[k] += v
            elif isinstance(other, Const):
                self.polynomial_dict[0] += other.functions[0]

            elif isinstance(other, (np.ndarray, Number)):
                self.polynomial_dict[0] += other
            elif isinstance(other, Function) or callable(other):
                raise ParameterTypeError("错误的数据类型")
            else:
                raise ParameterTypeError("错误的数据类型")
        else:
            poly = self.polynomial_dict.copy()
            if isinstance(other, Polynomial):
                for k, v in other.polynomial_dict.items():
                    if k in poly:
                        poly[k] += v
                    else:
                        poly[k] = v
            elif isinstance(other, Const):
                if 0 in poly:
                    poly[0] += other.functions[0]
                else:
                    poly[0] = other.functions[0]
            elif isinstance(other, (np.ndarray, Number)):
                if 0 in poly:
                    poly[0] += other
                else:
                    poly[0] = other
            elif isinstance(other, Function) or callable(other):
                return super().add(other)
            else:
                raise ParameterTypeError("错误的数据类型")
            return Polynomial(poly)

    def sub(self, other, *, inplace=False):
        if inplace:
            if isinstance(other, Polynomial):
                for k, v in other.polynomial_dict.items():
                    if k in self.polynomial_dict:
                        self.polynomial_dict[k] -= v
                    else:
                        self.polynomial_dict[k] = -v
            elif isinstance(other, Const):
                if 0 in self.polynomial_dict:
                    self.polynomial_dict[0] -= other.functions[0]
                else:
                    self.polynomial_dict[0] = -other.functions[0]
            elif isinstance(other, (np.ndarray, Number)):
                if 0 in self.polynomial_dict:
                    self.polynomial_dict[0] -= other
                else:
                    self.polynomial_dict[0] = -other
            else:
                raise ParameterTypeError("错误的数据类型")
        else:
            poly = self.polynomial_dict.copy()
            if isinstance(other, Polynomial):
                for k, v in other.polynomial_dict.items():
                    poly[k] -= v
            elif isinstance(other, Const):
                if 0 in self.polynomial_dict:
                    poly[0] -= other.functions[0]
            elif isinstance(other, (np.ndarray, Number)):
                poly[0] -= other
            else:
                return super().sub(other, inplace=False)
            return Polynomial(poly, expression=self.to_string("x"), domain_of_definition=self.domain_of_definition)

    def mul(self, other, *args, inplace=False, unfolding='false', max_term=10, eps=1e-10, **kwargs):

        if isinstance(other, Number):
            polynomial_dict = collections.defaultdict(float)
            polynomial_dict.update({k: other * v for k, v in self.polynomial_dict.items()})
            if inplace:
                self.polynomial_dict = polynomial_dict
                return self
            else:
                return Polynomial(polynomial_dict, domain_of_definition=self.domain_of_definition)
        elif isinstance(other, Polynomial):
            new_poly = {}
            for (k1, v1), (k2, v2) in itertools.product(self.polynomial_dict.items(), other.polynomial_dict.items()):
                k = k1 + k2
                new_poly[k] = new_poly.get(k, 0) + v1 * v2
            if inplace:
                self.polynomial_dict = new_poly
                self.simplify(eps)
                return self
            else:
                res = Polynomial(new_poly, domain_of_definition=self.domain_of_definition)
                self.simplify(eps)
                return res
        else:
            return super().mul(other, inplace=inplace, unfolding=unfolding, max_term=max_term)

    def diff(self, eps=1e-8):
        """
        导函数
        """
        return Polynomial({k - 1: k * v for k, v in self.polynomial_dict.items() if not (-eps < k < eps)},
                          expression=self.to_string("x"),
                          domain_of_definition=self.domain_of_definition)

    def derivative(self, delta_t=1e-8, eps=1e-10, *args, inplace=False, **kwargs):
        return self.diff(eps)

    def neg(self, *, inplace=False):
        if inplace:
            dic = {k: -v for k, v in self.polynomial_dict.items()}
            self.polynomial_dict = collections.defaultdict(float)
            self.polynomial_dict.update(dic)
            self.expression = self.to_string("x")
        else:
            dic = {k: -v for k, v in self.polynomial_dict.items()}
            return Polynomial(dic, domain_of_definition=self.domain_of_definition)

    def get(self, x, *args, eps=1e-10, **kwargs):
        """
        获得x对应的值
        """
        if isinstance(x, Polynomial):
            x = x.simplify(eps, inplace=False)
        if isinstance(x, Const):
            polynomial_dict = {k: v * x.number for k, v in self.polynomial_dict.items()}
            result = Polynomial(polynomial_dict, domain_of_definition=self.domain_of_definition.intersection(x.domain_of_definition))
            return result
        elif isinstance(x, Polynomial):
            if len(x.polynomial_dict) == 1:
                key, value = next(x.polynomial_dict.items())
                polynomial_dict = {k + key: v * value for k, v in self.polynomial_dict.items()}
                result = Polynomial(polynomial_dict, domain_of_definition=self.domain_of_definition.intersection(x.domain_of_definition))
                return result
        elif isinstance(x, Number):
            y = 0.0
            if x in self.domain_of_definition:
                for k, v in self.polynomial_dict.items():
                    y += (v * x ** k)
                return y
            else:
                return np.nan
        elif isinstance(x, np.ndarray):
            xind = self.domain_of_definition.contains(x)
            # print("xind:", xind)
            new_x = x.copy()
            new_x[~xind] = np.nan
            y = np.zeros_like(x, dtype=float)
            for k, v in self.polynomial_dict.items():
                y += (v * new_x ** k)
            return y

        return super().get(x)

    def indefinite_integral(self, *args, inplace=False, **kwargs):
        if inplace:
            if -1 in self.polynomial_dict:
                raise NotImplemented
            self.polynomial_dict = {k + 1: v / (k + 1) for k, v in self.polynomial_dict.items()}
            self.expression = self.to_string()
            return self
        else:
            poly = self.polynomial_dict.copy()
            log_func = None
            if -1 in poly:
                log_func = self.polynomial_dict.pop(-1) * Ln()
            poly = {k + 1: v / (k + 1) for k, v in poly.items()}
            integral = Polynomial(poly, domain_of_definition=self.domain_of_definition)
            if log_func is None:
                return integral
            else:
                return integral + log_func

    def simplify(self, eps=1e-8, inplace=True):
        """
        化简多项式，删去系数为0的项
        :param eps: 判断0的精度
        :return:
        """
        if inplace:
            polynomial_dict = collections.defaultdict(float)
            polynomial_dict.update({k: v for k, v in self.polynomial_dict.items() if not (-eps < v < eps)})
            self.polynomial_dict = polynomial_dict
            return self
        else:
            polynomial_dict = collections.defaultdict(float)
            polynomial_dict.update({k: v for k, v in self.polynomial_dict.items() if not (-eps < v < eps)})
            if len(polynomial_dict) == 0:
                return Const(0, domain_of_definition=self.domain_of_definition)
            elif len(polynomial_dict) == 1 and (0 in polynomial_dict):
                return Const(polynomial_dict[0], domain_of_definition=self.domain_of_definition)
            return deepcopy(self)

    def __isub__(self, other):
        return self.sub(other, inplace=True)

    def __radd__(self, other):
        return self.add(other, inplace=False)

    def __rsub__(self, other):
        return self.neg(inplace=False) + other

    def __sub__(self, other):
        return self.sub(other, inplace=False)

    def __neg__(self):
        return self.neg(inplace=False)

    def to_string(self, symbol='x', *args, **kwargs):
        res = [(k, v) for k, v in self.polynomial_dict.items()]
        res.sort()
        s = []
        for p, c in self.polynomial_dict.items():
            if np.isclose(c, 1):
                c_str = '1' if p == 0 else ''
            elif np.isclose(c, -1):
                c_str = '-'
            elif np.isclose(c, 0):
                continue
            else:
                c_str = "{c}".format(c=c)

            if np.isclose(p, 0):
                p_str = ''
            elif np.isclose(p, 1):
                p_str = '{symbol}'.format(symbol=symbol)
            elif p > 0:
                p_str = '{symbol}^{p}'.format(symbol=symbol, p=p)
            else:
                p_str = '{symbol}^({p})'.format(symbol=symbol, p=p)
            s.append(c_str + p_str)

        s_str = '+'.join(s)
        return s_str.replace("+-", "-")

    def __str__(self):
        return self.to_string('x')


class TrigonometricFunction(Function):
    pass


class Sin(TrigonometricFunction):
    def __init__(self, *, domain_of_definition=R):
        super().__init__([np.sin], expression=self.to_string('x'), domain_of_definition=domain_of_definition)

    def derivative(self, delta_t=1e-8, eps=1e-10, *args, inplace=False, **kwargs):
        return Cos(domain_of_definition=self.domain_of_definition)

    def to_string(self, symbol='x', *args, **kwargs):
        return "sin({symbol})".format(symbol=symbol)

    def mul(self, other, *args, inplace=False, unfolding='false', max_term=10, **kwargs):
        if isinstance(other, TrigonometricFunction):
            if isinstance(other, Sec):
                return Tan(domain_of_definition=self.domain_of_definition.intersection(other.domain_of_definition))
            elif isinstance(other, Cot):
                return Cos(domain_of_definition=self.domain_of_definition.intersection(other.domain_of_definition))
            elif isinstance(other, Csc):
                return Const(1, domain_of_definition=self.domain_of_definition.intersection(other.domain_of_definition))
        return super().mul(other, *args, inplace=inplace, unfolding=unfolding, max_term=max_term, **kwargs)

    def rdiv(self, other, *args, inplace=False, **kwargs):
        if inplace:
            return super().rdiv(other, inplace=inplace)
        if isinstance(other, Number):
            if np.isclose(other, 0):
                return Const(0, domain_of_definition=self.domain_of_definition)
            if np.isclose(other, 1):
                return Csc(domain_of_definition=self.domain_of_definition)
            return other * Csc(domain_of_definition=self.domain_of_definition)
        elif isinstance(other, np.ndarray):
            return other * Csc(domain_of_definition=self.domain_of_definition)
        return super().rdiv(other, inplace=inplace)

    def __str__(self):
        return self.to_string('x')


class Cos(TrigonometricFunction):
    def __init__(self, *, domain_of_definition=R):
        super().__init__([np.cos], expression=self.to_string('x'), domain_of_definition=domain_of_definition)

    def derivative(self, delta_t=1e-8, eps=1e-10, *args, inplace=False, **kwargs):
        return -Sin(domain_of_definition=self.domain_of_definition)

    def to_string(self, symbol='x', *args, **kwargs):
        return "cos({symbol})".format(symbol=symbol)

    def mul(self, other, *args, inplace=False, unfolding='false', max_term=10, **kwargs):
        if isinstance(other, TrigonometricFunction):
            if isinstance(other, Csc):
                return Cot(domain_of_definition=self.domain_of_definition.intersection(other.domain_of_definition))
            elif isinstance(other, Tan):
                return Sin(domain_of_definition=self.domain_of_definition.intersection(other.domain_of_definition))

        return super().mul(other, *args, inplace=inplace, unfolding=unfolding, max_term=max_term, **kwargs)

    def rdiv(self, other, *args, inplace=False, **kwargs):
        if inplace:
            return super().rdiv(other, inplace=inplace)
        if isinstance(other, Number):
            if np.isclose(other, 0):
                return Const(0, domain_of_definition=self.domain_of_definition)
            if np.isclose(other, 1):
                return Sec(domain_of_definition=self.domain_of_definition)
            return other * Sec(domain_of_definition=self.domain_of_definition)
        elif isinstance(other, np.ndarray):
            return other * Sec(domain_of_definition=self.domain_of_definition)
        return super().rdiv(other, inplace=inplace)

    def indefinite_integral(self, *args, inplace=False, **kwargs):
        if inplace:
            raise NotImplemented
        else:
            return Sin(domain_of_definition=self.domain_of_definition)

    def __str__(self):
        return self.to_string('x')


class Tan(TrigonometricFunction):
    def __init__(self, *, domain_of_definition=R):
        super().__init__([np.tan], expression=self.to_string('x'), domain_of_definition=domain_of_definition)

    def mul(self, other, *args, inplace=False, unfolding='false', max_term=10, **kwargs):
        if isinstance(other, TrigonometricFunction):
            if isinstance(other, Cos):
                return Sin(domain_of_definition=self.domain_of_definition.intersection(other.domain_of_definition))
            elif isinstance(other, Csc):
                return Sec(domain_of_definition=self.domain_of_definition.intersection(other.domain_of_definition))
            elif isinstance(other, Cot):
                return Const(1, domain_of_definition=self.domain_of_definition.intersection(other.domain_of_definition))

        return super().mul(other, *args, inplace=inplace, unfolding=unfolding, max_term=max_term, **kwargs)

    def rdiv(self, other, *args, inplace=False, **kwargs):
        if inplace:
            return super().rdiv(other, inplace=inplace)
        if isinstance(other, Number):
            if np.isclose(other, 0):
                return Const(0, domain_of_definition=self.domain_of_definition)
            if np.isclose(other, 1):
                return Cot(domain_of_definition=self.domain_of_definition)
            return other * Cot(domain_of_definition=self.domain_of_definition)
        elif isinstance(other, np.ndarray):
            return other * Cot(domain_of_definition=self.domain_of_definition)
        return super().rdiv(other, inplace=inplace)

    def derivative(self, delta_t=1e-8, eps=1e-10, *args, inplace=False, **kwargs):
        return Sec(domain_of_definition=self.domain_of_definition) * Sec(domain_of_definition=self.domain_of_definition)

    def indefinite_integral(self, *args, inplace=False, **kwargs):
        if inplace:
            raise NotImplemented
        return -Ln(domain_of_definition=self.domain_of_definition).get(Abs().get(Cos()))

    def to_string(self, symbol='x', *args, **kwargs):
        return "tan({symbol})".format(symbol=symbol)

    def __str__(self):
        return self.to_string('x')


class Sec(TrigonometricFunction):
    def __init__(self, *, domain_of_definition=R):
        super().__init__([self], expression=self.to_string('x'), domain_of_definition=domain_of_definition)

    def mul(self, other, *args, inplace=False, unfolding='false', max_term=10, **kwargs):
        if isinstance(other, TrigonometricFunction):
            if isinstance(other, Cos):
                return Const(1, domain_of_definition=self.domain_of_definition.intersection(other.domain_of_definition))
            elif isinstance(other, Sin):
                return Tan(domain_of_definition=self.domain_of_definition.intersection(other.domain_of_definition))
            elif isinstance(other, Cot):
                return Csc(domain_of_definition=self.domain_of_definition.intersection(other.domain_of_definition))
        return super().mul(other, *args, inplace=inplace, unfolding=unfolding, max_term=max_term, **kwargs)

    def rdiv(self, other, *args, inplace=False, **kwargs):
        if inplace:
            return super().rdiv(other, inplace=inplace)
        if isinstance(other, Number):
            if np.isclose(other, 0):
                return Const(0, domain_of_definition=self.domain_of_definition)
            if np.isclose(other, 1):
                return Cos(domain_of_definition=self.domain_of_definition)
            return other * Cos(domain_of_definition=self.domain_of_definition)
        elif isinstance(other, np.ndarray):
            return other * Cos(domain_of_definition=self.domain_of_definition)
        return super().rdiv(other, inplace=inplace)

    def get(self, x, *args, **kwargs):
        if isinstance(x, Number):
            if x in self.domain_of_definition:
                return 1 / np.cos(x)
            else:
                return np.nan
        elif isinstance(x, np.ndarray):
            xind_self = self.domain_of_definition.contains(x)
            new_x_self = x.copy()
            new_x_self[~xind_self] = np.nan
            res = 1 / np.cos(new_x_self)
            res[~xind_self] = np.nan
            return res
        return super().get(x, *args, **kwargs)

    def derivative(self, delta_t=1e-8, eps=1e-10, *args, inplace=False, **kwargs):
        return Sec(domain_of_definition=self.domain_of_definition) * Tan(domain_of_definition=self.domain_of_definition)

    def indefinite_integral(self, *args, inplace=False, **kwargs):
        if inplace:
            raise NotImplemented
        return Ln(domain_of_definition=self.domain_of_definition).get(Sec() + Tan())

    def to_string(self, symbol='x', *args, **kwargs):
        return "sec({symbol})".format(symbol=symbol)

    def __str__(self):
        return self.to_string('x')


class Csc(TrigonometricFunction):
    def __init__(self, *, domain_of_definition=R):
        super().__init__([], expression=self.to_string('x'), domain_of_definition=domain_of_definition)
        self.functions = [Polynomial({-1: 1}, domain_of_definition=domain_of_definition).get(Sin())]

    def mul(self, other, *args, inplace=False, unfolding='false', max_term=10, **kwargs):
        if isinstance(other, TrigonometricFunction):
            if isinstance(other, Cos):
                return Cot(domain_of_definition=self.domain_of_definition.intersection(other.domain_of_definition))
            elif isinstance(other, Sin):
                return Const(1, domain_of_definition=self.domain_of_definition.intersection(other.domain_of_definition))
            elif isinstance(other, Tan):
                return Sec(domain_of_definition=self.domain_of_definition.intersection(other.domain_of_definition))
        return super().mul(other, *args, inplace=inplace, unfolding=unfolding, max_term=max_term, **kwargs)

    def rdiv(self, other, *args, inplace=False, **kwargs):
        if inplace:
            return super().rdiv(other, inplace=inplace)
        if isinstance(other, Number):
            if np.isclose(other, 0):
                return Const(0, domain_of_definition=self.domain_of_definition)
            if np.isclose(other, 1):
                return Sin(domain_of_definition=self.domain_of_definition)
            return other * Sin(domain_of_definition=self.domain_of_definition)
        elif isinstance(other, np.ndarray):
            return other * Sin(domain_of_definition=self.domain_of_definition)
        return super().rdiv(other, inplace=inplace)

    def derivative(self, delta_t=1e-8, eps=1e-10, *args, inplace=False, **kwargs):
        return -Cot(domain_of_definition=self.domain_of_definition) * Csc(domain_of_definition=self.domain_of_definition)

    def to_string(self, symbol='x', *args, **kwargs):
        return "csc({symbol})".format(symbol=symbol)

    def indefinite_integral(self, *args, inplace=False, **kwargs):
        if inplace:
            raise NotImplemented
        return Ln(domain_of_definition=self.domain_of_definition).get(Abs().get(Csc() - Cot()))

    def get(self, x, *args, **kwargs):
        if isinstance(x, Number):
            if x in self.domain_of_definition:
                return 1 / np.sin(x)
            else:
                return np.nan
        elif isinstance(x, np.ndarray):
            xind_self = self.domain_of_definition.contains(x)
            new_x_self = x.copy()
            new_x_self[~xind_self] = np.nan
            res = 1 / np.sin(new_x_self)
            res[~xind_self] = np.nan
            return res
        return super().get(x, *args, **kwargs)

    def __str__(self):
        return self.to_string('x')


class Cot(TrigonometricFunction):
    def __init__(self, *, domain_of_definition=R):
        super().__init__([self], expression=self.to_string('x'), domain_of_definition=domain_of_definition)

    def mul(self, other, *args, inplace=False, unfolding='false', max_term=10, **kwargs):
        if isinstance(other, TrigonometricFunction):
            if isinstance(other, Sin):
                return Cos(domain_of_definition=self.domain_of_definition.intersection(other.domain_of_definition))
            elif isinstance(other, Tan):
                return Const(1, domain_of_definition=self.domain_of_definition.intersection(other.domain_of_definition))
            elif isinstance(other, Sec):
                return Csc(domain_of_definition=self.domain_of_definition.intersection(other.domain_of_definition))
        return super().mul(other, *args, inplace=inplace, unfolding=unfolding, max_term=max_term, **kwargs)

    def rdiv(self, other, *args, inplace=False, **kwargs):
        if inplace:
            return super().rdiv(other, inplace=inplace)
        if isinstance(other, Number):
            if np.isclose(other, 0):
                return Const(0, domain_of_definition=self.domain_of_definition)
            if np.isclose(other, 1):
                return Tan(domain_of_definition=self.domain_of_definition)
            return other * Tan(domain_of_definition=self.domain_of_definition)
        elif isinstance(other, np.ndarray):
            return other * Tan(domain_of_definition=self.domain_of_definition)
        return super().rdiv(other, inplace=inplace)

    def derivative(self, delta_t=1e-8, eps=1e-10, *args, inplace=False, **kwargs):
        return -Csc(domain_of_definition=self.domain_of_definition) * Csc(domain_of_definition=self.domain_of_definition)

    def indefinite_integral(self, *args, inplace=False, **kwargs):
        if inplace:
            raise NotImplemented
        return Ln(domain_of_definition=self.domain_of_definition).get(Abs().get(Sin()))

    def to_string(self, symbol='x', *args, **kwargs):
        return "cot({symbol})".format(symbol=symbol)

    def get(self, x, *args, **kwargs):
        if isinstance(x, Number):
            if x in self.domain_of_definition:
                return 1 / np.tan(x)
            else:
                return np.nan
        elif isinstance(x, np.ndarray):
            xind_self = self.domain_of_definition.contains(x)
            new_x_self = x.copy()
            new_x_self[~xind_self] = np.nan
            res = 1 / np.tan(new_x_self)
            res[~xind_self] = np.nan
            return res
        return super().get(x, *args, **kwargs)

    def __str__(self):
        return self.to_string('x')


class Arcsin(Function):
    def __init__(self, *, domain_of_definition=ListIntervals(ContinuousBaseIntervals([-1, 1], open_or_closed=(IntervalType.Closed, IntervalType.Closed)))):
        super().__init__([np.arcsin], expression=self.to_string('x'), domain_of_definition=domain_of_definition)

    def derivative(self, delta_t=1e-8, eps=1e-10, *args, inplace=False, **kwargs):
        one_plus_neqx2 = Polynomial({2: -1, 0: 1}, domain_of_definition=self.domain_of_definition)
        neqsqrt = Polynomial({-0.5: 1}, domain_of_definition=self.domain_of_definition)
        res = neqsqrt.get(one_plus_neqx2)
        return res

    def indefinite_integral(self, *args, inplace=False, **kwargs):
        if inplace:
            raise NotImplemented
        x = Polynomial({1: 1})
        mysqrt = Polynomial({0.5: 1})
        _1_p_x2 = Polynomial({2: -1, 0: 1})
        x_sqrt_1_x2 = mysqrt.get(_1_p_x2)
        f = x_sqrt_1_x2 + x * Arcsin()
        return f

    def to_string(self, symbol='x', *args, **kwargs):
        return "arcsin({symbol})".format(symbol=symbol)

    def __str__(self):
        return self.to_string('x')


class Arccos(Function):
    def __init__(self, *, domain_of_definition=ListIntervals(ContinuousBaseIntervals([-1, 1], open_or_closed=(IntervalType.Closed, IntervalType.Closed)))):
        super().__init__([np.arccos], expression=self.to_string('x'), domain_of_definition=domain_of_definition)

    def derivative(self, delta_t=1e-8, eps=1e-10, *args, inplace=False, **kwargs):
        from astar_math.functions import Polynomial
        one_plus_neqx2 = Polynomial({2: -1, 0: 1}, domain_of_definition=self.domain_of_definition)
        neqsqrt = Polynomial({-0.5: -1}, domain_of_definition=self.domain_of_definition)
        res = neqsqrt.get(one_plus_neqx2)
        return res

    def to_string(self, symbol='x', *args, **kwargs):
        return "arccos({symbol})".format(symbol=symbol)

    def __str__(self):
        return self.to_string('x')


class Arctan(Function):
    def __init__(self, *, domain_of_definition=R):
        super().__init__([np.arctan], expression=self.to_string('x'), domain_of_definition=domain_of_definition)

    def derivative(self, delta_t=1e-8, eps=1e-10, *args, inplace=False, **kwargs):
        return Polynomial({-1: 1}, domain_of_definition=self.domain_of_definition).get(Polynomial({2: 1, 0: 1}))

    def to_string(self, symbol='x', *args, **kwargs):
        return "arctan({symbol})".format(symbol=symbol)

    def __str__(self):
        return self.to_string('x')


class Power(Function):
    def __init__(self, a, *, expression=None, name=None, domain_of_definition=R):
        self.a = a
        if isinstance(a, (Number, np.ndarray)):
            if expression is None:
                expression = self.to_string('x')
            super().__init__([lambda x: np.power(a, x)], expression=expression, domain_of_definition=domain_of_definition)
        elif isinstance(a, Function):
            if expression is None:
                expression = self.to_string('x')
            func = lambda x: np.power(a.get(x), x)
            super().__init__([func], expression=expression, domain_of_definition=domain_of_definition)
        elif callable(a):
            if expression is None:
                expression = ''
            func = lambda x: np.power(a(x), x)
            super().__init__([func], expression=expression, domain_of_definition=domain_of_definition)
        else:
            raise ParameterTypeError("参数 a 需为ndarray或者数字类型")

    def derivative(self, delta_t=1e-8, eps=1e-10, *args, inplace=False, **kwargs):
        if isinstance(self.a, (Number, np.ndarray)):
            return np.log(self.a) * Power(self.a, domain_of_definition=self.domain_of_definition)
        elif isinstance(self.a, Function):
            f1 = self * self.a.derivative()
            f2 = Ln(domain_of_definition=self.domain_of_definition).get(self.a) * Power(self.a, domain_of_definition=self.domain_of_definition)
            f3 = f1 + f2
            return f3
        else:
            raise MethodNotFoundError()

    def pow(self, power, modulo=None, *, inplace=False):
        if modulo is None:
            expression = "({})^({})".format(self.expression, power)
        else:
            expression = "(({})^({}))%({})".format(self.expression, power, modulo)
        if inplace:
            if isinstance(power, (Number, np.ndarray)):
                obj = deepcopy(self)
                self.functions = [lambda x: pow(obj.get(x), power, modulo)]
                self.expression = expression
                return self
            else:
                power_result = Power(self, domain_of_definition=self.domain_of_definition)
                if modulo is None:
                    res = power_result.get(power)
                else:
                    mod_result = Mod(modulo, domain_of_definition=self.domain_of_definition)
                    res = mod_result.get(power_result)

                self.functions = res.functions
                self.expression = res.expression
                return self
        else:
            if isinstance(power, (Number, np.ndarray)):
                return Function([lambda x: pow(self.get(x), power, modulo)], expression=expression)
            else:
                power_result = Power(self, domain_of_definition=self.domain_of_definition)
                if modulo is None:
                    return power_result.get(power)
                else:
                    mod_result = Mod(modulo, domain_of_definition=self.domain_of_definition)
                    return mod_result.get(power_result)

    def rpow(self, other, *, inplace=False):
        expression = "({})^({})".format(other, self.expression)

        if inplace:
            obj = deepcopy(self)
            self.functions = Power(other, domain_of_definition=self.domain_of_definition).get(obj).functions
            self.expression = expression
            return self
        else:
            p = Power(other, domain_of_definition=self.domain_of_definition).get(self)
            p.expression = expression
            return p

    def to_string(self, symbol='x', *args, **kwargs):
        if isinstance(self.a, Function):
            return "({a})^({symbol})".format(a=self.a, symbol=symbol)
        elif isinstance(self.a, (Number, np.ndarray)):
            return "{a}^({symbol})".format(a=self.a, symbol=symbol)
        else:
            return ''

    def __str__(self):
        return self.to_string('x')


class Exp(Power):
    def __init__(self, *, domain_of_definition=R):
        super(Exp, self).__init__(np.e, domain_of_definition=domain_of_definition)

    def derivative(self, delta_t=1e-8, eps=1e-10, *args, inplace=False, **kwargs):
        return Exp(domain_of_definition=self.domain_of_definition)

    def to_string(self, symbol='x', *args, **kwargs):
        return "exp({symbol})".format(symbol=symbol)

    def indefinite_integral(self, *args, inplace=False, **kwargs):
        if inplace:
            return self
        return deepcopy(self)

    def __str__(self):
        return self.to_string('x')


class Log(Function):
    def __init__(self, a=np.e, *, domain_of_definition=ListIntervals(ContinuousBaseIntervals([0, np.inf], open_or_closed=(IntervalType.Open, IntervalType.Open)))):
        self.a = a
        function = Ln() / np.log(self.a)
        super().__init__(function, expression=self.to_string('x'), domain_of_definition=domain_of_definition)

    def derivative(self, delta_t=1e-8, eps=1e-10, *args, inplace=False, **kwargs):
        if isinstance(self.a, (Number, Function)):
            return Polynomial({-1: 1 / np.log(self.a)}, domain_of_definition=self.domain_of_definition)
        else:
            raise MethodNotFoundError()

    def to_string(self, symbol='x', *args, **kwargs):
        return "log{a}({symbol})".format(a=self.a, symbol=symbol)

    def __str__(self):
        return self.to_string('x')


class Ln(Function):
    def __init__(self, *, domain_of_definition=ListIntervals(ContinuousBaseIntervals([0, np.inf], open_or_closed=(IntervalType.Open, IntervalType.Open)))):
        super().__init__([], domain_of_definition=domain_of_definition)
        self.functions = [np.log]

    def derivative(self, delta_t=1e-8, eps=1e-10, *args, inplace=False, **kwargs):
        if inplace:
            raise NotImplemented
        return Polynomial({-1: 1})

    def to_string(self, symbol='x', *args, **kwargs):
        return "ln({symbol})".format(symbol=symbol)

    def __str__(self):
        return self.to_string('x')


class Abs(Function):
    def __init__(self, *, domain_of_definition=R):
        super().__init__([np.abs], expression=self.to_string('x'), domain_of_definition=domain_of_definition)

    def to_string(self, symbol='x', *args, **kwargs):
        return "|{symbol}|".format(symbol=symbol)

    def __str__(self):
        return self.to_string('x')

    def derivative(self, delta_t=1e-8, eps=1e-10, *args, inplace=False, **kwargs):
        left_set = ListIntervals(ContinuousBaseIntervals((-np.inf, 0), open_or_closed=(IntervalType.Open, IntervalType.Open)))
        right_set = ListIntervals(ContinuousBaseIntervals((0, np.inf), open_or_closed=(IntervalType.Open, IntervalType.Open)))
        return Function([Const(-1, domain_of_definition=left_set & self.domain_of_definition),
                         Const(1, domain_of_definition=right_set & self.domain_of_definition)],
                        domain_of_definition=self.domain_of_definition)


class Mod(Function):
    def __init__(self, mod, *, domain_of_definition=R):
        self.mod = mod
        super().__init__([lambda x: np.mod(x, self.mod)], expression=self.to_string('x'), domain_of_definition=domain_of_definition)

    def to_string(self, symbol='x', *args, **kwargs):
        return "mod({symbol}, {mod})".format(symbol=symbol, mod=self.mod)

    def __str__(self):
        return self.to_string('x')

    def derivative(self, delta_t=1e-8, eps=1e-10, *args, inplace=False, **kwargs):
        raise MethodNotFoundError()


class Neq(Polynomial):
    def __init__(self, *, domain_of_definition=R):
        super().__init__({1: -1}, domain_of_definition=domain_of_definition)

    def to_string(self, symbol='x', *args, **kwargs):
        return "-({symbol})".format(symbol=symbol)

    def __str__(self):
        return self.to_string('x')

    def derivative(self, delta_t=1e-8, eps=1e-10, *args, inplace=False, **kwargs):
        return Const(-1, domain_of_definition=self.domain_of_definition)


class Fourier(Function):
    def __init__(self, param=None, *, domain_of_definition=R):
        if param is None:
            self.param = np.array([1, 1, 1, 1])
        else:
            self.param = np.array(param)
        super().__init__([lambda x: fourier(x, param)], domain_of_definition=domain_of_definition)

    def to_string(self, symbol='x', *args, **kwargs):
        return "-({symbol})".format(symbol=symbol)

    def __str__(self):
        return self.to_string('x')

    def derivative(self, delta_t=1e-8, eps=1e-10, *args, inplace=False, **kwargs):
        res = [self.param[0]]
        param_reshape = self.param.reshape((-1, 2))
        iw = 0
        x = Polynomial({1: 1})
        for i, (a, b) in enumerate(param_reshape[1:]):
            iw += self.param[1]
            iwx = iw * x
            res.append(a * Cos().get(iwx))
            res.append(b * Sin().get(iwx))
        fourier_func = Function(res, expression=self.expression, name=self.name, domain_of_definition=self.domain_of_definition)
        return fourier_func.derivative()


class CumulativeAreaFunction(Function):
    def __init__(self, func, expression=None, name=None, *args, domain_of_definition=R, **kwargs):
        if isinstance(func, Function):
            self.func = func
        else:
            self.func = Function(func, domain_of_definition=self.domain_of_definition)
        super().__init__([self], expression=expression, name=name, domain_of_definition=domain_of_definition)

    def derivative(self, delta_t=1e-8, eps=1e-10, *args, inplace=False, **kwargs):
        if inplace:
            self.functions = self.func.functions
            self.expression = self.func.expression
            self.name = self.func.name
        else:
            return self.func

    def to_string(self, symbol='x', symbol2="t", *args, **kwargs) -> str:
        return "∫^{}({})d{}".format(symbol2, self.func.to_string(symbol2), symbol2)

    def get(self, x, *args, **kwargs):
        """
        获得x对应的值
        """
        if isinstance(x, Number):
            return self.func.integral(lower_limit=0, upper_limit=x)
        if isinstance(x, np.ndarray):
            xi = np.insert(x, 0, 0)
            return np.cumsum(self.integral(lower_limit=a, upper_limit=b) for a, b in zip(xi[:-1], xi[1:]))
        else:
            return super().get(x)


class MulFunction(Function):
    def __init__(self, f, g, expression=None, name=None, *args, domain_of_definition=R, **kwargs):
        if isinstance(f, Function):
            self.f = f
        elif callable(f):
            self.f = Function(f)
        else:
            self.f = Const(f)
        if isinstance(g, Function):
            self.g = g
        elif callable(g):
            self.g = Function(g)
        else:
            self.g = Const(g)
        if isinstance(self.g, Const):
            self.f, self.g = self.g, self.f
        if expression is None or expression == "":
            expression = self.to_string()
        super().__init__([self], expression=expression, name=name, domain_of_definition=domain_of_definition)

    def derivative(self, delta_t=1e-8, eps=1e-10, *args, inplace=False, **kwargs):
        f_derivative = self.f.derivative()
        g_derivative = self.g.derivative()
        return f_derivative * self.g + self.f * g_derivative

    def get(self, x, *args, **kwargs):
        return self.f.get(x) * self.g.get(x)

    def to_string(self, symbol='x', *args, **kwargs):
        return "({})*({})".format(self.f.to_string(symbol), self.g.to_string(symbol))

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.to_string("x")


class CompositeFunction(Function):
    def __init__(self, outer, inner, expression=None, name=None, *args, domain_of_definition=R, **kwargs):
        if isinstance(outer, Function):
            self.f = outer
        elif callable(outer):
            self.f = Function(outer)
        else:
            self.f = Const(outer)
        if isinstance(inner, Function):
            self.g = inner
        elif callable(inner):
            self.g = Function(inner)
        else:
            self.g = Const(inner)
        if expression is None:
            expression = self.to_string()
        this_domain_of_definition = domain_of_definition.intersection(self.g.domain_of_definition)
        super().__init__([self], expression=expression, name=name, domain_of_definition=this_domain_of_definition)

    def derivative(self, delta_t=1e-8, eps=1e-10, *args, inplace=False, **kwargs):
        f_derivative = self.f.derivative().get(self.g)
        g_derivative = self.g.derivative()
        return f_derivative * g_derivative

    def get(self, x, *args, **kwargs):
        if isinstance(x, Function):
            expression = self.to_string("(" + x.expression + ")")
            return CompositeFunction(self, x, expression=expression)
        elif isinstance(x, Number):
            if x in self.domain_of_definition:
                return self.f.get(self.g.get(x))
            else:
                return np.nan
        elif isinstance(x, np.ndarray):
            return self.f.get(self.g.get(x))
        elif callable(x):
            return CompositeFunction(self, x, expression="")
        else:
            raise ParameterTypeError("x type error")

    def to_string(self, symbol='x', *args, **kwargs):
        return self.f.to_string("(" + self.g.to_string(symbol) + ")")


self = Polynomial({1: 1})
