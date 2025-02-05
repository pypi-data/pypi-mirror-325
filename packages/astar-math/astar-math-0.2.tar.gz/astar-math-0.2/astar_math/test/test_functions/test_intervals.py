import itertools
import unittest

import numpy as np

from astar_math.functions import DiscreteBaseIntervals, ContinuousBaseIntervals, ListIntervals, IntervalType, EMPTY

npa = np.array


class TestDiscreteBaseIntervals(unittest.TestCase):
    def setUp(self) -> None:
        self.empty_0 = DiscreteBaseIntervals(values={})
        self.empty_1 = DiscreteBaseIntervals((0, 1), open_or_closed=(IntervalType.Open, IntervalType.Open))
        self.discrete_0_1 = DiscreteBaseIntervals(values={0})
        self.discrete_0_2 = DiscreteBaseIntervals([-1, 1], open_or_closed=[IntervalType.Open, IntervalType.Open])
        self.discrete_0_3 = DiscreteBaseIntervals([-1, 0], open_or_closed=[IntervalType.Open, IntervalType.Closed])
        self.discrete_0_4 = DiscreteBaseIntervals([0, 1], open_or_closed=[IntervalType.Closed, IntervalType.Open])
        self.discrete_01 = DiscreteBaseIntervals(values={0, 1})
        self.discrete_neq5_5 = DiscreteBaseIntervals([-5, 5], open_or_closed=[IntervalType.Closed, IntervalType.Closed])

    def test_equals_empty_case_1(self):
        self.assertEqual(self.empty_0, self.empty_1)

    # def test_equals_empty_case_2(self):
    #     self.assertEquals(self.empty_0, EMPTY)

    def test_equals_case_1(self):
        self.assertEqual(self.discrete_0_1, self.discrete_0_2)

    def test_equals_case_2(self):
        self.assertEqual(self.discrete_0_1, self.discrete_0_3)

    def test_equals_case_3(self):
        self.assertEqual(self.discrete_0_1, self.discrete_0_4)

    def test_equals_case_4(self):
        self.assertEqual(self.discrete_0_2, self.discrete_0_4)


class TestContinuousBaseIntervals(unittest.TestCase):
    def setUp(self) -> None:
        self.continuous_11_oo = ContinuousBaseIntervals([-1, 1], open_or_closed=[IntervalType.Open, IntervalType.Open])
        self.continuous_11_oc = ContinuousBaseIntervals([-1, 1], open_or_closed=[IntervalType.Open, IntervalType.Closed])
        self.continuous_11_co = ContinuousBaseIntervals([-1, 1], open_or_closed=[IntervalType.Closed, IntervalType.Open])
        self.continuous_11_cc = ContinuousBaseIntervals([-1, 1], open_or_closed=[IntervalType.Closed, IntervalType.Closed])

        self.continuous_23_oo = ContinuousBaseIntervals([2, 3], open_or_closed=[IntervalType.Open, IntervalType.Open])
        self.continuous_23_oc = ContinuousBaseIntervals([2, 3], open_or_closed=[IntervalType.Open, IntervalType.Closed])
        self.continuous_23_co = ContinuousBaseIntervals([2, 3], open_or_closed=[IntervalType.Closed, IntervalType.Open])
        self.continuous_23_cc = ContinuousBaseIntervals([2, 3], open_or_closed=[IntervalType.Closed, IntervalType.Closed])

        self.continuous_12_oo = ContinuousBaseIntervals([1, 2], open_or_closed=[IntervalType.Open, IntervalType.Open])
        self.continuous_12_oc = ContinuousBaseIntervals([1, 2], open_or_closed=[IntervalType.Open, IntervalType.Closed])
        self.continuous_12_co = ContinuousBaseIntervals([1, 2], open_or_closed=[IntervalType.Closed, IntervalType.Open])
        self.continuous_12_cc = ContinuousBaseIntervals([1, 2], open_or_closed=[IntervalType.Closed, IntervalType.Closed])

        self.continuous_0515_oo = ContinuousBaseIntervals([0.5, 1.5], open_or_closed=[IntervalType.Open, IntervalType.Open])
        self.continuous_0515_oc = ContinuousBaseIntervals([0.5, 1.5], open_or_closed=[IntervalType.Open, IntervalType.Closed])
        self.continuous_0515_co = ContinuousBaseIntervals([0.5, 1.5], open_or_closed=[IntervalType.Closed, IntervalType.Open])
        self.continuous_0515_cc = ContinuousBaseIntervals([0.5, 1.5], open_or_closed=[IntervalType.Closed, IntervalType.Closed])

        self.continuous_0505_oo = ContinuousBaseIntervals([-0.5, 0.5], open_or_closed=[IntervalType.Open, IntervalType.Open])
        self.continuous_0505_oc = ContinuousBaseIntervals([-0.5, 0.5], open_or_closed=[IntervalType.Open, IntervalType.Closed])
        self.continuous_0505_co = ContinuousBaseIntervals([-0.5, 0.5], open_or_closed=[IntervalType.Closed, IntervalType.Open])
        self.continuous_0505_cc = ContinuousBaseIntervals([-0.5, 0.5], open_or_closed=[IntervalType.Closed, IntervalType.Closed])

        self.continuous_21_oo = ContinuousBaseIntervals([-2, -1], open_or_closed=[IntervalType.Open, IntervalType.Open])
        self.continuous_21_oc = ContinuousBaseIntervals([-2, -1], open_or_closed=[IntervalType.Open, IntervalType.Closed])
        self.continuous_21_co = ContinuousBaseIntervals([-2, -1], open_or_closed=[IntervalType.Closed, IntervalType.Open])
        self.continuous_21_cc = ContinuousBaseIntervals([-2, -1], open_or_closed=[IntervalType.Closed, IntervalType.Closed])

        self.continuous_32_oo = ContinuousBaseIntervals([-3, -2], open_or_closed=[IntervalType.Open, IntervalType.Open])
        self.continuous_32_oc = ContinuousBaseIntervals([-3, -2], open_or_closed=[IntervalType.Open, IntervalType.Closed])
        self.continuous_32_co = ContinuousBaseIntervals([-3, -2], open_or_closed=[IntervalType.Closed, IntervalType.Open])
        self.continuous_32_cc = ContinuousBaseIntervals([-3, -2], open_or_closed=[IntervalType.Closed, IntervalType.Closed])

        self.continuous_112_oo = ContinuousBaseIntervals([-1, 2], open_or_closed=[IntervalType.Open, IntervalType.Open])
        self.continuous_112_oc = ContinuousBaseIntervals([-1, 2], open_or_closed=[IntervalType.Open, IntervalType.Closed])
        self.continuous_112_co = ContinuousBaseIntervals([-1, 2], open_or_closed=[IntervalType.Closed, IntervalType.Open])
        self.continuous_112_cc = ContinuousBaseIntervals([-1, 2], open_or_closed=[IntervalType.Closed, IntervalType.Closed])
        self.continuous_112 = [self.continuous_112_oo, self.continuous_112_oc, self.continuous_112_co, self.continuous_112_cc]

    def test_equals_1(self):
        ls = [self.continuous_11_oo, self.continuous_11_oc, self.continuous_11_co, self.continuous_11_cc]
        for a, b in itertools.combinations(ls, 2):
            self.assertNotEqual(a, b)

    def test_union_1(self):
        # 区间相离
        self.continuous_11 = [self.continuous_11_oo, self.continuous_11_oc, self.continuous_11_co, self.continuous_11_cc]
        self.continuous_23 = [self.continuous_23_oo, self.continuous_23_oc, self.continuous_23_co, self.continuous_23_cc]

        for a, b in itertools.product(self.continuous_11, self.continuous_23):
            res = ListIntervals([a, b])
            self.assertEqual(res, a.union(b))

    def test_union_2(self):
        # 区间相接
        self.continuous_11 = [self.continuous_11_oo, self.continuous_11_oc, self.continuous_11_co, self.continuous_11_cc]
        self.continuous_12 = [self.continuous_12_oo, self.continuous_12_oc, self.continuous_12_co, self.continuous_12_cc]

        res_mat = [[ListIntervals([self.continuous_11_oo, self.continuous_12_oo]),
                    ListIntervals([self.continuous_11_oo, self.continuous_12_oc]),
                    self.continuous_112_oo,
                    self.continuous_112_oc],

                   [self.continuous_112_oo,
                    self.continuous_112_oc,
                    self.continuous_112_oo,
                    self.continuous_112_oc],

                   [ListIntervals([self.continuous_11_co, self.continuous_12_oo]),
                    ListIntervals([self.continuous_11_co, self.continuous_12_oc]),
                    self.continuous_112_co,
                    self.continuous_112_cc],

                   [self.continuous_112_co,
                    self.continuous_112_cc,
                    self.continuous_112_co,
                    self.continuous_112_cc],
        ]

        for ind, (ai, bi) in enumerate(itertools.product(range(4), range(4))):
            a, b = self.continuous_11[ai], self.continuous_12[bi]
            res_i = a.union(b)
            print(res_mat[ai][bi], res_i)
            print(type(res_mat[ai][bi]), type(res_i))

            self.assertEqual(res_mat[ai][bi], res_i, f"{ind}, {ai},{bi}错误")


class TestListIntervals(unittest.TestCase):
    def setUp(self) -> None:
        pass

