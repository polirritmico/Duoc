#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Grade:
    def __init__(
        self,
        name: str,
        weight: float = 1.0,
        grades: "Grade | list[Grade] | None" = None,
    ):
        self.name = name
        self.weight = weight
        self.score: float | None = None
        if isinstance(grades, Grade):
            self.grades = [grades]
        else:
            self.grades = grades

    def set_score(self, score: float) -> None:
        self.score: float = score

    def get(self, name: str) -> "Grade":
        if self.name == name:
            return self
        if not self.grades:
            return
        for grade in self.grades:
            match = grade.get(name)
            if match:
                return match

    def calculate_score(self) -> float:
        if not self.grades or self.weight == 1:
            return self.score

        sum_of_weights = 0
        score = 0
        for grade in self.grades:
            score += grade.score * grade.weight
            sum_of_weights += grade.weight

        if sum_of_weights != 1:
            raise ValueError("Sum of weights is not 100%")

        return score


class Course:
    def __init__(self, course_name: str, grades: Grade):
        if not course_name:
            raise ValueError("The course name could not be empty")
        if not grades:
            raise ValueError("The course grades could not be None")

        self.name: str = course_name
        self.grades: Grade = grades

    def get_quiz(self, name: str) -> Grade | None:
        if not name:
            raise ValueError("The quiz name should not be empty")

        match = self.grades.get(name)
        if match:
            return match

        raise ValueError(f"Quiz '{name}' not found")

    def calculate_score(self) -> float:
        score = self.grades.calculate_score()
        return score
