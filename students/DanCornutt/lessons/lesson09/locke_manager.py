#!/usr/bin/env python3


class BoatError(Exception):
    pass


class Locke():
    """Open and close the lockes"""

    def __init__(self, max_boats):
        """Initialize context manager with maximum number of boats locke
        can handle"""
        self.max_boats = max_boats

    def __enter__(self):
        """Ener the context locke manager"""
        print("Stop Pumps")
        print("Opening Door")
        return self

    def move_boats_through(self, num_boats):
        """Boats attempt to enter, don't let them enter if too many"""
        if num_boats > self.max_boats:
            raise BoatError("Too many boats!")
        print("Closing Doors")
        print("Starting Pumps")
        print("Going thorugh the lock")
        print("Stop Pumps")
        print("Opening Door")

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Closing the doors")
        print("Starting Pumps")
        if exc_type:
            print(f'exc_type: {exc_type}')
            print(f'exc_value: {exc_value}')
            print(f'exc_traceback: {exc_traceback}')


if __name__ == "__main__":
    small_locke = Locke(5)
    large_locke = Locke(10)
    boats = 8


with large_locke
