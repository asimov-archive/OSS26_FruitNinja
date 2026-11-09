# 팀 규칙(Team Rules)

## 1. 풀 리퀘스트(PR) 규칙(Pull Request Rules)

- PR 하나는 **기능 하나, 버그 수정 하나, 또는 특정 작업 하나**에만 집중한다.
- PR은 작게 유지하며, 변경 줄 수는 **150줄 이하**를 권장한다.
- PR이 이보다 크면 나눌 수 없는 이유를 설명한다.
- 모든 PR에는 변경 내용과 테스트 방법을 간단히 적는다.
- PR 제목과 설명은 **한국어**로 작성한다.
- `main` 브랜치에 코드를 직접 push하지 않는다.

- Each PR should focus on **one feature, one bug fix, or one specific task**.
- Keep PRs small, ideally around **150 changed lines or fewer**.
- If a PR is larger, explain why it cannot be split.
- Every PR must include a brief description of the changes and how they were tested.
- PR titles and descriptions should be written in **Korean**.
- Do not push code directly to the `main` branch.

## 2. 코드 리뷰 규칙(Code Review Rules)

- 모든 PR은 머지 전에 **다른 팀원 최소 1명의 승인**을 받아야 한다.
- 리뷰어는 **48시간 이내**에 피드백을 준다.
- 해결되지 않은 치명적 문제, 실패한 테스트, 머지 충돌이 있는 PR은 머지할 수 없다.
- 리뷰어는 건설적이고 정중하게 피드백한다.
- 작성자는 머지 전에 머지를 막는 코멘트(blocking comment)를 모두 해결한다.

- Every PR requires **at least one approval from another team member** before merging.
- Reviewers should provide feedback within **48 hours**.
- A PR cannot be merged if it has unresolved critical issues, failing tests, or merge conflicts.
- Reviewers should give constructive and respectful feedback.
- The author must address blocking comments before merging.

## 3. 머지 규칙(Merge Rules)

- 승인을 받은 뒤 머지는 PR 작성자가 직접 한다.
- 커밋 기록을 깔끔하게 유지하기 위해 **Squash and Merge**를 사용한다.
- 머지 후에는 기능 브랜치를 삭제한다.
- `main` 브랜치는 항상 안정적인 상태로 유지한다.
- `main`에 절대 force-push하지 않는다.

- The PR author is responsible for merging after receiving approval.
- Use **Squash and Merge** to maintain a clean commit history.
- Delete the feature branch after merging.
- The `main` branch must always remain stable.
- Never force-push to `main`.

## 4. 브랜치 이름 규칙(Branch Naming Rules)

브랜치 이름은 아래 형식으로 통일한다.

(Use consistent branch names.)

- `feature/description` — 새 기능(New features)
- `fix/description` — 버그 수정(Bug fixes)
- `docs/description` — 문서(Documentation)
- `test/description` — 테스트(Tests)
- `chore/description` — 유지보수 작업(Maintenance tasks)

예시(Example): `feature/user-login`

## 5. 커밋 메시지 규칙(Commit Message Rules)

커밋 메시지는 `type: 짧은 설명` 형식으로 쓴다. `type` 접두어는 영어로 쓰고, 설명은 **한국어**로 짧고 명확하게 쓴다.

(Use the format `type: short description`. Keep the `type` prefix in English, and write the description in **Korean**, short and clear.)

예시(Examples):
- `feat: 로그인 기능 추가`
- `fix: 로그인 오류 수정`
- `docs: README 업데이트`
- `test: 로그인 테스트 추가`
- `refactor: 인증 코드 단순화`

## 6. 팀 소통 규칙(Team Communication Rules)

- 일상적인 소통과 간단한 질문은 **카카오톡**을 사용한다.
- 작업, 버그, 기능 요청은 **GitHub Issues**로 관리한다.
- 중요한 기술적 결정은 GitHub Issues나 PR 토론에 기록한다.
- 작업이 늦어지거나 막히면 최대한 빨리 팀에 알린다.

- Use **KakaoTalk** for daily communication and quick questions.
- Use **GitHub Issues** to track tasks, bugs, and feature requests.
- Important technical decisions must be documented in GitHub Issues or PR discussions.
- Inform the team as early as possible if a task is delayed or blocked.

## 7. AI 사용 규칙(AI Usage Rules)

- **수업에서 정한 AI 사용 공개 요건**을 따른다.
- 코드, 문서, 테스트에 AI 도움을 받았다면 수업 요건에 맞게 명확히 밝힌다.
- AI를 활용한 PR에는 사용한 AI 도구, 사용 목적, 결과 검증 방법을 적는다.
- AI가 생성한 코드는 제출자가 직접 검토하고, 이해하고, 테스트해야 한다.
- 동작을 이해하지 못한 AI 생성 결과물은 절대 제출하지 않는다.
- 민감한 정보, 인증 정보, 비공개 프로젝트 데이터를 AI 도구와 공유하지 않는다.

- Follow the **AI disclosure requirements specified by the course**.
- Clearly disclose any AI assistance used in code, documentation, or tests, as required by the course.
- For AI-assisted PRs, identify the AI tool, what it was used for, and how the result was verified.
- All AI-generated code must be reviewed, understood, and tested by the person submitting it.
- Never submit AI-generated content without understanding its functionality.
- Do not share sensitive information, credentials, or private project data with AI tools.

## 8. 동의 및 개정(Agreement and Updates)

- 이 규칙은 팀원 전원이 동의한 뒤에 적용한다.
- 규칙을 바꿀 때는 PR을 통해 팀이 논의하고 승인한다.
- 이 규칙은 모든 팀원에게 똑같이 적용된다.

- All team members must agree on these rules before adoption.
- Changes to the rules should be discussed and approved by the team through a PR.
- These rules apply equally to every team member.
