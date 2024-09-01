from structs.linked_list import LinkedList
from structs.stack import Stack
from strategy.pattern import DataStructure

class Rubix:
    def __init__(self):
        self.data_structure = None

    def set_data_structure(self, ds: DataStructure):
        self.data_structure = ds

    def add_element(self, element):
        if self.data_structure:
            self.data_structure.add_element(element)

    def remove_element(self, element):
        if self.data_structure:
            self.data_structure.remove_element(element)

    def access_element(self, element):
        if self.data_structure:
            return self.data_structure.access_element(element)
        return None

    def show(self):
        if isinstance(self.data_structure, LinkedList):
            self.data_structure.traverse()
        elif isinstance(self.data_structure, Stack):
            print(self.data_structure.data)


    def binary_search(self, arr, target):
        L, R = 0, len(arr) - 1

        while L <= R:
            mid = (L + R) // 2

            if target > arr[mid]:
                L = mid + 1
            elif target < arr[mid]:
                R = mid - 1
            else:
                return mid
        return -1

    def two_pointer(self, arr):
        l, r = 0, len(arr) - 1

        while l < r:
            print(arr[l], arr[r])
            l += 1
            r -= 1

    def fixed_two_pointer(self, nums, k):
        window = set()
        L = 0

        for R in range(len(nums)):
            if R - L + 1 > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])

        return False

    # Dynamic Programming: Longest Increasing Subsequence (LIS)
    def longest_increasing_subsequence(self, nums):
        if not nums:
            return 0

        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    # Greedy Algorithm: Activity Selection (Interval Scheduling)
    def activity_selection(self, intervals):
        intervals.sort(key=lambda x: x[1])  # Sort by finish time
        last_end = float('-inf')
        count = 0

        for start, end in intervals:
            if start >= last_end:
                count += 1
                last_end = end

        return count

    # Backtracking: Finding all paths between two nodes in a graph
    def find_all_paths(self, graph, start, end):
        def backtrack(current_node, path):
            if current_node == end:
                paths.append(path[:])
                return

            for neighbor in graph.adjacency_list.get(current_node, []):
                if neighbor not in path:
                    path.append(neighbor)
                    backtrack(neighbor, path)
                    path.pop()

        paths = []
        backtrack(start, [start])
        return paths

    def add_problem(self, problem):
        self.queue.enqueue(problem)

    def execute_problems(self):
        while not self.queue.is_empty():
            problem = self.queue.get_front()
            problem()  # Execute the problem
            self.queue.dequeue()


    """def struct_mode(self):
        data_s = input()

        match:
            case "a":
                self.rubix = Array()
    """
