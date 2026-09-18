"""
문제: 완주하지 못한 선수
링크: https://school.programmers.co.kr/learn/courses/30/lessons/42576
난이도: Lv.1

이번 주 핵심 문제! 아래 3가지 방식을 전부 구현해보자.
  1) solution_brute_force : 완전탐색 (이중 반복) -> O(n^2)
  2) solution_sort        : 정렬 후 비교          -> O(n log n)
  3) solution_hash        : 해시맵(Counter) 이용   -> O(n)

# 각 함수 위에 시간복잡도를 직접 주석으로 적어보기
"""

from collections import Counter


def solution_brute_force(participant: list, completion: list) -> str:
    # TODO: 여기 직접 구현 (이중 for문으로 완전탐색)
    pass


def solution_sort(participant: list, completion: list) -> str:
    # TODO: 여기 직접 구현 (정렬 후 같은 인덱스끼리 비교)
    pass


def solution_hash(participant: list, completion: list) -> str:
    # TODO: 여기 직접 구현 (Counter로 등장 횟수 비교)
    pass


if __name__ == "__main__":
    p1 = ["leo", "kiki", "eden"]
    c1 = ["eden", "kiki"]
    print(solution_brute_force(p1, c1))   # 예상 결과: "leo"
    print(solution_sort(p1, c1))          # 예상 결과: "leo"
    print(solution_hash(p1, c1))          # 예상 결과: "leo"
