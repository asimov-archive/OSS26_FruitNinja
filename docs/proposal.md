# 프로젝트 제안서(Project proposal): "핑거 슬래시(Finger Slash)"

## 1. 프로젝트 주제(Project topic)

### 만들고 싶은 프로그램(What we want to build)

웹캠으로 사용자의 손을 인식하고, 검지 손가락 끝의 움직임으로 화면에 날아오르는 과일을 베는 Python 데스크톱 게임을 개발한다. 키보드·마우스 없이 손동작만으로 게임을 조작한다.
(We will build a Python desktop game in which the player slices fruits flying across the screen by moving their index fingertip in front of a webcam. The game is controlled only by hand movements, without a keyboard or mouse.)

### 사용자 정의 및 해결할 문제(Users and problem)

컴퓨터 비전이나 AI에 관심은 있지만 직접 체험해 볼 기회가 적은 학생·일반인이 주 사용자다. 손 인식 같은 기술은 설명이나 데모 영상으로 접하면 와닿지 않고, 직접 써 보려 해도 코드를 실행하고 결과 수치를 읽어야 해서 진입 장벽이 높다. 이 프로그램은 웹캠만 있으면 게임을 통해 실시간 손 추적이 어떻게 동작하는지(얼마나 빠르고 정확한지, 언제 인식이 끊기는지)를 몸으로 체험하게 해 준다. 학과 홍보 부스나 동아리 행사처럼 짧은 시간에 여러 사람이 번갈아 즐기는 상황에도 쓸 수 있다.
(Our main users are students and other people who are curious about computer vision and AI but rarely get to try it themselves. Explanations and demo videos of hand tracking feel abstract, and running the code directly means reading raw numbers, which is a barrier. With just a webcam, this game lets users experience through play how real-time hand tracking behaves — how fast and accurate it is and when it loses track. It also suits events such as department booths or club fairs, where many people take short turns.)

## 2. 개발할 기능(Planned features)

### 입력(Input)

- 노트북 내장 또는 USB 웹캠의 실시간 영상(기본 640×480, 약 30fps)
- 게임 시작·재시작은 손을 화면의 버튼 영역에 일정 시간 올려두는 방식으로 입력(키보드 없이 조작)
- 이전에 저장된 최고 점수 파일(`highscore.json`, 없으면 새로 생성)

(Real-time video from a built-in or USB webcam (default 640×480, about 30 fps). Starting and restarting the game is done by holding the hand over an on-screen button area for a moment, with no keyboard. The previously saved high score file (`highscore.json`) is read if it exists, or created if it does not.)

### 처리(Processing)

1. **영상 입력**: OpenCV로 웹캠 프레임을 읽고, 거울처럼 보이도록 좌우 반전한 뒤 BGR을 RGB로 변환한다.
   (Read webcam frames with OpenCV, flip them horizontally so the view acts like a mirror, and convert BGR to RGB.)
2. **손 검출 및 손끝 추적**: MediaPipe Hand Landmarker로 프레임마다 손의 21개 랜드마크를 검출하고, 그중 검지 끝(8번 랜드마크)의 정규화 좌표(0~1)를 게임 화면 픽셀 좌표로 변환한다. 손이 검출되지 않은 프레임은 궤적을 끊는다.
   (Detect the 21 hand landmarks in each frame with MediaPipe Hand Landmarker, and convert the normalized coordinates (0–1) of the index fingertip (landmark 8) to game-screen pixel coordinates. The trail is broken on frames where no hand is detected.)
3. **궤적 생성**: 최근 약 10프레임의 손끝 좌표를 저장해 화면에 칼날 궤적으로 그린다. 좌표가 튀는 것을 줄이기 위해 이동 평균으로 간단히 보정한다.
   (Store the fingertip coordinates from roughly the last 10 frames and draw them as a blade trail. A simple moving average reduces jitter.)
4. **과일·폭탄 생성**: 화면 아래에서 과일과 폭탄을 무작위 위치·속도로 발사하고, 중력을 적용해 포물선으로 움직이게 한다.
   (Launch fruits and bombs from the bottom of the screen at random positions and speeds, and apply gravity so they follow parabolic paths.)
5. **자르기 판정**: 직전 프레임 손끝 위치와 현재 위치를 잇는 선분과 각 물체(원으로 근사) 중심 사이의 거리가 반지름보다 작고, 손끝 이동 속도가 기준값 이상일 때만 "베었다"고 판정한다. 손을 가만히 대고 있는 것은 자르기로 치지 않는다.
   (A slice is registered only when the distance from an object's center (approximated as a circle) to the segment between the previous and current fingertip positions is less than its radius, and the fingertip speed exceeds a threshold. Simply holding the hand over an object does not count.)
6. **점수·목숨 처리**: 과일을 베면 점수 +1(짧은 시간 안에 여러 개를 베면 콤보 보너스), 폭탄을 베면 목숨 −1, 과일을 놓쳐 화면 아래로 떨어뜨려도 목숨 −1. 목숨은 3개로 시작하며 0이 되면 게임 오버.
   (Slicing a fruit gives +1 point, with a combo bonus for several slices in a short time. Slicing a bomb or letting a fruit fall off the screen costs one life. The player starts with 3 lives; the game ends at 0.)
7. **난이도 상승**: 30초마다 과일 생성 간격을 줄이고, 발사 속도와 폭탄 등장 비율을 높인다.
   (Every 30 seconds, shorten the spawn interval and increase launch speed and the proportion of bombs.)
8. **최고 점수 저장**: 게임 오버 시 현재 점수가 최고 점수보다 높으면 `highscore.json`에 점수와 날짜를 저장한다.
   (At game over, if the score beats the high score, save the score and date to `highscore.json`.)

### 결과(Output)

- Pygame 게임 창(예: 1280×720): 웹캠 영상(반투명 배경), 손끝 궤적, 과일·폭탄, 현재 점수·최고 점수·남은 목숨·경과 시간이 표시된다.
- 게임 오버 화면: 최종 점수와 최고 점수 갱신 여부를 보여 주고, 손을 버튼에 올려 다시 시작할 수 있다.
- 로컬 파일 `highscore.json`: 최고 점수와 기록 날짜를 저장하며 게임을 다시 켜도 유지된다.
- 웹캠 영상은 실시간 처리에만 쓰며 녹화·저장하지 않는다.

(A Pygame window (e.g. 1280×720) showing the webcam feed as a semi-transparent background, the fingertip trail, fruits and bombs, and the current score, high score, remaining lives and elapsed time. A game-over screen shows the final score and whether a new high score was set, with a hand-activated restart button. A local `highscore.json` file keeps the high score and date across sessions. Webcam video is used only for real-time processing and is never recorded or saved.)

### 개발 범위(Scope)

- 포함할 기능(In scope): 웹캠 실시간 입력, 한 손 검지 끝 추적, 손끝 궤적 표시, 과일·폭탄 생성과 물리 이동, 자르기 판정, 점수·콤보·목숨 시스템, 시간 기반 난이도 상승, 손동작으로 시작·재시작, 로컬 최고 점수 저장.
  (Real-time webcam input, tracking one index fingertip, drawing the trail, spawning and moving fruits and bombs, slice detection, score/combo/lives system, time-based difficulty, hand-gesture start/restart, and local high-score saving.)
- 제외할 기능(Out of scope): 두 손 동시 조작·멀티플레이어, 온라인 랭킹, 사용자 계정, 모바일·웹 버전, 과일이 실제로 갈라지는 3D 효과, 별도 AI 모델 학습(MediaPipe의 사전 학습 모델을 그대로 사용).
  (Two-hand or multiplayer play, online leaderboards, user accounts, mobile or web versions, realistic 3D splitting effects, and training our own AI model — we use MediaPipe's pretrained model as is.)
- 한계(Limitation): 조명이 어둡거나 배경이 복잡하면 손 인식이 끊기거나 좌표가 튈 수 있고, 저사양 컴퓨터에서는 인식 지연 때문에 판정이 늦게 느껴질 수 있다. 웹캠이 없는 환경에서는 실행할 수 없다.
  (Hand tracking may drop out or jitter in dim lighting or with a cluttered background, and on low-end computers the detection delay may make slices feel late. The game cannot run without a webcam.)

### 사용 예시(Usage example)

학과 홍보 부스에서 학생이 노트북 앞에 서서 `python main.py`로 게임을 실행한다. 화면에 거울처럼 비친 자신의 모습 위에 "START" 버튼이 나타나고, 검지를 버튼 위에 1초간 올려 게임을 시작한다. 날아오르는 사과와 수박을 향해 손가락을 빠르게 휘두르자 궤적이 그려지며 과일이 잘리고 점수가 오른다. 1분쯤 지나자 과일이 더 빨리, 더 많이 나오고 폭탄도 자주 섞인다. 폭탄을 실수로 베어 목숨을 모두 잃자 게임 오버 화면에 "최종 점수 42점, 최고 기록 갱신!"이 표시되고, 기록은 `highscore.json`에 저장된다. 다음 사람은 손을 "RESTART" 버튼에 올려 바로 이어서 플레이한다.
(At a department booth, a student stands in front of a laptop and runs the game with `python main.py`. A "START" button appears over their mirrored image, and they hold their index finger over it for one second to begin. As they swipe quickly at flying apples and watermelons, a trail appears, the fruits are sliced, and the score rises. After about a minute, fruits come faster and more often, with more bombs mixed in. After accidentally slicing bombs and losing all lives, the game-over screen shows "Final score 42 — new high score!", which is saved to `highscore.json`. The next person holds their hand over "RESTART" and plays right away.)
