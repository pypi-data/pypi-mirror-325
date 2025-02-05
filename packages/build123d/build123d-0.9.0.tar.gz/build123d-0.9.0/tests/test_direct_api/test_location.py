"""
build123d imports

name: test_location.py
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

# Always equal to any other object, to test that __eq__ cooperation is working
import copy
import json
import math
import os
import unittest
from random import uniform

import numpy as np
from OCP.gp import (
    gp_Ax1,
    gp_Dir,
    gp_EulerSequence,
    gp_Pnt,
    gp_Quaternion,
    gp_Trsf,
    gp_Vec,
)
from build123d.build_common import GridLocations
from build123d.build_enums import Extrinsic, Intrinsic
from build123d.geometry import Axis, Location, LocationEncoder, Plane, Pos, Vector
from build123d.topology import Edge, Solid, Vertex


class AlwaysEqual:
    def __eq__(self, other):
        return True


class TestLocation(unittest.TestCase):
    def test_location(self):
        loc0 = Location()
        T = loc0.wrapped.Transformation().TranslationPart()
        np.testing.assert_allclose((T.X(), T.Y(), T.Z()), (0, 0, 0), 1e-6)
        angle = math.degrees(
            loc0.wrapped.Transformation().GetRotation().GetRotationAngle()
        )
        self.assertAlmostEqual(0, angle)

        # Tuple
        loc0 = Location((0, 0, 1))

        T = loc0.wrapped.Transformation().TranslationPart()
        np.testing.assert_allclose((T.X(), T.Y(), T.Z()), (0, 0, 1), 1e-6)

        # List
        loc0 = Location([0, 0, 1])

        T = loc0.wrapped.Transformation().TranslationPart()
        np.testing.assert_allclose((T.X(), T.Y(), T.Z()), (0, 0, 1), 1e-6)

        # Vector
        loc1 = Location(Vector(0, 0, 1))

        T = loc1.wrapped.Transformation().TranslationPart()
        np.testing.assert_allclose((T.X(), T.Y(), T.Z()), (0, 0, 1), 1e-6)

        # rotation + translation
        loc2 = Location(Vector(0, 0, 1), Vector(0, 0, 1), 45)

        angle = math.degrees(
            loc2.wrapped.Transformation().GetRotation().GetRotationAngle()
        )
        self.assertAlmostEqual(45, angle)

        # gp_Trsf
        T = gp_Trsf()
        T.SetTranslation(gp_Vec(0, 0, 1))
        loc3 = Location(T)

        self.assertEqual(
            loc1.wrapped.Transformation().TranslationPart().Z(),
            loc3.wrapped.Transformation().TranslationPart().Z(),
        )

        # Test creation from the OCP.gp.gp_Trsf object
        loc4 = Location(gp_Trsf())
        np.testing.assert_allclose(loc4.to_tuple()[0], (0, 0, 0), 1e-7)
        np.testing.assert_allclose(loc4.to_tuple()[1], (0, 0, 0), 1e-7)

        # Test creation from Plane and Vector
        loc4 = Location(Plane.XY, (0, 0, 1))
        np.testing.assert_allclose(loc4.to_tuple()[0], (0, 0, 1), 1e-7)
        np.testing.assert_allclose(loc4.to_tuple()[1], (0, 0, 0), 1e-7)

        # Test composition
        loc4 = Location((0, 0, 0), Vector(0, 0, 1), 15)

        loc5 = loc1 * loc4
        loc6 = loc4 * loc4
        loc7 = loc4**2

        T = loc5.wrapped.Transformation().TranslationPart()
        np.testing.assert_allclose((T.X(), T.Y(), T.Z()), (0, 0, 1), 1e-6)

        angle5 = math.degrees(
            loc5.wrapped.Transformation().GetRotation().GetRotationAngle()
        )
        self.assertAlmostEqual(15, angle5)

        angle6 = math.degrees(
            loc6.wrapped.Transformation().GetRotation().GetRotationAngle()
        )
        self.assertAlmostEqual(30, angle6)

        angle7 = math.degrees(
            loc7.wrapped.Transformation().GetRotation().GetRotationAngle()
        )
        self.assertAlmostEqual(30, angle7)

        # Test error handling on creation
        with self.assertRaises(TypeError):
            Location("xy_plane")

        # Test that the computed rotation matrix and intrinsic euler angles return the same

        about_x = uniform(-2 * math.pi, 2 * math.pi)
        about_y = uniform(-2 * math.pi, 2 * math.pi)
        about_z = uniform(-2 * math.pi, 2 * math.pi)

        rot_x = gp_Trsf()
        rot_x.SetRotation(gp_Ax1(gp_Pnt(0, 0, 0), gp_Dir(1, 0, 0)), about_x)
        rot_y = gp_Trsf()
        rot_y.SetRotation(gp_Ax1(gp_Pnt(0, 0, 0), gp_Dir(0, 1, 0)), about_y)
        rot_z = gp_Trsf()
        rot_z.SetRotation(gp_Ax1(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1)), about_z)
        loc1 = Location(rot_x * rot_y * rot_z)

        q = gp_Quaternion()
        q.SetEulerAngles(
            gp_EulerSequence.gp_Intrinsic_XYZ,
            about_x,
            about_y,
            about_z,
        )
        t = gp_Trsf()
        t.SetRotationPart(q)
        loc2 = Location(t)

        np.testing.assert_allclose(loc1.to_tuple()[0], loc2.to_tuple()[0], 1e-6)
        np.testing.assert_allclose(loc1.to_tuple()[1], loc2.to_tuple()[1], 1e-6)

        loc1 = Location((1, 2), 34)
        np.testing.assert_allclose(loc1.to_tuple()[0], (1, 2, 0), 1e-6)
        np.testing.assert_allclose(loc1.to_tuple()[1], (0, 0, 34), 1e-6)

        rot_angles = (-115.00, 35.00, -135.00)
        loc2 = Location((1, 2, 3), rot_angles)
        np.testing.assert_allclose(loc2.to_tuple()[0], (1, 2, 3), 1e-6)
        np.testing.assert_allclose(loc2.to_tuple()[1], rot_angles, 1e-6)

        loc3 = Location(loc2)
        np.testing.assert_allclose(loc3.to_tuple()[0], (1, 2, 3), 1e-6)
        np.testing.assert_allclose(loc3.to_tuple()[1], rot_angles, 1e-6)

    def test_location_parameters(self):
        loc = Location((10, 20, 30))
        self.assertAlmostEqual(loc.position, (10, 20, 30), 5)

        loc = Location((10, 20, 30), (10, 20, 30))
        self.assertAlmostEqual(loc.position, (10, 20, 30), 5)
        self.assertAlmostEqual(loc.orientation, (10, 20, 30), 5)

        loc = Location((10, 20, 30), (10, 20, 30), Intrinsic.XYZ)
        self.assertAlmostEqual(loc.position, (10, 20, 30), 5)
        self.assertAlmostEqual(loc.orientation, (10, 20, 30), 5)

        loc = Location((10, 20, 30), (30, 20, 10), Extrinsic.ZYX)
        self.assertAlmostEqual(loc.position, (10, 20, 30), 5)
        self.assertAlmostEqual(loc.orientation, (10, 20, 30), 5)

        with self.assertRaises(TypeError):
            Location(x=10)

        with self.assertRaises(TypeError):
            Location((10, 20, 30), (30, 20, 10), (10, 20, 30))

        with self.assertRaises(TypeError):
            Location(Intrinsic.XYZ)

    def test_location_repr_and_str(self):
        self.assertEqual(
            repr(Location()), "(p=(0.00, 0.00, 0.00), o=(-0.00, 0.00, -0.00))"
        )
        self.assertEqual(
            str(Location()),
            "Location: (position=(0.00, 0.00, 0.00), orientation=(-0.00, 0.00, -0.00))",
        )
        loc = Location((1, 2, 3), (33, 45, 67))
        self.assertEqual(
            str(loc),
            "Location: (position=(1.00, 2.00, 3.00), orientation=(33.00, 45.00, 67.00))",
        )

    def test_location_inverted(self):
        loc = Location(Plane.XZ)
        self.assertAlmostEqual(loc.inverse().orientation, (-90, 0, 0), 6)

    def test_set_position(self):
        loc = Location(Plane.XZ)
        loc.position = (1, 2, 3)
        self.assertAlmostEqual(loc.position, (1, 2, 3), 6)
        self.assertAlmostEqual(loc.orientation, (90, 0, 0), 6)

    def test_set_orientation(self):
        loc = Location((1, 2, 3), (90, 0, 0))
        loc.orientation = (-90, 0, 0)
        self.assertAlmostEqual(loc.position, (1, 2, 3), 6)
        self.assertAlmostEqual(loc.orientation, (-90, 0, 0), 6)

    def test_copy(self):
        loc1 = Location((1, 2, 3), (90, 45, 22.5))
        loc2 = copy.copy(loc1)
        loc3 = copy.deepcopy(loc1)
        self.assertAlmostEqual(loc1.position, loc2.position.to_tuple(), 6)
        self.assertAlmostEqual(loc1.orientation, loc2.orientation.to_tuple(), 6)
        self.assertAlmostEqual(loc1.position, loc3.position.to_tuple(), 6)
        self.assertAlmostEqual(loc1.orientation, loc3.orientation.to_tuple(), 6)

    def test_to_axis(self):
        axis = Location((1, 2, 3), (-90, 0, 0)).to_axis()
        self.assertAlmostEqual(axis.position, (1, 2, 3), 6)
        self.assertAlmostEqual(axis.direction, (0, 1, 0), 6)

    def test_equal(self):
        loc = Location((1, 2, 3), (4, 5, 6))
        same = Location((1, 2, 3), (4, 5, 6))

        self.assertEqual(loc, same)
        self.assertEqual(loc, AlwaysEqual())

    def test_not_equal(self):
        loc = Location((1, 2, 3), (40, 50, 60))
        diff_position = Location((3, 2, 1), (40, 50, 60))
        diff_orientation = Location((1, 2, 3), (60, 50, 40))

        self.assertNotEqual(loc, diff_position)
        self.assertNotEqual(loc, diff_orientation)
        self.assertNotEqual(loc, object())

    def test_neg(self):
        loc = Location((1, 2, 3), (0, 35, 127))
        n_loc = -loc
        self.assertAlmostEqual(n_loc.position, (1, 2, 3), 5)
        self.assertAlmostEqual(n_loc.orientation, (180, -35, -127), 5)

    def test_mult_iterable(self):
        locs = Location((1, 2, 0)) * GridLocations(4, 4, 2, 1)
        self.assertAlmostEqual(locs[0].position, (-1, 2, 0), 5)
        self.assertAlmostEqual(locs[1].position, (3, 2, 0), 5)

    def test_as_json(self):
        data_dict = {
            "part1": {
                "joint_one": Location((1, 2, 3), (4, 5, 6)),
                "joint_two": Location((7, 8, 9), (10, 11, 12)),
            },
            "part2": {
                "joint_one": Location((13, 14, 15), (16, 17, 18)),
                "joint_two": Location((19, 20, 21), (22, 23, 24)),
            },
        }

        # Serializing json with custom Location encoder
        json_object = json.dumps(data_dict, indent=4, cls=LocationEncoder)

        # Writing to sample.json
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)

        # Reading from sample.json
        with open("sample.json") as infile:
            read_json = json.load(infile, object_hook=LocationEncoder.location_hook)

        # Validate locations
        for key, value in read_json.items():
            for k, v in value.items():
                if key == "part1" and k == "joint_one":
                    self.assertAlmostEqual(v.position, (1, 2, 3), 5)
                elif key == "part1" and k == "joint_two":
                    self.assertAlmostEqual(v.position, (7, 8, 9), 5)
                elif key == "part2" and k == "joint_one":
                    self.assertAlmostEqual(v.position, (13, 14, 15), 5)
                elif key == "part2" and k == "joint_two":
                    self.assertAlmostEqual(v.position, (19, 20, 21), 5)
                else:
                    self.assertTrue(False)
        os.remove("sample.json")

    def test_intersection(self):
        e = Edge.make_line((0, 0, 0), (1, 1, 1))
        l0 = e.location_at(0)
        l1 = e.location_at(1)
        self.assertIsNone(l0 & l1)
        self.assertEqual(l1 & l1, l1)

        i = l1 & Vector(1, 1, 1)
        self.assertTrue(isinstance(i, Vector))
        self.assertAlmostEqual(i, (1, 1, 1), 5)

        i = l1 & Axis((0.5, 0.5, 0.5), (1, 1, 1))
        self.assertTrue(isinstance(i, Location))
        self.assertEqual(i, l1)

        p = Plane.XY.rotated((45, 0, 0)).shift_origin((1, 0, 0))
        l = Location((1, 0, 0), (1, 0, 0), 45)
        i = l & p
        self.assertTrue(isinstance(i, Location))
        self.assertAlmostEqual(i.position, (1, 0, 0), 5)
        self.assertAlmostEqual(i.orientation, l.orientation, 5)

        b = Solid.make_box(1, 1, 1)
        l = Location((0.5, 0.5, 0.5), (1, 0, 0), 45)
        i = (l & b).vertex()
        self.assertTrue(isinstance(i, Vertex))
        self.assertAlmostEqual(Vector(i), (0.5, 0.5, 0.5), 5)

        e1 = Edge.make_line((0, -1), (2, 1))
        e2 = Edge.make_line((0, 1), (2, -1))
        e3 = Edge.make_line((0, 0), (2, 0))

        i = e1.intersect(e2, e3)
        self.assertTrue(isinstance(i, Vertex))
        self.assertAlmostEqual(Vector(i), (1, 0, 0), 5)

        e4 = Edge.make_line((1, -1), (1, 1))
        e5 = Edge.make_line((2, -1), (2, 1))
        i = e3.intersect(e4, e5)
        self.assertIsNone(i)

        self.assertIsNone(b.intersect(b.moved(Pos(X=10))))

        # Look for common vertices
        e1 = Edge.make_line((0, 0), (1, 0))
        e2 = Edge.make_line((1, 0), (1, 1))
        e3 = Edge.make_line((1, 0), (2, 0))
        i = e1.intersect(e2)
        self.assertEqual(len(i.vertices()), 1)
        self.assertEqual(tuple(i.vertex()), (1, 0, 0))
        i = e1.intersect(e3)
        self.assertEqual(len(i.vertices()), 1)
        self.assertEqual(tuple(i.vertex()), (1, 0, 0))

        # Intersect with plane
        e1 = Edge.make_line((0, 0), (2, 0))
        p1 = Plane.YZ.offset(1)
        i = e1.intersect(p1)
        self.assertEqual(len(i.vertices()), 1)
        self.assertEqual(tuple(i.vertex()), (1, 0, 0))

        e2 = Edge.make_line(p1.origin, p1.origin + 2 * p1.x_dir)
        i = e2.intersect(p1)
        self.assertEqual(len(i.vertices()), 2)
        self.assertEqual(len(i.edges()), 1)
        self.assertAlmostEqual(i.edge().length, 2, 5)

        with self.assertRaises(ValueError):
            e1.intersect("line")

    def test_pos(self):
        with self.assertRaises(TypeError):
            Pos(0, "foo")
        self.assertEqual(Pos(1, 2, 3).position, Vector(1, 2, 3))
        self.assertEqual(Pos((1, 2, 3)).position, Vector(1, 2, 3))
        self.assertEqual(Pos(v=(1, 2, 3)).position, Vector(1, 2, 3))
        self.assertEqual(Pos(X=1, Y=2, Z=3).position, Vector(1, 2, 3))
        self.assertEqual(Pos(Vector(1, 2, 3)).position, Vector(1, 2, 3))
        self.assertEqual(Pos(1, Y=2, Z=3).position, Vector(1, 2, 3))


if __name__ == "__main__":
    unittest.main()
