# SW Campus AI

AI Inference 전용 서버로, `FastAPI` 기반으로 동작하며, `Spring Boot` 서버([sw-campus-server](https://github.com/sw-campus/sw-campus-server))와 연동하여 실제 서비스 기능을 수행합니다.

<br />

## 📁 프로젝트 구조

```
sw-campus-ai/
  ├─ app/
  │   ├─ ocr/
  │   ├─ core/
  │   └─ main.py
  ├─ pyproject.toml
  ├─ uv.lock
  └─ Dockerfile
```

**구조 특징**

- 기능 단위 패키지 구조
- 각 기능은 `router.py`, `service.py`, `engine(loader).py`
- FastAPI 라우터는 `main.py`에서 통합

<br />

## 🧩 기술 스택

설치된 패키지는 `pyproject.toml` 및 `uv.lock`에서 관리됩니다.

- FastAPI
- PaddleOCR 3.3.2
- PaddlePaddle CPU
- Python 3.9+
- uv 패키지/런타임 매니저

<br />

## 🔧 설치

모든 실행은 `uv run`으로 자동 가상환경 사용

### 1. 가상환경 생성

```
uv venv
```

### 2. 패키지 설치

```
uv sync
```

### 3. 개발 서버 실행

```
uv run uvicorn app.main:app --reload
```

접속: [http://127.0.0.1:8000](http://127.0.0.1:8000)

<br />

## 🔍 OCR API

### 엔드포인트

```
POST /ocr/extract
```

### curl 테스트

```
curl -X POST "http://localhost:8000/ocr/extract" \
  -F "image=@/path/to/image.jpg"
```

### 응답 예시

```json
{
  "text": "문서 전체 OCR 결과",
  "lines": [
    "Certificate of Completion",
    "John Smith",
    "..."
  ],
  "scores": [
    0.9796,
    0.9648,
    0.9741
  ]
}
```

### 필드 설명

| 필드 | 의미 |
| --- | --- |
| text | 전체 OCR 텍스트(줄바꿈 포함) |
| lines | 줄 단위 OCR 결과 |
| scores | 각 줄의 OCR confidence score (0 ~ 1) |
