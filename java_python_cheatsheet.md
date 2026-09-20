# Java → Python 문법 치트시트

자바 위주로 코딩해왔던 사람이 파이썬 코딩테스트를 볼 때 자주 막히는 문법들을 정리했어.
새로운 문법이 나올 때마다 이 파일에 계속 추가하자 (막혔던 것 = 다음에 또 까먹을 확률이 높은 것).

## 반복문 / 기본 흐름

| 상황 | Java | Python |
|---|---|---|
| 0~n-1 반복 | `for(int i=0;i<n;i++)` | `for i in range(n):` |
| a~b-1 반복 | `for(int i=a;i<b;i++)` | `for i in range(a, b):` |
| step 주기 | `for(int i=0;i<n;i+=2)` | `for i in range(0, n, 2):` |
| 역순 반복 | `for(int i=n-1;i>=0;i--)` | `for i in range(n-1, -1, -1):` |
| 배열 순회 (인덱스 필요없을 때) | `for(int x : arr)` | `for x in arr:` |
| 인덱스 + 값 같이 순회 | 직접 `int i=0` 관리 | `for i, x in enumerate(arr):` |
| 삼항 연산자 | `a > b ? a : b` | `a if a > b else b` |

## 값 교환 / 변수

| 상황 | Java | Python |
|---|---|---|
| 값 swap | `int tmp=a; a=b; b=tmp;` | `a, b = b, a` |
| 여러 변수 동시 선언 | `int a=1, b=2;` | `a, b = 1, 2` |
| null 체크 | `if (obj == null)` | `if obj is None:` |

## 숫자 / 문자열

| 상황 | Java | Python |
|---|---|---|
| 두 값 중 큰/작은 값 | `Math.max(a,b)` / `Math.min(a,b)` | `max(a, b)` / `min(a, b)` |
| 여러 값 중 최댓값 | `Collections.max(list)` | `max(list)` |
| 절댓값 | `Math.abs(x)` | `abs(x)` |
| 거듭제곱 | `Math.pow(a, b)` | `a ** b` |
| 몫/나머지 | `a / b`, `a % b` | `a // b`, `a % b` (주의: 몫은 `//`) |
| 문자열 뒤집기 | `new StringBuilder(s).reverse().toString()` | `s[::-1]` |
| 문자열 자르기(부분열) | `s.substring(1, 3)` | `s[1:3]` |
| 공백 기준 분리 | `s.split(" ")` | `s.split(" ")` (동일) |
| 문자 하나씩 리스트로 | `s.toCharArray()` | `list(s)` |
| 리스트 → 문자열 합치기 | `String.join(",", list)` | `",".join(list)` |
| 문자열 포맷 | `String.format("%d개", n)` | `f"{n}개"` |
| 대소문자 변환 | `s.toUpperCase()` | `s.upper()` |

## 배열 / 리스트

| 상황 | Java | Python |
|---|---|---|
| 배열/리스트 선언 | `int[] arr = new int[n];` | `arr = [0] * n` |
| 동적 배열 | `ArrayList<Integer>` | `list` (그냥 `[]`) |
| 원소 추가 | `list.add(x)` | `list.append(x)` |
| 정렬 (오름차순) | `Arrays.sort(arr)` | `arr.sort()` (제자리) 또는 `sorted(arr)` (새 리스트) |
| 정렬 (내림차순) | `Collections.reverseOrder()` | `arr.sort(reverse=True)` |
| 커스텀 기준 정렬 | `Comparator.comparing(...)` | `sorted(arr, key=lambda x: ...)` |
| 리스트 뒤집기 | `Collections.reverse(list)` | `arr.reverse()` 또는 `arr[::-1]` |
| 리스트 안 포함 여부 | `list.contains(x)` | `x in list` (O(n), 주의) |
| 2차원 배열 | `int[][] arr = new int[n][m];` | `arr = [[0]*m for _ in range(n)]` |
| 조건 걸러서 새 리스트 만들기 | for문 + if + add | `[x for x in arr if 조건]` (리스트 컴프리헨션) |

## 자료구조 (해시 관련 - week06에서 더 깊게 다룰 예정)

| 상황 | Java | Python |
|---|---|---|
| Map | `HashMap<K,V>` | `dict` (`{}`) |
| Set | `HashSet<T>` | `set` |
| 등장 횟수 세기 | 직접 HashMap 루프 | `from collections import Counter` |
| 키 존재 확인 | `map.containsKey(k)` | `k in dict` |
| 기본값 있는 조회 | `map.getOrDefault(k, 0)` | `dict.get(k, 0)` |

## 자주 헷갈리는 포인트

- **몫 연산자는 `//`, `/`는 실수(float) 나눗셈**이야. 자바의 `int / int`처럼 정수 나눗셈을 기대하고 `/`만 쓰면 결과가 `float`으로 나와서 틀릴 수 있어.
- **`in` 연산은 자료구조에 따라 시간복잡도가 다름**: `list`에서는 O(n) (순회), `set`/`dict`에서는 O(1) (해시). (week01 lecture.md 참고)
- 파이썬은 **세미콜론, 중괄호가 없고 들여쓰기가 문법**이야. 들여쓰기 오류가 자바보다 훨씬 치명적(문법 에러남).
- 파이썬 함수/변수 선언에 **타입을 안 써도 되지만**, 코딩테스트 답안 가독성을 위해 `def solution(a: int, b: int) -> int:` 처럼 타입 힌트를 달아두는 습관을 들이면 자바 감각과 비슷해서 편해.

## 메모

- 새로운 문법 막힐 때마다 여기 추가하기.
