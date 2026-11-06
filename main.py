"""
import: 가져오다
json: JSON 데이터를 처리할 수 있는 python 모듈
"""
import json

"""
open(): 파일을 열 때 사용하는 Python 내장 함수
open("dictionary.json", "r", encoding="utf-8") as file: 
어떤 파일을 열 것인가 -> dictionary.json/ JSON에 저장된 단어 읽기/ 인코딩(숫자를 어떤 문자로 해석할지 정하는 방식) 한국어 일본어 둘 다 사용하므로 utf-8 지정 / as file 열림 파일에 이름 붙이기
with 실행 순서(1. 파일 열기-> 파일 내용 읽기-> 들여쓰기 된 코드 실행 종료 -> 파일 자동으로 닫기)
"""
# 사전 파일 불러오기
with open("dictionary.json", "r", encoding="utf-8") as file:
    dictionary = json.load(file) # json.load() -> json : JSON 모듈 / load() : 파일에 저장된 JSON 데이터를 읽어오는 함수 / file : 우리가 앞에서 열어 둔 파일
    
while True:
    # 히라가나 불러오기
    word = input("히라가나를 입력하세요: ")

    # 사전에서 한글 찾기
    result = dictionary.get(word) # .get(word)-> 딕셔너리에서 원하는 값 찾아오기

    # 결과 출력
    if result:
        print(f"변환 결과: {result}")
    else:
        print("등록되지 않은 단어입니다.")
        break