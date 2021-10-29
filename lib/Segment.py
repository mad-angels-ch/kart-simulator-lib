import math

from .vector import Vector
from .point import Point
from .Line import Line


class Segment(Line):
    def __init__(self, begin: Point, vectorOrEnd: "Vector | Point") -> None:
        super().__init__(begin, vectorOrEnd)

    def begin(self) -> Point:
        """Retourne une extrémité du segment"""
        return self.point()

    def end(self) -> Point:
        """Retourne l'autre extrémité du segment"""
        return Point(self.point()).translate(self.vector())

    def length(self) -> float:
        """Retourne la longueur du segment"""
        return self.vector().norm()

    def passBy(self, point: Point) -> bool:
        """Retourne True si le point donné en paramètre se trouve sur le segment"""
        vector = Vector.fromPoints(self._point, point)
        if not super().passBy(point):
            return False

        begin = self.begin()
        end = self.end()
        for i in range(len(point)):
            if min(begin[i], end[i]) >= point[i] or max(begin[i], end[i]) <= point[i]:
                return False

        return True

    def intercepts(self, other: "Segment") -> bool:
        """Retourne True si les deux segments se coupent"""
        coefficient = self._vectorCoefficientToIntersectionPoint(other)
        if not coefficient:
            return False
        return 0 <= coefficient and coefficient <= 1

    def intersection(self, other: "Segment") -> "Point | None":
        """Retourne le point d'intersection entre les segments s'il existe"""
        coefficient = self._vectorCoefficientToIntersectionPoint(other)
        if not coefficient:
            return
        elif coefficient < 0 or 1 < coefficient:
            return
        else:
            return Point(
                *[
                    self.begin()[i] + coefficient * self.vector()[i]
                    for i in range(self.begin())
                ]
            )
