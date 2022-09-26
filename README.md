현업에서의 고민
=============
레포지토리 설명 및 목적
> 1. 탄생 배경  
 현업에서 개발을 하면서 고민한 내용과 제 기준에서 많이 헤메이던 내용을 토대로 작성할 예정입니다.  
 제대로 알지 못하고 그냥 넘어갔던 부분을 다시 리마인드하고 정확히 알고 넘어가는데 중점을 둘 것 입니다.  
> 2. 목적  
 첫 번째, 블루프린트 형식처럼 코드 제공  
 두 번째, 생산성 증대  
 세 번째, 프레임워크에 대한 숙련도 및 이해도 증진  
> 3. 영역  
 프레임워크(장고) 및 각종 써드파티(DRF, yasg) 등등..  
> 4. 개발 환경  
 Python  
 Django   
 Drf-yasg  
 Drf-spectacular   

- Django Rest Framework
    - 기본 설정
      - 설명
        - 프로젝트의 전반적인 설정에 관련된 부분을 작성하는 곳
      - 테스트 배경
        - 설정되는 수 많은 DRF 설정에 대한 정보를 정확히 알고 넘어가려고 합니다. 그냥 블로그에서 사용했으니 복사 붙여넣고 넘어가는 부분들이 많아 제대로 알고 가도록 하겠습니다

    - context
      - 설명
        - 기본적으로 제공하지 않는 데이터 혹은 필드를 직렬화에서 사용하고 싶을 때 해당 기능을 사용한다
      - 테스트 배경
        - 해당 테스트의 주 목적은 실제 현업에서 기본 제공되는 context를 제대로 파악하지 못하고 context를 남발하다 보니 기능이 제대로 작동하지 않고 오류가 남으로 써 해당 기능에 대한 테스트를 진행합니다.
      - 테스트 리스트
        - [X] default provide context
        - [X] extra context
        - [X] default provide & extra context

- formatting
    - [ ] isort
    - [ ] context 테스트
    - [ ] black
    - [ ] flake8
    - [ ] pre-commit

- Drf-yasg

- Drf-spectacular

- DocString