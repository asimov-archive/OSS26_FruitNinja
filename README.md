# Finger Slash

A Python library project for developers working with webcam-based hand tracking and fingertip coordinates.

## 1. What it does

Finger Slash는 웹캠을 이용하여 사용자의 손을 인식하고 검지 손끝의 좌표를 추적하는 Python 프로젝트입니다.

현재 개발 중인 첫 번째 저장소는 다른 Python 프로젝트에서 사용할 수 있는 손끝 좌표 처리 라이브러리를 목표로 합니다.

프로젝트 제안서에 명시된 기술은 다음과 같습니다.

- OpenCV를 이용한 웹캠 영상 입력 및 처리
- MediaPipe Hand Landmarker를 이용한 손 랜드마크 검출
- 검지 끝(8번 랜드마크)의 좌표 추적
- 정규화된 좌표를 화면 픽셀 좌표로 변환

현재 `src/fruit_ninja/core.py`에는 `track_fingertip()`, `detect_slice()`, `save_high_score()` 함수의 인터페이스가 정의되어 있습니다.

실제 구현은 진행 중입니다.

## 2. Installation

TODO: TestPyPI 업로드가 완료되면 실제 패키지 이름과 버전을 사용한 설치 명령어를 추가합니다.

TestPyPI 설치 명령어 형식:

```bash
pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ <package-name>==<version>
```

정식 PyPI 배포 이후 설치 명령어:

```bash
pip install <package-name>
```

위 명령어의 `<package-name>`과 `<version>`은 실제 배포 정보로 교체해야 합니다.

## 3. Quick start

`track_fingertip()` 함수는 정규화된 좌표를 화면 픽셀 좌표로 변환하도록 정의되어 있습니다.

```python
from fruit_ninja.core import track_fingertip

x, y = track_fingertip(0.5, 0.5, 1280, 720)
print(x, y)
# Expected: (640, 360)
```

현재 함수가 구현되지 않았기 때문에 위 코드는 정상 실행되지 않습니다.

TODO: 함수 구현 이후 실제 입력과 출력이 확인된 5줄 이내의 실행 예제로 수정합니다.

## 4. Dependencies

프로젝트 제안서에 명시된 주요 라이브러리입니다.

| Library | Import | Purpose | License |
|---|---|---|---|
| OpenCV | `cv2` | Webcam input and image processing | TODO |
| MediaPipe | `mediapipe` | Hand landmark detection | TODO |
| Pygame | `pygame` | Game display | TODO |

TODO: 실제 패키지의 import 목록과 `pyproject.toml`을 기준으로 의존성 및 라이선스를 확정합니다.

## 5. Tests

TODO

## 6. Documentation

프로젝트 관련 문서는 다음 링크에서 확인할 수 있습니다.

- [Documentation](https://asimov-archive.github.io/OSS26_FruitNinja/)
- [API Documentation](docs/api.md)
- [Project Proposal](docs/proposal.md)
- [Team Rules](docs/team-rules.md)

문서 사이트의 실제 배포 상태는 확인이 필요합니다.

## 7. Release

TODO

## 8. Team

### Team Members

| Name | GitHub ID |
|---|---|
| 양희 | TODO |
| 김민찬 | TODO |
| 하나근 | TODO |
| 유재준 | TODO |
| 이지민 | TODO |

### Team Rules

프로젝트의 협업 규칙은 [team-rules.md](docs/team-rules.md)를 참고하세요.

### AI Use

- **AI Tool:** ChatGPT
- **Purpose:** README 초안 작성 및 교수님 템플릿에 맞춘 문서 구성
- **Verification:** 기존 프로젝트 제안서, 함수 정의 및 팀 규칙과 내용 비교. 실행 및 배포 검증은 아직 수행하지 않음.

## 9. License

This project is licensed under the MIT License.

자세한 내용은 [LICENSE](LICENSE)를 참고하세요.