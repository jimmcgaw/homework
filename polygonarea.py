"""
Python module for finding the area of a regular polygon using 
the following formula, given a list of coordinate tuples:
Area = 1/2 X Perimeter X Apothem

Usage:
get_polygon_area([(x1, y1), (x2, y2)...(xn, yn)])

Tests require pytest. Install, uncomment out test below, and run:
$ pytest polygonarea.py

"""
# Python 10+ uses builtins for typing, do this for earlier versions
from typing import List, Tuple
import itertools
import math


def euclidean_distance(coord1: Tuple[int], coord2: Tuple[int]) -> float:
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)


def get_perimeter(coordinate_pairs: List[Tuple[Tuple[int]]]) -> float:
    return sum(euclidean_distance(*coordinate_pair) for coordinate_pair in coordinate_pairs)


def get_centroid(coordinates: List[Tuple[int]]) -> Tuple[float]:
    x = sum(c[0] for c in coordinates) / len(coordinates)
    y = sum(c[1] for c in coordinates) / len(coordinates)
    return (x, y)


def get_midpoint(coord1: Tuple[int], coord2: Tuple[int]) -> Tuple[float]:
    x = (coord1[0] + coord2[0]) / 2
    y = (coord1[1] + coord2[1]) / 2
    return (x, y)


def get_apothem(coordinates: List[Tuple[int]]) -> float:
    midpoint = get_midpoint(coordinates[0], coordinates[1])
    centroid = get_centroid(coordinates)
    return euclidean_distance(midpoint, centroid)


def get_polygon_area(coordinates: List[Tuple[int]]) -> float:
    # generate list of edges by listing all vertex pairs
    iterator1, iterator2 = itertools.tee(coordinates)
    next(iterator2, None)
    coordinate_pairs = list(zip(iterator1, iterator2))
    # close the loop in pairs list
    coordinate_pairs.append((coordinates[-1], coordinates[0]))

    perimeter = get_perimeter(coordinate_pairs)
    apothem = get_apothem(coordinates)

    return 0.5 * apothem * perimeter


# import unittest
# import pytest

# class TestPolygonArea(unittest.TestCase):
#     coordinates = [
#         (2,2), (2,4), (4,4), (4,2)
#     ]

#     coordinate_pairs = [
#         ((2,2), (2,4)),
#         ((2,4), (4,4)),
#         ((4,4), (4,2)),
#         ((4,2), (2,2)),
#     ]

#     def test_euclidean_distance(self):
#         assert euclidean_distance((2, 2), (5, 6)) == pytest.approx(5.0, 0.0001)

#     def test_get_perimeter(self):
#         assert get_perimeter(self.coordinate_pairs) == pytest.approx(8.0, 0.0001)

#     def test_get_midpoint(self):
#         assert get_midpoint(self.coordinates[0], self.coordinates[1]) == (2, 3)

#     def test_get_centroid(self):
#         assert get_centroid(self.coordinates) == (3, 3)

#     def test_get_apothem(self):
#         assert get_apothem(self.coordinates) == pytest.approx(1, 0.0001)

#     def test_get_area(self):
#         assert get_polygon_area(self.coordinates) == pytest.approx(4, 0.001)

#     def test_get_area_pentagon(self):
#         coordinates = [(5,3), (3,4), (4,7), (6, 7), (7, 4)]
#         assert get_polygon_area(coordinates) == pytest.approx(11.535, 0.001)