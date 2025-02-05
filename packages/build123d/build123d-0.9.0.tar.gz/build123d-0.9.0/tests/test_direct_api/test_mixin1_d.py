"""
build123d imports

name: test_mixin1_d.py
by:   Gumyr
date: January 22, 2025

desc:
    This python module contains tests for the build123d project.

license:

    Copyright 2025 Gumyr

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

"""

import math
import unittest

from build123d.build_enums import CenterOf, GeomType, PositionMode, Side, SortBy
from build123d.geometry import Axis, Location, Plane, Vector
from build123d.objects_part import Box, Cylinder
from build123d.topology import Compound, Edge, Face, Wire


class TestMixin1D(unittest.TestCase):
    """Test the add in methods"""

    def test_position_at(self):
        self.assertAlmostEqual(
            Edge.make_line((0, 0, 0), (1, 1, 1)).position_at(0.5),
            (0.5, 0.5, 0.5),
            5,
        )
        # Not sure what PARAMETER mode returns - but it's in the ballpark
        point = (
            Edge.make_line((0, 0, 0), (1, 1, 1))
            .position_at(0.5, position_mode=PositionMode.PARAMETER)
            .to_tuple()
        )
        self.assertTrue(all([0.0 < v < 1.0 for v in point]))

        wire = Wire([Edge.make_line((0, 0, 0), (10, 0, 0))])
        self.assertAlmostEqual(wire.position_at(0.3), (3, 0, 0), 5)
        self.assertAlmostEqual(
            wire.position_at(3, position_mode=PositionMode.LENGTH), (3, 0, 0), 5
        )
        self.assertAlmostEqual(wire.edge().position_at(0.3), (3, 0, 0), 5)
        self.assertAlmostEqual(
            wire.edge().position_at(3, position_mode=PositionMode.LENGTH), (3, 0, 0), 5
        )

        circle_wire = Wire(
            [
                Edge.make_circle(1, start_angle=0, end_angle=180),
                Edge.make_circle(1, start_angle=180, end_angle=360),
            ]
        )
        p1 = circle_wire.position_at(math.pi, position_mode=PositionMode.LENGTH)
        p2 = circle_wire.position_at(math.pi / circle_wire.length)
        self.assertAlmostEqual(p1, (-1, 0, 0), 14)
        self.assertAlmostEqual(p2, (-1, 0, 0), 14)
        self.assertAlmostEqual(p1, p2, 14)

        circle_edge = Edge.make_circle(1)
        p3 = circle_edge.position_at(math.pi, position_mode=PositionMode.LENGTH)
        p4 = circle_edge.position_at(math.pi / circle_edge.length)
        self.assertAlmostEqual(p3, (-1, 0, 0), 14)
        self.assertAlmostEqual(p4, (-1, 0, 0), 14)
        self.assertAlmostEqual(p3, p4, 14)

        circle = Wire(
            [
                Edge.make_circle(2, start_angle=0, end_angle=180),
                Edge.make_circle(2, start_angle=180, end_angle=360),
            ]
        )
        self.assertAlmostEqual(
            circle.position_at(0.5),
            (-2, 0, 0),
            5,
        )
        self.assertAlmostEqual(
            circle.position_at(2 * math.pi, position_mode=PositionMode.LENGTH),
            (-2, 0, 0),
            5,
        )

    def test_positions(self):
        e = Edge.make_line((0, 0, 0), (1, 1, 1))
        distances = [i / 4 for i in range(3)]
        pts = e.positions(distances)
        for i, position in enumerate(pts):
            self.assertAlmostEqual(position, (i / 4, i / 4, i / 4), 5)

    def test_tangent_at(self):
        self.assertAlmostEqual(
            Edge.make_circle(1, start_angle=0, end_angle=90).tangent_at(1.0),
            (-1, 0, 0),
            5,
        )
        tangent = (
            Edge.make_circle(1, start_angle=0, end_angle=90)
            .tangent_at(0.0, position_mode=PositionMode.PARAMETER)
            .to_tuple()
        )
        self.assertTrue(all([0.0 <= v <= 1.0 for v in tangent]))

        self.assertAlmostEqual(
            Edge.make_circle(1, start_angle=0, end_angle=180).tangent_at(
                math.pi / 2, position_mode=PositionMode.LENGTH
            ),
            (-1, 0, 0),
            5,
        )

    def test_tangent_at_point(self):
        circle = Wire(
            [
                Edge.make_circle(1, start_angle=0, end_angle=180),
                Edge.make_circle(1, start_angle=180, end_angle=360),
            ]
        )
        pnt_on_circle = Vector(math.cos(math.pi / 4), math.sin(math.pi / 4))
        tan = circle.tangent_at(pnt_on_circle)
        self.assertAlmostEqual(tan, (-math.sqrt(2) / 2, math.sqrt(2) / 2), 5)

    def test_tangent_at_by_length(self):
        circle = Edge.make_circle(1)
        tan = circle.tangent_at(circle.length * 0.5, position_mode=PositionMode.LENGTH)
        self.assertAlmostEqual(tan, (0, -1), 5)

    def test_tangent_at_error(self):
        with self.assertRaises(ValueError):
            Edge.make_circle(1).tangent_at("start")

    def test_normal(self):
        self.assertAlmostEqual(
            Edge.make_circle(
                1, Plane(origin=(0, 0, 0), z_dir=(1, 0, 0)), start_angle=0, end_angle=60
            ).normal(),
            (1, 0, 0),
            5,
        )
        self.assertAlmostEqual(
            Edge.make_ellipse(
                1,
                0.5,
                Plane(origin=(0, 0, 0), z_dir=(1, 1, 0)),
                start_angle=0,
                end_angle=90,
            ).normal(),
            (math.sqrt(2) / 2, math.sqrt(2) / 2, 0),
            5,
        )
        self.assertAlmostEqual(
            Edge.make_spline(
                [
                    (1, 0),
                    (math.sqrt(2) / 2, math.sqrt(2) / 2),
                    (0, 1),
                ],
                tangents=((0, 1, 0), (-1, 0, 0)),
            ).normal(),
            (0, 0, 1),
            5,
        )
        with self.assertRaises(ValueError):
            Edge.make_line((0, 0, 0), (1, 1, 1)).normal()

    def test_center(self):
        c = Edge.make_circle(1, start_angle=0, end_angle=180)
        self.assertAlmostEqual(c.center(), (0, 1, 0), 5)
        self.assertAlmostEqual(
            c.center(CenterOf.MASS),
            (0, 0.6366197723675814, 0),
            5,
        )
        self.assertAlmostEqual(c.center(CenterOf.BOUNDING_BOX), (0, 0.5, 0), 5)

    def test_location_at(self):
        loc = Edge.make_circle(1).location_at(0.25)
        self.assertAlmostEqual(loc.position, (0, 1, 0), 5)
        self.assertAlmostEqual(loc.orientation, (0, -90, -90), 5)

        loc = Edge.make_circle(1).location_at(
            math.pi / 2, position_mode=PositionMode.LENGTH
        )
        self.assertAlmostEqual(loc.position, (0, 1, 0), 5)
        self.assertAlmostEqual(loc.orientation, (0, -90, -90), 5)

    def test_locations(self):
        locs = Edge.make_circle(1).locations([i / 4 for i in range(4)])
        self.assertAlmostEqual(locs[0].position, (1, 0, 0), 5)
        self.assertAlmostEqual(locs[0].orientation, (-90, 0, -180), 5)
        self.assertAlmostEqual(locs[1].position, (0, 1, 0), 5)
        self.assertAlmostEqual(locs[1].orientation, (0, -90, -90), 5)
        self.assertAlmostEqual(locs[2].position, (-1, 0, 0), 5)
        self.assertAlmostEqual(locs[2].orientation, (90, 0, 0), 5)
        self.assertAlmostEqual(locs[3].position, (0, -1, 0), 5)
        self.assertAlmostEqual(locs[3].orientation, (0, 90, 90), 5)

    def test_project(self):
        target = Face.make_rect(10, 10, Plane.XY.rotated((0, 45, 0)))
        circle = Edge.make_circle(1).locate(Location((0, 0, 10)))
        ellipse: Wire = circle.project(target, (0, 0, -1))
        bbox = ellipse.bounding_box()
        self.assertAlmostEqual(bbox.min, (-1, -1, -1), 5)
        self.assertAlmostEqual(bbox.max, (1, 1, 1), 5)

    def test_project2(self):
        target = Cylinder(1, 10).faces().filter_by(GeomType.PLANE, reverse=True)[0]
        square = Wire.make_rect(1, 1, Plane.YZ).locate(Location((10, 0, 0)))
        projections: list[Wire] = square.project(
            target, direction=(-1, 0, 0), closest=False
        )
        self.assertEqual(len(projections), 2)

    def test_is_forward(self):
        plate = Box(10, 10, 1) - Cylinder(1, 1)
        hole_edges = plate.edges().filter_by(GeomType.CIRCLE)
        self.assertTrue(hole_edges.sort_by(Axis.Z)[-1].is_forward)
        self.assertFalse(hole_edges.sort_by(Axis.Z)[0].is_forward)

    def test_offset_2d(self):
        base_wire = Wire.make_polygon([(0, 0), (1, 0), (1, 1)], close=False)
        corner = base_wire.vertices().group_by(Axis.Y)[0].sort_by(Axis.X)[-1]
        base_wire = base_wire.fillet_2d(0.4, [corner])
        offset_wire = base_wire.offset_2d(0.1, side=Side.LEFT)
        self.assertTrue(offset_wire.is_closed)
        self.assertEqual(len(offset_wire.edges().filter_by(GeomType.LINE)), 6)
        self.assertEqual(len(offset_wire.edges().filter_by(GeomType.CIRCLE)), 2)
        offset_wire_right = base_wire.offset_2d(0.1, side=Side.RIGHT)
        self.assertAlmostEqual(
            offset_wire_right.edges()
            .filter_by(GeomType.CIRCLE)
            .sort_by(SortBy.RADIUS)[-1]
            .radius,
            0.5,
            4,
        )
        h_perimeter = Compound.make_text("h", font_size=10).wire()
        with self.assertRaises(RuntimeError):
            h_perimeter.offset_2d(-1)

        # Test for returned Edge - can't find a way to do this
        # base_edge = Edge.make_circle(10, start_angle=40, end_angle=50)
        # self.assertTrue(isinstance(offset_edge, Edge))
        # offset_edge = base_edge.offset_2d(2, side=Side.RIGHT, closed=False)
        # self.assertTrue(offset_edge.geom_type == GeomType.CIRCLE)
        # self.assertAlmostEqual(offset_edge.radius, 12, 5)
        # base_edge = Edge.make_line((0, 1), (1, 10))
        # offset_edge = base_edge.offset_2d(2, side=Side.RIGHT, closed=False)
        # self.assertTrue(isinstance(offset_edge, Edge))
        # self.assertTrue(offset_edge.geom_type == GeomType.LINE)
        # self.assertAlmostEqual(offset_edge.position_at(0).X, 3)

    def test_common_plane(self):
        # Straight and circular lines
        l = Edge.make_line((0, 0, 0), (5, 0, 0))
        c = Edge.make_circle(2, Plane.XZ, -90, 90)
        common = l.common_plane(c)
        self.assertAlmostEqual(common.z_dir.X, 0, 5)
        self.assertAlmostEqual(abs(common.z_dir.Y), 1, 5)  # the direction isn't known
        self.assertAlmostEqual(common.z_dir.Z, 0, 5)

        # Co-axial straight lines
        l1 = Edge.make_line((0, 0), (1, 1))
        l2 = Edge.make_line((0.25, 0.25), (0.75, 0.75))
        common = l1.common_plane(l2)
        # the z_dir isn't know
        self.assertAlmostEqual(common.x_dir.Z, 0, 5)

        # Parallel lines
        l1 = Edge.make_line((0, 0), (1, 0))
        l2 = Edge.make_line((0, 1), (1, 1))
        common = l1.common_plane(l2)
        self.assertAlmostEqual(common.z_dir.X, 0, 5)
        self.assertAlmostEqual(common.z_dir.Y, 0, 5)
        self.assertAlmostEqual(abs(common.z_dir.Z), 1, 5)  # the direction isn't known

        # Many lines
        common = Edge.common_plane(*Wire.make_rect(10, 10).edges())
        self.assertAlmostEqual(common.z_dir.X, 0, 5)
        self.assertAlmostEqual(common.z_dir.Y, 0, 5)
        self.assertAlmostEqual(abs(common.z_dir.Z), 1, 5)  # the direction isn't known

        # Wire and Edges
        c = Wire.make_circle(1, Plane.YZ)
        lines = Wire.make_rect(2, 2, Plane.YZ).edges()
        common = c.common_plane(*lines)
        self.assertAlmostEqual(abs(common.z_dir.X), 1, 5)  # the direction isn't known
        self.assertAlmostEqual(common.z_dir.Y, 0, 5)
        self.assertAlmostEqual(common.z_dir.Z, 0, 5)

    def test_edge_volume(self):
        edge = Edge.make_line((0, 0), (1, 1))
        self.assertAlmostEqual(edge.volume, 0, 5)

    def test_wire_volume(self):
        wire = Wire.make_rect(1, 1)
        self.assertAlmostEqual(wire.volume, 0, 5)


if __name__ == "__main__":
    unittest.main()
