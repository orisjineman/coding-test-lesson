"""
문제: 자연수 뒤집어 배열로 만들기
링크: https://school.programmers.co.kr/learn/courses/30/lessons/12932

문제 설명
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

제한 조건
n은 10,000,000,000이하인 자연수입니다.
입출력 예
n	return
12345	[5,4,3,2,1]

난이도: Lv.1

# 시간복잡도: (직접 계산해서 적어보기)
"""

# O(n)
# 문자열로 변환 후 뒤집기
def solution1(n: int) -> list:
    str_n = str(n)
    result = []
    for value in range(len(str_n), 0, -1):
        result.append(value)
    return result

# 나머지(%) 몫(//) 연산으로 뒤집기
def solution2(n: int) -> list:
    result = []
    while n > 0:
        digit = n % 10
        result.append(digit)
        n = n // 10

    return result


if __name__ == "__main__":
    print(solution1(12345))   # 예상 결과: [5, 4, 3, 2, 1]
    print(solution2(12345))   # 예상 결과: [5, 4, 3, 2, 1]
