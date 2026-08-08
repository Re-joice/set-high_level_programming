#!/usr/bin/python3
"""Defines the Base class."""

import csv
import json
import turtle


class Base:
    """Base class for all other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation to a file."""
        filename = cls.__name__ + ".json"

        if list_objs is None:
            list_dictionaries = []
        else:
            list_dictionaries = [obj.to_dictionary() for obj in list_objs]

        json_string = cls.to_json_string(list_dictionaries)

        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r") as file:
                json_string = file.read()
        except FileNotFoundError:
            return []

        list_dictionaries = cls.from_json_string(json_string)

        return [cls.create(**dictionary) for dictionary in list_dictionaries]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize objects to a CSV file."""
        filename = cls.__name__ + ".csv"

        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)

            if list_objs is None:
                return

            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([
                        obj.id,
                        obj.width,
                        obj.height,
                        obj.x,
                        obj.y
                    ])
                else:
                    writer.writerow([
                        obj.id,
                        obj.size,
                        obj.x,
                        obj.y
                    ])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize objects from a CSV file."""
        filename = cls.__name__ + ".csv"

        try:
            with open(filename, "r", newline="") as file:
                reader = csv.reader(file)
                instances = []

                for row in reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])
                        }
                    else:
                        dictionary = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])
                        }

                    instances.append(cls.create(**dictionary))

                return instances

        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window and draw all rectangles and squares."""
        screen = turtle.Screen()
        screen.title("Almost a Circle - Shapes")

        pen = turtle.Turtle()
        pen.speed(0)
        pen.penup()

        for rectangle in list_rectangles:
            pen.goto(
                rectangle.x,
                -rectangle.y
            )
            pen.pendown()

            for _ in range(2):
                pen.forward(rectangle.width)
                pen.left(90)
                pen.forward(rectangle.height)
                pen.left(90)

            pen.penup()

        for square in list_squares:
            pen.goto(
                square.x,
                -square.y
            )
            pen.pendown()

            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)

            pen.penup()

        turtle.done()
