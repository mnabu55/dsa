from typing import List

from remove_duplicates_from_sorted_array import Solution


def run_case(nums: List[int], expected_length: int, expected_values: List[int]) -> bool:
    nums_copy = nums.copy()
    result_length = Solution().removeDuplicatesFromSortedArray(nums_copy)
    if result_length != expected_length:
        print(
            "FAIL:",
            f"input={nums}",
            f"got_length={result_length}",
            f"got_values={nums_copy[:result_length]}",
            f"expected_length={expected_length}",
            f"expected_values={expected_values}",
        )
        return False
    print(
        "PASS:",
        f"input={nums}",
        f"result_length={result_length}",
        f"result_values={nums_copy[:result_length]}",
    )
    return True


def main() -> None:
    test_cases = [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([1], 1, [1]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
    ]

    failures = 0
    for nums, length, values in test_cases:
        if not run_case(nums, length, values):
            failures += 1

    if failures:
        raise SystemExit(f"{failures} test(s) failed")


if __name__ == "__main__":
    main()
