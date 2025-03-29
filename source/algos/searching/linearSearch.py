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


"""
Time Complexity -> O(n)
Best Case O(1) -> first element returns immediate
Worst Case O(n) -> iterating n + n for target
Average Case O(n) -> usually checking half of array n/2 

Space Complexity -> O(1)
in place use and no new structures allocated

"""