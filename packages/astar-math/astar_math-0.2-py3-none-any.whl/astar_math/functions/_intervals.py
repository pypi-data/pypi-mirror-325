import itertools
import numbers
from abc import ABCMeta, abstractmethod
from typing import Iterable, List

import numpy as np
from astartool.error import ParameterTypeError

npa = np.array

__all__ = [
    'BaseIntervals',
    'Intervals',
    'IntervalType',
    'ListIntervals',
    'DiscreteBaseIntervals',
    'ContinuousBaseIntervals',
    'R',
    'Z',
    'N',
    'EMPTY',

    'get_min_discrete_base_intervals'
]


class IntervalType:
    Discrete = 1
    Continuous = 2
    Open = 3
    Closed = 4


class BaseIntervals:
    def __init__(self, boundary=None, continuous=True, open_or_closed=(IntervalType.Closed, IntervalType.Open), values=None):
        if boundary is None:
            boundary = np.empty(0)
        if isinstance(boundary, (list, tuple)):
            boundary = npa(boundary)
        if isinstance(boundary, np.ndarray):
            len_boundary = len(boundary)
            assert len_boundary in {0, 2}
            if len_boundary == 2:
                assert boundary[1] >= boundary[0]
            self.boundary = boundary

        self.discrete_or_continuous = IntervalType.Continuous if continuous else IntervalType.Discrete
        self.open_or_closed = open_or_closed
        if self.is_discrete():
            if values is not None:
                self.use_values = True
                self.values = set(values)
            else:
                self.use_values = False
                self.values = None
        else:
            self.use_values = False
            self.values = None

    def is_discrete(self):
        """
        判断是否是离散区间
        :return:
        """
        return self.discrete_or_continuous == IntervalType.Discrete

    def is_continuous(self):
        """
        判断是否是连续区间
        :return:
        """
        return self.discrete_or_continuous == IntervalType.Continuous

    def is_valid(self):
        return self.is_empty() or self.boundary[1] > self.boundary[0] or \
            (self.open_or_closed == (IntervalType.Closed, IntervalType.Closed) and self.boundary[0] == self.boundary[1])

    def is_empty(self):
        if self.is_continuous():
            return len(self.boundary) == 0 or \
                (self.boundary[0] == self.boundary[1] and
                 (self.open_or_closed[0] == IntervalType.Open or self.open_or_closed[1] == IntervalType.Open))
        else:
            if self.use_values and len(self.values) == 0:
                return True
            elif len(self.boundary) > 0:
                # 避免inf的情况
                if (np.isinf(self.boundary[0]) and np.sign(self.boundary[0]) < 0) or (np.isinf(self.boundary[1]) and np.sign(self.boundary[1]) > 0):
                    return False
                if int(self.boundary[0]) == int(self.boundary[1]):
                    return True
                return False
            else:
                return True

    @abstractmethod
    def intersects(self, other):
        pass

    @abstractmethod
    def intersection(self, other):
        pass

    @abstractmethod
    def union(self, other):
        pass

    @abstractmethod
    def sub(self, other):
        pass

    @abstractmethod
    def contains(self, item):
        pass

    def __and__(self, other):
        return self.intersection(other)

    def __or__(self, other):
        return self.union(other)

    def __contains__(self, item):
        return self.contains(item)

    def __str__(self):
        return self.to_string()

    def __repr__(self):
        return str(self)

    @abstractmethod
    def to_string(self):
        pass


def get_min_discrete_base_intervals(base_intervals: BaseIntervals):
    """
    化简离散区间:
    若存在非inf的开区间，则转成闭区间
    若离散区间可以表示成集合的形式，则转化成集合的形式
    :param base_intervals: 待化简的区间
    :return: 化简以后的区间
    """
    boundary = list(base_intervals.boundary)
    open_or_closed_start, open_or_closed_end = base_intervals.open_or_closed
    if np.isinf(boundary[0]):
        pass
    else:
        ceil = np.ceil(boundary[0])
        if open_or_closed_start == IntervalType.Open:
            boundary[0] = int(ceil + 1) if np.isclose(ceil, boundary[0]) else int(ceil)
        else:
            boundary[0] = int(ceil)
        open_or_closed_start = IntervalType.Closed
    if np.isinf(boundary[1]):
        pass
    else:
        floor = np.floor(boundary[1])
        if open_or_closed_end == IntervalType.Open:
            boundary[1] = int(floor - 1) if np.isclose(floor, boundary[1]) else int(floor)
        else:
            boundary[1] = int(floor)
        open_or_closed_end = IntervalType.Closed

    if open_or_closed_start == IntervalType.Closed and open_or_closed_end == IntervalType.Closed:
        new_intervals = {i for i in range(boundary[0], boundary[1] + 1)}
        return DiscreteBaseIntervals(values=new_intervals)
    else:
        return DiscreteBaseIntervals(boundary, (open_or_closed_start, open_or_closed_end))


class DiscreteBaseIntervals(BaseIntervals):
    def __init__(self, boundary=None, open_or_closed=(IntervalType.Closed, IntervalType.Open), values=None):
        super().__init__(boundary, False, open_or_closed, values)

    def __repr__(self):
        return f"DiscreteBaseIntervals<{str(self)}>"

    def __eq__(self, other):
        if not other.is_discrete():
            return False

        if not self.use_values:
            intervals_1 = get_min_discrete_base_intervals(self)
        else:
            intervals_1 = self
        if not other.use_values:
            intervals_2 = get_min_discrete_base_intervals(other)
        else:
            intervals_2 = other
        if intervals_1.use_values and intervals_2.use_values:
            return intervals_1.values == intervals_2.values
        return np.allclose(intervals_1.boundary, intervals_2.boundary)

    def to_string(self):
        if self.use_values:
            s = "{" + ",".join(map(str, self.values)) + "}"
        else:
            left = "(" if self.open_or_closed[0] == IntervalType.Open else "["
            right = ")" if self.open_or_closed[1] == IntervalType.Open else "]"
            s = f"{left}{self.boundary[0]}, {self.boundary[1]}{right}" if not self.use_values else "{}"
        return s

    def intersects(self, other) -> bool:
        """
        判断区间是否相交
        :param other: 另一个区间
        :return:
        """
        if self.is_empty() or other.is_empty():
            return False
        if self.use_values and other.use_values:
            return len(self.values.intersects(other.values)) > 0
        elif self.use_values:
            cmp_left = (lambda it, y: it >= y) if other.open_or_closed[0] == IntervalType.Closed else (lambda it, y: it > y)
            cmp_right = (lambda it, y: it <= y) if other.open_or_closed[1] == IntervalType.Closed else (lambda it, y: it < y)
            return np.any([cmp_left(each, other.boundary[0]) and cmp_right(each, other.boundary[1]) for each in self.values])
        elif other.use_values:
            cmp_left = (lambda it, y: it >= y) if self.open_or_closed[0] == IntervalType.Closed else (lambda it, y: it > y)
            cmp_right = (lambda it, y: it <= y) if self.open_or_closed[1] == IntervalType.Closed else (lambda it, y: it < y)
            return np.any([cmp_left(each, self.boundary[0]) and cmp_right(each, self.boundary[1]) for each in other.values])
        else:
            (a, b), type1 = self.boundary, self.open_or_closed[1]
            (c, d), type2 = other.boundary, other.open_or_closed[0]
            if a > c:
                a, b, c, d, type1, type2 = c, d, a, b, type2, type1
            if b > c:
                return True
            if b == c and type2 == IntervalType.Closed and type1 == IntervalType.Closed:
                return True
            return False

    def intersection(self, other):
        if self.is_empty() or other.is_empty():
            return DiscreteBaseIntervals()
        if other.is_discrete():
            if self.use_values and other.use_values:
                return DiscreteBaseIntervals(values=self.values.intersects(other.values))
            elif self.use_values:
                cmp_left = (lambda it, y: it >= y) if other.open_or_closed[0] == IntervalType.Closed else (lambda it, y: it > y)
                cmp_right = (lambda it, y: it <= y) if other.open_or_closed[1] == IntervalType.Closed else (lambda it, y: it < y)
                return DiscreteBaseIntervals(values=[each for each in self.values if cmp_left(each, other.boundary[0]) and cmp_right(each, other.boundary[1])])
            elif other.use_values:
                cmp_left = (lambda it, y: it >= y) if self.open_or_closed[0] == IntervalType.Closed else (lambda it, y: it > y)
                cmp_right = (lambda it, y: it <= y) if self.open_or_closed[1] == IntervalType.Closed else (lambda it, y: it < y)
                return DiscreteBaseIntervals(values=[each for each in other.values if cmp_left(each, self.boundary[0]) and cmp_right(each, self.boundary[1])])
            else:
                (a, b), type1 = self.boundary, self.open_or_closed
                (c, d), type2 = other.boundary, other.open_or_closed
                # type_res = [IntervalType.Closed, IntervalType.Closed]
                if a > c:
                    a, b, c, d, type1, type2 = c, d, a, b, type2, type1
                elif a == c and type1[0] == IntervalType.Open:
                    a, b, c, d, type1, type2 = c, d, a, b, type2, type1
                if b > c:
                    if b > d:
                        return DiscreteBaseIntervals(boundary=(c, d), open_or_closed=type2)
                    else:
                        return DiscreteBaseIntervals(boundary=(c, b), open_or_closed=(type2[0], type1[1]))
                elif b == c and type2 == IntervalType.Closed and type1 == IntervalType.Closed:
                    return DiscreteBaseIntervals(values=[b])
                else:
                    return DiscreteBaseIntervals(values=set())
        raise NotImplemented

    def union(self, other):
        """
        区间求并
        :param other:
        :return:
        """
        if self.is_empty():
            return other
        if other.is_empty():
            return self

        if other.is_discrete():
            if self.use_values and other.use_values:
                return DiscreteBaseIntervals(values=self.values.union(other.values))
        raise NotImplemented

    def sub(self, other):
        """
        离散区间做差
        :param other:
        :return:
        """
        if isinstance(other, numbers.Number):
            if self.use_values:
                return DiscreteBaseIntervals(values=self.values - {other})
            else:
                raise NotImplemented
        elif isinstance(other, BaseIntervals):
            if self.use_values:
                cmp_left = (lambda it, y: it >= y) if self.open_or_closed[0] == IntervalType.Closed else (lambda it, y: it > y)
                cmp_right = (lambda it, y: it <= y) if self.open_or_closed[1] == IntervalType.Closed else (lambda it, y: it < y)
                return DiscreteBaseIntervals(values={each for each in self.values if cmp_left(each, other.boundary[0]) and cmp_right(each, other.boundary[1])})
            else:
                raise NotImplemented
        raise NotImplemented

    def contains(self, item):
        if self.use_values:
            return item in self.values
        elif isinstance(item, numbers.Number):
            if self.use_values:
                return item in self.values
            else:
                item = int(item)
                cmp_left = (lambda it, y: it >= y) if self.open_or_closed[0] == IntervalType.Closed else (lambda it, y: it > y)
                cmp_right = (lambda it, y: it <= y) if self.open_or_closed[1] == IntervalType.Closed else (lambda it, y: it < y)
                return np.all(cmp_left(item, self.boundary[0])) and np.all(cmp_right(item, self.boundary[1]))

        elif isinstance(item, Iterable):
            if self.use_values:
                item_list = list(item)
                return len(self.values.intersects(item_list)) == len(item_list)
            else:
                item = npa(list(item)).astype(int)
                cmp_left = (lambda it, y: it >= y) if self.open_or_closed[0] == IntervalType.Closed else (lambda it, y: it > y)
                cmp_right = (lambda it, y: it <= y) if self.open_or_closed[1] == IntervalType.Closed else (lambda it, y: it < y)
                return np.all(cmp_left(item, self.boundary[0])) and np.all(cmp_right(item, self.boundary[1]))
        elif isinstance(item, BaseIntervals):
            if self.use_values:
                return len(self.values.intersects(item)) != 0
            else:
                raise NotImplemented
        raise ParameterTypeError


class ContinuousBaseIntervals(BaseIntervals):
    def __init__(self, boundary=None, open_or_closed=(IntervalType.Closed, IntervalType.Open)):
        super().__init__(boundary, True, open_or_closed, values=None)

    def __repr__(self):
        return f"ContinuousBaseIntervals<{str(self)}>"

    def to_string(self):
        left = "(" if self.open_or_closed[0] == IntervalType.Open else "["
        right = ")" if self.open_or_closed[1] == IntervalType.Open else "]"
        return f"{left}{self.boundary[0]}, {self.boundary[1]}{right}" if not self.is_empty() else "{}"

    def intersects(self, other):
        if self.is_empty() or other.is_empty():
            return False
        (a, b), (type1_start, type1) = self.boundary, self.open_or_closed
        (c, d), (type2, type2_end) = other.boundary, other.open_or_closed
        if a > c:
            a, b, c, d, type1, type2 = c, d, a, b, type2_end, type1_start
        if b > c:
            return True
        if b == c and type2 == IntervalType.Closed and type1 == IntervalType.Closed:
            return True
        return False

    def intersection(self, other):
        """
        区间求交集
        :param other:
        :return:
        """
        if self.is_empty() or other.is_empty():
            return ContinuousBaseIntervals()
        if other.is_continuous():
            interval = ContinuousBaseIntervals()
            (a, b), (ta, tb) = self.boundary, self.open_or_closed
            (c, d), (tc, td) = other.boundary, other.open_or_closed
            if a > c or (a == c and tc == IntervalType.Closed):
                a, b, c, d, ta, tb, tc, td = c, d, a, b, tc, td, ta, tb
            if b > c:
                if b > d or (b == d and tb == IntervalType.Closed):
                    interval.open_or_closed = (tc, td)
                    interval.boundary = npa([c, d])
                else:
                    interval.open_or_closed = (tc, tb)
                    interval.boundary = npa([c, b])
                return interval
            elif b == c and tb == IntervalType.Closed and tc == IntervalType.Closed:
                interval.boundary = npa([b, c])
                interval.open_or_closed = (IntervalType.Closed, IntervalType.Closed)
                return interval
            return interval
        raise NotImplemented

    def contains(self, item, return_mat=True):
        if isinstance(item, numbers.Number):
            cmp_left = (lambda it, y: it >= y) if self.open_or_closed[0] == IntervalType.Closed else (lambda it, y: it > y)
            cmp_right = (lambda it, y: it <= y) if self.open_or_closed[1] == IntervalType.Closed else (lambda it, y: it < y)
            return (cmp_left(item, self.boundary[0])) and (cmp_right(item, self.boundary[1]))
        elif isinstance(item, np.ndarray):
            cmp_left = (lambda it, y: it >= y) if self.open_or_closed[0] == IntervalType.Closed else (lambda it, y: it > y)
            cmp_right = (lambda it, y: it <= y) if self.open_or_closed[1] == IntervalType.Closed else (lambda it, y: it < y)
            if return_mat:
                try:
                    return cmp_left(item, self.boundary[0]) & cmp_right(item, self.boundary[1])
                except:
                    aaa = 1
            else:
                return (cmp_left(item, self.boundary[0])) and (cmp_right(item, self.boundary[1]))
        elif isinstance(item, Iterable):
            cmp_left = (lambda it, y: it >= y) if self.open_or_closed[0] == IntervalType.Closed else (lambda it, y: it > y)
            cmp_right = (lambda it, y: it <= y) if self.open_or_closed[1] == IntervalType.Closed else (lambda it, y: it < y)
            return np.all(cmp_left(item, self.boundary[0])) and np.all(cmp_right(item, self.boundary[1]))

        elif isinstance(item, BaseIntervals):
            cmp_left = (lambda it, y: it >= y) if not (self.open_or_closed[0] == IntervalType.Open and item.open_or_closed[0] == IntervalType.Closed) else (lambda it, y: it > y)
            cmp_right = (lambda it, y: it <= y) if not (self.open_or_closed[1] == IntervalType.Open and item.open_or_closed[1] == IntervalType.Closed) else (lambda it, y: it < y)
            return np.all(cmp_left(item.boundary[0], self.boundary[0])) and np.all(cmp_right(item.boundary[1], self.boundary[1]))

        raise ParameterTypeError

    def union(self, other):
        if isinstance(other, ContinuousBaseIntervals):
            interval = ContinuousBaseIntervals()
            (a, b), (ta, tb) = self.boundary, self.open_or_closed
            (c, d), (tc, td) = other.boundary, other.open_or_closed
            if a > c or (a == c and tc == IntervalType.Closed):
                a, b, c, d, ta, tb, tc, td = c, d, a, b, tc, td, ta, tb
            if b > c:
                if b > d or (b == d and tb == IntervalType.Closed):
                    interval.open_or_closed = (ta, tb)
                    interval.boundary = npa([a, b])
                else:
                    interval.open_or_closed = (ta, td)
                    interval.boundary = npa([a, d])
                return interval
            elif b == c and (tb == IntervalType.Closed or tc == IntervalType.Closed):
                interval.boundary = npa([a, d])
                interval.open_or_closed = (ta, td)
                return interval
            else:
                from . import ListIntervals
                return ListIntervals([self, other])

        raise ParameterTypeError

    def sub(self, other):
        if isinstance(other, ContinuousBaseIntervals):
            (a, b), (ta, tb) = self.boundary, self.open_or_closed
            (c, d), (tc, td) = other.boundary, other.open_or_closed

            if b < c or (b == c and tb == IntervalType.Open):
                # a, b, c, d的情况
                return ContinuousBaseIntervals(self.boundary, open_or_closed=self.open_or_closed)
            elif b == c and tc == IntervalType.Closed:
                # a, b, c, d的情况
                return ContinuousBaseIntervals(self.boundary, open_or_closed=(self.open_or_closed[0], IntervalType.Open))

            if a > d or (a == d and ta == IntervalType.Open):
                # c, d, a, b 的情况
                return ContinuousBaseIntervals(self.boundary, open_or_closed=self.open_or_closed)
            elif a == d and td == IntervalType.Closed:
                # c, d, a, b 的情况
                return ContinuousBaseIntervals(self.boundary, open_or_closed=(IntervalType.Open, self.open_or_closed[1]))

            if c >= a:
                if d <= b:
                    # a, c, d, b 的情况
                    from . import ListIntervals
                    ca = ContinuousBaseIntervals((a, c), open_or_closed=(self.open_or_closed[0], IntervalType.Closed if other.open_or_closed[0] == IntervalType.Open else IntervalType.Open))
                    cb = ContinuousBaseIntervals((d, b), open_or_closed=(IntervalType.Closed if other.open_or_closed[1] == IntervalType.Open else IntervalType.Open, self.open_or_closed[1]))

                    if not ca.is_empty():
                        if not ca.is_empty():
                            return ListIntervals([ca, cb])
                        else:
                            return ca
                    else:
                        return cb
                else:
                    # a, c, b, d 的情况
                    return ContinuousBaseIntervals((a, c), open_or_closed=(self.open_or_closed[0], IntervalType.Closed if other.open_or_closed[1] == IntervalType.Open else IntervalType.Open))
            else:
                if d <= b:
                    # c, a, d, b 的情况
                    return ContinuousBaseIntervals((d, b), open_or_closed=(IntervalType.Closed if other.open_or_closed[1] == IntervalType.Open else IntervalType.Open, self.open_or_closed[1]))
                else:
                    # c, a, b, d 的情况
                    return ContinuousBaseIntervals()

        raise ParameterTypeError

    def __eq__(self, other):
        return isinstance(other, ContinuousBaseIntervals) and \
            self.open_or_closed[0] == other.open_or_closed[0] and \
            self.open_or_closed[1] == other.open_or_closed[1] and \
            np.allclose(self.boundary, other.boundary)


class Intervals(metaclass=ABCMeta):
    def __init__(self, intervals: (BaseIntervals, Iterable[BaseIntervals]) = None, simple=False):
        if isinstance(intervals, Intervals):
            self.intervals = intervals.intervals.copy()
        elif isinstance(intervals, BaseIntervals):
            self.intervals = [intervals]
        elif isinstance(intervals, Iterable):
            self.intervals: List[BaseIntervals] = list(intervals)
            for each in self.intervals:
                assert isinstance(each, BaseIntervals)

        self.is_simple = simple

    def __repr__(self):
        return f"Intervals<{str(self)}>"

    def __str__(self):
        return self.to_string()

    def to_string(self):
        return "[" + ','.join(map(str, self.intervals)) + "]"

    def is_empty(self, simplify=True):
        if not self.is_simple:
            res = self.simplify(inplace=simplify)
            return len(res.intervals) == 0
        else:
            return len(self.intervals) == 0

    @abstractmethod
    def union(self, other, inplace=False, simple=True):
        pass

    @abstractmethod
    def intersection(self, other, inplace=False, simple=True):
        pass

    @abstractmethod
    def sub(self, other, inplace=False, simple=True):
        pass

    @abstractmethod
    def simplify(self, inplace=True):
        pass

    @abstractmethod
    def contains(self, other):
        pass

    def __and__(self, other):
        return self.intersection(other)

    def __iand__(self, other):
        return self.intersection(other, inplace=True)

    def __sub__(self, other):
        return self.sub(other, inplace=False)

    def __isub__(self, other):
        return self.sub(other, inplace=True)

    def __or__(self, other):
        return self.union(other)

    def __ior__(self, other):
        return self.union(other, inplace=True)


class ListIntervals(Intervals):

    def __init__(self, intervals: (BaseIntervals, Iterable[BaseIntervals]) = None, simple=False):
        super().__init__(intervals, simple)

    def simplify(self, inplace=True):
        intervals = [each for each in self.intervals if each.is_valid() and not each.is_empty()]
        if len(intervals) >= 2:
            intervals_use_values = [interval for interval in intervals if isinstance(interval, DiscreteBaseIntervals) and interval.use_values]
            res = []
            if intervals_use_values:
                myset = set()
                for s in intervals_use_values:
                    myset.update(s.values)
                interval_set = DiscreteBaseIntervals(values=myset)
                res.append(interval_set)
            intervals_others = [interval for interval in intervals if not (isinstance(interval, DiscreteBaseIntervals) and interval.use_values)]
            intervals = sorted(intervals_others, key=lambda x: x.boundary[0])
            current_interval: BaseIntervals = intervals[0]
            for each in intervals[1:]:
                tmp = current_interval.union(each)
                if isinstance(tmp, BaseIntervals):
                    current_interval = tmp
                else:
                    res.append(current_interval)
                    current_interval = each
            else:
                res.append(current_interval)
            intervals = res
        if inplace:
            self.intervals = intervals
            return self
        else:
            return ListIntervals(intervals)

    def union(self, other, inplace=False, simple=True):
        if inplace:
            if isinstance(other, Intervals):
                self.intervals.extend(other.intervals)
                if simple:
                    self.simplify(inplace)
            elif isinstance(other, BaseIntervals):
                self.intervals.append(other)
                if simple:
                    self.simplify(inplace)
            elif isinstance(other, Iterable):
                self.intervals.extend(other)
                if simple:
                    self.simplify(inplace)
            else:
                raise ParameterTypeError
            return self
        else:
            if isinstance(other, ListIntervals):
                new_intervals = ListIntervals(self.intervals + other.intervals)
                if simple:
                    new_intervals.simplify(inplace)
            elif isinstance(other, BaseIntervals):
                new_intervals = ListIntervals(self.intervals + [other])
                if simple:
                    new_intervals.simplify(inplace)
            elif isinstance(other, Iterable):
                new_intervals = ListIntervals(self.intervals + other)
                if simple:
                    new_intervals.simplify(inplace)
            else:
                raise ParameterTypeError
            return new_intervals

    def sub(self, other, inplace=False, simple=True):
        if isinstance(other, ListIntervals):
            if inplace:
                self.intervals = [a.sub(b) for a, b in itertools.product(self.intervals, other.intervals)]
                if simple:
                    self.simplify(inplace)
                return self
            else:
                intervals = [a.sub(b) for a, b in itertools.product(self.intervals, other.intervals)]
                new_intervals = ListIntervals(intervals, simple)
                return new_intervals
        raise NotImplemented

    def intersection(self, other, inplace=False, simple=True):
        if inplace:
            if isinstance(other, Intervals):
                res = [a.intersection(b) for a, b in itertools.product(self.intervals, other.intervals)]
                self.intervals = res
                if simple:
                    self.simplify(inplace)
            elif isinstance(other, BaseIntervals):
                res = [a.intersection(other) for a in self.intervals]
                self.intervals = res
                if simple:
                    self.simplify(inplace)
            elif isinstance(other, Iterable):
                res = [a.intersection(b) for a, b in itertools.product(self.intervals, other)]
                self.intervals = res
                if simple:
                    self.simplify(inplace)
            else:
                raise ParameterTypeError
            return self
        else:
            if isinstance(other, Intervals):
                res = [a.intersection(b) for a, b in itertools.product(self.intervals, other.intervals)]
                result = ListIntervals(res)
                if simple:
                    result.simplify(inplace)
            elif isinstance(other, Iterable):
                res = [a.intersection(b) for a, b in itertools.product(self.intervals, other)]
                result = ListIntervals(res)
                if simple:
                    result.simplify(inplace)
            else:
                raise ParameterTypeError
            return result

    def __eq__(self, other):
        if isinstance(other, ListIntervals):
            res1 = self.simplify(False)
            res2 = other.simplify(False)
            r = [a == b for a, b in zip(res1.intervals, res2.intervals)]
            return (len(res1.intervals) == len(res2.intervals)) and np.all(r)
        return False

    def __contains__(self, item):
        return self.contains(item)

    def contains(self, x):
        if isinstance(x, numbers.Number):
            for each in self.intervals:
                if each.contains(x):
                    return True
            return False
        elif isinstance(x, np.ndarray):
            res = np.zeros_like(x, dtype=bool)
            for each in self.intervals:
                res = res | each.contains(x)
                # print(str(each), "contains", res)
            return res
        raise ParameterTypeError("目前只支持数或者ndarray类型")

    def to_string(self):
        return '∪'.join(map(str, self.intervals))


EMPTY = ListIntervals(ContinuousBaseIntervals())
R = ListIntervals(ContinuousBaseIntervals((-np.inf, np.inf), (IntervalType.Open, IntervalType.Open)))
Z = ListIntervals(DiscreteBaseIntervals((-np.inf, np.inf), (IntervalType.Open, IntervalType.Open)))
N = ListIntervals(DiscreteBaseIntervals((0, np.inf), (IntervalType.Closed, IntervalType.Open)))
