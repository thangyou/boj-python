import requests
import json

# API 요청을 보낼 URL
api_url = "https://openapi.foodsafetykorea.go.kr/api/sample/COOKRCP01/json/1/5"

try:
    # API로부터 데이터 가져오기
    response = requests.get(api_url)

    # API 응답 데이터를 JSON 형식으로 파싱
    api_data = response.json()

    # JSON 파일로 저장
    with open("recipe.json", "w", encoding="utf-8") as json_file:
        json.dump(api_data, json_file, ensure_ascii=False, indent=4)

    print("API 데이터가 JSON 파일로 저장되었습니다.")
except requests.exceptions.RequestException as e:
    print(f"API 요청 중 오류 발생: {e}")
except json.JSONDecodeError as e:
    print(f"JSON 파싱 중 오류 발생: {e}")
except IOError as e:
    print(f"파일 저장 중 오류 발생: {e}")
