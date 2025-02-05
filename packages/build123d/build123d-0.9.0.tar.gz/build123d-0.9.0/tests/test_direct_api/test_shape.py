"""
build123d imports

name: test_shape.py
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
import unittest
from random import uniform
from unittest.mock import patch

import numpy as np
from build123d.build_enums import CenterOf, Keep
from build123d.geometry import (
    Axis,
    Color,
    Location,
    Matrix,
    Plane,
    Pos,
    Rotation,
    Vector,
)
from build123d.objects_part import Box, Cylinder
from build123d.objects_sketch import Circle
from build123d.operations_part import extrude
from build123d.topology import (
    Compound,
    Edge,
    Face,
    Shape,
    ShapeList,
    Shell,
    Solid,
    Vertex,
    Wire,
)


class AlwaysEqual:
    def __eq__(self, other):
        return True


class TestShape(unittest.TestCase):
    """Misc Shape tests"""

    def test_mirror(self):
        box_bb = Solid.make_box(1, 1, 1).mirror(Plane.XZ).bounding_box()
        self.assertAlmostEqual(box_bb.min.X, 0, 5)
        self.assertAlmostEqual(box_bb.max.X, 1, 5)
        self.assertAlmostEqual(box_bb.min.Y, -1, 5)
        self.assertAlmostEqual(box_bb.max.Y, 0, 5)

        box_bb = Solid.make_box(1, 1, 1).mirror().bounding_box()
        self.assertAlmostEqual(box_bb.min.Z, -1, 5)
        self.assertAlmostEqual(box_bb.max.Z, 0, 5)

    def test_compute_mass(self):
        with self.assertRaises(NotImplementedError):
            Shape.compute_mass(Vertex())

    def test_combined_center(self):
        objs = [Solid.make_box(1, 1, 1, Plane((x, 0, 0))) for x in [-2, 1]]
        self.assertAlmostEqual(
            Shape.combined_center(objs, center_of=CenterOf.MASS),
            (0, 0.5, 0.5),
            5,
        )

        objs = [Solid.make_sphere(1, Plane((x, 0, 0))) for x in [-2, 1]]
        self.assertAlmostEqual(
            Shape.combined_center(objs, center_of=CenterOf.BOUNDING_BOX),
            (-0.5, 0, 0),
            5,
        )
        with self.assertRaises(ValueError):
            Shape.combined_center(objs, center_of=CenterOf.GEOMETRY)

    def test_shape_type(self):
        self.assertEqual(Vertex().shape_type(), "Vertex")

    def test_scale(self):
        self.assertAlmostEqual(Solid.make_box(1, 1, 1).scale(2).volume, 2**3, 5)

    def test_fuse(self):
        box1 = Solid.make_box(1, 1, 1)
        box2 = Solid.make_box(1, 1, 1, Plane((1, 0, 0)))
        combined = box1.fuse(box2, glue=True)
        self.assertTrue(combined.is_valid())
        self.assertAlmostEqual(combined.volume, 2, 5)
        fuzzy = box1.fuse(box2, tol=1e-6)
        self.assertTrue(fuzzy.is_valid())
        self.assertAlmostEqual(fuzzy.volume, 2, 5)

    def test_faces_intersected_by_axis(self):
        box = Solid.make_box(1, 1, 1, Plane((0, 0, 1)))
        intersected_faces = box.faces_intersected_by_axis(Axis.Z)
        self.assertTrue(box.faces().sort_by(sort_by=Axis.Z)[0] in intersected_faces)
        self.assertTrue(box.faces().sort_by(sort_by=Axis.Z)[-1] in intersected_faces)

    def test_split(self):
        shape = Box(1, 1, 1) - Pos((0, 0, -0.25)) * Box(1, 0.5, 0.5)
        split_shape = shape.split(Plane.XY, keep=Keep.BOTTOM)
        self.assertTrue(isinstance(split_shape, list))
        self.assertEqual(len(split_shape), 2)
        self.assertAlmostEqual(split_shape[0].volume + split_shape[1].volume, 0.25, 5)
        split_shape = shape.split(Plane.XY, keep=Keep.TOP)
        self.assertEqual(len(split_shape.solids()), 1)
        self.assertTrue(isinstance(split_shape, Solid))
        self.assertAlmostEqual(split_shape.volume, 0.5, 5)

        s = Solid.make_cone(1, 0.5, 2, Plane.YZ.offset(10))
        tool = Solid.make_sphere(11).rotate(Axis.Z, 90).face()
        s2 = s.split(tool, keep=Keep.TOP)
        self.assertLess(s2.volume, s.volume)
        self.assertGreater(s2.volume, 0.0)

    def test_split_by_non_planar_face(self):
        box = Solid.make_box(1, 1, 1)
        tool = Circle(1).wire()
        tool_shell: Shell = Shell.extrude(tool, Vector(0, 0, 1))
        top, bottom = box.split(tool_shell, keep=Keep.BOTH)

        self.assertFalse(top is None)
        self.assertFalse(bottom is None)
        self.assertGreater(top.volume, bottom.volume)

    def test_split_by_shell(self):
        box = Solid.make_box(5, 5, 1)
        tool = Wire.make_rect(4, 4)
        tool_shell: Shell = Shell.extrude(tool, Vector(0, 0, 1))
        split = box.split(tool_shell, keep=Keep.TOP)
        inner_vol = 2 * 2
        outer_vol = 5 * 5
        self.assertAlmostEqual(split.volume, outer_vol - inner_vol)

    def test_split_keep_all(self):
        shape = Box(1, 1, 1)
        split_shape = shape.split(Plane.XY, keep=Keep.ALL)
        self.assertTrue(isinstance(split_shape, ShapeList))
        self.assertEqual(len(split_shape), 2)

    def test_split_edge_by_shell(self):
        edge = Edge.make_line((-5, 0, 0), (5, 0, 0))
        tool = Wire.make_rect(4, 4)
        tool_shell: Shell = Shell.extrude(tool, Vector(0, 0, 1))
        top = edge.split(tool_shell, keep=Keep.TOP)
        self.assertEqual(len(top), 2)
        self.assertAlmostEqual(top[0].length, 3, 5)

    def test_split_return_none(self):
        shape = Box(1, 1, 1) - Pos((0, 0, -0.25)) * Box(1, 0.5, 0.5)
        split_shape = shape.split(Plane.XY, keep=Keep.INSIDE)
        self.assertIsNone(split_shape)

    def test_split_by_perimeter(self):
        # Test 0 - extract a spherical cap
        target0 = Solid.make_sphere(10).rotate(Axis.Z, 90)
        circle = Plane.YZ.offset(15) * Circle(5).face()
        circle_projected = circle.project_to_shape(target0, (-1, 0, 0))[0]
        circle_outerwire = circle_projected.edge()
        inside0, outside0 = target0.split_by_perimeter(circle_outerwire, Keep.BOTH)
        self.assertLess(inside0.area, outside0.area)

        # Test 1 - extract ring of a sphere
        ring = Pos(Z=15) * (Circle(5) - Circle(3)).face()
        ring_projected = ring.project_to_shape(target0, (0, 0, -1))[0]
        ring_outerwire = ring_projected.outer_wire()
        inside1, outside1 = target0.split_by_perimeter(ring_outerwire, Keep.BOTH)
        if isinstance(inside1, list):
            inside1 = Compound(inside1)
        if isinstance(outside1, list):
            outside1 = Compound(outside1)
        self.assertLess(inside1.area, outside1.area)
        self.assertEqual(len(outside1.faces()), 2)

        # Test 2 - extract multiple faces
        target2 = Box(1, 10, 10)
        square = Face.make_rect(3, 3, Plane((12, 0, 0), z_dir=(1, 0, 0)))
        square_projected = square.project_to_shape(target2, (-1, 0, 0))[0]
        outside2 = target2.split_by_perimeter(
            square_projected.outer_wire(), Keep.OUTSIDE
        )
        self.assertTrue(isinstance(outside2, Shell))
        inside2 = target2.split_by_perimeter(square_projected.outer_wire(), Keep.INSIDE)
        self.assertTrue(isinstance(inside2, Face))

        # Test 4 - invalid inputs
        with self.assertRaises(ValueError):
            _, _ = target2.split_by_perimeter(Edge.make_line((0, 0), (1, 0)), Keep.BOTH)

        with self.assertRaises(ValueError):
            _, _ = target2.split_by_perimeter(Edge.make_circle(1), Keep.TOP)

    def test_distance(self):
        sphere1 = Solid.make_sphere(1, Plane((-5, 0, 0)))
        sphere2 = Solid.make_sphere(1, Plane((5, 0, 0)))
        self.assertAlmostEqual(sphere1.distance(sphere2), 8, 5)

    def test_distances(self):
        sphere1 = Solid.make_sphere(1, Plane((-5, 0, 0)))
        sphere2 = Solid.make_sphere(1, Plane((5, 0, 0)))
        sphere3 = Solid.make_sphere(1, Plane((-5, 0, 5)))
        distances = [8, 3]
        for i, distance in enumerate(sphere1.distances(sphere2, sphere3)):
            self.assertAlmostEqual(distances[i], distance, 5)

    def test_max_fillet(self):
        test_solids = [Solid.make_box(10, 8, 2), Solid.make_cone(5, 3, 8)]
        max_values = [0.96, 3.84]
        for i, test_object in enumerate(test_solids):
            with self.subTest("solids" + str(i)):
                max = test_object.max_fillet(test_object.edges())
                self.assertAlmostEqual(max, max_values[i], 2)
        with self.assertRaises(RuntimeError):
            test_solids[0].max_fillet(
                test_solids[0].edges(), tolerance=1e-6, max_iterations=1
            )
        with self.assertRaises(ValueError):
            box = Solid.make_box(1, 1, 1)
            box.fillet(0.75, box.edges())
            # invalid_object = box.fillet(0.75, box.edges())
            # invalid_object.max_fillet(invalid_object.edges())

    @patch.object(Shape, "is_valid", return_value=False)
    def test_max_fillet_invalid_shape_raises_error(self, mock_is_valid):
        box = Solid.make_box(1, 1, 1)

        # Assert that ValueError is raised
        with self.assertRaises(ValueError) as max_fillet_context:
            max = box.max_fillet(box.edges())

        # Check the error message
        self.assertEqual(str(max_fillet_context.exception), "Invalid Shape")

        # Verify is_valid was called
        mock_is_valid.assert_called_once()

    def test_locate_bb(self):
        bounding_box = Solid.make_cone(1, 2, 1).bounding_box()
        relocated_bounding_box = Plane.XZ.from_local_coords(bounding_box)
        self.assertAlmostEqual(relocated_bounding_box.min.X, -2, 5)
        self.assertAlmostEqual(relocated_bounding_box.max.X, 2, 5)
        self.assertAlmostEqual(relocated_bounding_box.min.Y, 0, 5)
        self.assertAlmostEqual(relocated_bounding_box.max.Y, -1, 5)
        self.assertAlmostEqual(relocated_bounding_box.min.Z, -2, 5)
        self.assertAlmostEqual(relocated_bounding_box.max.Z, 2, 5)

    def test_is_equal(self):
        box = Solid.make_box(1, 1, 1)
        self.assertTrue(box.is_equal(box))

    def test_equal(self):
        box = Solid.make_box(1, 1, 1)
        self.assertEqual(box, box)
        self.assertEqual(box, AlwaysEqual())

    def test_not_equal(self):
        box = Solid.make_box(1, 1, 1)
        diff = Solid.make_box(1, 2, 3)
        self.assertNotEqual(box, diff)
        self.assertNotEqual(box, object())

    def test_tessellate(self):
        box123 = Solid.make_box(1, 2, 3)
        verts, triangles = box123.tessellate(1e-6)
        self.assertEqual(len(verts), 24)
        self.assertEqual(len(triangles), 12)

    def test_transformed(self):
        """Validate that transformed works the same as changing location"""
        rotation = (uniform(0, 360), uniform(0, 360), uniform(0, 360))
        offset = (uniform(0, 50), uniform(0, 50), uniform(0, 50))
        shape = Solid.make_box(1, 1, 1).transformed(rotation, offset)
        predicted_location = Location(offset) * Rotation(*rotation)
        located_shape = Solid.make_box(1, 1, 1).locate(predicted_location)
        intersect = shape.intersect(located_shape)
        self.assertAlmostEqual(intersect.volume, 1, 5)

    def test_position_and_orientation(self):
        box = Solid.make_box(1, 1, 1).locate(Location((1, 2, 3), (10, 20, 30)))
        self.assertAlmostEqual(box.position, (1, 2, 3), 5)
        self.assertAlmostEqual(box.orientation, (10, 20, 30), 5)

    def test_distance_to_with_closest_points(self):
        s0 = Solid.make_sphere(1).locate(Location((0, 2.1, 0)))
        s1 = Solid.make_sphere(1)
        distance, pnt0, pnt1 = s0.distance_to_with_closest_points(s1)
        self.assertAlmostEqual(distance, 0.1, 5)
        self.assertAlmostEqual(pnt0, (0, 1.1, 0), 5)
        self.assertAlmostEqual(pnt1, (0, 1, 0), 5)

    def test_closest_points(self):
        c0 = Edge.make_circle(1).locate(Location((0, 2.1, 0)))
        c1 = Edge.make_circle(1)
        closest = c0.closest_points(c1)
        self.assertAlmostEqual(closest[0], c0.position_at(0.75).to_tuple(), 5)
        self.assertAlmostEqual(closest[1], c1.position_at(0.25).to_tuple(), 5)

    def test_distance_to(self):
        c0 = Edge.make_circle(1).locate(Location((0, 2.1, 0)))
        c1 = Edge.make_circle(1)
        distance = c0.distance_to(c1)
        self.assertAlmostEqual(distance, 0.1, 5)

    def test_intersection(self):
        box = Solid.make_box(1, 1, 1)
        intersections = (
            box.intersect(Axis((0.5, 0.5, 4), (0, 0, -1))).vertices().sort_by(Axis.Z)
        )
        self.assertAlmostEqual(Vector(intersections[0]), (0.5, 0.5, 0), 5)
        self.assertAlmostEqual(Vector(intersections[1]), (0.5, 0.5, 1), 5)

    def test_clean_error(self):
        """Note that this test is here to alert build123d to changes in bad OCCT clean behavior
        with spheres or hemispheres. The extra edge in a sphere seems to be the cause of this.
        """
        sphere = Solid.make_sphere(1)
        divider = Solid.make_box(0.1, 3, 3, Plane(origin=(-0.05, -1.5, -1.5)))
        positive_half, negative_half = (s.clean() for s in sphere.cut(divider).solids())
        self.assertGreater(abs(positive_half.volume - negative_half.volume), 0, 1)

    def test_clean_empty(self):
        obj = Solid()
        self.assertIs(obj, obj.clean())

    def test_relocate(self):
        box = Solid.make_box(10, 10, 10).move(Location((20, -5, -5)))
        cylinder = Solid.make_cylinder(2, 50).move(Location((0, 0, 0), (0, 90, 0)))

        box_with_hole = box.cut(cylinder)
        box_with_hole.relocate(box.location)

        self.assertEqual(box.location, box_with_hole.location)

        bbox1 = box.bounding_box()
        bbox2 = box_with_hole.bounding_box()
        self.assertAlmostEqual(bbox1.min, bbox2.min, 5)
        self.assertAlmostEqual(bbox1.max, bbox2.max, 5)

    def test_project_to_viewport(self):
        # Basic test
        box = Solid.make_box(10, 10, 10)
        visible, hidden = box.project_to_viewport((-20, 20, 20))
        self.assertEqual(len(visible), 9)
        self.assertEqual(len(hidden), 3)

        # Contour edges
        cyl = Solid.make_cylinder(2, 10)
        visible, hidden = cyl.project_to_viewport((-20, 20, 20))
        # Note that some edges are broken into two
        self.assertEqual(len(visible), 6)
        self.assertEqual(len(hidden), 2)

        # Hidden contour edges
        hole = box - cyl
        visible, hidden = hole.project_to_viewport((-20, 20, 20))
        self.assertEqual(len(visible), 13)
        self.assertEqual(len(hidden), 6)

        # Outline edges
        sphere = Solid.make_sphere(5)
        visible, hidden = sphere.project_to_viewport((-20, 20, 20))
        self.assertEqual(len(visible), 1)
        self.assertEqual(len(hidden), 0)

    def test_vertex(self):
        v = Edge.make_circle(1).vertex()
        self.assertTrue(isinstance(v, Vertex))
        with self.assertWarns(UserWarning):
            Wire.make_rect(1, 1).vertex()

    def test_edge(self):
        e = Edge.make_circle(1).edge()
        self.assertTrue(isinstance(e, Edge))
        with self.assertWarns(UserWarning):
            Wire.make_rect(1, 1).edge()

    def test_wire(self):
        w = Wire.make_circle(1).wire()
        self.assertTrue(isinstance(w, Wire))
        with self.assertWarns(UserWarning):
            Solid.make_box(1, 1, 1).wire()

    def test_compound(self):
        c = Compound.make_text("hello", 10)
        self.assertTrue(isinstance(c, Compound))
        c2 = Compound.make_text("world", 10)
        with self.assertWarns(UserWarning):
            Compound(children=[c, c2]).compound()

    def test_face(self):
        f = Face.make_rect(1, 1)
        self.assertTrue(isinstance(f, Face))
        with self.assertWarns(UserWarning):
            Solid.make_box(1, 1, 1).face()

    def test_shell(self):
        s = Solid.make_sphere(1).shell()
        self.assertTrue(isinstance(s, Shell))
        with self.assertWarns(UserWarning):
            extrude(Compound.make_text("two", 10), amount=5).shell()

    def test_solid(self):
        s = Solid.make_sphere(1).solid()
        self.assertTrue(isinstance(s, Solid))
        with self.assertWarns(UserWarning):
            Compound(Solid.make_sphere(1).split(Plane.XY, keep=Keep.BOTH)).solid()

    def test_manifold(self):
        self.assertTrue(Solid.make_box(1, 1, 1).is_manifold)
        self.assertTrue(Solid.make_box(1, 1, 1).shell().is_manifold)
        self.assertFalse(
            Solid.make_box(1, 1, 1)
            .shell()
            .cut(Solid.make_box(0.5, 0.5, 0.5))
            .is_manifold
        )
        self.assertTrue(
            Compound(
                children=[Solid.make_box(1, 1, 1), Solid.make_cylinder(1, 1)]
            ).is_manifold
        )

    def test_inherit_color(self):
        # Create some objects and assign colors to them
        b = Box(1, 1, 1).locate(Pos(2, 2, 0))
        b.color = Color("blue")  # Blue
        c = Cylinder(1, 1).locate(Pos(-2, 2, 0))
        a = Compound(children=[b, c])
        a.color = Color(0, 1, 0)
        # Check that assigned colors stay and iheritance works
        np.testing.assert_allclose(tuple(a.color), (0, 1, 0, 1), 1e-5)
        np.testing.assert_allclose(tuple(b.color), (0, 0, 1, 1), 1e-5)

    def test_ocp_section(self):
        # Vertex
        verts, edges = Vertex(1, 2, 0)._ocp_section(Vertex(1, 2, 0))
        self.assertListEqual(verts, [])  # ?
        self.assertListEqual(edges, [])

        verts, edges = Vertex(1, 2, 0)._ocp_section(Edge.make_line((0, 0), (2, 4)))
        self.assertListEqual(verts, [])  # ?
        self.assertListEqual(edges, [])

        verts, edges = Vertex(1, 2, 0)._ocp_section(Face.make_rect(5, 5))
        np.testing.assert_allclose(tuple(verts[0]), (1, 2, 0), 1e-5)
        self.assertListEqual(edges, [])

        verts, edges = Vertex(1, 2, 0)._ocp_section(Face.make_plane(Plane.XY))
        np.testing.assert_allclose(tuple(verts[0]), (1, 2, 0), 1e-5)
        self.assertListEqual(edges, [])

        # spline = Spline((-10, 10, -10), (-10, -5, -5), (20, 0, 5))
        # cylinder = Pos(Z=-10) * extrude(Circle(5), 20)
        # cylinder2 = (Rot((0, 90, 0)) * cylinder).face()
        # pln = Plane.XY
        # box1 = Box(10, 10, 10, align=(Align.CENTER, Align.CENTER, Align.MIN))
        # box2 = Pos(Z=-10) * box1

        # # vertices, edges = ocp_section(spline, Face.make_rect(1e6, 1e6, pln))
        # vertices1, edges1 = spline.ocp_section(Face.make_plane(pln))
        # print(vertices1, edges1)

        # vertices2, edges2 = cylinder.ocp_section(Face.make_plane(pln))
        # print(vertices2, edges2)

        # vertices3, edges3 = cylinder2.ocp_section(Face.make_plane(pln))
        # print(vertices3, edges3)

        # # vertices4, edges4 = cylinder2.ocp_section(cylinder)

        # vertices5, edges5 = box1.ocp_section(Face.make_plane(pln))
        # print(vertices5, edges5)

        # vertices6, edges6 = box1.ocp_section(box2.faces().sort_by(Axis.Z)[-1])

    def test_copy_attributes_to(self):
        box = Box(1, 1, 1)
        box2 = Box(10, 10, 10)
        box.label = "box"
        box.color = Color("Red")
        box.children = [Box(1, 1, 1), Box(2, 2, 2)]
        box.topo_parent = box2

        blank = Compound()
        box.copy_attributes_to(blank)
        self.assertEqual(blank.label, "box")
        self.assertTrue(all(c1 == c2 for c1, c2 in zip(blank.color, Color("Red"))))
        self.assertTrue(all(c1 == c2 for c1, c2 in zip(blank.children, box.children)))
        self.assertEqual(blank.topo_parent, box2)

    def test_empty_shape(self):
        empty = Solid()
        box = Solid.make_box(1, 1, 1)
        self.assertIsNone(empty.location)
        self.assertIsNone(empty.position)
        self.assertIsNone(empty.orientation)
        self.assertFalse(empty.is_manifold)
        with self.assertRaises(ValueError):
            empty.geom_type
        self.assertIs(empty, empty.fix())
        self.assertEqual(hash(empty), 0)
        self.assertFalse(empty.is_same(Solid()))
        self.assertFalse(empty.is_equal(Solid()))
        self.assertTrue(empty.is_valid())
        empty_bbox = empty.bounding_box()
        self.assertEqual(tuple(empty_bbox.size), (0, 0, 0))
        self.assertIs(empty, empty.mirror(Plane.XY))
        self.assertEqual(Shape.compute_mass(empty), 0)
        self.assertEqual(empty.entities("Face"), [])
        self.assertEqual(empty.area, 0)
        self.assertIs(empty, empty.rotate(Axis.Z, 90))
        translate_matrix = [
            [1.0, 0.0, 0.0, 1.0],
            [0.0, 1.0, 0.0, 2.0],
            [0.0, 0.0, 1.0, 3.0],
            [0.0, 0.0, 0.0, 1.0],
        ]
        self.assertIs(empty, empty.transform_shape(Matrix(translate_matrix)))
        self.assertIs(empty, empty.transform_geometry(Matrix(translate_matrix)))
        with self.assertRaises(ValueError):
            empty.locate(Location())
        empty_loc = Location()
        empty_loc.wrapped = None
        with self.assertRaises(ValueError):
            box.locate(empty_loc)
        with self.assertRaises(ValueError):
            empty.located(Location())
        with self.assertRaises(ValueError):
            box.located(empty_loc)
        with self.assertRaises(ValueError):
            empty.move(Location())
        with self.assertRaises(ValueError):
            box.move(empty_loc)
        with self.assertRaises(ValueError):
            empty.moved(Location())
        with self.assertRaises(ValueError):
            box.moved(empty_loc)
        with self.assertRaises(ValueError):
            empty.relocate(Location())
        with self.assertRaises(ValueError):
            box.relocate(empty_loc)
        with self.assertRaises(ValueError):
            empty.distance_to(Vector(1, 1, 1))
        with self.assertRaises(ValueError):
            empty.distance_to_with_closest_points(Vector(1, 1, 1))
        with self.assertRaises(ValueError):
            empty.distance_to(Vector(1, 1, 1))
        with self.assertRaises(ValueError):
            box.intersect(empty_loc)
        self.assertEqual(empty._ocp_section(Vertex(1, 1, 1)), ([], []))
        self.assertEqual(empty.faces_intersected_by_axis(Axis.Z), ShapeList())
        with self.assertRaises(ValueError):
            empty.split_by_perimeter(Circle(1).wire())
        with self.assertRaises(ValueError):
            empty.distance(Vertex(1, 1, 1))
        with self.assertRaises(ValueError):
            list(empty.distances(Vertex(0, 0, 0), Vertex(1, 1, 1)))
        with self.assertRaises(ValueError):
            list(box.distances(empty, Vertex(1, 1, 1)))
        with self.assertRaises(ValueError):
            empty.mesh(0.001)
        with self.assertRaises(ValueError):
            empty.tessellate(0.001)
        with self.assertRaises(ValueError):
            empty.to_splines()
        empty_axis = Axis((0, 0, 0), (1, 0, 0))
        empty_axis.wrapped = None
        with self.assertRaises(ValueError):
            box.vertices().group_by(empty_axis)
        empty_wire = Wire()
        with self.assertRaises(ValueError):
            box.vertices().group_by(empty_wire)
        with self.assertRaises(ValueError):
            box.vertices().sort_by(empty_axis)
        with self.assertRaises(ValueError):
            box.vertices().sort_by(empty_wire)

    def test_empty_selectors(self):
        self.assertEqual(Vertex(1, 1, 1).edges(), ShapeList())
        self.assertEqual(Vertex(1, 1, 1).wires(), ShapeList())
        self.assertEqual(Vertex(1, 1, 1).faces(), ShapeList())
        self.assertEqual(Vertex(1, 1, 1).shells(), ShapeList())
        self.assertEqual(Vertex(1, 1, 1).solids(), ShapeList())
        self.assertEqual(Vertex(1, 1, 1).compounds(), ShapeList())
        self.assertIsNone(Vertex(1, 1, 1).edge())
        self.assertIsNone(Vertex(1, 1, 1).wire())
        self.assertIsNone(Vertex(1, 1, 1).face())
        self.assertIsNone(Vertex(1, 1, 1).shell())
        self.assertIsNone(Vertex(1, 1, 1).solid())
        self.assertIsNone(Vertex(1, 1, 1).compound())


if __name__ == "__main__":
    unittest.main()
