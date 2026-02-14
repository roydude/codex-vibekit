# codex-vibekit (Light Mode)

영문 버전: [`README.md`](README.md)
문서 정책: `README.md`를 원본으로 유지하고, `README.ko.md`는 항상 동기화합니다.

`codex-vibekit`은 프로젝트 루트에 운영 스캐폴드(문서, 로그, 스킬, 규칙)를 주입해, 과도한 프로세스 없이 코딩 세션을 구조화해 주는 경량 CLI입니다.

## 철학

`codex-vibekit`은 아래 5가지 원칙을 기반으로 합니다.

1. 개발자가 체계를 위해 일하지 않고, 체계가 개발자를 위해 일해야 한다.
2. 로그는 한 곳(`logs/work/`)에 모은다.
3. 역할 모델은 최소화한다(orchestrator, planner, builder, critic).
4. 되돌리기 어려운 고영향 의사결정 시점(API 계약, 데이터 모델, 인증, 아키텍처)에서만 인간 확인을 받는다.
5. 문서 형식보다 실제 전달 속도를 우선한다.

## 목적

이 도구의 목적은 특히 Codex 환경에서 AI 보조 코딩 세션의 시작/운영 방식을 반복 가능하게 만드는 것입니다.

- 프로젝트 구조를 빠르게 표준화
- `PROJECT_HUB.md`로 현재 상태 가시화
- 일일 작업 이력(`WORKLOG`) 누락 방지
- 일관된 운영 규칙을 가진 재사용 가능한 스킬 제공

## 목표

- 빠른 부트스트랩: 명령 1회로 바로 시작
- 안전한 병합: 기존 파일 기본 비덮어쓰기
- 에이전트 친화 컨텍스트: Codex가 즉시 활용 가능한 스캐폴드
- 이식성: 신규/기존 저장소 모두 적용 가능

## 사용 사례

다음 상황에서 `codex-vibekit`을 사용하세요.

- 새 바이브코딩 프로젝트를 시작할 때
- 문서/로그가 흩어진 기존 프로젝트를 정리할 때
- `AGENTS.md`, `PROJECT_HUB.md` 기반으로 Codex 세션 컨텍스트를 안정화할 때
- 무거운 프로세스 대신 경량 운영 체계가 필요할 때

## Roles
| Role | Purpose |
|---|---|
| `orchestrator` | 태스크 분해, 스킬 선택, 결과 통합 |
| `planner` | 요구사항을 구현 가능한 계획으로 변환 |
| `builder` | 코드/설계/계약 구현 |
| `critic` | 품질 검증, 리스크 식별, 개선안 제시 |

## Techniques (보조 스킬)
| Technique | Used by | Purpose |
|---|---|---|
| `brainstorming` | `orchestrator`, `planner` | 모호한 요구사항 정제, 접근법 탐색, 설계 승인 질문 정리 |

## Codex 워크플로우

`codex-vibekit`은 오케스트레이터 중심 모델에 맞춰 Codex에 최적화되어 있습니다. 인간은 목표와 승인 중심으로 개입하고, 실행/분해/병렬 판단은 오케스트레이터가 담당합니다.

### 운영 모델 (인간 입력 최소화)

1. 메인 스레드 1개를 `orchestrator`로 시작
2. 오케스트레이터가 `PROJECT_HUB.md`와 최신 `WORKLOG`를 읽고 다음 행동 결정
3. 필요 시 `planner`/`builder`/`critic`를 선택해 작업 수행
4. 병렬 리소스가 필요하면 오케스트레이터가 지원 스레드 개설을 요청
5. 사용자는 요청된 프롬프트를 새 스레드에 전달하는 라우터 역할 수행
6. 메인 오케스트레이터가 결과 통합, 충돌 정리, 허브/워크로그 업데이트

### 프롬프트 예시 (오케스트레이터 시작)

메인 스레드:
```text
Act as orchestrator.
Read PROJECT_HUB.md and latest WORKLOG.
From now on, you decide task breakdown and which skill to run.
If additional parallel resources are needed, ask me to open a new thread with a ready-to-send prompt.
Only ask me at high-impact decision points.
```

일상 시작용 최소 문구(권장):
```text
Continue in orchestrator mode.
```

스캐폴드 규칙에 기본 동작이 정의되어 있으므로, 긴 프롬프트는 초기 설정/리셋 시점에만 사용하면 됩니다.

### 지원 스레드 전달 패턴

오케스트레이터가 아래 형태로 요청하면:

```text
Open Thread 2 and send this:
"Act as builder focused on API contract for <feature>.
Create docs/contracts/API-0001-<slug>.md.
Return only contract draft, assumptions, and open risks."
```

사용자는 Thread 2를 열어 그대로 전달합니다.

메인 스레드로 복귀 시:
```text
Thread 2 is done. Here is the result: <paste summary>.
Please integrate, resolve conflicts, and continue orchestration.
```

### 병렬 판단 책임

- 인간은 세부 태스크 분해를 직접 하지 않는다.
- 오케스트레이터가 병렬 분기 필요 여부를 판단한다.
- 인간은 스레드 라우팅과 결과 전달을 담당한다.
- 최종 우선순위/충돌 정리는 메인 오케스트레이터가 담당한다(필요 시 사용자 승인 요청).

## IDE 참고

- Codex: 최적 궁합. `AGENTS.md`와 스캐폴드 문서를 운영 컨텍스트로 바로 활용 가능
- Cursor/기타 IDE 에이전트: `AGENTS.md`를 자동 반영하지 않을 수 있어 `.cursorrules`, `CLAUDE.md`, 프롬프트 프리앰블 같은 보조 설정이 필요할 수 있음
- 권장 방식: 스캐폴드를 단일 진실 소스로 두고, IDE별 설정 파일에 핵심 규칙만 미러링
- 글로벌 Codex 가이던스(`~/.codex/AGENTS.md`)는 선택 사항입니다. 회사 업무와 바이브코딩을 같이 쓰는 경우, 글로벌 규칙은 최소화하고 워크플로우 규칙은 프로젝트 `AGENTS.md`에 두는 것이 안전합니다.
- 필요할 때만 `~/.codex/AGENTS.override.md`를 임시로 사용하고, 끝나면 제거하세요.

## 설치

### 권장: `uv tool`

```bash
uv tool install --from git+https://github.com/roydude/codex-vibekit.git codex-vibekit
```

### 대안: `pipx`

```bash
pipx install git+https://github.com/roydude/codex-vibekit.git
```

### 대안: 프로젝트 로컬 `venv + pip`

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install git+https://github.com/roydude/codex-vibekit.git
```

## 설치 후 세팅 순서 (Codex App, 자연어)

1. 위 방법 중 하나로 `codex-vibekit` 설치
2. 프로젝트 루트에서 아래 실행:

```bash
codex-vibekit init .
```

3. Codex App에서 새 스레드를 열고 아래 자연어 프롬프트 전달:

```text
Use `$skill-installer`. Install all skills discovered from `skills/**/SKILL.md` into `$CODEX_HOME/skills`, then report discovered skill names and installed absolute paths. Fail fast with exact error if any install fails.
```

4. 이후 메인 스레드는 아래 한 줄로 시작:

```text
Continue in orchestrator mode.
```

## 제거 (Uninstall)

### `uv tool`로 설치한 경우

```bash
uv tool uninstall codex-vibekit
```

### `pipx`로 설치한 경우

```bash
pipx uninstall codex-vibekit
```

### 프로젝트 가상환경에 설치한 경우

```bash
python -m pip uninstall codex-vibekit
```

참고: CLI를 제거해도 프로젝트에 이미 주입된 스캐폴드 파일은 자동 삭제되지 않습니다.

## 사용법

```bash
codex-vibekit check
codex-vibekit init .
codex-vibekit codex-setup
```

## Codex App 1회 초기 세팅

`init` 실행 후 아래 명령으로 세팅 프롬프트를 출력합니다.

```bash
codex-vibekit codex-setup
```

그 다음 Codex에서 새 스레드를 열고 출력된 프롬프트를 붙여넣어 `$skill-installer`가 프로젝트 `skills/**/SKILL.md` 기반으로 스킬을 설치하게 합니다.

1회 세팅 이후 일상 시작 문구:

```text
Continue in orchestrator mode.
```

## `init` 동작

- `src/codex_vibekit/assets/scaffold/`를 대상 디렉토리로 복사
- 기존 파일은 덮어쓰지 않음
- 동일 경로 파일이 이미 있으면 `*.vibekit-new`로 저장
- 당일 `logs/work/WORKLOG-YYYY-MM-DD.md`가 없으면 생성

### 주요 생성 결과

- `AGENTS.md`
- `PROJECT_HUB.md`
- `docs/templates/*`
- `docs/decisions/`, `docs/specs/`, `docs/design/`, `docs/contracts/`
- `logs/work/WORKLOG-YYYY-MM-DD.md`
- `skills/orchestrator/SKILL.md`
- `skills/planner/SKILL.md`
- `skills/builder/SKILL.md`
- `skills/critic/SKILL.md`

## 빠른 스모크 테스트 (리포 체크아웃 환경)

```bash
mkdir -p /tmp/vibekit-test && cd /tmp/vibekit-test
PYTHONPATH=/path/to/your/clone/src python3 -m codex_vibekit init .
find . -maxdepth 3 -type f | sort
```
