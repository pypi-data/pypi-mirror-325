# Spaceone Dashboard Generator

FastAPI를 사용하여 대시보드를 생성하는 애플리케이션입니다. 이 애플리케이션은 사용자로 하여금 대시보드 템플릿을 생성하고 관리할 수 있도록 도와줍니다.

## 기능

- 대시보드 템플릿 생성
- 대시보드 템플릿 목록 조회
- 대시보드 템플릿 삭제
- 환경 파일 목록 조회

## 설치

1. 이 저장소를 클론합니다.

   ```bash
   git clone https://github.com/yourusername/spaceone-dashboard-gen.git
   cd spaceone-dashboard-gen
   ```

2. 가상 환경을 생성하고 활성화합니다.

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows의 경우 `venv\Scripts\activate`
   ```

3. 필요한 패키지를 설치합니다.

   ```bash
   pip install -r requirements.txt
   ```

## 사용법

1. FastAPI 서버를 실행합니다.

   ```bash
   uvicorn main:app --reload
   ```

2. 웹 브라우저에서 `http://127.0.0.1:8000`으로 이동하여 대시보드 생성기를 사용합니다.

## API 엔드포인트

- `GET /`: 메인 페이지를 반환합니다.
- `POST /dashboard-generator`: 대시보드를 생성합니다.
- `GET /environment-files`: 환경 파일 목록을 반환합니다.
- `POST /run-create-template-by-subprocess`: 서브프로세스를 통해 템플릿을 생성합니다.
- `GET /list-dashboard-templates-by-subprocess`: 서브프로세스를 통해 대시보드 템플릿 목록을 반환합니다.
- `GET /delete-dashboard-template`: 대시보드 템플릿을 삭제합니다.

## 기여

기여를 환영합니다! 버그 리포트, 기능 제안, 풀 리퀘스트 등을 통해 프로젝트에 기여할 수 있습니다.

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요. 