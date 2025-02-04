import unittest
from typing import TypeVar, Union, Optional
from collections.abc import Iterable

from gloe import Transformer
from gloe._typing_utils import _match_types, _specify_types, _format_return_annotation
from gloe.collection import MapOver


A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")


class TestTypeMatching(unittest.TestCase):
    def assertEqualTypes(self, type1, type2):
        self.assertEqual(str(type1), str(type2))

    def test_basic_match_case(self):
        generic = tuple[
            Iterable[A],
            tuple[int, Iterable[Transformer[str, B]], Union[C, float, None]],
        ]
        specific = tuple[
            list[float],
            tuple[int, list[MapOver[str, dict]], Optional[Union[list, float]]],
        ]

        matched_types = _match_types(generic, specific)
        self.assertDictEqual(matched_types, {A: float, B: dict, C: list})

        new_generic = _specify_types(generic, matched_types)
        expected_type = tuple[
            Iterable[float],
            tuple[int, Iterable[Transformer[str, dict]], Optional[Union[list, float]]],
        ]
        self.assertEqualTypes(new_generic, _specify_types(expected_type, {}))

        wrong_type = tuple[
            Iterable[float],
            tuple[int, Iterable[Transformer[str, dict]], tuple[list, float, None]],
        ]
        matched_generic = _match_types(generic, wrong_type)

        self.assertDictEqual(matched_generic, {A: float, B: dict})

        self.assertDictEqual(_match_types(tuple[int, str], tuple[int]), {})

    def test_format(self):
        _format = _format_return_annotation
        self.assertEqual(_format(float), "float")
        self.assertEqual(_format(tuple[float, int]), "(float, int)")
        self.assertEqual(_format(Union[float, int]), "(float | int)")
        self.assertEqual(_format((float, int)), "(float, int)")
