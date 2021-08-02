from unittest import TestCase
from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("Rob")
        self.student2 = Student("Joe", {"Python": ["note"]})

    def test_init_courses_none(self):
        self.assertEqual("Rob", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_init_with_courses(self):
        self.assertEqual({"Python": ["note"]}, self.student2.courses)

    def test_enroll_course_already_in_courses(self):
        result = self.student2.enroll("Python", ["note2", "note3"], "")
        self.assertEqual({"Python": ["note", "note2", "note3"]}, self.student2.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_course_not_in_courses(self):
        result = self.student.enroll("Java", ["note2", "note3"], "")
        self.assertEqual(["note2", "note3"], self.student.courses["Java"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_course_not_in_courses_with_YES(self):
        result = self.student.enroll("Java", ["note2", "note3"], "Y")
        self.assertEqual(["note2", "note3"], self.student.courses["Java"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_course_not_in_courses_dont_add_notes(self):
        result = self.student.enroll("Java", ["note2", "note3"], "NO")
        self.assertEqual([], self.student.courses["Java"])
        self.assertEqual("Course has been added.", result)

    def test_add_notes(self):
        result = self.student2.add_notes("Python", "note2")
        self.assertEqual(["note", "note2"], self.student2.courses["Python"])
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_expect_exception(self):
        with self.assertRaises(Exception) as msg:
            self.student.add_notes("Python", "note")
        self.assertEqual("Cannot add notes. Course not found.", str(msg.exception))

    def test_leave_course(self):
        result = self.student2.leave_course("Python")
        self.assertEqual({}, self.student2.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_expect_exception(self):
        with self.assertRaises(Exception) as msg:
            self.student.leave_course("Python")
        self.assertEqual("Cannot remove course. Course not found.", str(msg.exception))






