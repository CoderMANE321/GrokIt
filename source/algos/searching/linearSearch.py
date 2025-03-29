from typing import List

class linearSearch:
    def __init__(self):
        pass


    def search(self, arr: List, target: int) -> bool:
       #  Search for a target value in an array using linear search."
        for i in arr:
            if i == target:
                return True
        return False