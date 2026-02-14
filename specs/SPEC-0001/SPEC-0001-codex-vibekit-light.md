아래는 **Codex에서 바로 작업을 시작할 수 있도록** 만든 `codex-vibekit` 개발 명세입니다.
**Light Mode** — 1인 바이브코딩에 최적화된 경량 버전.

---

# SPEC: codex-vibekit (Light Mode)

## 0. 목표

별도 리포지토리(`codex-vibekit`)를 만들고, CLI로 설치/실행하여 각 "바이브코딩 프로젝트" 루트에 **운영 스캐폴딩(폴더/문서/스킬)** 을 주입한다.

* 1차 범위: **스캐폴딩 주입 + 운영 문서/스킬 번들 제공 + 기본 워크플로우 고정**
* 2차 범위(보류): 슬래시 커맨드, 에이전트별 자동 실행, 고급 병합/업그레이드, Full Mode(팀용 8스킬 체계)

### 설계 원칙 (Light Mode)

1. **체계가 나를 위해 일한다** — 내가 체계를 유지하기 위해 일하지 않는다
2. **로깅은 하나로** — WORKLOG 하나에 모든 기록을 남긴다
3. **역할은 4개로 충분하다** — orchestrator, planner, builder, critic
4. **게이트는 진짜 필요할 때만** — 아키텍처 결정(Gate B)만 필수, 나머지는 선택
5. **형식보다 속도** — Final Block은 중요한 결정이 있을 때만 작성

---

## 1. 사용자 플로우

### Flow A: 킷 리포지토리 세팅 (GitHub 연결)

1. `codex-vibekit` 리포를 만든다 (GitHub)
   - 리포지토리: https://github.com/roydude/codex-vibekit.git
2. 리포에 CLI 패키지 + 스캐폴딩 자산(assets)을 포함한다
3. `uv tool install --from git+...`로 설치 가능하게 만든다

### Flow B: 프로젝트에서 사용

1. 바이브코딩을 위한 새 프로젝트 폴더를 만든다 (또는 기존 프로젝트)
2. 프로젝트 폴더에서 `codex-vibekit` CLI를 설치한다(전역 설치 권장)
3. `codex-vibekit init .` 실행
4. 프로젝트 루트에 운영 구조 생성됨(AGENTS.md, PROJECT_HUB.md, docs/logs/skills …)
5. Codex에서 프로젝트 폴더를 열고 작업 시작
   * 모든 스킬은 `PROJECT_HUB.md` 최신 헤더를 읽고 작업한다
   * 산출물은 `logs/work/`에 기록한다

---

## 2. 범위(1차 MVP)

### 반드시 포함

* CLI 커맨드
  * `codex-vibekit init [PATH]`
    * `PATH`가 디렉토리면 그 안에 스캐폴딩 생성/병합
    * `PATH`가 없으면 현재 디렉토리(`.`) 기본
  * `codex-vibekit check`
    * uv, git 존재 여부 확인(가능하면), 설치 안내 출력

* 스캐폴딩(프로젝트에 복사되는 파일/폴더)
  * `AGENTS.md` (Codex 작업 규칙)
  * `PROJECT_HUB.md` (단일 진실)
  * `docs/templates/*` (SPEC/ADR/WORKLOG 템플릿)
  * `docs/decisions/`, `docs/specs/`, `docs/design/`, `docs/contracts/`
  * `logs/work/` (통합 작업 로그)
  * `skills/*/SKILL.md` (역할별 스킬 번들; orchestrator/planner/builder/critic)

* 네이밍 규칙/운영 규칙 문서화
  * 파일명 규칙(ADR-0001-*, SPEC-0001-* 등)
  * Gate B 트리거 규칙

### 제외(2차로 미룸)

* `upgrade`(템플릿 병합 고도화)
* GitHub Actions, 릴리즈 자동화
* 슬래시 커맨드 통합
* 프로젝트별 스택 탐지/툴체인 설치 자동화
* Full Mode (8스킬 체계, Gate A/C, CONSTITUTION.md, 스레드 헌장, SYNC 로그)

---

## 3. 산출물 구조(킷 리포지토리)

`codex-vibekit` 리포는 아래를 따른다.

```text
codex-vibekit/
  README.md
  LICENSE
  pyproject.toml
  src/
    codex_vibekit/
      __init__.py
      cli.py
      assets/
        scaffold/
          AGENTS.md
          PROJECT_HUB.md
          docs/
            templates/
              TEMPLATE-ADR.md
              TEMPLATE-SPEC.md
              TEMPLATE-WORKLOG.md
            decisions/
            specs/
            design/
            contracts/
          logs/
            work/
              WORKLOG-YYYY-MM-DD.md
          skills/
            orchestrator/SKILL.md
            planner/SKILL.md
            builder/SKILL.md
            critic/SKILL.md
```

---

## 4. CLI 동작 명세

### 4.1 `codex-vibekit init <path>`

**입력**

* `<path>`: 디렉토리 경로
  * 생략 시 `.`

**동작**

* `<path>`가 없으면 생성
* `assets/scaffold/` 내용을 `<path>/`에 복사
* 이미 파일이 있을 경우:
  * 기본 정책(1차): **덮어쓰기 금지**, 충돌 시 `*.vibekit-new`로 저장하거나 "스킵 + 리포트 출력"
  * 단, 빈 디렉토리면 그대로 생성
* 실행 후, 생성/스킵/충돌 파일을 요약 출력

**성공 기준**

* 프로젝트 루트에 `AGENTS.md`, `PROJECT_HUB.md`가 존재
* `docs/`, `logs/`, `skills/`가 존재

### 4.2 `codex-vibekit check`

**동작**

* `uv` 사용 가능 여부 안내(없으면 설치 링크/가이드 메시지)
* `git` 존재 여부 안내
* (선택) Python 버전 확인 (예: 3.11+ 권장)

---

## 5. 프로젝트 루트 스캐폴딩의 핵심 파일 요구사항

### 5.1 `AGENTS.md` 필수 포함 규칙

* 작업 시작 전: `PROJECT_HUB.md` 상단 "최근 변경(헤더)" 확인
* 작업 종료 시:
  * `logs/work/WORKLOG-YYYY-MM-DD.md`에 작업 내용 기록 (append 방식, 타임스탬프로 구분)
  * 새 문서 만들면 `PROJECT_HUB.md`에 링크 등록
* Gate 규칙:
  * Gate B: 아키텍처/계약(Contract) 결정이 필요할 때 사용자에게 확인 요청
  * (선택) Gate A/C: 필요시 사용자가 직접 트리거
* 네이밍 규칙/저장 위치 강제

### 5.2 `PROJECT_HUB.md`

* 최근 변경(최신 10줄)
* North Star / MVP Scope
* Docs 링크 섹션(SPEC/ADR/CONTRACT)
* Current Status(이번 주 목표, 블로커)
* Open Questions(결정 필요 사항, 간단한 목록)

---

## 6. Skills 번들 요구사항

각 스킬 폴더는 최소 `SKILL.md`를 가진다.

### 공통 출력 규약

중요한 결정이 포함된 작업에서만 아래 블록을 포함한다 (간단한 작업에서는 생략 가능):

* 결정 필요(Yes/No):
* 리스크(있다면):
* 다음 액션:
* 생성/수정한 문서(있다면):

### 포함할 스킬(Light Mode)

| 스킬 | 역할 | Full Mode 대응 |
|------|------|----------------|
| orchestrator | 워크플로우 조율, 스킬 선택, 로깅 | orchestrator |
| planner | 아이디어 → 스펙, 스코프 정의, 태스크 분해 | planner + doc-lead |
| builder | 설계 + 구현 (FE/BE/UX 통합) | designer + frontend + backend + tpm |
| critic | 품질 평가, 사용성 검증, 리스크 식별 | critic |

---

## 7. 작업 태스크(코덱스에서 바로 실행용)

### Phase 1: `codex-vibekit` 리포지토리 구축

1. GitHub에 `codex-vibekit` 리포 생성 및 기본 파일 추가
   * README.md, LICENSE, pyproject.toml, src/ 구조
2. Python CLI 구현
   * `codex-vibekit` 실행 엔트리포인트 설정
   * `init`, `check` 구현
3. `assets/scaffold`에 스캐폴딩 파일들 작성
   * 본 스펙의 폴더/문서/템플릿/skills 포함
4. 로컬에서 테스트
   * 빈 폴더에 `codex-vibekit init .` 실행 → 구조 생성 확인
   * 일부 파일이 있는 폴더에서 init → 충돌 정책 확인
5. 문서 작성
   * README에 설치/사용법, 예시 커맨드, 생성되는 파일 설명

### Phase 2: 실제 프로젝트에 적용

1. 임의의 프로젝트 폴더 생성(또는 기존 프로젝트)
2. `uv tool install --from git+<repo-url>`로 설치
3. 프로젝트 루트에서 `codex-vibekit init .`
4. Codex App에서 그 프로젝트 폴더 열고:
   * 첫 작업으로 `PROJECT_HUB.md` 업데이트
   * orchestrator 스킬로 현재 상태 파악 및 다음 액션 결정

---

## 8. 인수 기준(Acceptance Criteria)

### 킷 리포지토리

* `uv tool install --from git+...`로 설치 가능
* `codex-vibekit init .` 실행 시 스캐폴딩이 생성됨
* 충돌 시 덮어쓰지 않고, 충돌 파일 처리(스킵 또는 `.vibekit-new`)가 동작
* README에 설치/사용 예시가 있음

### 프로젝트 적용

* 프로젝트 루트에 `AGENTS.md`, `PROJECT_HUB.md`가 존재
* `skills/*/SKILL.md`가 존재하고, 4개 역할이 명확히 구분됨
* `docs/`와 `logs/` 구조가 존재
* orchestrator가 Pull(허브 헤더 읽기) → 산출물 기록(work log) 규칙을 따를 수 있게 문서/규칙이 갖춰짐

---

## 9. 코덱스에서 작업 개시 프롬프트(첫 메시지 템플릿)

Codex에서 `codex-vibekit` 리포를 열고, 첫 요청은 아래처럼 시작한다.

**요청 템플릿**

* "이 리포에서 `codex-vibekit` CLI를 구현해줘."
* "`codex-vibekit init`는 `src/codex_vibekit/assets/scaffold/`를 현재 폴더에 복사해야 해."
* "스캐폴딩은 본 스펙의 구조/파일을 그대로 포함해야 해."
* "덮어쓰기 금지, 충돌은 `.vibekit-new`로 저장해."
* "완료 후 로컬에서 init 동작을 검증할 수 있는 간단한 테스트 절차도 README에 추가해."

---

## 10. Light → Full 확장 경로

Light Mode에서 검증된 후, 필요시 아래를 점진적으로 추가:

| 단계 | 추가 요소 |
|------|-----------|
| +designer | builder에서 UX 설계 분리, `docs/design/UX-*` 활성화 |
| +frontend/backend | builder에서 FE/BE 분리, 계약 기반 협업 |
| +tpm | 기술 결정 분석(ADR) 전담, Gate B 강화 |
| +doc-lead | 문서 아키텍처 전담, 템플릿 관리 |
| +Gate A/C | 스코프 승인, 릴리즈 승인 게이트 추가 |
| +CONSTITUTION.md | 프로젝트 원칙/가드레일 문서 |
| +threads/CHARTER | 스레드별 역할 고정 헌장 |
| +SYNC 로그 | 멀티 스레드 동기화 로그 |