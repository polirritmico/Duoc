#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from .course import Course, Grade


def test_get_grade_single() -> None:
    case = "Quiz A"

    quiz_a = Grade("Quiz A", 0.55)
    course_quizzes = Grade("Quizzes", 1, [quiz_a])
    course = Course("Course", course_quizzes)
    expected = quiz_a

    output = course.get_quiz(case)
    assert expected == output


def test_get_grade_simple() -> None:
    case = "Quiz B"

    quiz_a = Grade("Quiz A", 0.55)
    quiz_b = Grade("Quiz B", 0.45)
    course_quizzes = Grade("Quizzes", 1, [quiz_a, quiz_b])
    course = Course("Course", course_quizzes)
    expected = quiz_b

    output = course.get_quiz(case)
    assert expected == output


def test_get_grade_multiple() -> None:
    case_a = "Quiz A"
    case_b = "Quiz B"
    case_c = "Quiz C"
    case_ab = "Quiz AB"

    quiz_a = Grade(case_a, 0.55)
    quiz_b = Grade(case_b, 0.45)
    quiz_ab = Grade(case_ab, 0.65, [quiz_a, quiz_b])
    quiz_c = Grade(case_c, 0.45)

    expected_a = quiz_a
    expected_b = quiz_b
    expected_c = quiz_c
    expected_ab = quiz_ab

    course_quizzes = Grade("Quizzes", 1, [quiz_ab, quiz_c])
    course = Course("Course", course_quizzes)
    output_a = course.get_quiz(case_a)
    output_b = course.get_quiz(case_b)
    output_c = course.get_quiz(case_c)
    output_ab = course.get_quiz(case_ab)

    assert expected_a == output_a
    assert expected_b == output_b
    assert expected_c == output_c
    assert expected_ab == output_ab


def test_all_grades_have_been_scored() -> None:
    quiz_a = Grade("Quiz A", 0.5)
    quiz_b = Grade("Quiz B", 0.5)

    course_quizzes = Grade("Quizzes", 1, [quiz_a, quiz_b])
    course = Course("Course", course_quizzes)
    course.get_quiz("Quiz A").set_score(42)

    assert not course.all_grades_have_been_scored()
    quiz_b.set_score(5)
    assert course.all_grades_have_been_scored()


def test_acceptance_calculate_grade_average() -> None:
    case_quiz1_weight = 0.25
    case_quiz2_weight = 0.35
    case_quiz3_weight = 0.40
    case_quizzes_weigth = 0.6
    case_exam_weight = 0.4

    case_quiz1_grade = 5.3
    case_quiz2_grade = 6.1
    case_quiz3_grade = 4.9
    case_exam_grade = 5.9

    expected_grade_average = 5.612

    math_quiz1 = Grade("First quiz", case_quiz1_weight)
    math_quiz2 = Grade("Second quiz", case_quiz2_weight)
    math_quiz3 = Grade("Third quiz", case_quiz3_weight)
    math_quizzes = Grade(
        "Quizzes Grade", case_quizzes_weigth, [math_quiz1, math_quiz2, math_quiz3]
    )
    math_exam = Grade("Course Exam", case_exam_weight)
    course_grades = Grade("Course Grade", 1, [math_quizzes, math_exam])
    course = Course("Math Course", course_grades)

    course.get_quiz("First quiz").set_score(case_quiz1_grade)
    course.get_quiz("Second quiz").set_score(case_quiz2_grade)
    course.get_quiz("Third quiz").set_score(case_quiz3_grade)
    course.get_quiz("Course Exam").set_score(case_exam_grade)
    output_grade = course.calculate_score()

    assert expected_grade_average == output_grade
