K = int(input()) # 각 가족 그룹의 구성원 수
total = list(map(int, input().split())) # 정리되지 않은 총 객실 목록

A = set(total) # set 함수를 사용하여 line2의 total에서 중복된 객실 번호를 제거한다.

for i in A:
    total.remove(i) # line2의 total list에서 첫번째로 등장하는 집합 A의 요소를 하나씩만 삭제한다.

B = set(total) # 위의 for문의 결과로 캡틴의 객실 번호가 지워진 집합이 만들어 진다. (=집합B)

result = A - B # result의 결과로는 캡틴 객실 번호가 집합 형태로 나타난다.
print (*result) # result에서 요소를 빼내어 출력 = 캡틴의 방 번호만을 출력

# 런코드는 되지만 서밋 시에 2, 5번 케이스에서 타임오류 발생.
