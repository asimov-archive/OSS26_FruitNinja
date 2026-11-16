# Finger Slash

Finger Slash is a Python library for developers working with webcam-based hand tracking and fingertip coordinates.

## 1. What it does

Finger Slash는 웹캠을 이용해 사용자의 손을 인식하고, 검지 손끝의 움직임으로 과일을 자르는 게임을 개발하기 위한 Python 프로젝트입니다.

첫 번째 저장소에서는 다른 Python 프로젝트에서도 사용할 수 있는 라이브러리를 개발합니다.

주요 기능은 다음과 같습니다.

- OpenCV를 이용한 웹캠 영상 처리
- MediaPipe를 이용한 손 인식 및 손끝 좌표 추적
- 정규화된 손끝 좌표를 픽셀 좌표로 변환
- 손끝 이동 경로를 이용한 과일 슬라이스 판정
- JSON 파일을 이용한 최고 점수 저장

현재 핵심 함수들을 구현하고 있으며, 일부 기능은 개발 중입니다.

## 2. Installation

Python 3.10 이상을 사용하는 환경을 대상으로 합니다.

패키지는 pip를 이용하여 설치할 수 있도록 개발하고 있습니다.

TestPyPI 설치 방법:

```bash
pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ <package-name>==<version>
```

정식 PyPI 배포 이후:

```bash
pip install <package-name>
```

TODO: 실제 TestPyPI 업로드가 완료되면 패키지 이름과 버전을 반영합니다.

## 3. Quick start

Finger Slash의 핵심 함수는 Python 코드에서 불러와 사용할 수 있습니다.

다음은 손끝의 이동 경로를 이용하여 과일과 충돌했는지 확인하는 예제입니다.

```python
from fruit_ninja import detect_slice

result = detect_slice((0, 50), (100, 50), (50, 50), 20, 10)
print(result)  # True
```

위 코드는 손끝의 이동 경로가 과일과 교차하고 최소 이동 거리를 충족하면 `True`를 반환합니다.

TODO: 패키지 배포 후 실제 설치 환경에서 예제를 검증합니다.

## 4. Dependencies

프로젝트에서 사용하거나 사용할 예정인 주요 라이브러리는 다음과 같습니다.

| Library | Purpose | License |
|---|---|---|
| NumPy | 좌표 계산 및 슬라이스 충돌 판정 | BSD-3-Clause |
| OpenCV | 웹캠 영상 입력 및 처리 (예정) | TODO |
| MediaPipe | 손 인식 및 랜드마크 추적 (예정) | TODO |
| Pygame | 게임 화면 구현 (예정) | TODO |

현재 구현된 핵심 함수에서는 NumPy를 사용합니다.

TODO: `pyproject.toml`과 실제 코드에 맞춰 의존성 및 라이선스를 최종 확인합니다.

## 5. Tests

TODO

## 6. Documentation

프로젝트에 대한 자세한 내용은 다음 문서에서 확인할 수 있습니다.

- [Documentation](https://asimov-archive.github.io/OSS26_FruitNinja/)
- [API Documentation](docs/api.md)
- [Project Proposal](docs/proposal.md)
- [Team Rules](docs/team-rules.md)

프로젝트 문서는 개발 과정에 따라 계속 업데이트할 예정입니다.

## 7. Release

TODO

## 8. Team

### Team Members

| Name | GitHub ID |
|---|---|
| 양희 | asimov |
| 김민찬 | QuivyGM |
| 하나근 | nageun-ha |
| 유재준 | yj2trigger |
| 이지민 | leejimin1016 |

### Team Rules

팀의 협업 규칙은 [team-rules.md](docs/team-rules.md)를 참고하세요.

### AI Use

- **AI Tool:** ChatGPT
- **Purpose:** README 초안 작성 및 문서 구성 지원
- **Verification:** 프로젝트 제안서와 기존 함수 정의를 참고하여 작성하였으며, 실제 설치 및 배포 검증은 추후 진행할 예정입니다.

## 9. License

This project is licensed under the MIT License.

자세한 내용은 [LICENSE](LICENSE)를 참고하세요.