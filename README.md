# 레포지토리 탄생 배경
---
 - 프로젝트에 치이는 일상을 겪다보니 제대로 알지 못하고 사용을 하는 기술스택들이 난무함으로 인해 매번 선연치않은 마음을 안고 프로젝트를 진행했다. 해당 레포지토리를 통해 제대로 알지 못하고 넘어간 내용에 대해서 정리를 하고자 해당 레포지토리를 생성하게 되었습니다.

# 목표
---
 - 첫 번째, 블루프린트 형식처럼 코드 제공
 - 두 번째, 협업에서 생산성 증대
 - 세 번째, 프레임워크에 대한 숙련도 및 이해도 증진

# 작성 방식
---
 - Discusstion 기능을 활용해 작성

# 영역
 - 영역에 크게 의미를 두지 않으려고 한다
---
### 1. 백엔드
|Name|Version|
|:--:|:--:|
|Python|3.9.9|
|Django|4.1.1|
|DRF|3.14|

### 2. IDE
|Name|Version|
|:--:|:--:|
|Vscode|-|

### 3. Linter & Formatter
|Name|Version|
|:--:|:--:|
|Flake8|5.0.4|
|Isort|5.10.1|
|Black|22.8.0|

### 4. Git hooks
|Name|Version|
|:--:|:--:|
|Pre-commit|2.20.0|

---

#### 1. DRF
 - Context

|Topic|Description|Link|
|:--:|:--:|:--:|
|Context|현업에서 context에 대한 기능을 제대로 파악하지 못하고 남발하는 사례|#4|

- Django Rest Framework
    - 기본 설정
    - context
      - 테스트 배경
        - 실제 현업에서 기본 제공되는 context에 대한 기능을 제대로 파악하지 못하고 context 남발해 오류를 야기함
      - 테스트 리스트
        - [X] default provide context
        - [X] extra context
        - [X] default provide & extra context

- Code Style
  - 테스트 배경
    - 정해진 규칙 없이 개발자들의 스타일에 맞게 코딩을 진행하고 있어 정해진 규칙과 스타일을 통해 코드의 통일성을 높이는데 목적
  - 테스트 리스트
    - Lint
      - [X] flake8
    - Formatter
      - [X] black
      - [X] isort
    - Git hooks
      - [X] pre-commit

- Drf-yasg

- Drf-spectacular

- DocString

- Git
  - 테스트 배경
    - 명령어들의 기능을 정확히 알지 못하고 대략적인 감으로 이런 방식으로 하면 되니까 하고 넘어간 부분이 많음
  - 테스트 리스트
    - [ ] 다양한 명령어
      - [ ] Tagging
      - [ ] Merge
      - [ ] Release
      - [ ] Add
      - [ ] Rebase
      - [ ] Pull
      - [ ] Reset
    - [ ] Confilct

- Github
  - 테스트 배경
    - 실제로 깃허브에서 제공하는 다양한 기능을 제대로 활용하고 있지 않고 있음
  - 테스트 리스트
    - [ ] 기능
      - [ ] Discussion
      - [ ] Action
      - [ ] PR
      - [ ] Issue
