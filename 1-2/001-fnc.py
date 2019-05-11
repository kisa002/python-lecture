'''
1. main () 정의
① 리스트 변수 선언
② init_list () 호출
③ display () 호출하며 리스트 전달
2. init_list () 정의
① 리스트 생성 및 값 대입
a. matrix [row][col] = row * n + col
② matrix 반환
3. display () 정의
① 리스트 matrix 전달 받음
② 전체 요소의 합을 화면에 출력
③ 각 짝수 요소의 합을 출력
④ 각 홀수 요소의 합을 출력
'''
m = 3
n = 5

row = 3
col = 4

def main():
    list = []
    list = init_list()
    display(list)

def init_list():
    matrix = []

    for i in range(row):
        for j in range(col):

    return matrix

def display():
