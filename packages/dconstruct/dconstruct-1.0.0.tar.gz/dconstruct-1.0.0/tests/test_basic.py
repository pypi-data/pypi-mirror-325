import unittest
from dataclasses import dataclass
from typing import List

from dconstruct import construct


@dataclass
class Person:
    name: str
    age: int


@dataclass
class NonHumanAnimal:
    name: str
    species: str


@dataclass
class Zoo:
    location: str
    animals: List


def animal_types():
    return dict(Person=Person, NonHumanAnimal=NonHumanAnimal)


def location_types():
    return dict(
        Zoo=lambda location, animal_specs: Zoo(
            location=location,
            animals=[
                construct(animal_types(), spec, name="Default") for spec in animal_specs
            ],
        ),
    )


class TestConstruct(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_basic(self):
        self.assertEqual(
            construct(animal_types(), dict(type="Person", name="Julian", age=30)),
            Person(name="Julian", age=30),
        )

    def test_override(self):
        self.assertEqual(
            construct(animal_types(), dict(type="Person", name="Julian"), age=30),
            Person(name="Julian", age=30),
        )

        self.assertEqual(
            construct(
                animal_types(), dict(type="Person", name="Julian", age=29), age=30
            ),
            Person(name="Julian", age=29),
        )

    def test_nested(self):
        self.assertEqual(
            construct(
                location_types(),
                dict(
                    type="Zoo",
                    location="San Diego",
                    animal_specs=[
                        dict(
                            type="NonHumanAnimal", name="Lion", species="Panthera leo"
                        ),
                        dict(type="NonHumanAnimal", species="Canis lupus"),
                        dict(type="Person", name="Julian", age=30),
                    ],
                ),
            ),
            Zoo(
                location="San Diego",
                animals=[
                    NonHumanAnimal(name="Lion", species="Panthera leo"),
                    NonHumanAnimal(name="Default", species="Canis lupus"),
                    Person(name="Julian", age=30),
                ],
            ),
        )
