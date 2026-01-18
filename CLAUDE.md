# CLAUDE.md - AI Service

This file provides guidance to Claude Code when working with sw-campus-ai.

## Project Overview

SW Campus AI 서비스 (FastAPI, Python 3.9+)

## Development Commands

```bash
uv venv                                    # 가상환경 생성
uv sync                                    # 패키지 설치
uv run uvicorn app.main:app --reload      # 개발 서버 (localhost:8000)
```

## Architecture

```
sw-campus-ai/app/
├── ocr/
│   ├── router.py        # FastAPI 라우터
│   ├── service.py       # 비즈니스 로직
│   └── ocr_engine.py    # PaddleOCR 엔진
└── main.py              # 라우터 통합
```
