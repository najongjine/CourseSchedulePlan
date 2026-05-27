WEEKS = [
    {"week": 1, "tech": "C", "title": "입력과 판단", "project": "업다운 숫자 맞히기 게임"},
    {"week": 2, "tech": "C", "title": "배열과 함수", "project": "분식집 주문 계산기"},
    {"week": 3, "tech": "Java", "title": "값을 가진 객체", "project": "나의 용돈 지갑"},
    {"week": 4, "tech": "Java", "title": "상품 객체의 변화", "project": "음료 자판기"},
    {"week": 5, "tech": "Python", "title": "리스트로 분석하기", "project": "일주일 공부시간 분석기"},
    {"week": 6, "tech": "Python", "title": "상품과 할인 계산", "project": "장바구니 할인 계산기"},
    {"week": 7, "tech": "PostgreSQL", "title": "표준 SQL CRUD", "project": "작은 쇼핑몰 상품 DB"},
    {"week": 8, "tech": "PostgreSQL", "title": "관계와 집계", "project": "주문 및 매출 분석 DB"},
    {"week": 9, "tech": "React", "title": "화면 컴포넌트", "project": "쇼핑몰 상품 목록 화면"},
    {"week": 10, "tech": "React + API", "title": "DB 상품 연결", "project": "상품 조회 및 등록"},
    {"week": 11, "tech": "React + API", "title": "장바구니와 주문", "project": "장바구니 주문 저장"},
    {"week": 12, "tech": "통합", "title": "테스트와 발표", "project": "우리 반 미니 쇼핑몰"},
]


def L(week, day, tech, title, intro, goals, sense_title, theory, diagram, gesture,
      typing_intro, code, output, walk, modify, exam_tag, exam_intro, exam_code,
      exam_question, exam_answer, tasks, task_answer, project, project_step, check):
    if day == 5:
        flow = [
            ("1교시", "핵심 문법 미니 테스트와 손 추적"),
            ("2교시", "완성 코드를 기능별로 입력"),
            ("3교시", "실행, 오류 수정, 선택 기능"),
            ("4교시", "시연하고 자기 코드 설명"),
        ]
    else:
        flow = [
            ("1교시", "개념을 그림과 코드로 이해"),
            ("2교시", "예제를 직접 입력하고 실행"),
            ("3교시", "금요일 작품 기능 한 조각 작성"),
            ("4교시", "값을 바꾸고 손 추적 연습"),
        ]
    return {
        "week": week, "day": day, "tech": tech, "title": title, "intro": intro,
        "goals": goals, "flow": flow, "sense_title": sense_title, "theory": theory,
        "diagram": diagram, "gesture": gesture, "typing_intro": typing_intro,
        "code": code, "output": output, "walk": walk, "modify": modify,
        "exam_tag": exam_tag, "exam_intro": exam_intro, "exam_code": exam_code,
        "exam_question": exam_question, "exam_answer": exam_answer, "tasks": tasks,
        "task_answer": task_answer, "project": project, "project_step": project_step,
        "check": check,
    }


LESSONS = [
    L(1, 1, "C", "컴퓨터에게 값을 맡기는 첫날",
      "게임을 만들기 전에 컴퓨터가 문장을 출력하고 숫자를 기억하는 방식을 몸으로 익힌다.",
      ["소스 코드와 실행 결과를 구분한다.", "정수 변수에 값을 저장하고 출력한다.", "대입문 뒤 값이 바뀌는 문제를 추적한다."],
      "변수는 이름표가 붙은 한 칸짜리 상자",
      ["컴퓨터는 의미를 짐작하지 않는다. `score`라는 상자를 만들고 10을 넣으라고 적어야 10을 기억한다.",
       "`score = score + 5`는 수학 등식이 아니라, 기존 상자의 값을 꺼내 5를 더한 뒤 다시 넣으라는 명령이다."],
      [("코드", "score = 10"), ("메모리 상자", "score: 10"), ("출력", "10점")],
      "종이에 score 상자를 그리고 10, 15를 차례대로 지우고 다시 써 본다.",
      "아래 코드를 새 파일 `day1.c`에 한 줄씩 입력한다. 세미콜론과 큰따옴표도 코드의 일부다.",
      """#include <stdio.h>

int main(void) {
    int score = 10;
    printf("시작 점수: %d\\n", score);

    score = score + 5;
    printf("문제를 맞힌 뒤: %d\\n", score);
    return 0;
}""",
      "시작 점수: 10\n문제를 맞힌 뒤: 15",
      ["`int score = 10;`에서 정수를 담을 상자를 만들고 10을 넣는다.",
       "`%d` 위치에 현재 `score`의 정수 값이 들어간다.",
       "`score = score + 5;` 실행 뒤 상자에는 15가 남는다."],
      "`score`의 시작값을 20으로, 더하는 값을 3으로 바꾸고 실행 전 출력 두 줄을 먼저 예측한다.",
      "C 변수", "정보처리기사 코드 문제는 실행 뒤 변수에 남은 값을 묻는 일이 많다. 종이에 상자를 그려 추적한다.",
      """int a = 3;
int b = a + 2;
a = b * 2;
printf("%d %d", a, b);""",
      "출력되는 두 숫자는 무엇인가?",
      "`b`에는 5가 저장되고, 그 뒤 `a`에는 5 * 2인 10이 저장된다. 출력은 `10 5`이다.",
      ["`coin` 변수를 만들고 500을 저장하여 `보유 코인: 500`을 출력한다.",
       "`life`를 3으로 시작하여 1을 뺀 뒤 두 번 출력되는 값을 예상하고 실행한다.",
       "`%d`를 빠뜨리거나 세미콜론을 지우고 컴파일 오류 메시지를 관찰한 뒤 되돌린다."],
      "중요한 것은 정답보다 실행 순서다. 값이 바뀔 때마다 종이 상자의 숫자를 갱신하면 된다.",
      "금요일: 업다운 숫자 맞히기 게임",
      "오늘은 게임의 시작 화면과 `answer`, `guess`, `count`가 들어갈 메모리 상자 개념을 준비한다.",
      ["`day1.c`가 실행된다.", "변수 변화표 한 장을 작성한다."]),

    L(1, 2, "C", "키보드 입력을 숫자로 받기",
      "사용자가 숫자를 입력해야 게임이 대화하듯 반응한다. 입력이 변수에 들어가는 과정을 확인한다.",
      ["`scanf`로 정수를 입력받는다.", "입력값으로 계산한 결과를 출력한다.", "입력-저장-처리-출력 흐름을 말할 수 있다."],
      "입력은 키보드에서 변수 상자로 이동하는 배달",
      ["화면에 7을 타이핑하는 것만으로 프로그램이 그 숫자를 아는 것은 아니다. `scanf`가 숫자를 읽어 `guess` 주소의 상자에 넣는다.",
       "`&guess`의 `&`는 오늘은 'guess 상자의 위치'라고 이해한다. 깊은 포인터 설명은 나중에 한다."],
      [("키보드", "7 입력"), ("scanf", "&guess"), ("상자", "guess: 7"), ("printf", "입력: 7")],
      "한 학생이 숫자 카드를 들고, 다른 학생이 `guess` 이름표 상자 역할을 해 카드를 전달해 본다.",
      "값 두 개를 입력하고 계산해 보자. 컴파일 후 8과 3을 차례대로 입력한다.",
      """#include <stdio.h>

int main(void) {
    int first;
    int second;

    printf("첫 숫자: ");
    scanf("%d", &first);
    printf("둘째 숫자: ");
    scanf("%d", &second);

    printf("합계: %d\\n", first + second);
    printf("차이: %d\\n", first - second);
    return 0;
}""",
      "첫 숫자: 8\n둘째 숫자: 3\n합계: 11\n차이: 5",
      ["`first`, `second`는 선언 직후 아직 수업에서 믿고 쓸 값이 없는 빈 상자다.",
       "첫 번째 `scanf`가 끝나면 `first`는 8이다.",
       "출력할 때는 상자를 바꾸지 않고 두 값을 읽어 계산한다."],
      "입력을 3과 8로 바꾸면 차이가 음수가 된다. 실행하기 전에 결과를 적어 본다.",
      "C 입력/연산", "입력문이 있어도 시험 문제에서는 입력값이 주어지고, 그 뒤 계산을 손으로 수행하면 된다.",
      """int n = 4;
int result = n * 3;
result = result - n;
printf("%d", result);""",
      "`result`의 최종 출력은 무엇인가?",
      "먼저 4 * 3으로 12, 그 다음 12 - 4로 8이 된다. 출력은 `8`이다.",
      ["나이와 내년 나이를 입력/계산하는 프로그램을 작성한다.",
       "`price`와 `count`를 입력받아 결제 금액을 출력한다.",
       "게임용 `guess`를 입력받아 `당신의 선택: 숫자`를 출력한다."],
      "곱셈은 금액 계산으로, `guess` 입력은 바로 금요일 게임의 한 조각으로 다시 사용된다.",
      "금요일: 업다운 숫자 맞히기 게임",
      "게임의 사용자가 추측한 숫자를 입력받는 부분을 완성한다. 아직 정답 비교는 하지 않는다.",
      ["입력 숫자가 그대로 출력된다.", "`scanf`에서 `&`가 필요한 이유를 위치 전달이라고 설명한다."]),

    L(1, 3, "C", "조건문으로 UP과 DOWN 가르기",
      "같은 입력이라도 정답보다 작거나 큰지에 따라 다른 문장을 보여 주는 게임의 핵심 날이다.",
      ["비교식의 참과 거짓을 이해한다.", "`if / else if / else`를 작성한다.", "조건 순서가 결과에 미치는 영향을 추적한다."],
      "조건문은 세 갈래 표지판",
      ["프로그램은 모든 길을 동시에 걷지 않는다. 위에서부터 조건을 검사하여 처음 참인 길 하나만 실행한다.",
       "정답보다 작은지, 큰지, 둘 다 아닌지를 순서대로 묻으면 마지막 길은 자연스럽게 정답인 경우다."],
      [("guess", "23"), ("guess < answer?", "참"), ("선택된 길", "UP 출력")],
      "정답을 30으로 정하고 교사가 23, 45, 30 카드를 들 때 어느 길로 갈지 손으로 표시한다.",
      "정답은 우선 고정값 30으로 둔다. 세 입력을 각각 실행해 결과가 어떻게 갈리는지 확인한다.",
      """#include <stdio.h>

int main(void) {
    int answer = 30;
    int guess;

    printf("숫자를 입력하세요: ");
    scanf("%d", &guess);

    if (guess < answer) {
        printf("UP\\n");
    } else if (guess > answer) {
        printf("DOWN\\n");
    } else {
        printf("정답!\\n");
    }
    return 0;
}""",
      "숫자를 입력하세요: 23\nUP",
      ["`guess < answer`는 23 < 30이므로 참이다.",
       "첫 조건이 참이면 아래의 `else if`, `else`는 실행하지 않는다.",
       "30을 입력하면 두 비교가 모두 거짓이므로 마지막 `else`가 실행된다."],
      "`answer`를 50으로 변경하고 입력 50, 60, 40의 문구를 실행 전 각각 적는다.",
      "C 조건문", "기사 문제에서는 조건의 경계값, 특히 `<`와 `<=`의 차이를 노린다.",
      """int score = 60;
if (score > 60) {
    printf("A");
} else if (score >= 60) {
    printf("B");
} else {
    printf("C");
}""",
      "출력 문자는 무엇이며, 첫 조건이 거짓인 이유는 무엇인가?",
      "`score > 60`은 60이 60보다 크지 않으므로 거짓이다. 두 번째 `score >= 60`은 참이므로 `B`가 출력된다.",
      ["정답이 10인 홀짝 아닌 숫자 맞히기 판정 코드를 직접 작성한다.",
       "입력 가능 범위가 1~100이 아니면 `범위 오류`를 먼저 출력하도록 조건을 추가한다.",
       "`<` 하나를 `<=`로 바꿨을 때 정답 입력에서 발생하는 문제를 설명한다."],
      "정답까지 UP으로 처리되는 버그가 생길 수 있다. 경계값을 직접 입력해 보는 습관이 중요하다.",
      "금요일: 업다운 숫자 맞히기 게임",
      "입력 한 번에 대해 UP, DOWN, 정답을 출력하는 게임의 판정 엔진을 완성한다.",
      ["23, 45, 30 세 입력을 시험했다.", "조건 경계값 오류를 말로 설명한다."]),

    L(1, 4, "C", "맞힐 때까지 반복하기",
      "한 번만 묻던 프로그램에 반복을 붙여 게임처럼 만든다. 반복 전과 후의 변수값을 손으로 적는다.",
      ["`while`의 조건을 읽는다.", "반복마다 시도 횟수를 증가시킨다.", "종료 조건이 없는 반복의 위험을 이해한다."],
      "반복문은 조건이 참인 동안 도는 회전문",
      ["`while (guess != answer)`는 추측이 정답과 다른 동안 다시 질문하라는 뜻이다.",
       "매 바퀴마다 `count`를 1 늘리지 않으면 몇 번 시도했는지 알 수 없다. 상태가 바뀌지 않는 반복은 끝나지 않을 수 있다."],
      [("검사", "다른가?"), ("입력/판정", "UP 또는 DOWN"), ("count", "+1"), ("다시 검사", "정답이면 종료")],
      "손으로 원을 그리고 입력 10, 40, 30마다 원을 한 바퀴씩 짚으며 count 값을 말한다.",
      "어제의 판정을 반복문 안으로 이동한다. 이 코드는 금요일 완성본의 거의 전체 흐름이다.",
      """#include <stdio.h>

int main(void) {
    int answer = 30;
    int guess = 0;
    int count = 0;

    while (guess != answer) {
        printf("숫자 입력: ");
        scanf("%d", &guess);
        count = count + 1;

        if (guess < answer) printf("UP\\n");
        else if (guess > answer) printf("DOWN\\n");
        else printf("정답!\\n");
    }
    printf("%d번 만에 성공\\n", count);
    return 0;
}""",
      "숫자 입력: 10\nUP\n숫자 입력: 40\nDOWN\n숫자 입력: 30\n정답!\n3번 만에 성공",
      ["시작 전 `guess`는 0이어서 30과 다르므로 반복에 들어간다.",
       "각 입력 직후 `count`가 증가하므로 정답 입력도 시도 횟수에 포함된다.",
       "정답 입력 뒤 반복의 처음으로 돌아가 조건이 거짓이 되어 마지막 출력으로 이동한다."],
      "`count = count + 1;`을 조건문 안의 UP 부분으로 옮기면 입력 10, 40, 30의 횟수가 왜 잘못되는지 확인한다.",
      "C 반복 추적", "시험에서는 반복문이 끝날 때 변수에 남는 값을 묻는다. 각 바퀴마다 표 한 행을 쓴다.",
      """int i = 1;
int total = 0;
while (i <= 3) {
    total = total + i;
    i = i + 1;
}
printf("%d %d", total, i);""",
      "반복 종료 뒤 `total`과 `i`는 각각 얼마인가?",
      "i가 1, 2, 3일 때 total은 1, 3, 6이 된다. 이후 i는 4여서 조건이 거짓이다. 출력은 `6 4`이다.",
      ["입력 범위를 1~100으로 제한하고 범위 밖이면 시도 횟수에 포함할지 규칙을 정한다.",
       "반복 표에 `guess`, `count`, `출력` 열을 만들고 3회 플레이를 기록한다.",
       "정답을 처음 입력하는 경우의 출력과 count를 확인한다."],
      "반복 문제는 표를 그리면 눈으로 보인다. 첫 입력이 정답이어도 count가 1이어야 자연스럽다.",
      "금요일: 업다운 숫자 맞히기 게임",
      "필수 게임 흐름이 완성됐다. 내일은 코드를 다시 조립하고 테스트·설명을 한다.",
      ["세 번 입력 시 변수 추적표가 있다.", "정답 입력에서 반복이 종료됨을 설명한다."]),

    L(1, 5, "C", "완성: 업다운 숫자 맞히기 게임",
      "이번 주의 변수, 입력, 조건, 반복을 하나로 모아 직접 플레이할 수 있는 첫 작품을 완성한다.",
      ["빈 화면에서 완성 코드를 단계별로 입력한다.", "경계값과 종료 조건을 테스트한다.", "조건문과 반복문을 자기 말로 설명한다."],
      "게임은 입력-판정-피드백의 반복",
      ["게임이 재미있는 이유는 사용자의 입력이 바로 다음 반응을 만든다는 데 있다. 오늘의 코드는 화면은 단순하지만 실제 게임의 기본 고리를 갖는다.",
       "코드를 외우는 것이 목적이 아니다. `guess` 상자와 `count` 상자가 매 시도마다 어떻게 달라지는지 보이면 성공이다."],
      [("입력", "guess"), ("판정", "UP/DOWN"), ("기록", "count"), ("종료", "정답")],
      "친구가 입력을 말하면 기록 담당이 표에 guess와 count를 적고 실행 화면과 대조한다.",
      "먼저 필수 기능을 그대로 입력해 성공시킨 뒤, 시간이 남는 학생만 범위 오류 검사를 추가한다.",
      """#include <stdio.h>

int main(void) {
    int answer = 30;
    int guess = 0;
    int count = 0;

    printf("=== UP & DOWN ===\\n");
    while (guess != answer) {
        printf("1~100 숫자 입력: ");
        scanf("%d", &guess);

        if (guess < 1 || guess > 100) {
            printf("범위를 벗어났습니다.\\n");
            continue;
        }

        count++;
        if (guess < answer) {
            printf("UP\\n");
        } else if (guess > answer) {
            printf("DOWN\\n");
        } else {
            printf("정답!\\n");
        }
    }
    printf("시도 횟수: %d\\n", count);
    return 0;
}""",
      "=== UP & DOWN ===\n1~100 숫자 입력: 101\n범위를 벗어났습니다.\n1~100 숫자 입력: 20\nUP\n1~100 숫자 입력: 30\n정답!\n시도 횟수: 2",
      ["범위 오류 입력은 `continue`로 아래 판정과 count 증가를 건너뛴다.",
       "`count++`는 올바른 범위의 추측만 센다는 게임 규칙이다.",
       "맞힌 뒤 `guess != answer`가 거짓이 되면서 반복이 종료된다."],
      "범위 오류도 횟수에 포함하는 게임으로 규칙을 바꾸려면 `count++`를 어디로 옮겨야 하는가?",
      "C 조건/반복", "코드 추적에서는 `continue`가 아래 문장을 실행하지 않고 곧장 조건 검사로 돌아간다는 점을 놓치지 않는다.",
      """int n = 0;
int count = 0;
while (n < 5) {
    n++;
    if (n == 3) continue;
    count++;
}
printf("%d", count);""",
      "`count`의 출력값은 무엇인가?",
      "n은 1,2,3,4,5가 된다. n이 3인 바퀴만 `count++`를 건너뛰므로 총 네 번 증가하여 `4`가 출력된다.",
      ["정답 30에 대해 `101, 20, 30`을 입력하고 예상 count와 실제 count를 비교한다.",
       "정답을 77로 바꿔 친구가 플레이하게 하고 UP/DOWN 문구가 맞는지 검사한다.",
       "프로그램의 입력, 처리, 출력, 반복을 네 문장으로 적는다."],
      "필수 시연은 오류 없이 끝까지 플레이하는 것이다. 선택 기능보다 추적 설명이 우선이다.",
      "제출 작품: 업다운 숫자 맞히기 게임",
      "완성 파일과 테스트 기록을 제출한다. 다음 주에는 여러 가격을 배열에 넣어 주문 금액을 계산한다.",
      ["실행 가능한 `updown.c`", "입력 3세트 테스트표와 코드 설명"]),

    L(2, 1, "C", "같은 종류의 값을 줄 세우는 배열",
      "분식집 메뉴 세 개의 가격을 별도 변수 세 개가 아니라 배열 한 줄로 저장한다.",
      ["배열과 인덱스를 그림으로 이해한다.", "`for`로 배열을 순회한다.", "가격 목록을 출력한다."],
      "배열은 번호가 붙은 사물함 줄",
      ["가격이 세 개일 때 `price1`, `price2`, `price3`로 만들 수도 있지만, 반복해서 다루기 어렵다.",
       "`prices[0]`은 첫 칸이다. C의 배열 번호는 0부터 시작한다는 점이 코드 추적의 핵심이다."],
      [("prices[0]", "3000"), ("prices[1]", "2500"), ("prices[2]", "2000")],
      "의자 세 개에 0,1,2 번호를 붙이고 가격 카드를 올린 후 `prices[1]`을 말하면 해당 카드를 든다.",
      "가격 세 개를 배열에 넣고 반복 출력한다. 인덱스와 메뉴 번호가 다를 수 있음을 관찰한다.",
      """#include <stdio.h>

int main(void) {
    int prices[3] = {3000, 2500, 2000};
    int i;

    for (i = 0; i < 3; i++) {
        printf("%d번 칸 가격: %d원\\n", i, prices[i]);
    }
    return 0;
}""",
      "0번 칸 가격: 3000원\n1번 칸 가격: 2500원\n2번 칸 가격: 2000원",
      ["배열에는 세 칸만 있으므로 쓸 수 있는 인덱스는 0, 1, 2이다.",
       "`i++`마다 다음 칸을 읽는다.",
       "`i < 3`이 거짓인 i=3에서는 `prices[3]`을 읽지 않는다."],
      "가격을 `{3500, 3000, 1500}`으로 바꾸고, `i <= 3`으로 잘못 쓰면 왜 위험한지 설명한다.",
      "C 배열/반복", "배열 문제는 인덱스 시작과 반복 종료 조건을 먼저 표시하면 실수가 줄어든다.",
      """int a[4] = {2, 4, 6, 8};
int sum = 0;
for (int i = 1; i < 4; i++) {
    sum += a[i];
}
printf("%d", sum);""",
      "어떤 칸들이 더해지며 결과는 무엇인가?",
      "i는 1,2,3이므로 4 + 6 + 8만 더한다. `a[0]`의 2는 빠지고 결과는 `18`이다.",
      ["음료 가격 4개를 배열로 만들고 모두 출력한다.",
       "가격 배열의 모든 값을 합산하는 반복문을 작성한다.",
       "인덱스가 0부터 시작하는 이유를 오늘 코드 예로 설명한다."],
      "총합은 `sum` 상자를 0으로 놓고 각 사물함 값을 하나씩 넣어 커지게 하면 된다.",
      "금요일: 분식집 주문 계산기",
      "오늘은 금요일 메뉴판의 가격 저장 방식과 출력 반복을 만든다.",
      ["가격 배열과 출력 코드", "배열 인덱스 손 추적 문제 풀이"]),

    L(2, 2, "C", "선택 번호로 가격 꺼내기",
      "손님이 메뉴를 선택하면 배열의 올바른 칸에서 가격을 찾아 수량과 곱한다.",
      ["메뉴 번호와 배열 인덱스를 변환한다.", "수량을 곱해 소계를 구한다.", "잘못된 번호를 막는다."],
      "사람은 1번부터, 배열은 0번부터 센다",
      ["화면에는 1. 떡볶이처럼 보여 주는 편이 자연스럽다. 그러나 첫 가격은 `prices[0]`에 있다.",
       "따라서 손님 선택값 `menu`가 1이면 배열에서는 `menu - 1`칸을 꺼낸다."],
      [("손님 선택", "menu=2"), ("변환", "menu-1=1"), ("배열", "prices[1]=2500"), ("수량 3", "7500원")],
      "메뉴 카드 번호는 1부터 붙이고, 뒤집은 카드 뒷면에 배열 인덱스 0부터를 적어 비교한다.",
      "선택과 수량으로 한 주문의 소계를 출력한다.",
      """#include <stdio.h>

int main(void) {
    int prices[3] = {3000, 2500, 2000};
    int menu;
    int quantity;

    printf("1. 떡볶이  2. 김밥  3. 튀김\\n");
    printf("메뉴 번호와 수량: ");
    scanf("%d %d", &menu, &quantity);

    if (menu >= 1 && menu <= 3 && quantity > 0) {
        printf("소계: %d원\\n", prices[menu - 1] * quantity);
    } else {
        printf("잘못된 주문입니다.\\n");
    }
    return 0;
}""",
      "1. 떡볶이  2. 김밥  3. 튀김\n메뉴 번호와 수량: 2 3\n소계: 7500원",
      ["메뉴 2는 배열 인덱스 1로 바뀌어 김밥 가격 2500을 읽는다.",
       "`&&`는 두 조건이 모두 참이어야 주문 계산으로 간다는 의미다.",
       "메뉴 0을 입력하면 배열에 접근하기 전에 오류 문구로 빠진다."],
      "입력 `3 4`, `0 2`, `1 0`의 출력 결과를 실행 전 표로 작성한다.",
      "C 배열 조건", "유효성 검사를 먼저 하는 습관은 실무뿐 아니라 배열 범위 오류 이해에도 중요하다.",
      """int price[3] = {1000, 2000, 3000};
int choice = 3;
int count = 2;
printf("%d", price[choice - 1] * count);""",
      "출력값은 얼마이며 읽은 배열 위치는 어디인가?",
      "`choice - 1`은 2이며 `price[2]`는 3000이다. 수량 2를 곱해 `6000`이 출력된다.",
      ["메뉴 4개 버전을 작성하고 마지막 메뉴의 금액을 계산한다.",
       "메뉴 번호가 유효하지 않으면 배열을 읽지 않는 조건을 작성한다.",
       "`menu - 1`을 빼지 않은 코드에서 메뉴 3 선택이 왜 위험한지 말한다."],
      "선택 번호를 배열 번호로 바꾸는 한 줄이 쇼핑몰 상품 선택에도 그대로 이어진다.",
      "금요일: 분식집 주문 계산기",
      "메뉴 번호와 수량을 입력받아 소계를 만드는 기능을 저장한다.",
      ["정상/오류 입력 각 1회 테스트", "메뉴 번호와 인덱스 차이 설명"]),

    L(2, 3, "C", "계산을 함수로 포장하기",
      "주문 금액 계산을 함수로 분리하여 입력과 계산의 역할을 구분한다.",
      ["함수의 매개변수와 반환값을 구분한다.", "소계 계산 함수를 작성한다.", "호출된 함수의 값을 추적한다."],
      "함수는 값을 받아 결과를 내놓는 계산 창구",
      ["함수에 가격과 수량을 건네면 함수 안의 지역 변수로 계산하고 결과를 돌려준다.",
       "프로그램이 길어질수록 계산 규칙을 함수 한곳에 두면 읽고 고치기 쉬워진다."],
      [("호출", "calculate(2500,3)"), ("함수 안", "2500*3"), ("return", "7500"), ("total", "7500")],
      "가격 카드와 수량 카드를 창구 역할 학생에게 주고 계산 결과 카드만 되돌려 받는다.",
      "함수 선언을 `main` 위에 두고, 반환값을 변수에 담아 출력한다.",
      """#include <stdio.h>

int calculate_price(int price, int quantity) {
    int subtotal = price * quantity;
    return subtotal;
}

int main(void) {
    int prices[3] = {3000, 2500, 2000};
    int menu = 2;
    int quantity = 3;
    int total = calculate_price(prices[menu - 1], quantity);

    printf("주문 금액: %d원\\n", total);
    return 0;
}""",
      "주문 금액: 7500원",
      ["`prices[menu - 1]`가 먼저 계산되어 2500이 함수로 전달된다.",
       "함수의 `subtotal`은 함수 안에서만 사용하는 상자다.",
       "`return subtotal`의 7500이 `total` 상자에 저장된다."],
      "함수 안에서 100원을 할인하도록 `return subtotal - 100;`으로 변경하고 결과를 예측한다.",
      "C 함수", "함수 문제는 전달되는 인자값, 함수 내부 변화, 반환된 값의 저장 위치를 세 단계로 나눠 적는다.",
      """int change(int n) {
    n = n + 5;
    return n * 2;
}
int main(void) {
    int a = 3;
    int b = change(a);
    printf("%d %d", a, b);
}""",
      "`a`와 `b`는 각각 무엇이 출력되는가?",
      "함수에는 a의 값 3이 복사되어 전달된다. 함수 결과는 16이므로 b=16이고 원래 a는 3 그대로다. 출력은 `3 16`.",
      ["`add_tax(price)`처럼 가격에 10%를 더하는 정수 함수 하나를 만든다.",
       "가격과 수량을 세 가지로 바꾸어 함수 반환값을 표에 기록한다.",
       "함수에 전달된 값이 원래 변수 자체인지 복사된 값인지 오늘 예제로 설명한다."],
      "이번 단계에서는 포인터가 없으므로 함수가 바꾼 매개변수는 원래 `a`를 바꾸지 않는다.",
      "금요일: 분식집 주문 계산기",
      "소계 계산을 함수로 분리해 주문 계산기의 읽기 쉬운 핵심 부품을 만든다.",
      ["실행 가능한 함수 예제", "함수 인자/반환값 추적표"]),

    L(2, 4, "C", "누적 금액과 거스름돈",
      "주문을 두 번 받아 총액을 누적하고, 받은 돈에서 총액을 빼 거스름돈을 계산한다.",
      ["누적 변수의 변화를 추적한다.", "반복 입력과 계산 함수를 결합한다.", "결제 가능 여부를 조건으로 검사한다."],
      "총액은 주문이 지나갈 때마다 커지는 계산대 표시판",
      ["첫 주문 소계를 `total`에 넣고, 다음 주문은 기존 total 위에 더한다.",
       "받은 돈이 total보다 작으면 거스름돈을 계산하기보다 돈이 부족하다고 알려야 한다."],
      [("첫 주문", "3000"), ("total", "3000"), ("둘째 주문", "+5000"), ("total", "8000"), ("10000원", "거스름 2000")],
      "두 개의 주문 카드 금액을 차례로 total 칸에 더해 적고, 현금 카드와 비교한다.",
      "반복을 두 번만 돌려 주문을 받는 간단한 버전이다.",
      """#include <stdio.h>

int main(void) {
    int prices[3] = {3000, 2500, 2000};
    int total = 0;
    int order;

    for (order = 0; order < 2; order++) {
        int menu, quantity;
        printf("메뉴와 수량: ");
        scanf("%d %d", &menu, &quantity);
        total = total + prices[menu - 1] * quantity;
        printf("현재 총액: %d원\\n", total);
    }

    int money;
    printf("받은 돈: ");
    scanf("%d", &money);
    if (money >= total) printf("거스름돈: %d원\\n", money - total);
    else printf("금액이 부족합니다.\\n");
    return 0;
}""",
      "메뉴와 수량: 1 1\n현재 총액: 3000원\n메뉴와 수량: 2 2\n현재 총액: 8000원\n받은 돈: 10000\n거스름돈: 2000원",
      ["`total`은 반복 밖에서 0으로 한 번만 만들어져 두 주문의 값을 기억한다.",
       "두 번째 반복에서 기존 3000에 김밥 5000이 추가된다.",
       "받은 돈 비교는 모든 주문 계산이 끝난 뒤 한 번 수행한다."],
      "두 주문을 `3 2`, `1 1`로 바꾸고 받은 돈 6000을 입력했을 때 출력 흐름을 예상한다.",
      "C 누적/반복", "누적 변수는 초깃값을 무엇으로 두는지와 반복마다 어떤 값을 더하는지 표시한다.",
      """int total = 0;
int a[3] = {2, 5, 3};
for (int i = 0; i < 3; i++) {
    total = total + a[i] * i;
}
printf("%d", total);""",
      "`total`의 출력값은 무엇인가?",
      "i=0일 때 0, i=1일 때 5, i=2일 때 6을 더한다. total은 `11`이다.",
      ["주문 횟수를 3으로 바꾸고 총액 변화표를 작성한다.",
       "돈 부족 입력과 충분한 입력을 각각 시험한다.",
       "유효하지 않은 메뉴를 막는 조건을 반복 안에 추가할 위치를 표시한다."],
      "내일 완성본에서는 잘못된 메뉴 접근을 막고 계산 함수를 결합한다.",
      "금요일: 분식집 주문 계산기",
      "여러 주문의 누적 합계와 결제/거스름돈 흐름까지 연결했다.",
      ["두 주문 총액 출력 성공", "누적 변수 추적표"]),

    L(2, 5, "C", "완성: 분식집 주문 계산기",
      "배열, 반복, 함수, 조건을 사용하여 메뉴를 골라 결제하는 콘솔 프로그램을 완성한다.",
      ["메뉴 가격 배열과 계산 함수를 조립한다.", "정상/오류/돈 부족 상황을 검사한다.", "배열과 함수 문제를 손으로 푼다."],
      "주문 프로그램도 입력-검사-계산-출력의 순서",
      ["프로그램은 먼저 메뉴 번호가 안전한지 검사하고, 안전할 때만 배열에서 가격을 꺼낸다.",
       "화면은 단순하지만 상품 목록, 선택, 금액 계산은 나중 쇼핑몰에서도 그대로 되풀이된다."],
      [("메뉴/수량 입력", "2, 2"), ("검사", "유효함"), ("함수 계산", "2500*2"), ("결제", "5000원")],
      "테스트 담당과 실행 담당으로 짝을 지어 정상 주문, 잘못된 메뉴, 돈 부족 카드를 한 장씩 시험한다.",
      "필수 기능은 한 번의 주문으로 제한해 학생이 처음부터 끝까지 직접 입력할 수 있게 한다.",
      """#include <stdio.h>

int calculate_price(int price, int quantity) {
    return price * quantity;
}

int main(void) {
    int prices[3] = {3000, 2500, 2000};
    int menu, quantity, total, money;

    printf("=== 분식집 ===\\n");
    printf("1. 떡볶이 3000원\\n2. 김밥 2500원\\n3. 튀김 2000원\\n");
    printf("메뉴 번호와 수량: ");
    scanf("%d %d", &menu, &quantity);

    if (menu < 1 || menu > 3 || quantity < 1) {
        printf("주문을 확인하세요.\\n");
        return 0;
    }

    total = calculate_price(prices[menu - 1], quantity);
    printf("총액: %d원\\n받은 돈: ", total);
    scanf("%d", &money);

    if (money >= total) printf("거스름돈: %d원\\n", money - total);
    else printf("돈이 %d원 부족합니다.\\n", total - money);
    return 0;
}""",
      "=== 분식집 ===\n1. 떡볶이 3000원\n2. 김밥 2500원\n3. 튀김 2000원\n메뉴 번호와 수량: 2 2\n총액: 5000원\n받은 돈: 10000\n거스름돈: 5000원",
      ["오류 조건은 `||`로 연결되어 하나라도 잘못되면 즉시 종료한다.",
       "검사를 통과한 경우에만 `prices[menu - 1]`을 읽는다.",
       "함수 반환값이 total에 들어간 후 돈과 비교된다."],
      "선택 기능으로 주문을 두 번 받으려면 `total`을 0으로 시작하고 어느 부분을 반복해야 하는지 상자로 표시한다.",
      "C 배열/함수", "함수와 배열이 함께 등장하면 먼저 함수로 넘어가는 실제 인자값을 구한 뒤 반환값을 기록한다.",
      """int calc(int a[], int n) {
    int result = 0;
    for (int i = 0; i < n; i++) result += a[i];
    return result;
}
int main(void) {
    int price[3] = {3, 2, 5};
    printf("%d", calc(price, 2));
}""",
      "출력값은 무엇인가? 배열의 몇 칸까지 더해지는가?",
      "함수에는 n=2가 전달되어 i=0,1만 순회한다. 3+2인 `5`가 출력되고 세 번째 값 5는 더하지 않는다.",
      ["메뉴 1/수량 2/현금 10000의 거스름돈을 확인한다.",
       "메뉴 4를 입력해 배열 접근 없이 오류가 출력되는지 확인한다.",
       "코드에서 배열, 함수, 조건문, 입력을 서로 다른 색으로 표시한다."],
      "색으로 기능을 나누면 긴 코드도 작은 역할들의 합으로 읽을 수 있다.",
      "제출 작품: 분식집 주문 계산기",
      "C 구간을 마친다. 다음 주에는 같은 값 변경 로직을 Java 객체의 `balance`로 옮긴다.",
      ["실행 가능한 `snack_shop.c`", "C 핵심 코드 추적 미니 테스트"]),

    L(3, 1, "Java", "Java로 다시 만나는 입력과 출력",
      "새 언어지만 값 저장과 입력/출력의 원리는 C와 같다. 문법 모양의 차이를 먼저 비교한다.",
      ["Java 프로그램의 시작점을 찾는다.", "`Scanner`로 정수를 입력받는다.", "C와 Java의 같은 역할 코드를 연결한다."],
      "언어가 바뀌어도 입력-처리-출력 뼈대는 같다",
      ["C의 `printf`, `scanf`와 Java의 `System.out.println`, `Scanner`는 생김새가 다르지만 사용자와 값을 주고받는 역할은 같다.",
       "Java는 코드를 `class`라는 큰 상자 안에 적고 `main`에서 실행을 시작한다."],
      [("키보드", "10000"), ("Scanner", "nextInt()"), ("balance", "10000"), ("화면", "잔액 출력")],
      "C에서 쓰던 입력/출력 문장과 Java 문장을 좌우로 적고 서로 선으로 연결한다.",
      "`WalletApp.java` 파일로 저장하고 클래스 이름과 파일 이름을 같게 맞춘다.",
      """import java.util.Scanner;

public class WalletApp {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int balance;

        System.out.print("시작 용돈: ");
        balance = scanner.nextInt();
        System.out.println("현재 잔액: " + balance + "원");
    }
}""",
      "시작 용돈: 10000\n현재 잔액: 10000원",
      ["`new Scanner(System.in)`은 키보드 입력을 읽을 도구를 만든다.",
       "`nextInt()`가 읽은 정수는 `balance` 변수에 저장된다.",
       "문자열 뒤의 `+ balance`는 출력 문장에 숫자를 이어 붙인다."],
      "시작 용돈을 5000으로 입력하고, 잔액 뒤에 `공부 파이팅` 문장을 추가해 출력한다.",
      "Java 변수/연산", "Java 코드 문제도 대입 순서와 출력 조합을 묻는다. 새 문법 표면에 겁먹지 않고 값을 쫓는다.",
      """int money = 1000;
money = money + 500;
money -= 200;
System.out.print(money);""",
      "최종 출력되는 잔액은 얼마인가?",
      "1000에서 500을 더해 1500, 200을 빼 1300이다. 출력은 `1300`.",
      ["입금 금액 하나를 추가 입력받아 잔액과 합산 출력한다.",
       "C의 `int balance`와 Java의 `int balance`가 같은 점을 적는다.",
       "`+`가 숫자 더하기로 쓰일 때와 문자열 연결로 쓰일 때 예를 각각 만든다."],
      "문자열이 먼저 나오면 숫자가 출력 문장에 이어지고, 두 정수끼리면 먼저 계산된다.",
      "금요일: 나의 용돈 지갑",
      "지갑의 시작 잔액을 입력하고 보여 주는 첫 화면을 만든다.",
      ["`WalletApp.java` 실행", "C/Java 입력 문법 비교 메모"]),

    L(3, 2, "Java", "조건문으로 지출 허락하기",
      "가진 돈보다 더 많이 쓸 수 없게 만드는 규칙을 Java 조건문으로 구현한다.",
      ["지출 가능 조건을 식으로 작성한다.", "필드가 아닌 지역 변수로 먼저 계산한다.", "분기 후 잔액 변화를 추적한다."],
      "조건문은 지갑 문 앞의 확인 직원",
      ["지출 금액이 잔액 이하일 때만 돈을 뺀다. 거절된 지출은 잔액을 바꾸면 안 된다.",
       "조건문을 읽을 때는 '어떤 경우에 상자의 값이 바뀌는가'를 표시한다."],
      [("잔액", "5000"), ("지출", "2000"), ("가능?", "참"), ("새 잔액", "3000")],
      "잔액 카드와 지출 카드 두 장을 비교하여 허락이면 잔액 카드를 새 값으로 교체한다.",
      "오늘은 아직 클래스 없이 조건 규칙만 정확히 만든다.",
      """import java.util.Scanner;

public class SpendPractice {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int balance = 5000;

        System.out.print("쓸 금액: ");
        int amount = scanner.nextInt();

        if (amount <= balance) {
            balance = balance - amount;
            System.out.println("지출 완료");
        } else {
            System.out.println("잔액 부족");
        }
        System.out.println("남은 돈: " + balance + "원");
    }
}""",
      "쓸 금액: 2000\n지출 완료\n남은 돈: 3000원",
      ["2000 <= 5000은 참이므로 뺄셈 문장이 실행된다.",
       "6000을 입력하면 `else`로 가며 balance는 여전히 5000이다.",
       "마지막 출력은 어느 길을 지나든 실행된다."],
      "입력 5000은 허용되는가? `<=`를 `<`로 바꾸면 같은 입력에서 결과가 어떻게 달라지는가?",
      "Java 조건문", "경계값은 C와 Java 모두 단골 문제다. 정확히 같은 금액을 쓸 수 있는지 조건 기호를 본다.",
      """int balance = 3000;
int amount = 3000;
if (amount < balance) {
    balance -= amount;
} else {
    balance += 100;
}
System.out.print(balance);""",
      "출력은 얼마이며, 지출이 되지 않은 이유는 무엇인가?",
      "`amount < balance`는 같은 값일 때 거짓이다. else에서 100을 더하므로 `3100`이 출력된다.",
      ["입금 기능을 조건문 없이 한 줄로 추가한다.",
       "음수 지출을 입력하면 돈이 늘어나는 문제를 발견하고 `amount > 0` 조건을 결합한다.",
       "정상 지출, 잔액과 같은 지출, 잔액 초과 지출을 표로 기록한다."],
      "입력 검사는 코드를 복잡하게 하는 장식이 아니라 값의 규칙을 지키는 문이다.",
      "금요일: 나의 용돈 지갑",
      "입력된 지출 금액을 검사하여 잔액을 변경하는 규칙을 준비한다.",
      ["세 경계값 테스트표", "잔액 변경 조건 설명"]),

    L(3, 3, "Java", "지갑을 객체로 만들기",
      "잔액이라는 값과 입금·확인 기능을 `Wallet` 클래스 한곳에 모은다.",
      ["클래스와 객체의 차이를 말한다.", "필드와 메서드를 작성한다.", "객체의 필드값 변화를 확인한다."],
      "클래스는 지갑 설계도, 객체는 실제 내 지갑",
      ["`Wallet` 클래스는 어떤 지갑도 가질 수 있는 잔액과 행동을 정의한 설계도다.",
       "`new Wallet()`을 실행해야 실제 메모리에 잔액을 가진 지갑 객체 하나가 생긴다."],
      [("설계도", "Wallet"), ("new", "실제 생성"), ("myWallet", "balance=0"), ("deposit(5000)", "balance=5000")],
      "종이에 지갑 설계도를 한 장 그리고, 학생 이름이 붙은 실제 지갑 상자 두 개를 따로 그린다.",
      "한 파일에 `Wallet` 클래스와 실행 클래스 `WalletApp`을 함께 작성한다.",
      """class Wallet {
    int balance = 0;

    void deposit(int amount) {
        balance = balance + amount;
    }

    void showBalance() {
        System.out.println("잔액: " + balance + "원");
    }
}

public class WalletApp {
    public static void main(String[] args) {
        Wallet myWallet = new Wallet();
        myWallet.deposit(5000);
        myWallet.showBalance();
    }
}""",
      "잔액: 5000원",
      ["`new Wallet()` 뒤 객체 안의 `balance`는 0으로 시작한다.",
       "`myWallet.deposit(5000)`은 myWallet 객체의 balance를 변경한다.",
       "메서드 앞의 `myWallet.`은 어느 지갑에 행동을 시킬지 지정한다."],
      "`Wallet friendWallet = new Wallet();`을 하나 더 만들어 3000원을 넣는다. 두 지갑 잔액이 섞이지 않는지 확인한다.",
      "Java 객체", "객체 문제는 객체마다 필드 상자를 따로 그린 뒤 어떤 객체의 메서드인지 표시한다.",
      """class Box {
    int value = 1;
    void add(int n) { value += n; }
}
Box a = new Box();
Box b = new Box();
a.add(3);
b.add(5);
System.out.print(a.value + " " + b.value);""",
      "`a.value`와 `b.value`는 무엇인가?",
      "두 객체는 각자의 value를 가진다. a는 1+3=4, b는 1+5=6이므로 `4 6`이다.",
      ["`Wallet`에 1000원을 입금하는 호출을 두 번 실행하고 잔액을 예상한다.",
       "두 Wallet 객체를 만들어 서로 다른 금액을 넣는다.",
       "설계도와 실제 객체의 차이를 친구에게 한 문장으로 설명한다."],
      "한 설계도로 여러 지갑을 만들 수 있지만, 각 지갑의 잔액 상자는 별개다.",
      "금요일: 나의 용돈 지갑",
      "잔액과 입금 기능을 가진 `Wallet` 객체를 프로그램 중심으로 삼는다.",
      ["`Wallet` 객체 실행 코드", "객체별 필드 추적 그림"]),

    L(3, 4, "Java", "메뉴를 반복하고 지출 메서드 붙이기",
      "지갑 객체에 지출 규칙을 넣고 사용자가 종료할 때까지 메뉴를 반복한다.",
      ["지출 메서드가 필드를 안전하게 바꾼다.", "`while` 메뉴를 구성한다.", "객체 메서드 호출 순서를 추적한다."],
      "객체가 스스로 규칙을 지키게 한다",
      ["지갑 밖에서 잔액을 마구 빼기보다 `spend` 메서드가 돈이 충분한지 확인한 뒤 변경하게 만든다.",
       "사용자는 메뉴 번호를 선택하고, 반복문은 종료 번호를 선택할 때까지 다시 메뉴를 보여 준다."],
      [("메뉴 선택", "2 지출"), ("spend", "잔액 검사"), ("balance", "감소/유지"), ("다음 메뉴", "반복")],
      "메뉴 1=입금, 2=지출, 3=확인, 0=종료 카드를 순서대로 들며 지갑 상자를 갱신한다.",
      "금요일 완성본 직전 코드다. `spend`의 조건과 반복 종료를 유심히 본다.",
      """class Wallet {
    int balance;
    void deposit(int amount) { balance += amount; }
    void spend(int amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            System.out.println("사용 완료");
        } else {
            System.out.println("사용할 수 없습니다.");
        }
    }
}

public class WalletMenu {
    public static void main(String[] args) {
        Wallet wallet = new Wallet();
        wallet.deposit(10000);
        wallet.spend(3000);
        wallet.spend(9000);
        System.out.println(wallet.balance);
    }
}""",
      "사용 완료\n사용할 수 없습니다.\n7000",
      ["처음 입금 후 balance는 10000이다.",
       "3000 지출은 성공하여 7000으로 줄어든다.",
       "9000 지출은 현재 잔액보다 크므로 거절되고 7000이 유지된다."],
      "입금을 5000, 지출을 5000으로 바꿨을 때 잔액과 메시지를 예측한다.",
      "Java 메서드", "메서드 호출이 여러 번이면 호출 직후마다 객체 필드를 한 행씩 기록한다.",
      """class Account {
    int money = 100;
    void use(int n) {
        if (money >= n) money -= n;
        else money += 10;
    }
}
Account a = new Account();
a.use(60);
a.use(50);
System.out.print(a.money);""",
      "최종 `money`의 값은 무엇인가?",
      "첫 사용 뒤 40이 남는다. 두 번째 50은 부족하므로 10을 더하여 50이 된다. 출력은 `50`.",
      ["Scanner 메뉴 반복의 의사코드를 `선택 입력 -> 메서드 실행 -> 다시 메뉴` 순서로 적는다.",
       "지출 0 또는 음수를 거부하는 조건을 시험한다.",
       "필드값이 바뀌는 메서드 줄에 형광펜 표시를 한다."],
      "객체 코드를 읽을 때 모든 줄보다 필드를 바꾸는 줄을 먼저 찾으면 흐름이 빠르게 보인다.",
      "금요일: 나의 용돈 지갑",
      "지갑의 입금/지출 규칙이 완성됐다. 내일 반복 메뉴와 합쳐 시연한다.",
      ["입금/지출 테스트 결과", "객체 필드 변화표"]),

    L(3, 5, "Java", "완성: 나의 용돈 지갑",
      "사용자가 입금과 지출을 선택하며 잔액을 관리하는 첫 Java 객체 프로그램을 완성한다.",
      ["객체와 메뉴 반복을 조립한다.", "입력별 잔액을 테스트한다.", "객체 코드 추적 문제를 해결한다."],
      "화면 메뉴는 객체에게 명령을 전달하는 리모컨",
      ["메뉴 자체가 돈을 보관하는 것이 아니다. 사용자가 1을 누르면 `wallet.deposit`, 2를 누르면 `wallet.spend`를 호출한다.",
       "필드의 주인은 Wallet 객체 하나라는 사실이 보이면 Java 객체지향의 첫 감각을 잡은 것이다."],
      [("사용자", "메뉴 2"), ("main", "wallet.spend"), ("객체", "balance 변경"), ("출력", "잔액")],
      "한 학생은 사용자, 한 학생은 main 리모컨, 한 학생은 Wallet 잔액판 역할로 실행한다.",
      "클래스 코드 먼저 입력하고 컴파일한 뒤 메뉴 코드를 천천히 입력한다.",
      """import java.util.Scanner;

class Wallet {
    int balance;
    void deposit(int amount) { balance += amount; }
    void spend(int amount) {
        if (amount > 0 && amount <= balance) balance -= amount;
        else System.out.println("지출할 수 없습니다.");
    }
    void show() { System.out.println("잔액: " + balance + "원"); }
}

public class WalletApp {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Wallet wallet = new Wallet();
        int menu = -1;
        while (menu != 0) {
            System.out.print("1.입금 2.지출 3.잔액 0.종료: ");
            menu = sc.nextInt();
            if (menu == 1) {
                System.out.print("금액: ");
                wallet.deposit(sc.nextInt());
            } else if (menu == 2) {
                System.out.print("금액: ");
                wallet.spend(sc.nextInt());
            } else if (menu == 3) {
                wallet.show();
            }
        }
        wallet.show();
    }
}""",
      "1.입금 2.지출 3.잔액 0.종료: 1\n금액: 10000\n1.입금 2.지출 3.잔액 0.종료: 2\n금액: 3000\n1.입금 2.지출 3.잔액 0.종료: 0\n잔액: 7000원",
      ["`wallet` 객체는 반복 전에 한 번 생성되므로 메뉴가 반복되어도 잔액을 유지한다.",
       "메뉴가 1 또는 2일 때만 추가 금액 입력을 읽는다.",
       "0을 입력하면 다음 조건 검사에서 반복이 끝나고 마지막 잔액을 출력한다."],
      "지출 성공 메시지를 `spend` 안에 추가한다. 어느 곳에 넣어야 실패 때 출력되지 않는가?",
      "Java 객체/반복", "객체와 반복이 결합된 문제에서는 객체 필드를 별도 열에 두고 메뉴별 변경을 적는다.",
      """class Counter {
    int n = 1;
    void twice() { n = n * 2; }
}
Counter c = new Counter();
for (int i = 0; i < 3; i++) c.twice();
System.out.print(c.n);""",
      "최종 출력값은 무엇인가?",
      "n은 시작 1에서 반복마다 2, 4, 8로 변한다. 출력은 `8`이다.",
      ["입금 10000, 지출 3000, 잔액 조회, 종료 순서로 시연한다.",
       "잔액보다 큰 지출이 거절되는지 시험한다.",
       "객체, 필드, 메서드를 내 지갑 코드에서 각각 찾아 표시한다."],
      "기능을 추가하기보다 객체 하나가 값을 유지하며 바꾸는 모습을 설명할 수 있는지가 기준이다.",
      "제출 작품: 나의 용돈 지갑",
      "완성 Java 파일과 호출 순서 기록을 제출한다. 다음 주에는 상품 객체 여러 개를 사용한다.",
      ["실행 가능한 `WalletApp.java`", "객체/메서드 코드 추적 테스트"]),

    L(4, 1, "Java", "상품 하나를 객체로 표현하기",
      "자판기 상품을 이름, 가격, 재고라는 값 묶음으로 만든다.",
      ["생성자가 처음 값을 넣는 역할을 이해한다.", "상품 객체의 필드를 출력한다.", "하나의 현실 대상을 코드 값으로 옮긴다."],
      "상품 객체는 이름표, 가격표, 재고 칸을 가진 작은 상자",
      ["음료 하나에는 함께 움직이는 값이 세 개 있다. 클래스는 이 값을 따로 흩어 놓지 않고 한 객체로 묶는다.",
       "생성자는 새 상품을 만드는 순간 이름·가격·재고를 처음 채우는 입고 작업이다."],
      [("new Drink", "콜라,1200,3"), ("name", "콜라"), ("price", "1200"), ("stock", "3")],
      "실제 음료 그림 아래 이름/가격/재고 포스트잇 세 장을 붙여 한 상품 묶음을 만든다.",
      "상품 객체 한 개를 만들고 정보를 출력한다.",
      """class Drink {
    String name;
    int price;
    int stock;

    Drink(String name, int price, int stock) {
        this.name = name;
        this.price = price;
        this.stock = stock;
    }

    void show() {
        System.out.println(name + " " + price + "원 / 재고 " + stock);
    }
}

public class VendingStart {
    public static void main(String[] args) {
        Drink cola = new Drink("콜라", 1200, 3);
        cola.show();
    }
}""",
      "콜라 1200원 / 재고 3",
      ["생성자 매개변수 `name`을 `this.name` 필드에 넣는다.",
       "`cola` 객체 안에는 콜라, 1200, 3이 함께 저장된다.",
       "`show()`는 값을 바꾸지 않고 현재 상태를 출력한다."],
      "사이다 상품 객체를 하나 더 만들고 가격 1000, 재고 2를 출력한다.",
      "Java 생성자", "시험에서는 생성자가 필드를 어떻게 초기화하는지, 객체별 값이 무엇인지 물을 수 있다.",
      """class Item {
    int price;
    Item(int price) { this.price = price + 100; }
}
Item a = new Item(500);
Item b = new Item(700);
System.out.print(a.price + b.price);""",
      "출력되는 합계는 얼마인가?",
      "a.price는 600, b.price는 800으로 초기화된다. 합계 `1400`이 출력된다.",
      ["물, 커피 상품 객체를 각각 생성하고 출력한다.",
       "`this.price = price;`를 `price = price;`로 바꿔 결과를 관찰하고 왜 필드가 안 채워지는지 묻는다.",
       "상품 하나의 필드를 그림으로 그린다."],
      "`this`는 지금 만들어지는 객체 자신의 칸을 가리킨다.",
      "금요일: 음료 자판기",
      "자판기에 들어갈 상품 객체의 설계도를 완성한다.",
      ["`Drink` 클래스 파일", "생성자 초기화 추적 답안"]),

    L(4, 2, "Java", "상품 세 개를 배열에 진열하기",
      "음료 세 객체를 배열 한 줄에 넣고 반복문으로 메뉴판을 출력한다.",
      ["객체 배열을 생성한다.", "반복하며 상품 필드를 읽는다.", "선택 번호와 배열 위치를 연결한다."],
      "객체 배열은 자판기 진열대",
      ["C에서 가격만 배열에 넣었다면, 이제 각 칸에는 이름·가격·재고를 함께 가진 객체가 들어간다.",
       "첫 버튼을 1번으로 보여 주더라도 첫 상품은 배열의 0번 칸이다."],
      [("drinks[0]", "콜라 객체"), ("drinks[1]", "사이다 객체"), ("drinks[2]", "물 객체")],
      "세 상품 카드에 뒷면 인덱스 0,1,2를 적고 메뉴 표시 번호 1,2,3과 나란히 둔다.",
      "어제 작성한 `Drink` 클래스 아래 main 부분에서 배열을 사용한다.",
      """public class VendingMenu {
    public static void main(String[] args) {
        Drink[] drinks = {
            new Drink("콜라", 1200, 3),
            new Drink("사이다", 1000, 2),
            new Drink("물", 800, 5)
        };

        for (int i = 0; i < drinks.length; i++) {
            System.out.println((i + 1) + ". " + drinks[i].name
                + " " + drinks[i].price + "원");
        }
    }
}""",
      "1. 콜라 1200원\n2. 사이다 1000원\n3. 물 800원",
      ["`drinks.length`는 배열 칸 수 3이다.",
       "`drinks[i].name`은 i번 칸 객체의 이름 필드를 읽는다.",
       "화면 번호는 사용자에게 자연스럽게 보이도록 `i + 1`이다."],
      "네 번째 음료를 배열 끝에 추가하면 반복 조건을 고칠 필요가 없는 이유를 확인한다.",
      "Java 객체 배열", "객체 배열에서도 배열 인덱스 추적법은 C와 같다. 읽은 칸 안의 필드를 한 단계 더 확인한다.",
      """class Product {
    int price;
    Product(int p) { price = p; }
}
Product[] list = {new Product(2), new Product(4), new Product(6)};
int sum = 0;
for (int i = 0; i < list.length; i += 2) sum += list[i].price;
System.out.print(sum);""",
      "어떤 상품 가격이 더해지고 결과는 무엇인가?",
      "i는 0 다음 2가 된다. 가격 2와 6을 더해 `8`이 출력된다.",
      ["음료 네 개를 진열하는 배열을 만든다.",
       "가장 비싼 상품의 이름을 눈으로 찾아 출력 문장을 작성한다.",
       "선택 번호 2가 배열의 어느 객체인지 적는다."],
      "목요일 구매 기능은 `drinks[choice - 1]` 객체의 재고를 직접 바꾸게 된다.",
      "금요일: 음료 자판기",
      "상품 객체 세 개가 반복 출력되는 메뉴판을 완성한다.",
      ["상품 배열 메뉴 출력", "객체 배열 추적 문제"]),

    L(4, 3, "Java", "돈과 재고를 검사해 판매하기",
      "선택된 음료가 있고 돈과 재고가 충분할 때만 재고를 줄인다.",
      ["구매 조건을 순서대로 검사한다.", "객체 필드 `stock`을 변경한다.", "잔돈을 계산한다."],
      "판매는 세 개의 문을 통과해야 성공",
      ["먼저 선택 번호가 존재해야 하고, 다음으로 재고가 있어야 하며, 마지막으로 돈이 충분해야 한다.",
       "판매에 성공했을 때만 stock을 줄여야 사용자가 받지 못한 음료의 재고가 사라지지 않는다."],
      [("선택", "유효?"), ("재고", "stock > 0?"), ("돈", "money >= price?"), ("판매", "stock--")],
      "세 문을 종이에 그리고 잘못된 번호, 품절, 돈 부족, 성공 카드를 각각 어디서 멈추는지 놓는다.",
      "상품 한 개를 선택했다고 가정하고 판매 메서드를 붙인다.",
      """class Drink {
    String name;
    int price;
    int stock;
    Drink(String n, int p, int s) { name = n; price = p; stock = s; }

    void buy(int money) {
        if (stock == 0) {
            System.out.println("품절입니다.");
        } else if (money < price) {
            System.out.println("돈이 부족합니다.");
        } else {
            stock--;
            System.out.println(name + " 판매 / 잔돈 " + (money - price));
        }
    }
}

public class BuyTest {
    public static void main(String[] args) {
        Drink water = new Drink("물", 800, 1);
        water.buy(1000);
        water.buy(1000);
        System.out.println("남은 재고: " + water.stock);
    }
}""",
      "물 판매 / 잔돈 200\n품절입니다.\n남은 재고: 0",
      ["첫 구매 전 stock은 1이라 판매 성공 후 0이 된다.",
       "두 번째 호출은 돈이 충분해도 stock이 0이라 첫 조건에서 멈춘다.",
       "실패 경로에서는 `stock--`가 실행되지 않는다."],
      "초기 재고 2, 첫 돈 500, 둘째 돈 1000으로 바꾸면 최종 재고는 얼마인지 예상한다.",
      "Java 필드 변화", "객체 상태를 바꾸는 코드에서는 성공 경로와 실패 경로마다 필드값을 따로 기록한다.",
      """class Item {
    int stock = 2;
    void sell(int n) {
        if (stock >= n) stock -= n;
        else stock++;
    }
}
Item x = new Item();
x.sell(1);
x.sell(2);
System.out.print(x.stock);""",
      "최종 재고는 얼마인가?",
      "처음 2에서 1개 판매해 1이다. 두 번째 2개 판매는 불가하므로 else에서 1 증가하여 `2`가 출력된다.",
      ["가격보다 100원 부족한 돈을 넣어 stock이 그대로인지 확인한다.",
       "재고 0인 객체를 만들어 품절 메시지를 확인한다.",
       "성공했을 때만 실행되어야 할 줄을 코드에서 동그라미 친다."],
      "판매 규칙은 나중 DB 재고 감소의 전 단계다. 성공하지 않은 주문은 재고를 바꾸지 않는다.",
      "금요일: 음료 자판기",
      "음료 객체가 스스로 구매 가능 여부를 판정하고 재고를 줄이게 한다.",
      ["구매 메서드 실행", "성공/품절/돈 부족 테스트표"]),

    L(4, 4, "Java", "상속과 재정의는 짧게 읽어 보기",
      "자판기 필수 기능에 욕심을 더하지 않고, 시험에 나오는 오버라이딩의 출력 흐름을 할인 음료 한 개로 체험한다.",
      ["상속은 기존 특징을 이어받는 것임을 안다.", "재정의된 메서드가 선택되는 과정을 본다.", "필수 작품과 시험 연습 범위를 구분한다."],
      "같은 '가격 알려줘' 요청에 할인 상품은 다른 답을 한다",
      ["일반 음료는 원래 가격을 돌려주고, 할인 음료는 같은 `getPrice()` 이름으로 할인 가격을 돌려준다.",
       "프로젝트 필수 기능은 일반 Drink로 충분하다. 오늘 코드는 정보처리기사 Java 추적 연습을 위한 작은 확장이다."],
      [("Drink 참조", "getPrice()"), ("실제 객체", "SaleDrink"), ("재정의", "가격-200"), ("결과", "800")],
      "일반 상품 카드와 할인 스티커 상품 카드를 놓고 같은 가격 질문에 서로 다른 답 카드를 내민다.",
      "부모와 자식 클래스를 최소 코드로 입력하여 출력 결과를 확인한다.",
      """class Drink {
    int price;
    Drink(int price) { this.price = price; }
    int getPrice() { return price; }
}

class SaleDrink extends Drink {
    SaleDrink(int price) { super(price); }
    int getPrice() { return price - 200; }
}

public class OverrideTest {
    public static void main(String[] args) {
        Drink normal = new Drink(1000);
        Drink sale = new SaleDrink(1000);
        System.out.println(normal.getPrice());
        System.out.println(sale.getPrice());
    }
}""",
      "1000\n800",
      ["`sale` 변수의 타입은 Drink이지만 실제 만들어진 객체는 SaleDrink이다.",
       "실제 객체가 재정의한 `getPrice()`가 실행되어 800을 반환한다.",
       "자판기에 반드시 붙일 기능은 아니며 코드 읽기 문제에 대비한 예다."],
      "할인 금액을 300으로 바꾸어 출력값을 먼저 예측한 다음 실행한다.",
      "Java 오버라이딩", "기사형 Java 문제에서 부모 타입 변수에 자식 객체가 들어가면 재정의된 메서드 호출을 특히 확인한다.",
      """class A {
    int value() { return 1; }
}
class B extends A {
    int value() { return 3; }
}
A x = new B();
System.out.print(x.value() + 2);""",
      "출력값은 무엇인가?",
      "`x`가 가리키는 실제 객체는 B이므로 B의 value()가 3을 반환한다. 2를 더해 `5`가 출력된다.",
      ["`SaleDrink(1500)`의 할인 가격을 출력한다.",
       "일반 음료와 할인 음료를 한 배열에 넣고 가격을 두 줄 출력한다.",
       "상속 기능을 금요일 필수 코드에서 빼도 자판기가 작동하는 이유를 적는다."],
      "시험에 필요한 개념과 초보자가 완성할 프로젝트 필수 범위를 분리하는 것이 진도 관리의 핵심이다.",
      "금요일: 음료 자판기",
      "필수 자판기는 일반 상품 구매로 완성하고, 빠른 학생만 할인 음료를 선택 기능으로 붙인다.",
      ["오버라이딩 출력 예측 답", "필수/선택 기능 구분표"]),

    L(4, 5, "Java", "완성: 음료 자판기",
      "상품 객체 배열, 선택, 돈 검사, 재고 변화를 묶어 작동하는 자판기를 완성한다.",
      ["상품 목록에서 하나를 선택해 구매한다.", "오류와 품절을 시험한다.", "생성자·객체 배열·메서드 추적을 복습한다."],
      "자판기는 상품 객체의 상태를 바꾸는 프로그램",
      ["버튼을 누르는 것은 배열에서 객체 하나를 고르는 일이고, 판매는 그 객체의 stock을 한 개 줄이는 일이다.",
       "한 번의 판매가 확실히 동작하고 설명되면 성공이다. 반복 구매나 할인은 선택으로 남긴다."],
      [("배열", "상품 3개"), ("선택", "choice-1"), ("buy", "검사"), ("객체 stock", "-1")],
      "친구가 상품 번호와 돈을 불러 주면 배열 위치와 stock 변경을 종이에 기록한 뒤 실행 결과와 비교한다.",
      "코드가 길어 보이면 `Drink` 설계도와 `main` 사용 부분을 나누어 입력한다.",
      """import java.util.Scanner;

class Drink {
    String name;
    int price;
    int stock;
    Drink(String n, int p, int s) { name = n; price = p; stock = s; }
    void show(int no) {
        System.out.println(no + ". " + name + " " + price + "원 (" + stock + "개)");
    }
    void buy(int money) {
        if (stock < 1) System.out.println("품절입니다.");
        else if (money < price) System.out.println("돈이 부족합니다.");
        else {
            stock--;
            System.out.println(name + "가 나왔습니다. 잔돈: " + (money - price));
        }
    }
}

public class VendingMachine {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Drink[] drinks = { new Drink("콜라", 1200, 2),
                           new Drink("사이다", 1000, 2),
                           new Drink("물", 800, 3) };
        for (int i = 0; i < drinks.length; i++) drinks[i].show(i + 1);
        System.out.print("상품 번호와 돈: ");
        int choice = sc.nextInt();
        int money = sc.nextInt();
        if (choice >= 1 && choice <= drinks.length)
            drinks[choice - 1].buy(money);
        else
            System.out.println("없는 상품입니다.");
    }
}""",
      "1. 콜라 1200원 (2개)\n2. 사이다 1000원 (2개)\n3. 물 800원 (3개)\n상품 번호와 돈: 2 1500\n사이다가 나왔습니다. 잔돈: 500",
      ["배열 출력 후 사용자가 입력한 2는 배열 1번의 사이다 객체를 고른다.",
       "`buy` 메서드에서 재고와 돈을 통과해야만 해당 객체 stock이 줄어든다.",
       "없는 번호는 배열을 읽기 전에 거절하므로 안전하다."],
      "선택 기능으로 판매 뒤 해당 음료의 남은 재고를 출력하려면 `buy`의 성공 경로에 한 줄을 추가한다.",
      "Java 종합", "객체 배열 문제에서는 선택 인덱스, 실제 객체, 변경된 필드 세 칸을 표로 작성한다.",
      """class Item {
    int stock;
    Item(int s) { stock = s; }
    void sell() { if (stock > 0) stock--; }
}
Item[] items = {new Item(1), new Item(2)};
items[0].sell();
items[1].sell();
items[1].sell();
System.out.print(items[0].stock + items[1].stock);""",
      "출력값은 무엇인가?",
      "첫 객체는 1에서 0, 둘째 객체는 2에서 두 번 감소해 0이다. 두 값을 더한 출력은 `0`.",
      ["콜라를 정상 구매해 잔돈을 확인한다.",
       "없는 상품 번호와 부족한 돈을 각각 입력해 오류 경로를 확인한다.",
       "상품 객체 하나의 판매 전/후 값을 표로 제출한다."],
      "다음 Python 주차에서는 같은 합계와 목록 문제를 더 짧은 코드로 처리한다.",
      "제출 작품: 음료 자판기",
      "C와 Java 기초 프로젝트를 마감한다. 객체가 가진 가격·재고라는 발상은 쇼핑몰 DB의 상품 행으로 이어진다.",
      ["실행 가능한 `VendingMachine.java`", "Java 미니 테스트와 테스트표"]),
]

LESSONS += [
    L(5, 1, "Python", "짧게 쓰는 입력과 계산",
      "Python에서는 중괄호와 자료형 선언이 줄어든다. 그러나 입력값을 숫자로 바꾸고 계산하는 원리는 그대로다.",
      ["Python 파일을 실행한다.", "`input()`과 `int()`의 역할을 구분한다.", "C/Java/Python의 같은 흐름을 비교한다."],
      "언어의 옷은 달라도 값의 여행은 같다",
      ["`input()`으로 받은 값은 글자다. 공부시간 합계를 계산하려면 `int()`를 통과시켜 숫자로 바꿔야 한다.",
       "C와 Java에서 하던 입력-저장-계산-출력 흐름이 Python에서는 더 짧게 보인다."],
      [("input", "\"3\""), ("int", "3"), ("hours", "3"), ("출력", "목표까지 2시간")],
      "종이에 문자열 `\"3\"` 카드와 숫자 `3` 카드를 따로 만들어 `int()` 문을 통과시키며 교체한다.",
      "첫 프로그램은 하루 공부시간과 목표의 차이를 보여 준다.",
      """goal = 5
hours = int(input("오늘 공부시간: "))

print("오늘 기록:", hours, "시간")
if hours >= goal:
    print("목표 달성!")
else:
    print("목표까지", goal - hours, "시간 남음")""",
      "오늘 공부시간: 3\n오늘 기록: 3 시간\n목표까지 2 시간 남음",
      ["`input()` 결과를 `int()`가 정수로 바꾸어 hours에 넣는다.",
       "3 >= 5는 거짓이므로 else가 실행된다.",
       "목표와의 차이 5 - 3을 바로 출력한다."],
      "입력을 5와 7로 바꾸어 조건 경계와 목표 초과 상황의 출력을 예측한다.",
      "Python 조건", "Python도 시험에서는 들여쓰기 범위와 변수값 변화가 핵심이다.",
      """score = 70
if score >= 60:
    score = score + 5
else:
    score = score - 5
print(score)""",
      "무엇이 출력되는가?",
      "70은 60 이상이므로 5를 더해 `75`가 출력된다.",
      ["과목명과 공부시간을 입력받아 한 줄로 출력한다.",
       "목표시간을 사용자에게도 입력받도록 바꾼다.",
       "C의 조건문과 Python 조건문의 괄호/중괄호 차이를 적는다."],
      "짧아졌다고 실행 원리가 바뀐 것은 아니다. hours 상자의 값과 선택된 길을 추적한다.",
      "금요일: 일주일 공부시간 분석기",
      "한 날의 공부시간을 입력하고 목표 달성 여부를 알려 주는 기능을 만든다.",
      ["실행 가능한 `day1.py`", "세 언어 비교 메모"]),

    L(5, 2, "Python", "반복해서 다섯 날 기록하기",
      "월요일부터 금요일까지의 공부시간을 반복 입력하고 총 시간을 누적한다.",
      ["`for`와 `range`를 읽는다.", "누적 합계 변화를 기록한다.", "반복 횟수를 추적한다."],
      "반복문은 다섯 칸짜리 기록표를 한 칸씩 채우는 손",
      ["`range(5)`는 0,1,2,3,4라는 다섯 값을 차례로 제공한다.",
       "`total`은 매일 입력이 들어올 때마다 이전 값에 새 시간을 더해 기억한다."],
      [("day=0", "+2"), ("day=1", "+3"), ("day=2", "+1"), ("total", "6 ...")],
      "월~금 다섯 칸을 그리고 입력을 들을 때마다 total 옆의 숫자를 덧셈 결과로 바꾼다.",
      "우선 리스트 없이 합계만 계산해 반복과 누적에 집중한다.",
      """total = 0

for day in range(5):
    hours = int(input(f"{day + 1}일차 공부시간: "))
    total = total + hours
    print("지금까지:", total, "시간")

print("주간 총 공부시간:", total, "시간")""",
      "1일차 공부시간: 2\n지금까지: 2 시간\n2일차 공부시간: 3\n지금까지: 5 시간\n...\n주간 총 공부시간: 10 시간",
      ["`day`는 화면 번호를 위해 1을 더해 출력하지만 반복 횟수는 다섯 번이다.",
       "`total`은 반복 밖에서 만들어져 이전 날의 합계를 유지한다.",
       "마지막 print는 반복이 끝난 후 한 번만 실행된다."],
      "입력을 모두 1로 넣을 때 각 회차의 total을 종이에 먼저 적는다.",
      "Python 반복", "누적 문제에서는 초기값 0과 반복 횟수를 먼저 찾는다.",
      """total = 1
for n in range(1, 4):
    total = total * n
print(total)""",
      "`n`이 어떤 값을 거치고 무엇이 출력되는가?",
      "`range(1,4)`는 1,2,3이다. total은 1, 2, 6이 되어 `6`을 출력한다.",
      ["세 날만 입력받도록 range를 변경해 실행한다.",
       "합계 대신 공부시간에 10을 곱한 점수를 누적해 본다.",
       "반복 표에 day, hours, total 세 열을 채운다."],
      "반복을 읽는 감각은 C의 `for`와 동일하며 Python 표현만 간결하다.",
      "금요일: 일주일 공부시간 분석기",
      "다섯 날 입력과 합계 기능을 구현한다.",
      ["주간 합계 코드", "반복 변수 추적표"]),

    L(5, 3, "Python", "리스트에 기록을 남기기",
      "합계만 남기지 않고 다섯 날의 값을 리스트에 보관하여 평균과 최고 기록을 구한다.",
      ["리스트에 값을 추가한다.", "인덱스로 특정 날을 읽는다.", "`sum`, `max`를 직접 계산과 비교한다."],
      "리스트는 지우지 않는 주간 기록판",
      ["누적 total은 최종 합계만 남지만 리스트에는 매일의 값이 모두 남는다.",
       "리스트 첫 칸도 배열처럼 0번이다. C 배열을 이미 본 학생에게는 같은 줄의 상자라고 연결한다."],
      [("hours[0]", "2"), ("hours[1]", "4"), ("hours[2]", "3"), ("max", "4")],
      "C 배열 그림 옆에 Python 리스트 그림을 나란히 그리고 인덱스가 같은 것을 표시한다.",
      "입력을 리스트에 추가한 뒤 내장 함수로 결과를 확인한다.",
      """hours = []

for day in range(5):
    value = int(input(f"{day + 1}일차 시간: "))
    hours.append(value)

total = sum(hours)
average = total / len(hours)
print("기록:", hours)
print("총합:", total)
print("평균:", average)
print("최고:", max(hours))""",
      "1일차 시간: 2\n2일차 시간: 4\n3일차 시간: 3\n4일차 시간: 1\n5일차 시간: 5\n기록: [2, 4, 3, 1, 5]\n총합: 15\n평균: 3.0\n최고: 5",
      ["`append`는 리스트 끝에 새 값을 한 칸 추가한다.",
       "`len(hours)`는 입력한 기록 개수 5다.",
       "`max`는 저장된 값 중 가장 큰 값 하나를 찾는다."],
      "`max`를 쓰지 않고 반복문과 `best` 변수로 최고 시간을 찾는 코드를 작성해 본다.",
      "Python 리스트", "리스트 문제 역시 인덱스와 반복에 집중한다. 내장 함수 결과도 손으로 확인한다.",
      """data = [3, 1, 4, 2]
result = 0
for i in range(0, len(data), 2):
    result += data[i]
print(result)""",
      "더해지는 리스트 칸과 출력값은 무엇인가?",
      "i는 0과 2이므로 data[0]=3과 data[2]=4를 더해 `7`이다.",
      ["공부시간 `[2, 0, 4, 3, 1]`의 합계와 최고를 손으로 구한 뒤 코드로 확인한다.",
       "최저시간을 출력하는 기능을 추가한다.",
       "목표 3시간 이상인 값의 개수를 반복문으로 센다."],
      "금요일 작품에는 리스트가 있어야 달성일 수와 최고 시간을 다시 계산할 수 있다.",
      "금요일: 일주일 공부시간 분석기",
      "다섯 날의 원본 기록을 리스트로 남기고 총합·평균·최고 값을 출력한다.",
      ["리스트 분석 코드", "인덱스 문제 풀이"]),

    L(5, 4, "Python", "분석 규칙을 함수로 묶기",
      "목표 달성일 수를 계산하는 기능을 함수로 만들고 주간 기록을 전달한다.",
      ["함수의 매개변수로 리스트를 전달한다.", "조건에 맞는 개수를 누적한다.", "반환값이 저장되는 과정을 추적한다."],
      "함수는 기록판을 받아 질문에 답하는 분석 담당자",
      ["기록 리스트를 함수에 주면 함수는 목표 이상인 날만 세고 숫자 하나를 돌려준다.",
       "계산 규칙을 함수로 이름 붙이면 `count_success`라는 이름만 보고도 역할을 짐작할 수 있다."],
      [("hours", "[2,4,3,1,5]"), ("함수", ">=3 세기"), ("count", "3"), ("출력", "달성일 3일")],
      "공부시간 카드 중 목표 이상인 카드만 한쪽으로 옮기고 몇 장인지 센다.",
      "리스트는 예시값으로 먼저 실행한 뒤 사용자 입력과 결합한다.",
      """def count_success(hours, goal):
    count = 0
    for value in hours:
        if value >= goal:
            count += 1
    return count

records = [2, 4, 3, 1, 5]
goal = 3
success_days = count_success(records, goal)
print("목표 달성일:", success_days, "일")""",
      "목표 달성일: 3 일",
      ["함수 안 `value`는 리스트 값을 2,4,3,1,5 순서로 받는다.",
       "4,3,5에서 조건이 참이므로 count가 세 번 증가한다.",
       "반환된 3은 `success_days`에 저장된다."],
      "goal을 4로 변경할 때 참이 되는 값과 출력 숫자를 실행 전 적는다.",
      "Python 함수", "함수 문제에서는 반복 안의 조건이 몇 번 참인지 세면 반환값을 찾을 수 있다.",
      """def change(items):
    result = 0
    for x in items:
        if x % 2 == 0:
            result += x
    return result
print(change([1, 2, 3, 4]))""",
      "출력은 무엇인가?",
      "짝수인 2와 4만 result에 더해져 `6`을 출력한다.",
      ["목표 미달일 수를 반환하는 함수를 하나 더 만든다.",
       "빈 리스트라면 평균 계산이 왜 문제가 되는지 설명한다.",
       "내 기록 다섯 개를 넣고 함수 반환값을 표로 남긴다."],
      "분석 함수는 다음 주 상품 총액·할인 계산 함수와 같은 방식으로 작동한다.",
      "금요일: 일주일 공부시간 분석기",
      "목표 달성일을 함수로 계산하여 주간 분석 결과를 마무리할 준비를 한다.",
      ["목표 달성 함수", "함수 손 추적 답안"]),

    L(5, 5, "Python", "완성: 일주일 공부시간 분석기",
      "입력한 다섯 날 기록을 분석하여 총합, 평균, 최고, 목표 달성일을 보여 주는 프로그램을 완성한다.",
      ["리스트 입력과 분석 함수를 결합한다.", "실제 내 데이터로 결과를 확인한다.", "Python 추적 문제를 푼다."],
      "데이터가 쌓이면 질문을 던질 수 있다",
      ["리스트는 단순한 저장소가 아니라 '총 몇 시간?', '가장 긴 날?', '목표를 몇 번 달성?' 같은 질문에 답할 재료다.",
       "쇼핑몰에서도 상품과 주문 데이터가 쌓인 뒤 똑같이 합계와 조건을 묻게 된다."],
      [("입력", "5일 시간"), ("리스트", "[...]"), ("분석", "sum/max/count"), ("리포트", "결과 출력")],
      "네 명의 샘플 기록을 받아 칠판에 리스트로 쓰고, 프로그램 결과와 손계산이 같은지 확인한다.",
      "필수 코드 전체를 입력하고 내 기록 또는 제공된 테스트 기록으로 실행한다.",
      """def count_success(hours, goal):
    count = 0
    for value in hours:
        if value >= goal:
            count += 1
    return count

records = []
goal = 3
for day in range(5):
    hours = int(input(f"{day + 1}일차 공부시간: "))
    records.append(hours)

total = sum(records)
print("=== 주간 분석 ===")
print("총 공부시간:", total)
print("하루 평균:", total / len(records))
print("최고 기록:", max(records))
print("목표 달성일:", count_success(records, goal))""",
      "1일차 공부시간: 2\n2일차 공부시간: 4\n3일차 공부시간: 3\n4일차 공부시간: 1\n5일차 공부시간: 5\n=== 주간 분석 ===\n총 공부시간: 15\n하루 평균: 3.0\n최고 기록: 5\n목표 달성일: 3",
      ["입력될 때마다 리스트가 한 칸씩 길어진다.",
       "분석 결과는 같은 records 데이터를 서로 다른 방식으로 읽은 값이다.",
       "함수는 records를 바꾸지 않고 조건에 맞는 개수만 반환한다."],
      "선택 기능으로 공부시간이 가장 낮은 값도 출력하고, 왜 보충 학습 메시지와 연결할 수 있는지 적는다.",
      "Python 종합", "리스트가 함수에 전달되는 코드는 함수 내부 반복표를 만들면 안정적으로 풀 수 있다.",
      """def calc(data):
    total = 0
    for x in data:
        if x >= 3:
            total += x
    return total
values = [2, 4, 3, 1]
print(calc(values))""",
      "출력값은 무엇인가?",
      "3 이상인 4와 3만 합산한다. 출력은 `7`이다.",
      ["기록 `[2,4,3,1,5]`로 시연하고 손계산 결과와 대조한다.",
       "목표시간을 4로 바꿔 달성일 결과가 달라짐을 확인한다.",
       "리스트, 함수, 조건문이 각각 있는 줄을 표시한다."],
      "Python의 짧은 코드는 값을 읽지 않고 지나치기 쉽다. 설명할 때는 리스트 한 칸씩 짚는다.",
      "제출 작품: 일주일 공부시간 분석기",
      "다음 주에는 리스트 안의 숫자 대신 상품명과 가격을 가진 딕셔너리를 다루며 쇼핑몰 소재로 넘어간다.",
      ["실행 가능한 `study_report.py`", "Python 미니 테스트"]),

    L(6, 1, "Python", "상품을 딕셔너리로 저장하기",
      "상품 이름과 가격을 한 묶음으로 저장하고, 이름을 키로 가격을 찾는다.",
      ["딕셔너리의 키와 값을 구분한다.", "상품 가격을 조회한다.", "Java 객체와 Python 딕셔너리를 비교한다."],
      "딕셔너리는 이름표로 열어 보는 가격 서랍",
      ["리스트는 위치 번호로 찾지만 딕셔너리는 `'콜라'` 같은 키로 가격을 찾는다.",
       "Java의 Drink 객체와 목적은 비슷하지만 오늘은 간단히 가격표 한 장을 표현하는 데 집중한다."],
      [("products", "가격표"), ("\"콜라\"", "키"), ("products[키]", "1200"), ("계산", "수량 곱")],
      "상품 카드 앞면에는 이름, 뒷면에는 가격을 써서 이름을 말하면 가격을 뒤집어 확인한다.",
      "상품 세 개 가격을 딕셔너리로 만들고 선택 상품 가격을 출력한다.",
      """products = {
    "콜라": 1200,
    "물": 800,
    "초콜릿": 1500
}

name = input("상품명: ")
if name in products:
    print(name, "가격:", products[name], "원")
else:
    print("없는 상품입니다.")""",
      "상품명: 물\n물 가격: 800 원",
      ["`name in products`는 입력한 이름이 키로 존재하는지 확인한다.",
       "존재할 때만 `products[name]`으로 가격을 안전하게 읽는다.",
       "없는 상품을 바로 조회하면 오류가 날 수 있어 조건이 필요하다."],
      "상품 하나를 추가하고, 존재하는 상품과 없는 상품을 각각 입력해 본다.",
      "Python 딕셔너리", "기사 문제에서는 키로 꺼낸 값과 조건에 따라 바뀌는 결과를 추적할 수 있어야 한다.",
      """price = {"A": 1000, "B": 2000}
total = price["A"] + price["B"] * 2
print(total)""",
      "출력값은 무엇인가?",
      "A 가격 1000과 B 두 개 가격 4000을 더해 `5000`이다.",
      ["가격표에 `노트: 2000`을 추가하고 출력한다.",
       "선택 상품 수량을 입력받아 소계를 계산한다.",
       "Java 상품 객체와 딕셔너리 가격표의 공통점과 차이를 한 줄씩 쓴다."],
      "이번 프로젝트는 딕셔너리 키를 상품 선택 입력으로 사용한다.",
      "금요일: 장바구니 할인 계산기",
      "상품명으로 가격을 조회하는 가격표를 만든다.",
      ["상품 딕셔너리 코드", "존재/부재 입력 테스트"]),

    L(6, 2, "Python", "장바구니에 소계를 쌓기",
      "여러 상품의 이름과 수량을 입력하여 각 소계와 전체 총액을 계산한다.",
      ["반복해서 상품을 입력한다.", "가격과 수량을 곱한다.", "총액 누적을 추적한다."],
      "장바구니 총액은 고른 상품의 소계가 차곡차곡 더해진 값",
      ["상품 한 건의 가격 곱하기 수량은 소계이고, 여러 소계를 더한 값이 할인 전 총액이다.",
       "아직 데이터베이스는 없다. 입력하는 동안 메모리의 `total` 상자가 장바구니 합계를 기억한다."],
      [("물 x2", "1600"), ("초콜릿 x1", "1500"), ("total", "3100"), ("할인 전", "3100")],
      "상품과 수량 카드로 소계를 계산하고, 계산대 total 판에 차례로 더한다.",
      "구매 종류를 두 개로 제한하여 반복과 누적을 명확히 익힌다.",
      """products = {"콜라": 1200, "물": 800, "초콜릿": 1500}
total = 0

for i in range(2):
    name = input("상품명: ")
    count = int(input("수량: "))
    if name in products and count > 0:
        subtotal = products[name] * count
        total += subtotal
        print("소계:", subtotal)
    else:
        print("입력을 확인하세요.")

print("할인 전 총액:", total)""",
      "상품명: 물\n수량: 2\n소계: 1600\n상품명: 초콜릿\n수량: 1\n소계: 1500\n할인 전 총액: 3100",
      ["`total`은 반복 전 0으로 만들어 두 상품의 소계를 유지한다.",
       "정상 입력인 경우에만 subtotal을 계산하고 total에 더한다.",
       "잘못된 상품은 총액에 포함되지 않는다."],
      "두 번째 상품을 없는 이름으로 입력하면 총액이 첫 소계만 남는 이유를 확인한다.",
      "Python 누적", "리스트가 없어도 누적 변수는 기사 코드 추적의 중요한 기본이다.",
      """items = {"pen": 500, "book": 2000}
total = 0
for name in ["pen", "book", "pen"]:
    total += items[name]
print(total)""",
      "출력 총액은 무엇인가?",
      "펜 500, 책 2000, 펜 500을 더해 `3000`이다.",
      ["상품 종류 수를 3으로 늘리고 total 변화를 표로 쓴다.",
       "수량 0이나 음수를 입력했을 때 총액이 늘지 않게 확인한다.",
       "소계와 총액의 차이를 한 문장으로 설명한다."],
      "할인은 총액이 완성된 다음 적용한다. 계산 순서를 분리하면 실수가 적다.",
      "금요일: 장바구니 할인 계산기",
      "두 상품을 골라 할인 전 총액을 구하는 장바구니 부분을 완성한다.",
      ["누적 합계 코드", "두 상품 입력 추적표"]),

    L(6, 3, "Python", "총액에 따라 할인 적용하기",
      "할인 전 총액이 기준 금액 이상이면 일정 금액을 빼는 규칙을 함수로 만든다.",
      ["금액 조건을 함수로 분리한다.", "할인액과 결제액을 구분한다.", "경계 금액을 테스트한다."],
      "할인은 장바구니를 다 채운 뒤 찍는 쿠폰 도장",
      ["상품마다 마음대로 할인하는 것이 아니라 전체 total이 기준을 넘는지 확인한 뒤 discount를 결정한다.",
       "결제액은 `total - discount`이다. 할인 전/할인액/결제액 세 값을 화면에 따로 보여 주면 계산이 보인다."],
      [("총액", "12000"), ("기준", ">=10000"), ("할인액", "1000"), ("결제액", "11000")],
      "10000원 경계선을 바닥에 표시하고 총액 카드 9999, 10000, 12000을 어느 쪽에 놓을지 판단한다.",
      "함수를 단독 실행하여 경계값의 반환을 먼저 확인한다.",
      """def get_discount(total):
    if total >= 10000:
        return 1000
    return 0

total = 12000
discount = get_discount(total)
payment = total - discount
print("총액:", total)
print("할인:", discount)
print("결제:", payment)""",
      "총액: 12000\n할인: 1000\n결제: 11000",
      ["함수에 total=12000이 들어가 조건이 참이므로 1000을 반환한다.",
       "반환된 할인액은 원래 total을 자동으로 바꾸지 않는다.",
       "결제액을 계산하는 줄에서 실제 차감이 이루어진다."],
      "total을 9999와 10000으로 바꾸어 할인액이 달라지는 정확한 경계를 확인한다.",
      "Python 함수/조건", "경계값에서 `>=`와 `>`의 차이는 시험에도 프로젝트 버그에도 중요하다.",
      """def sale(total):
    if total > 5000:
        return total - 500
    return total
print(sale(5000), sale(5001))""",
      "두 출력값은 무엇인가?",
      "5000은 `>` 조건이 거짓이라 5000 그대로이고, 5001은 500을 빼 4501이다. `5000 4501`.",
      ["5000원 이상 500원 할인 규칙 함수를 작성한다.",
       "할인율 대신 고정 할인액을 쓰는 이유를 초보자 입장에서 적는다.",
       "어제의 장바구니 total에 함수를 연결한다."],
      "금요일에는 10000원 경계값을 반드시 테스트한다.",
      "금요일: 장바구니 할인 계산기",
      "총액 계산 뒤 자동 금액 할인을 적용하는 함수를 결합한다.",
      ["할인 함수 실행", "9999/10000 경계 테스트"]),

    L(6, 4, "Python", "쿠폰 문자열과 최종 결제금액",
      "사용자가 입력한 쿠폰 코드가 맞으면 추가 할인을 적용하고 영수증 문구를 출력한다.",
      ["문자열을 비교한다.", "함수 반환값을 결합한다.", "필수 계산과 선택 파일 저장을 구분한다."],
      "쿠폰은 정확히 맞는 글자 열쇠",
      ["`WELCOME`과 `welcome`은 컴퓨터에게 서로 다른 문자열이다. 정해 둔 쿠폰과 정확히 같은지 비교한다.",
       "필수 작품은 화면 출력까지다. 파일 저장은 계산을 완성한 학생에게만 선택 과제로 준다."],
      [("입력", "WELCOME"), ("비교", "=="), ("추가할인", "500"), ("결제액", "-500")],
      "쿠폰 글자 카드를 대문자/소문자로 두 종류 만들어 컴퓨터가 정확히 같은 카드만 받는다고 표시한다.",
      "자동 할인에 쿠폰 할인 하나를 더한다. 결제액이 음수가 되지 않도록 작은 값 입력도 생각한다.",
      """def amount_discount(total):
    if total >= 10000:
        return 1000
    return 0

total = 12000
coupon = input("쿠폰 코드: ")
discount = amount_discount(total)
if coupon == "WELCOME":
    discount += 500

payment = total - discount
print("할인 전:", total)
print("할인액:", discount)
print("최종 결제:", payment)""",
      "쿠폰 코드: WELCOME\n할인 전: 12000\n할인액: 1500\n최종 결제: 10500",
      ["금액 할인 함수가 먼저 1000을 반환한다.",
       "쿠폰 문자열이 정확히 같으면 기존 discount에 500을 추가한다.",
       "결제액은 두 할인을 합친 뒤 한 번 계산한다."],
      "쿠폰 입력을 `welcome`으로 바꿀 때 할인액을 예측하고, 대소문자를 허용하려면 `.upper()`를 어디에 쓸지 실험한다.",
      "Python 문자열", "문자열 비교와 조건 실행 횟수는 코드 문제의 쉬운 듯 틀리기 쉬운 지점이다.",
      """word = "SALE"
price = 3000
if word == "sale":
    price -= 500
elif word == "SALE":
    price -= 300
print(price)""",
      "출력 가격은 무엇인가?",
      "첫 비교는 대소문자가 달라 거짓이고 두 번째는 참이므로 300을 빼 `2700`이다.",
      ["쿠폰 없이 실행하고 쿠폰 적용 결과와 비교한다.",
       "총액 800원에 쿠폰 500원을 적용할 때 계산은 가능하지만 규칙상 허용할지 토론한다.",
       "선택 과제로 `receipt.txt`에 결제 결과 한 줄을 쓰는 코드를 교사와 함께 추가한다."],
      "시험 대비의 중심은 함수와 문자열 비교이며 파일 쓰기는 먼저 끝낸 학생만 다룬다.",
      "금요일: 장바구니 할인 계산기",
      "가격표, 장바구니 합계, 자동 할인, 쿠폰 할인을 모두 조립할 준비가 끝났다.",
      ["쿠폰 비교 코드", "함수/문자열 추적 풀이"]),

    L(6, 5, "Python", "완성: 장바구니 할인 계산기",
      "상품 두 개를 선택하고 금액 및 쿠폰 할인을 적용하여 최종 결제 금액을 출력한다.",
      ["쇼핑몰 계산 흐름을 완성한다.", "경계값과 잘못된 상품을 테스트한다.", "Python 코드 추적을 마무리한다."],
      "쇼핑몰의 가장 작은 핵심은 상품 선택과 합계 계산",
      ["아직 화면이나 DB는 없지만, 상품을 고르고 수량에 따라 합계를 계산하고 할인하는 규칙은 마지막 쇼핑몰에서도 같다.",
       "데이터의 저장 장소와 화면 모양은 바뀌어도 계산 로직을 이해한 학생은 통합 과정에서 길을 잃지 않는다."],
      [("상품표", "dict"), ("장바구니", "total"), ("할인", "함수/쿠폰"), ("출력", "payment")],
      "학생 두 명이 상품 선택을 말하고 한 명이 total, 한 명이 discount 칠판 칸을 갱신한다.",
      "필수 완성본은 외부 라이브러리가 전혀 필요 없다. Python 실행만으로 작동한다.",
      """def amount_discount(total):
    if total >= 10000:
        return 1000
    return 0

products = {"콜라": 1200, "물": 800, "초콜릿": 1500}
total = 0
print("상품:", products)

for i in range(2):
    name = input("담을 상품: ")
    count = int(input("수량: "))
    if name in products and count > 0:
        subtotal = products[name] * count
        total += subtotal
        print("소계:", subtotal)
    else:
        print("잘못된 입력")

coupon = input("쿠폰(없으면 Enter): ")
discount = amount_discount(total)
if coupon == "WELCOME":
    discount += 500

print("할인 전 총액:", total)
print("할인액:", discount)
print("결제 금액:", total - discount)""",
      "상품: {'콜라': 1200, '물': 800, '초콜릿': 1500}\n담을 상품: 초콜릿\n수량: 6\n소계: 9000\n담을 상품: 콜라\n수량: 1\n소계: 1200\n쿠폰(없으면 Enter): WELCOME\n할인 전 총액: 10200\n할인액: 1500\n결제 금액: 8700",
      ["두 소계가 total 상자에 더해져 10200이 된다.",
       "총액 기준 할인 1000과 쿠폰 할인 500이 합쳐진다.",
       "출력되는 결제 금액은 10200 - 1500이다."],
      "선택 과제로 구매한 이름과 수량도 리스트에 저장해 최종 영수증 줄을 여러 개 출력한다.",
      "Python 종합", "딕셔너리 조회, 반복 누적, 함수 반환, 문자열 조건을 순서대로 분리하여 읽는다.",
      """items = {"a": 1000, "b": 1500}
total = 0
for name, qty in [("a", 2), ("b", 1)]:
    total += items[name] * qty
if total >= 3000:
    total -= 500
print(total)""",
      "출력값은 무엇인가?",
      "소계는 a 두 개 2000, b 한 개 1500으로 총 3500이다. 조건이 참이라 500을 빼 `3000`이다.",
      ["총액이 9999 이하인 주문과 10000 이상인 주문을 각각 시험한다.",
       "쿠폰 문자열을 맞게/틀리게 입력하여 할인액을 비교한다.",
       "상품 딕셔너리, total, discount가 금요일 쇼핑몰에서 어떤 역할이 될지 적는다."],
      "상품은 다음 주 PostgreSQL 테이블로 옮겨 가고, total 계산은 이후 React 장바구니에서도 다시 만난다.",
      "제출 작품: 장바구니 할인 계산기",
      "설치 없는 언어 학습 구간을 마친다. 다음 주부터 상품을 PostgreSQL 데이터로 저장한다.",
      ["실행 가능한 `cart_discount.py`", "Python 종합 테스트"]),

    L(7, 1, "PostgreSQL", "테이블은 상품을 쌓는 표",
      "코드 안 딕셔너리에 있던 상품 데이터를 PostgreSQL의 `products` 테이블로 옮길 설계부터 시작한다.",
      ["행과 열을 구분한다.", "기본키의 필요성을 이해한다.", "표준 SQL 중심의 CREATE TABLE을 작성한다."],
      "테이블은 같은 종류의 카드가 줄 맞춰 들어가는 서랍장",
      ["한 행은 상품 하나이고, 열은 모든 상품이 공통으로 가져야 하는 항목이다.",
       "이름이 같아질 수도 있으므로 상품을 정확히 가리킬 고유 번호인 기본키를 둔다."],
      [("행", "상품 한 개"), ("열", "name/price/stock"), ("기본키", "product_id"), ("DB", "저장")],
      "상품 카드 세 장을 그리고, 각 카드에 같은 열 제목을 적은 뒤 고유 번호를 붙인다.",
      "PostgreSQL에서 새 데이터베이스에 접속한 뒤 테이블 하나를 생성한다.",
      """CREATE TABLE products (
    product_id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price INTEGER NOT NULL,
    stock INTEGER NOT NULL
);""",
      "CREATE TABLE\n-- products 테이블이 생성됨",
      ["`products`는 앞으로 상품을 보관할 테이블 이름이다.",
       "`GENERATED BY DEFAULT AS IDENTITY`는 입력하지 않아도 번호를 만들어 주는 표준 방식에 가까운 정의다.",
       "`NOT NULL`은 반드시 값이 있어야 하는 열이라는 규칙이다."],
      "price와 stock에 음수가 들어가면 안 된다는 생각을 적고, 나중 `CHECK` 조건으로 확장할 수 있음을 표시한다.",
      "SQL DDL", "기사 SQL에서는 테이블 정의와 기본키/외래키의 의미를 이해해야 한다.",
      """CREATE TABLE category (
    category_id INTEGER PRIMARY KEY,
    name VARCHAR(30) NOT NULL
);""",
      "`category_id`와 `name`의 역할을 각각 설명하라.",
      "`category_id`는 각 행을 유일하게 식별하는 기본키이며, `name`은 비어 있을 수 없는 최대 30자 이름 열이다.",
      ["종이에 products 행 3개를 그려 열 값을 채운다.",
       "상품명, 가격, 재고 중 비어 있으면 안 되는 값에 이유를 단다.",
       "`SERIAL`이 아닌 IDENTITY를 쓰는 이유를 표준 SQL 학습 원칙과 연결해 적는다."],
      "오늘은 데이터를 넣지 않는다. 먼저 저장 모양을 제대로 설계해야 내일부터 입력이 안전하다.",
      "금요일: 작은 쇼핑몰 상품 DB",
      "상품 DB의 필수 테이블 `products`를 만든다.",
      ["products 생성 SQL", "테이블 설계 그림"]),

    L(7, 2, "PostgreSQL", "INSERT로 상품 행 넣기",
      "테이블에 상품을 한 건씩 등록하고 SELECT로 저장된 결과를 확인한다.",
      ["INSERT 문을 작성한다.", "자동 생성된 키를 구분한다.", "SELECT 결과 표를 읽는다."],
      "INSERT는 빈 표에 상품 카드를 한 줄 끼워 넣는 동작",
      ["DB는 프로그램이 끝나도 행을 기억한다. 입력 SQL을 실행한 뒤 조회해야 실제로 어떤 값이 저장됐는지 보인다.",
       "product_id는 DB가 정해 주므로 INSERT 열 목록에서 빼고 name, price, stock만 제공한다."],
      [("INSERT", "콜라/1200/10"), ("DB 번호", "1"), ("행", "1 콜라 1200 10"), ("SELECT", "표시")],
      "어제 만든 빈 표 그림에 상품 카드 세 장을 한 행씩 추가한다.",
      "세 상품을 입력한 뒤 모든 열을 조회한다.",
      """INSERT INTO products (name, price, stock)
VALUES ('콜라', 1200, 10);

INSERT INTO products (name, price, stock)
VALUES ('물', 800, 20);

INSERT INTO products (name, price, stock)
VALUES ('초콜릿', 1500, 8);

SELECT product_id, name, price, stock
FROM products;""",
      " product_id | name   | price | stock\n------------+--------+-------+------\n 1          | 콜라   | 1200  | 10\n 2          | 물     | 800   | 20\n 3          | 초콜릿 | 1500  | 8",
      ["INSERT 열 순서와 VALUES 값 순서가 맞아야 한다.",
       "ID는 지정하지 않았지만 각 행에 서로 다른 번호가 생성된다.",
       "SELECT는 저장된 행을 읽을 뿐 값을 바꾸지 않는다."],
      "노트와 펜 상품을 두 건 더 INSERT하고 조회 결과의 행 수를 예상한다.",
      "SQL INSERT/SELECT", "SQL 결과 문제는 어떤 행이 생성되고 어떤 열이 표시되는지 표로 그린다.",
      """INSERT INTO products (name, price, stock)
VALUES ('펜', 500, 4);

SELECT name, price
FROM products;""",
      "마지막 SELECT 결과에 보이는 열은 무엇이며, 새 행에는 어떤 값이 저장되는가?",
      "결과 화면에는 `name`, `price` 두 열만 보인다. 저장된 새 상품 행은 펜, 500, 재고 4와 자동 생성된 product_id를 가진다.",
      ["직접 선택한 쇼핑몰 상품을 총 10개 등록한다.",
       "가격과 재고를 잘못 바꾸어 입력한 행이 없는지 전체 조회한다.",
       "조회 열 목록을 바꾸어 상품명만 표시한다."],
      "SQL을 실행할 때마다 INSERT가 다시 실행되면 중복 상품이 생긴다. 실행 구간을 구분하는 습관을 들인다.",
      "금요일: 작은 쇼핑몰 상품 DB",
      "상품 10건을 직접 등록하고 전체 조회 결과를 저장한다.",
      ["INSERT 문 모음", "전체 상품 조회 결과"]),

    L(7, 3, "PostgreSQL", "WHERE와 ORDER BY로 원하는 상품 찾기",
      "가격과 재고 조건으로 필요한 상품만 조회하고 정렬한다.",
      ["WHERE 조건을 작성한다.", "정렬 방향을 구분한다.", "조회는 저장값을 바꾸지 않음을 안다."],
      "조회 조건은 진열대에서 필요한 카드만 꺼내 보는 필터",
      ["`WHERE price >= 1000`은 비싼 상품 카드만 통과시키는 체다.",
       "`ORDER BY price DESC`는 통과한 카드의 줄 세우기 순서를 높은 가격부터로 바꾼다. DB 안 원본 위치를 바꾸는 것은 아니다."],
      [("전체 상품", "10건"), ("WHERE", "가격 >=1000"), ("ORDER BY", "비싼 순"), ("결과", "선별 표")],
      "상품 카드들을 가격 조건 선 뒤로 통과시키고 통과한 카드만 비싼 순으로 늘어놓는다.",
      "가격과 재고에 대한 자주 쓰는 조회를 직접 실행한다.",
      """SELECT name, price, stock
FROM products
WHERE price >= 1000
ORDER BY price DESC;

SELECT name, stock
FROM products
WHERE stock < 10
ORDER BY stock ASC;""",
      "-- 첫 조회: 1000원 이상 상품을 비싼 순으로 표시\n-- 둘째 조회: 재고 10개 미만 상품을 적은 순으로 표시",
      ["FROM에서 대상 표를 정하고 WHERE에서 남길 행을 고른다.",
       "ORDER BY는 결과 행 순서를 정한다.",
       "`DESC`는 큰 값부터, `ASC`는 작은 값부터다."],
      "조건을 `price BETWEEN 800 AND 1500`으로 작성해 포함되는 상품을 예상한다.",
      "SQL 조건/정렬", "기사에서는 WHERE 조건을 만족하는 행 수와 ORDER BY 결과 순서를 묻기 좋다.",
      """SELECT name, price
FROM products
WHERE price > 800 AND stock >= 10
ORDER BY price ASC;""",
      "콜라(1200,10), 물(800,20), 초콜릿(1500,8)만 있다고 할 때 어떤 상품이 결과에 나오는가?",
      "콜라는 두 조건을 모두 만족한다. 물은 가격이 800이라 `> 800`이 거짓이고, 초콜릿은 stock이 8이라 제외된다. 콜라 한 행이다.",
      ["내 상품 중 2000원 이하 상품 조회문을 작성한다.",
       "재고가 가장 많은 순으로 모든 상품을 조회한다.",
       "`AND`와 `OR` 결과가 달라지는 조건 한 쌍을 직접 실행한다."],
      "상품 목록 화면의 필터 기능은 결국 이런 조건 조회와 연결된다.",
      "금요일: 작은 쇼핑몰 상품 DB",
      "가격별·재고별 질문에 답하는 SELECT 문을 모은다.",
      ["조건 조회 SQL 4개", "결과 예측과 실행 비교"]),

    L(7, 4, "PostgreSQL", "UPDATE와 DELETE를 안전하게 사용하기",
      "가격이나 재고를 수정하고 판매하지 않을 상품을 삭제하되, 조건 없는 변경의 위험을 이해한다.",
      ["UPDATE와 DELETE 문을 작성한다.", "WHERE 없는 변경을 위험으로 인식한다.", "변경 전후를 SELECT로 확인한다."],
      "수정과 삭제는 연필이 아니라 도장: 실행하면 저장값이 바뀐다",
      ["SELECT는 보기지만 UPDATE와 DELETE는 데이터 자체를 바꾼다.",
       "따라서 먼저 같은 WHERE로 SELECT하여 대상 행을 확인한 뒤 변경하는 습관을 정한다."],
      [("SELECT", "대상 확인"), ("UPDATE", "price 변경"), ("SELECT", "변경 확인"), ("DELETE", "행 제거")],
      "상품 카드에서 바꿀 대상에만 포스트잇을 붙이고, 조건이 없으면 모든 카드가 바뀐다고 보여 준다.",
      "상품 번호를 확인한 뒤 한 행의 가격과 재고만 수정한다.",
      """SELECT product_id, name, price, stock
FROM products
WHERE name = '콜라';

UPDATE products
SET price = 1300, stock = 15
WHERE name = '콜라';

SELECT product_id, name, price, stock
FROM products
WHERE name = '콜라';

DELETE FROM products
WHERE name = '판매종료상품';""",
      "-- 콜라 한 행의 가격/재고만 변경됨\n-- 이름이 판매종료상품인 행만 삭제됨",
      ["첫 SELECT는 대상이 맞는지 확인하는 안전 절차다.",
       "UPDATE의 SET은 새 값을, WHERE는 어느 행인지를 말한다.",
       "WHERE를 빼면 products의 모든 행 가격과 재고가 같은 값으로 바뀔 수 있다."],
      "실제 실행 전에 `UPDATE products SET stock = 0;`의 피해를 말로 설명하고 절대 실행하지 않는다.",
      "SQL DML 안전성", "조건이 붙은 UPDATE/DELETE는 SQL 작성형 문제에서도 빈칸으로 출제하기 좋다.",
      """UPDATE products
SET stock = stock - 1
WHERE product_id = 2;""",
      "이 SQL은 어느 값을 어떻게 바꾸는가?",
      "상품 번호가 2인 한 행만 찾아 현재 stock에서 1을 빼 새 stock으로 저장한다.",
      ["내가 등록한 상품 하나의 가격을 변경하고 변경 전후를 조회한다.",
       "재고가 0인 상품을 찾는 SELECT를 먼저 작성한다.",
       "삭제 SQL 앞에 반드시 확인 SELECT를 두는 이유를 기록한다."],
      "나중 주문 저장 뒤 재고 감소도 UPDATE로 하게 되므로 변경 안전 원칙이 중요하다.",
      "금요일: 작은 쇼핑몰 상품 DB",
      "상품 수정과 삭제를 포함한 기본 CRUD 문장을 완성한다.",
      ["변경 전후 조회 캡처/결과", "안전한 SQL 규칙 한 문장"]),

    L(7, 5, "PostgreSQL", "완성: 작은 쇼핑몰 상품 DB",
      "테이블 생성, 상품 등록, 조회, 수정, 삭제를 직접 실행하며 상품 관리 데이터베이스를 완성한다.",
      ["CRUD 문장을 순서대로 실행한다.", "표준 SQL과 PostgreSQL 선택 문법을 구분한다.", "SQL 작성 문제에 답한다."],
      "DB 프로젝트의 시연은 질문과 답으로 보인다",
      ["화면 앱이 없어도 DB는 프로젝트다. '1000원 이상 상품 보여 줘', '재고 적은 순으로 보여 줘'라는 질문에 SQL 결과표로 답한다.",
       "자동 번호는 `IDENTITY`를 사용해 표준 SQL 중심 원칙을 유지한다."],
      [("CREATE", "표 만들기"), ("INSERT", "10건 저장"), ("SELECT", "질문 답"), ("UPDATE/DELETE", "관리")],
      "친구 한 명이 사장 역할로 질문하고, 작성자는 SQL을 선택해 결과를 보여 준다.",
      "금요일 제출용 핵심 SQL 묶음 일부다. 실제로는 상품 10건을 입력한다.",
      """CREATE TABLE products (
    product_id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price INTEGER NOT NULL,
    stock INTEGER NOT NULL
);

INSERT INTO products (name, price, stock) VALUES ('콜라', 1200, 10);
INSERT INTO products (name, price, stock) VALUES ('물', 800, 20);
INSERT INTO products (name, price, stock) VALUES ('초콜릿', 1500, 8);

SELECT name, price FROM products
WHERE price >= 1000 ORDER BY price DESC;

UPDATE products SET stock = stock + 5 WHERE name = '물';
SELECT name, stock FROM products ORDER BY stock ASC;""",
      "초콜릿 | 1500\n콜라   | 1200\n-- 이후 물의 재고는 기존 20에서 25로 변경됨",
      ["DDL로 저장 구조를 만들고 DML로 행을 조작한다.",
       "첫 조회는 가격 조건에 맞는 초콜릿과 콜라를 내림차순 출력한다.",
       "UPDATE 뒤 SELECT를 해야 변경된 재고를 확인할 수 있다."],
      "선택 기능으로 `CHECK (price >= 0)`과 `CHECK (stock >= 0)`을 새 테이블 정의에 넣어 본다.",
      "SQL CRUD", "SQL 답안은 문장 순서와 WHERE 조건을 정확히 작성하는 것이 코드 실행만큼 중요하다.",
      """SELECT name
FROM products
WHERE price < 1300 AND stock >= 10
ORDER BY name;""",
      "콜라(1200,10), 물(800,25), 초콜릿(1500,8) 중 결과 행은 무엇인가?",
      "콜라와 물이 두 조건을 만족한다. 초콜릿은 가격에서 제외된다. 결과는 이름 정렬에 따라 두 행이 표시된다.",
      ["상품 10건을 포함한 INSERT 문을 제출한다.",
       "가격 조건 조회, 재고 조건 조회, 수정 전후 조회를 시연한다.",
       "CREATE/INSERT/SELECT/UPDATE/DELETE가 각각 하는 일을 한 줄씩 적는다."],
      "다음 주에는 상품 행에 주문 행을 연결하여 판매량과 매출이라는 질문을 해결한다.",
      "제출 작품: 작은 쇼핑몰 상품 DB",
      "상품 관리의 기본 SQL을 완성한다. 쇼핑몰 후반의 React는 이 테이블을 조회해 화면에 그릴 것이다.",
      ["SQL 스크립트와 결과표", "CRUD 미니 테스트"]),

    L(8, 1, "PostgreSQL", "주문을 왜 두 표로 나누는가",
      "상품 여러 개가 한 주문에 들어갈 수 있으므로 orders와 order_items 관계를 설계한다.",
      ["주문과 주문상세의 역할을 구분한다.", "외래키 연결을 그림으로 이해한다.", "관계 테이블을 생성한다."],
      "영수증 머리와 상품 줄은 서로 다른 정보",
      ["주문자와 주문 시간은 영수증 전체에 한 번만 적지만, 상품과 수량은 여러 줄 들어간다.",
       "그래서 주문 머리 `orders`와 상품 줄 `order_items`를 나누고 같은 order_id로 묶는다."],
      [("orders", "주문 #1 민지"), ("order_id", "1"), ("order_items", "콜라2 / 물1"), ("products", "상품 정보")],
      "영수증 한 장을 그리고 상단 정보와 구매 품목 줄을 색으로 나누어 어떤 표에 들어갈지 표시한다.",
      "7주차 products가 이미 있다고 보고 주문 테이블 두 개를 추가한다.",
      """CREATE TABLE orders (
    order_id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    customer_name VARCHAR(50) NOT NULL,
    ordered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE order_items (
    order_item_id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    order_id INTEGER NOT NULL REFERENCES orders(order_id),
    product_id INTEGER NOT NULL REFERENCES products(product_id),
    quantity INTEGER NOT NULL,
    unit_price INTEGER NOT NULL
);""",
      "CREATE TABLE\nCREATE TABLE\n-- 주문과 주문상세 표가 생성됨",
      ["orders의 한 행은 주문 전체 한 건이다.",
       "order_items에는 같은 order_id가 여러 번 나타날 수 있다.",
       "`REFERENCES`는 존재하는 주문과 상품 번호에만 연결하라는 규칙이다."],
      "한 주문에 상품 두 개가 담긴 그림을 그리고 order_items 행이 몇 개인지 표시한다.",
      "SQL 관계/키", "기사 대비에서는 기본키가 한 행을 식별하고 외래키가 다른 표의 행을 참조한다는 설명이 필수다.",
      """CREATE TABLE child (
    child_id INTEGER PRIMARY KEY,
    product_id INTEGER REFERENCES products(product_id)
);""",
      "`product_id`가 외래키라는 것은 어떤 규칙을 뜻하는가?",
      "child의 product_id 값은 products 테이블에 실제로 존재하는 product_id를 가리켜야 한다는 뜻이다.",
      ["주문 한 건과 상품 세 줄이 연결되는 그림을 그린다.",
       "unit_price를 order_items에 저장하는 이유를 상품 가격이 나중에 바뀌는 상황으로 설명한다.",
       "테이블 생성 SQL을 직접 입력해 실행한다."],
      "주문 당시 가격을 남겨야 나중 상품 가격이 바뀌어도 과거 결제 금액을 다시 계산할 수 있다.",
      "금요일: 쇼핑몰 주문·매출 분석 DB",
      "주문과 주문상세 테이블 구조를 완성한다.",
      ["테이블 생성 SQL", "관계 그림"]),

    L(8, 2, "PostgreSQL", "한 주문에 여러 상품 저장하기",
      "주문 머리 한 건을 만들고 그 주문에 연결된 상품 행들을 입력한다.",
      ["주문 데이터 입력 순서를 이해한다.", "외래키 값을 맞춰 INSERT한다.", "저장된 원시 행을 조회한다."],
      "먼저 영수증 번호를 만들고, 그 번호를 상품 줄마다 적는다",
      ["order_items를 먼저 입력하려면 어느 주문인지 알 수 없다. 따라서 orders 행을 먼저 만들고 생성된 order_id를 확인한다.",
       "수업에서는 복잡한 자동 반환보다 SELECT로 번호를 확인한 뒤 직접 상세 행에 입력한다."],
      [("orders INSERT", "민지"), ("SELECT", "order_id=1"), ("items INSERT", "1, 상품1"), ("items INSERT", "1, 상품2")],
      "주문 번호 스티커를 먼저 만들고 두 상품 카드에 같은 번호를 붙인다.",
      "상품 ID를 조회한 뒤 주문 한 건과 상세 두 건을 입력한다.",
      """INSERT INTO orders (customer_name) VALUES ('민지');

SELECT order_id, customer_name FROM orders;
SELECT product_id, name, price FROM products;

INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (1, 1, 2, 1200);

INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (1, 2, 1, 800);

SELECT order_id, product_id, quantity, unit_price
FROM order_items;""",
      " order_id | product_id | quantity | unit_price\n----------+------------+----------+-----------\n 1        | 1          | 2        | 1200\n 1        | 2          | 1        | 800",
      ["orders 행이 먼저 있어야 order_items의 order_id=1 연결이 유효하다.",
       "상품 번호 역시 products에 먼저 있어야 한다.",
       "같은 order_id 두 줄이 하나의 장바구니 주문을 나타낸다."],
      "지훈의 주문 한 건에 초콜릿 3개를 입력하는 SQL을 작성한다. 실제 order_id는 조회 후 맞춘다.",
      "SQL INSERT 관계", "외래키가 있는 입력은 부모 행이 먼저, 연결되는 자식 행이 다음이라는 순서를 익힌다.",
      """-- orders에 order_id 2가 이미 존재하고 products의 3번 가격은 1500이다.
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (2, 3, 2, 1500);""",
      "이 행이 나타내는 구매 금액은 얼마인가?",
      "상품 3번을 단가 1500에 2개 구매한 상세 행이므로 금액은 3000원이다.",
      ["주문 세 건을 직접 입력한다.",
       "주문 하나에는 상품 두 종류 이상을 넣어 본다.",
       "없는 product_id를 쓰면 왜 거부되어야 하는지 적는다."],
      "이제 데이터는 들어갔지만 상품 이름과 주문자를 한 표로 보려면 JOIN이 필요하다.",
      "금요일: 쇼핑몰 주문·매출 분석 DB",
      "분석할 샘플 주문 데이터를 저장한다.",
      ["주문/상세 INSERT", "외래키 입력 순서 기록"]),

    L(8, 3, "PostgreSQL", "JOIN으로 흩어진 표 다시 읽기",
      "주문자, 상품명, 수량은 서로 다른 테이블에 있으므로 키를 기준으로 연결해 조회한다.",
      ["INNER JOIN의 연결 조건을 읽는다.", "세 테이블 결과를 표시한다.", "잘못된 연결의 문제를 안다."],
      "JOIN은 같은 번호를 가진 카드끼리 옆으로 붙이는 작업",
      ["order_items의 order_id와 orders의 order_id가 같을 때 주문자 이름을 옆에 붙인다.",
       "product_id가 같을 때 products의 상품명을 붙이면 사람이 읽을 수 있는 주문 내역이 된다."],
      [("orders", "#1 민지"), ("order_items", "#1 상품1 x2"), ("products", "상품1 콜라"), ("결과", "민지 콜라 2")],
      "세 종류 카드에서 같은 번호를 실로 이어 하나의 결과 줄을 만든다.",
      "JOIN 조건에 사용되는 키를 소리 내 읽은 뒤 SQL을 실행한다.",
      """SELECT o.customer_name, p.name, i.quantity, i.unit_price
FROM orders AS o
JOIN order_items AS i ON o.order_id = i.order_id
JOIN products AS p ON p.product_id = i.product_id
ORDER BY o.order_id, p.name;""",
      " customer_name | name | quantity | unit_price\n---------------+------+----------+-----------\n 민지          | 물   | 1        | 800\n 민지          | 콜라 | 2        | 1200",
      ["`AS o`, `AS i`, `AS p`는 테이블을 짧은 이름으로 부르는 별칭이다.",
       "첫 JOIN은 주문자와 상세 줄을 주문 번호로 연결한다.",
       "둘째 JOIN은 상품 번호를 상품명으로 읽을 수 있게 붙인다."],
      "결과 열에 `i.quantity * i.unit_price AS subtotal`을 추가하고 각 줄 금액을 확인한다.",
      "SQL JOIN", "JOIN 문제는 어떤 열끼리 같아야 올바른 연결인지 선으로 표시하고 푼다.",
      """SELECT p.name, i.quantity
FROM products p
JOIN order_items i ON p.product_id = i.product_id
WHERE i.quantity >= 2;""",
      "이 조회가 보여 주는 것은 무엇인가?",
      "주문상세 중 수량이 2개 이상인 줄만 골라, 연결된 상품 이름과 수량을 보여 준다.",
      ["세 테이블 연결 결과에 주문 번호도 출력한다.",
       "주문자 이름이 특정 학생인 행만 조회한다.",
       "JOIN 조건에서 product_id 대신 order_id를 잘못 연결하면 왜 의미가 틀리는지 말한다."],
      "쇼핑몰 주문 조회 API는 결국 이 JOIN 결과를 JSON으로 화면에 보낼 수 있다.",
      "금요일: 쇼핑몰 주문·매출 분석 DB",
      "저장된 번호 데이터를 사람이 읽는 주문 내역으로 조회한다.",
      ["JOIN 조회문 2개", "키 연결 그림"]),

    L(8, 4, "PostgreSQL", "GROUP BY로 판매량과 매출 묻기",
      "주문 줄들을 상품별로 묶어 총 판매 수량과 매출을 계산한다.",
      ["집계 함수 SUM을 사용한다.", "GROUP BY가 묶는 기준을 이해한다.", "HAVING과 WHERE의 역할을 구분한다."],
      "집계는 같은 상품 바구니에 주문 줄을 모아 합치는 작업",
      ["콜라가 여러 주문에 등장하면 줄 하나씩 보는 대신 콜라 바구니에 모아 수량과 금액을 더한다.",
       "WHERE는 묶기 전 줄을 고르고 HAVING은 묶은 뒤 합계 기준으로 그룹을 고른다."],
      [("주문줄", "콜라2, 콜라1"), ("GROUP BY", "콜라 묶음"), ("SUM", "수량3"), ("매출", "3600")],
      "상품명별 종이 바구니를 만들고 주문상세 카드를 분류한 뒤 수량과 금액을 합친다.",
      "상품별 판매량과 매출 조회를 작성한다.",
      """SELECT p.name,
       SUM(i.quantity) AS sold_count,
       SUM(i.quantity * i.unit_price) AS sales
FROM products p
JOIN order_items i ON p.product_id = i.product_id
GROUP BY p.product_id, p.name
ORDER BY sales DESC;""",
      " name | sold_count | sales\n------+------------+------\n 콜라 | 2          | 2400\n 물   | 1          | 800\n-- 입력한 주문에 따라 값은 달라짐",
      ["JOIN으로 먼저 상세 줄마다 상품명을 붙인다.",
       "`GROUP BY`가 같은 상품의 줄을 한 묶음으로 만든다.",
       "`SUM(quantity * unit_price)`가 상품별 매출이다."],
      "`HAVING SUM(i.quantity) >= 2`를 추가하면 어떤 묶음만 남을지 예측한다.",
      "SQL 집계", "GROUP BY SQL은 선택 열 중 집계하지 않는 열이 묶음 기준에 들어가는지 확인한다.",
      """SELECT product_id, SUM(quantity) AS total_qty
FROM order_items
GROUP BY product_id
HAVING SUM(quantity) >= 3;""",
      "이 SQL의 결과에 나타나는 상품은 어떤 상품인가?",
      "주문상세를 상품 번호별로 묶은 뒤 총 주문 수량이 3개 이상인 상품 번호와 합계만 결과에 나타난다.",
      ["주문별 총 결제금액을 구하려면 무엇을 GROUP BY해야 하는지 작성한다.",
       "판매량이 높은 순 조회와 매출이 높은 순 조회의 차이를 확인한다.",
       "WHERE와 HAVING을 한 문장으로 구분한다."],
      "금요일 시연에서 '가장 많이 팔린 상품' 질문에 SQL 결과로 답한다.",
      "금요일: 쇼핑몰 주문·매출 분석 DB",
      "상품별 판매량과 매출 조회 문장을 완성한다.",
      ["집계 SQL 3개", "손계산과 SQL 결과 비교"]),

    L(8, 5, "PostgreSQL", "완성: 주문과 매출 분석 DB",
      "상품·주문·주문상세 관계를 이용해 주문 내역과 매출 질문에 SQL로 답하는 프로젝트를 완성한다.",
      ["관계 데이터 입력과 조회를 시연한다.", "JOIN과 집계 SQL을 직접 설명한다.", "쇼핑몰 통합을 준비한다."],
      "DB는 화면 뒤에서 답을 만드는 엔진",
      ["아직 React 화면은 없지만, 상품 목록과 주문 내역과 매출을 모두 데이터로 다룰 수 있다.",
       "다음 주 화면을 붙일 때도 DB 구조는 그대로이고, 조회 결과를 사용자에게 보기 좋게 보여 줄 뿐이다."],
      [("products", "상품"), ("orders/items", "주문"), ("JOIN", "내역"), ("SUM", "매출")],
      "상품 조회 담당, 주문 입력 담당, JOIN 담당, 매출 담당으로 한 번씩 돌아가며 SQL을 실행한다.",
      "핵심 시연용 SQL은 저장된 주문에 대한 사람 읽기 결과와 상품별 매출을 보여 준다.",
      """SELECT o.customer_name, p.name, i.quantity,
       i.quantity * i.unit_price AS subtotal
FROM orders o
JOIN order_items i ON o.order_id = i.order_id
JOIN products p ON p.product_id = i.product_id
ORDER BY o.order_id;

SELECT p.name, SUM(i.quantity) AS sold,
       SUM(i.quantity * i.unit_price) AS sales
FROM products p
JOIN order_items i ON p.product_id = i.product_id
GROUP BY p.product_id, p.name
ORDER BY sales DESC;""",
      "-- 첫 표: 주문자별 구매 품목과 줄 금액\n-- 둘째 표: 상품별 총 판매량과 매출 내림차순",
      ["첫 SQL은 상세한 영수증 줄을 보여 준다.",
       "둘째 SQL은 같은 상품 줄을 모아 분석 결과를 만든다.",
       "두 결과 모두 order_items가 products에 올바른 외래키로 연결되어야 의미가 있다."],
      "선택 기능으로 재고 감소 UPDATE를 작성하되, 주문 저장과 재고 감소가 함께 성공해야 한다는 트랜잭션 개념을 설명만 한다.",
      "SQL 종합", "관계형 SQL 문제에서는 표를 작게 그린 뒤 JOIN 결과 행을 만들고 마지막에 집계한다.",
      """-- A 상품의 상세 행: 수량 2 단가 1000, 수량 3 단가 1000
SELECT SUM(quantity * unit_price)
FROM order_items
WHERE product_id = 1;""",
      "결과 매출은 얼마인가?",
      "두 행의 금액은 2000과 3000이며 SUM 결과는 `5000`이다.",
      ["주문 한 건을 추가하고 JOIN 조회 결과가 늘어나는지 확인한다.",
       "상품별 판매량/매출 SQL을 시연한다.",
       "상품-주문-상세 세 표를 분리한 이유를 그림으로 발표한다."],
      "React 구간에서는 전체 SQL을 다시 쓰지 않고 이 데이터가 화면으로 이동하는 경로를 이해한다.",
      "제출 작품: 쇼핑몰 주문·매출 분석 DB",
      "표준 SQL 중심 구간을 마친다. 다음 주 React는 우선 샘플 상품 배열을 카드 화면으로 렌더링한다.",
      ["SQL 스크립트와 결과표", "JOIN/GROUP BY 미니 테스트"]),
]

LESSONS += [
    L(9, 1, "React", "콘솔 밖으로: 화면에 상점 제목 띄우기",
      "이제까지 터미널과 결과표에서 보던 데이터를 브라우저 화면으로 보여 준다. 오늘은 React 앱의 시작점만 만진다.",
      ["React가 화면을 만드는 역할임을 안다.", "제공된 프로젝트를 실행한다.", "JSX로 문장과 가격을 표시한다."],
      "React는 값을 화면 모양으로 번역하는 진열 담당",
      ["PostgreSQL은 상품을 저장했고 Python은 계산했다. React는 사용자가 클릭하고 보는 화면을 담당한다.",
       "처음부터 설정 명령을 외우지 않는다. 교사가 준비한 실행 가능한 기본 폴더에서 `App.jsx`의 보이는 부분만 직접 바꾼다."],
      [("데이터", "상점명"), ("App", "JSX"), ("브라우저", "제목 표시")],
      "종이에 DB 창고, API 배송로, React 진열대 그림을 그리고 오늘은 진열대 표지판만 만드는 날임을 표시한다.",
      "교사가 제공한 React 기본 프로젝트에서 `src/App.jsx` 내용을 아래처럼 작성한다.",
      """export default function App() {
  const shopName = "우리 반 상점";
  const message = "필요한 학용품을 골라 보세요.";

  return (
    <main>
      <h1>{shopName}</h1>
      <p>{message}</p>
      <p>이번 주 목표: 상품 카드 만들기</p>
    </main>
  );
}""",
      "브라우저 화면:\n우리 반 상점\n필요한 학용품을 골라 보세요.\n이번 주 목표: 상품 카드 만들기",
      ["함수 `App`은 화면 조각을 반환한다.",
       "중괄호 `{shopName}`은 JavaScript 값을 화면 문장 안에 넣는다.",
       "저장하면 개발 서버가 변경된 화면을 다시 보여 준다."],
      "shopName과 message를 자기 상점 문구로 바꾸고 브라우저에 바로 반영되는지 확인한다.",
      "언어 비교", "React 자체는 기사 핵심 코드 범위보다 프로젝트 경험용이다. 대신 JavaScript 표현식의 값 흐름을 추적한다.",
      """const price = 1200;
const count = 2;
const text = price * count + "원";
// 화면에는 {text}를 표시한다.""",
      "`text`에 들어 있는 문자열은 무엇인가?",
      "먼저 숫자 곱셈 2400이 계산되고 문자열 `원`이 붙어 `2400원`이 된다.",
      ["`today` 변수를 만들어 오늘의 추천 상품 문구에 표시한다.",
       "숫자 가격 변수를 화면에 `1200원` 형태로 표시한다.",
       "React가 DB 대신 화면을 담당한다는 역할표를 작성한다."],
      "이번 주는 DB 연결 없이 샘플 값으로 화면 작성 감각만 익힌다.",
      "금요일: 쇼핑몰 상품 목록 화면",
      "상점 제목과 안내 문구가 표시되는 첫 React 화면을 실행한다.",
      ["실행 화면 확인", "App JSX 설명 한 문장"]),

    L(9, 2, "React", "ProductCard로 상품 한 장 만들기",
      "상품명, 가격, 재고를 받으면 한 장의 상품 카드가 되는 컴포넌트를 작성한다.",
      ["컴포넌트를 함수로 작성한다.", "props로 값을 전달한다.", "한 상품의 표시 구조를 만든다."],
      "컴포넌트는 모양이 같은 상품 카드 틀",
      ["콜라 카드와 물 카드는 값은 다르지만 보이는 모양은 같다. 카드 틀 하나를 만들고 서로 다른 값을 건네면 중복을 줄인다.",
       "`props`는 부모 화면이 카드에 건네는 상품 정보 봉투다."],
      [("App", "상품 값 전달"), ("props", "name/price/stock"), ("ProductCard", "카드 틀"), ("화면", "상품 한 장")],
      "빈 상품 카드 양식을 한 장 그리고, 이름/가격/재고 포스트잇만 바꿔 여러 상품이 되는 모습을 만든다.",
      "같은 `App.jsx`에서 작은 컴포넌트 함수를 위에 작성한다.",
      """function ProductCard({ name, price, stock }) {
  return (
    <article className="product-card">
      <h2>{name}</h2>
      <p>{price}원</p>
      <p>남은 수량: {stock}</p>
      <button>담기</button>
    </article>
  );
}

export default function App() {
  return (
    <main>
      <h1>우리 반 상점</h1>
      <ProductCard name="노트" price={2000} stock={5} />
    </main>
  );
}""",
      "화면에 노트 / 2000원 / 남은 수량: 5 / 담기 버튼이 카드로 표시됨",
      ["`ProductCard`는 전달받은 세 값을 자신의 화면 위치에 배치한다.",
       "`price={2000}`은 숫자 값을 전달한다.",
       "아직 담기 버튼은 보이기만 하고 클릭 기능은 없다."],
      "같은 컴포넌트를 한 번 더 호출해 펜 상품 카드를 추가한다.",
      "컴포넌트 값", "코드 결과를 읽을 때 같은 함수가 서로 다른 인자로 호출된다는 점은 이전 Java 메서드와 닮았다.",
      """function Label({ price }) {
  return <p>{price + 500}원</p>;
}
// <Label price={1000} />""",
      "화면 문구는 무엇인가?",
      "price 숫자 1000에 500을 더해 `1500원`이 표시된다.",
      ["상품 카드 두 장을 서로 다른 값으로 표시한다.",
       "stock을 0으로 바꾸고 아직 버튼이 그대로인 것을 관찰한다.",
       "Java Drink 객체의 필드와 ProductCard props의 차이를 적는다."],
      "props는 표시할 값이며, 다음에는 배열 데이터를 카드 여러 장으로 반복 표시한다.",
      "금요일: 쇼핑몰 상품 목록 화면",
      "재사용 가능한 상품 카드 한 장을 작성한다.",
      ["ProductCard 코드", "두 상품 표시 화면"]),

    L(9, 3, "React", "배열을 map으로 카드 목록에 펼치기",
      "샘플 상품 배열을 만들고 상품 수만큼 ProductCard를 화면에 표시한다.",
      ["객체 배열을 읽는다.", "`map`의 반복 표시를 이해한다.", "상품 ID를 key로 사용한다."],
      "map은 상품 박스를 하나씩 카드 틀에 넣는 컨베이어벨트",
      ["Python에서 상품 목록을 반복 계산했던 것처럼 React는 배열을 돌며 화면 카드를 하나씩 만든다.",
       "`key`는 React가 각 카드를 구별하기 위한 번호이며, DB의 product_id가 나중에 적합한 key가 된다."],
      [("products 배열", "3개"), ("map", "하나씩 꺼냄"), ("ProductCard", "3회 생성"), ("화면", "카드 3장")],
      "상품 카드 세 장을 ProductCard 틀 위로 한 장씩 통과시키는 화살표를 그린다.",
      "어제 카드 함수는 그대로 두고 App의 데이터와 반복 표시를 변경한다.",
      """const products = [
  { id: 1, name: "노트", price: 2000, stock: 5 },
  { id: 2, name: "펜", price: 1000, stock: 8 },
  { id: 3, name: "파일", price: 1500, stock: 0 }
];

export default function App() {
  return (
    <main>
      <h1>상품 목록</h1>
      <section className="products">
        {products.map((product) => (
          <ProductCard key={product.id}
            name={product.name}
            price={product.price}
            stock={product.stock} />
        ))}
      </section>
    </main>
  );
}""",
      "노트, 펜, 파일의 카드 총 3장이 화면에 표시됨",
      ["products에는 객체 세 개가 들어 있다.",
       "`map`은 각 객체를 `product`라는 이름으로 받아 ProductCard를 하나 반환한다.",
       "세 번째 객체 stock은 0이지만 조건 처리를 아직 하지 않아 카드가 그냥 표시된다."],
      "상품 하나를 배열 끝에 추가하고 카드 개수가 자동으로 늘어나는 것을 확인한다.",
      "배열 반복", "React 코드라도 배열 순회와 각 객체 값 읽기는 Java/Python에서 익힌 추적 감각을 사용한다.",
      """const data = [
  { price: 1000 },
  { price: 2000 },
  { price: 500 }
];
const total = data.reduce((sum, item) => sum + item.price, 0);""",
      "`total` 값은 얼마인가?",
      "세 가격을 차례로 더하여 `3500`이다. 장바구니 총액에서도 같은 누적 개념을 쓴다.",
      ["네 번째 상품을 추가하여 카드 네 장을 표시한다.",
       "상품 순서를 바꾸면 화면 순서도 달라지는지 관찰한다.",
       "map을 Python `for product in products`와 말로 비교한다."],
      "다음에는 stock 값에 따라 담기 버튼의 사용 여부를 다르게 표시한다.",
      "금요일: 쇼핑몰 상품 목록 화면",
      "샘플 상품 배열 네 개를 카드 목록으로 렌더링한다.",
      ["상품 배열과 map 코드", "카드 개수 확인"]),

    L(9, 4, "React", "품절 상태와 버튼 클릭 표시",
      "재고가 없는 상품은 담을 수 없다는 표시를 하고, 버튼 클릭 시 선택 상품을 알려 준다.",
      ["조건부 표시를 작성한다.", "클릭 이벤트 함수를 연결한다.", "데이터 상태와 화면 반응을 구분한다."],
      "화면은 데이터의 상태를 보여 주는 표정",
      ["stock이 0이라는 값이 있으면 화면은 버튼을 막고 품절이라고 알려야 한다.",
       "오늘 클릭은 장바구니 저장 전 단계로, 버튼을 눌렀다는 반응만 확인한다."],
      [("stock", "0"), ("조건", "stock === 0"), ("버튼", "disabled"), ("사용자", "품절 확인")],
      "상품 카드의 재고 숫자에 따라 초록 담기 카드와 회색 품절 카드를 나누어 놓는다.",
      "ProductCard에 클릭 함수와 조건을 추가한다.",
      """function ProductCard({ name, price, stock }) {
  function handleAdd() {
    alert(name + " 상품을 선택했습니다.");
  }

  return (
    <article className="product-card">
      <h2>{name}</h2>
      <p>{price}원</p>
      <p>{stock === 0 ? "품절" : "재고 " + stock + "개"}</p>
      <button onClick={handleAdd} disabled={stock === 0}>
        {stock === 0 ? "담을 수 없음" : "담기"}
      </button>
    </article>
  );
}""",
      "재고가 있는 카드는 담기 버튼 클릭 시 알림 표시\n재고 0 카드는 품절/담을 수 없음 표시와 비활성 버튼",
      ["삼항 연산자는 조건이 참일 때 앞 문구, 거짓일 때 뒤 문구를 고른다.",
       "`disabled={stock === 0}`은 품절일 때 버튼을 누를 수 없게 한다.",
       "클릭 함수는 상품명 props를 읽어 반응한다."],
      "재고 0인 파일 카드와 재고 1인 파일 카드의 화면 차이를 비교한다.",
      "조건 표현식", "프로젝트용 JavaScript에서도 조건의 참/거짓을 판별하는 연습은 기사 언어 문제와 공통이다.",
      """const stock = 0;
const label = stock === 0 ? "품절" : "판매중";
const disabled = stock === 0;""",
      "`label`과 `disabled`에는 무엇이 들어가는가?",
      "stock이 0과 정확히 같으므로 label은 `품절`, disabled는 참(`true`)이다.",
      ["품절 상품과 판매 상품을 각각 하나씩 화면에 표시한다.",
       "버튼 문구를 내 문구로 바꿔 본다.",
       "클릭은 아직 주문 저장이 아니라는 점을 데이터 흐름 그림에 표시한다."],
      "내일 프로젝트에는 화면 표시 기능만 필수로 하고 실제 장바구니 상태는 11주차에 다룬다.",
      "금요일: 쇼핑몰 상품 목록 화면",
      "품절 표시와 담기 버튼 반응을 카드 컴포넌트에 추가한다.",
      ["품절/판매 화면 검사", "클릭 이벤트 설명"]),

    L(9, 5, "React", "완성: 쇼핑몰 상품 목록 화면",
      "제공된 React 뼈대 위에서 상점 제목, 상품 카드, 품절 표시와 담기 반응을 완성해 시연한다.",
      ["상품 목록 화면을 처음부터 재구성한다.", "데이터가 카드로 변환되는 흐름을 설명한다.", "다음 주 API 연결 지점을 찾는다."],
      "오늘 화면의 상품은 임시 목록, 다음 주에는 DB 목록",
      ["지금은 `products` 배열이 파일 안에 직접 적혀 있다. 화면 구조를 배우기에는 충분하지만 새로고침해도 DB 변경과 연결되지 않는다.",
       "다음 주에는 배열을 PostgreSQL에서 API로 받은 결과로 교체한다. 카드 컴포넌트는 거의 그대로 재사용한다."],
      [("샘플 배열", "오늘"), ("ProductCard", "재사용"), ("API 응답", "다음 주"), ("화면", "같은 카드")],
      "오늘 배열에 적힌 상품과 7주차 DB 상품 표 사이에 다음 주 화살표를 그린다.",
      "상품 데이터와 카드 코드를 한 파일로 합친 필수 버전이다. CSS는 교사 제공 파일을 사용한다.",
      """function ProductCard({ name, price, stock }) {
  return (
    <article className="product-card">
      <h2>{name}</h2>
      <p>{price.toLocaleString()}원</p>
      <p>{stock === 0 ? "품절" : `재고 ${stock}개`}</p>
      <button disabled={stock === 0}>담기</button>
    </article>
  );
}

const products = [
  { id: 1, name: "노트", price: 2000, stock: 5 },
  { id: 2, name: "펜", price: 1000, stock: 8 },
  { id: 3, name: "파일", price: 1500, stock: 0 },
  { id: 4, name: "스티커", price: 500, stock: 12 }
];

export default function App() {
  return (
    <main>
      <h1>우리 반 상점</h1>
      <section className="products">
        {products.map(product => (
          <ProductCard key={product.id} {...product} />
        ))}
      </section>
    </main>
  );
}""",
      "우리 반 상점 제목 아래 상품 카드 4장 표시\n파일 상품만 품절 버튼으로 표시",
      ["네 상품 객체가 map을 통과하며 같은 ProductCard 모양 네 장이 된다.",
       "`{...product}`는 객체의 name, price, stock을 props로 전달하는 짧은 표기다.",
       "품절 조건은 각 카드가 받은 stock 값으로 판단한다."],
      "펼침 문법이 어렵다면 `name={product.name}` 방식으로 다시 적어 보고 같은 결과인지 확인한다.",
      "화면 데이터 흐름", "React는 기사 직접 범위보다 통합 경험을 위한 도구다. 배열/조건/함수 감각은 계속 활용한다.",
      """const products = [
  { name: "A", stock: 0 },
  { name: "B", stock: 2 }
];
const available = products.filter(p => p.stock > 0);""",
      "`available`에 남는 상품 이름은 무엇인가?",
      "stock이 0보다 큰 B만 남는다.",
      ["상품 네 장이 표시되는지 확인한다.",
       "품절 상품 버튼이 눌리지 않는지 확인한다.",
       "샘플 배열을 API 응답으로 바꿀 위치에 표시를 붙인다."],
      "금요일 완성 화면을 저장한다. 다음 주 공통 API 뼈대가 준비되면 DB 상품으로 같은 카드를 그린다.",
      "제출 작품: 쇼핑몰 상품 목록 화면",
      "브라우저 시연과 컴포넌트 설명을 제출한다.",
      ["동작하는 React 상품 화면", "배열 -> 카드 흐름 설명"]),

    L(10, 1, "React + API", "화면과 DB 사이에 API 놓기",
      "React가 PostgreSQL에 직접 접속하지 않고 Python API를 통해 상품 JSON을 받는 전체 경로를 먼저 경험한다.",
      ["프론트/API/DB 역할을 나눈다.", "제공된 서버를 실행해 JSON을 확인한다.", "SELECT 결과와 JSON을 연결한다."],
      "API는 창고와 매장 사이의 전달 창구",
      ["브라우저에 DB 비밀번호를 넣어 직접 연결하면 위험하고 구조도 복잡하다. 서버가 DB에 질문하고 필요한 결과만 JSON으로 전한다.",
       "서버 설정과 연결 코드는 교사 제공 뼈대를 사용한다. 학생의 핵심 학습은 조회 SQL과 화면 fetch 흐름이다."],
      [("React", "GET /products"), ("Python API", "SELECT"), ("PostgreSQL", "행"), ("JSON", "화면으로")],
      "세 사람을 React, API, DB 역할로 세워 상품 요청 카드와 결과 카드를 주고받는다.",
      "교사 제공 API의 조회 함수에서 학생이 직접 읽고 수정할 핵심 SQL 예시다.",
      """# 교사 제공 서버 뼈대 안의 핵심 함수 예시
def get_products(connection):
    sql = '''
        SELECT product_id, name, price, stock
        FROM products
        ORDER BY product_id
    '''
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return rows

# 브라우저에서 GET /products를 열면 JSON 상품 목록 확인""",
      '[{"product_id":1,"name":"콜라","price":1200,"stock":10}, ...]',
      ["React는 SQL을 직접 알 필요 없이 `/products` 주소에 목록을 요청한다.",
       "API 서버 내부에서는 7주차에 배운 SELECT가 실행된다.",
       "행 데이터가 JSON 모양으로 변환되어 브라우저로 전달된다."],
      "SQL의 `ORDER BY price DESC`로 바꾸면 JSON의 상품 순서가 어떻게 달라질지 예측한다.",
      "통합/SQL", "기사 대비에서는 여전히 SELECT 문장을 직접 읽고 작성하는 능력을 확인한다.",
      """SELECT name, price
FROM products
WHERE stock > 0
ORDER BY price ASC;""",
      "이 API가 화면에 제공하려는 상품 목록은 어떤 조건과 순서인가?",
      "재고가 1개 이상 있는 상품만 가격이 낮은 순으로 제공하려는 조회다.",
      ["React/API/DB를 각기 다른 색으로 칠한 흐름도를 작성한다.",
       "API가 실행할 상품 전체 조회 SQL을 직접 입력한다.",
       "브라우저에서 받은 JSON의 한 객체와 products의 한 행을 연결한다."],
      "서버의 패키지 설치와 연결 설정은 강사가 준비하며, 학생은 작동 흐름과 SQL을 이해한다.",
      "금요일: DB 연동 상품 목록과 등록",
      "DB 상품을 JSON으로 가져올 준비를 하고, API가 필요한 이유를 설명한다.",
      ["데이터 흐름 그림", "상품 조회 SQL"]),

    L(10, 2, "React + API", "fetch로 DB 상품 카드 표시하기",
      "지난주 파일 안 배열 대신 API에서 받은 상품 배열을 상태에 저장하여 같은 카드 화면을 그린다.",
      ["`useState`의 저장 역할을 안다.", "`useEffect`에서 한 번 조회한다.", "API 결과가 map으로 표시됨을 확인한다."],
      "상태는 화면이 기억하고 다시 그릴 현재 데이터",
      ["샘플 배열은 고정된 글씨였지만 API 상품은 요청이 끝난 뒤 도착한다. React는 도착한 배열을 `products` 상태에 저장하고 새 화면을 그린다.",
       "처음 빈 배열이라 카드가 없다가, fetch 완료 뒤 DB 상품 카드가 나타난다."],
      [("처음", "[]"), ("fetch", "GET /products"), ("setProducts", "DB 배열"), ("render", "카드 표시")],
      "빈 진열대를 그린 뒤 배송 트럭(API 결과)이 도착하면 카드 네 장을 올리는 장면을 그린다.",
      "기존 ProductCard는 유지하고 App에서 상품을 가져오는 부분을 작성한다.",
      """import { useEffect, useState } from "react";

export default function App() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/products")
      .then(response => response.json())
      .then(data => setProducts(data));
  }, []);

  return (
    <main>
      <h1>DB 상품 목록</h1>
      {products.map(product => (
        <ProductCard key={product.product_id} {...product} />
      ))}
    </main>
  );
}""",
      "PostgreSQL products에 저장된 상품들이 React 카드로 표시됨",
      ["상태의 시작값은 빈 배열이다.",
       "`[]`가 있는 useEffect는 화면 시작 시 한 번 상품을 요청하는 구조다.",
       "응답 데이터가 상태에 들어가면 map이 카드들을 만든다."],
      "DB에서 상품 가격 하나를 UPDATE하고 브라우저를 새로고침해 카드 가격 변화가 반영되는지 확인한다.",
      "데이터 입출력", "조회 화면의 정확성은 결국 서버가 실행한 SQL 결과가 맞는지에서 출발한다.",
      """-- DB 가격을 변경한 후 API가 실행하는 문장
SELECT name, price
FROM products
WHERE product_id = 2;""",
      "상품 2 가격을 1800으로 UPDATE했다면 화면에는 어떤 가격이 보여야 하는가?",
      "API가 최신 행을 다시 조회하므로 상품 2 카드는 1800원을 표시해야 한다.",
      ["API가 꺼져 있을 때 화면이 데이터를 못 받는 상황을 관찰한다.",
       "DB 상품 하나를 변경하고 화면 결과를 확인한다.",
       "샘플 배열과 API 상태 배열의 차이를 적는다."],
      "학생이 직접 작성할 React 핵심은 상태 선언, fetch, map 세 부분이다.",
      "금요일: DB 연동 상품 목록과 등록",
      "DB의 실제 상품 목록을 React 카드로 보여 준다.",
      ["fetch 작성 코드", "DB 변경-화면 확인 기록"]),

    L(10, 3, "React + API", "입력 폼으로 새 상품 받기",
      "상품명, 가격, 재고 입력값을 React 상태로 관리하고 저장 버튼을 만든다.",
      ["입력 필드 상태를 연결한다.", "숫자 입력을 변환한다.", "전송할 상품 객체를 확인한다."],
      "폼은 사용자가 새 상품 카드를 작성하는 입력지",
      ["화면의 입력칸 값은 사용자가 타이핑할 때마다 상태에 기록된다.",
       "가격과 재고는 화면에서 문자열로 들어오므로 서버에 보내기 전 숫자 변환과 빈 값 검사가 필요하다."],
      [("입력창", "노트"), ("state", "name/price/stock"), ("버튼", "전송 준비"), ("객체", "{...}")],
      "빈 상품 등록 카드에 이름·가격·재고를 직접 적은 뒤 세 값이 모두 있어야 제출 가능하다고 표시한다.",
      "오늘은 아직 실제 저장보다 폼 입력 상태와 제출 객체 확인에 집중한다.",
      """import { useState } from "react";

function ProductForm() {
  const [name, setName] = useState("");
  const [price, setPrice] = useState("");
  const [stock, setStock] = useState("");

  function handleSubmit(event) {
    event.preventDefault();
    const newProduct = {
      name: name,
      price: Number(price),
      stock: Number(stock)
    };
    console.log(newProduct);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input value={name} onChange={e => setName(e.target.value)} placeholder="상품명" />
      <input value={price} onChange={e => setPrice(e.target.value)} placeholder="가격" />
      <input value={stock} onChange={e => setStock(e.target.value)} placeholder="재고" />
      <button>상품 등록</button>
    </form>
  );
}""",
      "입력 후 버튼 클릭 시 개발자 콘솔:\n{name: '노트', price: 2000, stock: 5}",
      ["각 input은 상태값을 표시하고 입력 이벤트가 상태를 갱신한다.",
       "`preventDefault()`는 폼 제출 시 페이지가 새로 열리는 기본 행동을 막는다.",
       "`Number`는 DB에 숫자로 보낼 가격과 재고를 만든다."],
      "가격 칸에 글자를 입력하면 Number 결과가 올바른 숫자가 아닌 상황을 확인하고 검증 문구를 생각한다.",
      "입력 검증", "기사 보안·구현 관점에서도 외부 입력을 그대로 믿지 않고 검증한다는 원칙이 연결된다.",
      """const price = Number("2000");
const stock = Number("3");
const total = price * stock;""",
      "`total` 값은 얼마인가?",
      "문자열이 숫자로 변환되어 2000 * 3인 `6000`이다.",
      ["입력칸 3개를 화면에 표시한다.",
       "버튼 클릭 후 콘솔에 입력 객체가 보이는지 확인한다.",
       "빈 이름이나 음수 가격을 막아야 하는 이유를 적는다."],
      "내일은 이 입력 객체를 API로 보내 실제 INSERT 문을 실행한다.",
      "금요일: DB 연동 상품 목록과 등록",
      "상품 등록 폼과 전송할 데이터 모양을 완성한다.",
      ["상품 폼 화면", "입력 검증 메모"]),

    L(10, 4, "React + API", "POST와 INSERT로 상품 저장하기",
      "등록 폼의 상품 객체를 API로 보내고, API가 PostgreSQL에 INSERT하도록 연결한다.",
      ["POST 요청의 목적을 안다.", "서버 INSERT SQL을 읽고 작성한다.", "저장 후 목록을 다시 조회한다."],
      "등록은 화면 카드가 아니라 DB 창고에 새 상자를 넣는 일",
      ["화면에서만 상품을 추가하면 새로고침 뒤 사라진다. API가 INSERT를 실행해야 DB에 남는다.",
       "학생은 React의 fetch POST와 서버 함수 안의 표준 INSERT 문장을 핵심으로 입력한다. DB 연결 설정은 제공한다."],
      [("폼", "상품 객체"), ("POST", "/products"), ("INSERT", "products 행"), ("GET", "새 목록")],
      "상품 등록 카드를 API 창구를 통해 DB 표에 넣고, 다시 목록 요청으로 진열대에 올리는 그림을 그린다.",
      "서버 함수의 핵심 SQL과 React 제출 코드의 핵심 호출을 함께 본다.",
      """# API 함수 안에서 학생이 확인할 핵심 SQL
sql = '''
    INSERT INTO products (name, price, stock)
    VALUES (%s, %s, %s)
'''
cursor.execute(sql, (name, price, stock))

// React handleSubmit 안의 핵심 요청
await fetch("http://localhost:8000/products", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(newProduct)
});
loadProducts(); // 저장 후 GET으로 목록 다시 읽기""",
      "등록 폼에서 노트/2000/5 입력 -> DB products 새 행 생성 -> 상품 카드 목록에 노트 표시",
      ["SQL VALUES 자리는 입력값을 안전하게 전달하는 매개변수 방식으로 채운다.",
       "POST 성공 뒤 목록을 다시 조회해야 DB가 만든 product_id까지 화면에 반영된다.",
       "React 상태만 바꾼 것이 아니라 DB 행이 늘어났는지 SQL SELECT로 확인한다."],
      "등록 전후 `SELECT COUNT(*) FROM products;` 결과를 기록한다.",
      "SQL/보안", "입력 문자열을 SQL 문장에 직접 이어 붙이지 않고 매개변수로 전달하는 것은 SQL Injection 예방의 기본이다.",
      """-- 직접 연결하지 않는 안전한 작성 방향
INSERT INTO products (name, price, stock)
VALUES (?, ?, ?);
-- 실제 자리표시는 드라이버 방식에 따라 달라질 수 있다.""",
      "왜 입력한 상품명을 SQL 문자열에 그대로 더해 만들지 않는가?",
      "입력 내용이 SQL 명령으로 해석되는 공격과 문법 오류를 막기 위해 값은 매개변수로 전달한다.",
      ["상품 한 건을 폼으로 등록하고 DB 조회로 확인한다.",
       "빈 상품명이나 음수 값은 요청 전 막는 조건을 추가한다.",
       "React -> API -> INSERT -> GET -> React 흐름을 다섯 화살표로 적는다."],
      "금요일에는 상품 조회와 등록만 안정적으로 시연하면 완성이다.",
      "금요일: DB 연동 상품 목록과 등록",
      "새 상품을 저장하고 카드 목록에 다시 나타나게 연결한다.",
      ["INSERT 확인 결과", "등록 흐름 그림"]),

    L(10, 5, "React + API", "완성: DB 상품 조회와 등록",
      "PostgreSQL의 상품을 화면에 표시하고 입력 폼으로 새 상품을 등록하는 첫 통합 기능을 완성한다.",
      ["조회와 등록 흐름을 시연한다.", "오류 입력을 검사한다.", "SQL이 화면 기능과 연결되는 지점을 설명한다."],
      "하나의 버튼 뒤에 네 단계가 있다",
      ["상품 등록 버튼은 단순 클릭이 아니라 입력 검사, API 전송, DB INSERT, 목록 재조회라는 연쇄 동작을 시작한다.",
       "모든 서버 코드를 외우는 것이 아니라, 본인이 쓴 입력값과 SQL이 어디서 만나는지 설명하면 된다."],
      [("입력검사", "React"), ("전송", "POST"), ("저장", "INSERT"), ("표시", "GET/map")],
      "버튼을 누른 뒤 일어나는 네 단계를 학생마다 한 장씩 들고 순서대로 서 본다.",
      "금요일 학생 직접 작성 범위의 중심은 상품 조회와 등록 함수다.",
      """async function loadProducts() {
  const response = await fetch("http://localhost:8000/products");
  const data = await response.json();
  setProducts(data);
}

async function saveProduct(product) {
  if (!product.name || product.price < 0 || product.stock < 0) {
    alert("입력값을 확인하세요.");
    return;
  }
  await fetch("http://localhost:8000/products", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(product)
  });
  await loadProducts();
}""",
      "화면에서 상품 등록 -> PostgreSQL 행 증가 -> 새 카드가 목록에 나타남\n음수 가격 입력 -> 안내 후 저장되지 않음",
      ["loadProducts는 DB 결과가 담긴 API 응답으로 상태를 교체한다.",
       "saveProduct는 먼저 입력을 검사하여 잘못된 값이 서버로 가지 않게 한다.",
       "성공한 저장 뒤 loadProducts 호출로 화면과 DB를 일치시킨다."],
      "등록 뒤 화면에 보인다고 DB 저장을 단정하지 말고 SQL SELECT로도 확인한다.",
      "통합 구현", "통합 구현 문제는 데이터가 입력에서 저장, 출력까지 이동하는 단계를 분리해 이해한다.",
      """SELECT name, price, stock
FROM products
WHERE price >= 1000
ORDER BY product_id DESC;""",
      "새로 등록한 2000원 상품은 조건에 포함되는가? 결과 정렬은 무엇을 뜻하는가?",
      "2000원은 조건을 만족한다. 큰 product_id부터 표시하므로 일반적으로 최근 생성된 번호가 앞에 온다.",
      ["DB 상품 세 개 이상이 카드로 보이는지 확인한다.",
       "새 상품 한 건을 등록하고 SQL로 저장을 확인한다.",
       "음수 가격이 막히는지 검사하고 오류 기록을 제출한다."],
      "다음 주에는 지금 보이는 상품을 실제 장바구니 상태에 담고 orders 테이블에 저장한다.",
      "제출 작품: DB 연동 상품 목록과 등록",
      "상품 조회/등록의 작동 화면과 데이터 이동 설명을 제출한다.",
      ["React+API 실행 화면", "상품 등록 SQL 확인"]),

    L(11, 1, "React + API", "담기 버튼으로 장바구니 상태 만들기",
      "상품 카드의 담기 버튼을 누르면 선택한 상품이 cart 상태 배열에 들어가도록 만든다.",
      ["장바구니 상태를 선언한다.", "클릭 시 상품을 추가한다.", "상품 목록과 장바구니를 구분한다."],
      "상품 진열대와 장바구니는 서로 다른 목록",
      ["상품 목록은 판매 가능한 전체 상품이고, 장바구니는 사용자가 이번 주문에 선택한 상품이다.",
       "DB 주문 저장은 아직 하지 않는다. 먼저 화면 안에서 담기와 목록 표시가 정확해야 한다."],
      [("products", "진열대"), ("담기 클릭", "addToCart"), ("cart", "선택 목록"), ("화면", "장바구니")],
      "진열대 카드 복사본을 장바구니 영역으로 옮겨 놓되 원래 진열대 카드가 사라지지 않음을 보여 준다.",
      "App에 cart 상태와 추가 함수를 작성하고 버튼에 함수를 전달한다.",
      """const [cart, setCart] = useState([]);

function addToCart(product) {
  setCart([...cart, product]);
}

// 상품 카드 표시 부분
<button onClick={() => addToCart(product)}>담기</button>

// 장바구니 표시 부분
<h2>장바구니</h2>
{cart.map((item, index) => (
  <p key={index}>{item.name} - {item.price}원</p>
))}""",
      "노트 담기 버튼 클릭 -> 장바구니 영역에 `노트 - 2000원` 표시",
      ["cart는 처음 빈 배열이다.",
       "펼침 `...cart`는 이전 담긴 상품을 유지하고 새 상품을 끝에 더한다.",
       "오늘 버전은 같은 상품을 누를 때 행이 하나씩 추가되는 단순 규칙이다."],
      "같은 상품을 두 번 담아 행 두 개가 생기는지 확인하고, 수량 방식은 선택 확장임을 기록한다.",
      "배열 상태", "장바구니 합계는 6주차 Python의 total 누적과 같은 자료 흐름이다.",
      """const cart = [
  { price: 1000 },
  { price: 1000 },
  { price: 500 }
];
const total = cart.reduce((sum, item) => sum + item.price, 0);""",
      "`total`은 얼마인가?",
      "각 장바구니 행 가격을 더해 `2500`이다.",
      ["상품 두 개를 차례로 담아 표시한다.",
       "빈 장바구니일 때 안내 문구를 조건 표시한다.",
       "products와 cart가 무엇을 뜻하는지 표로 비교한다."],
      "내일은 cart 배열의 가격을 합산하여 결제 예정 금액을 표시한다.",
      "금요일: 장바구니 주문 저장",
      "화면 장바구니에 상품을 추가하는 기능을 만든다.",
      ["장바구니 표시 화면", "상태 변화 설명"]),

    L(11, 2, "React + API", "장바구니 총액 계산하기",
      "장바구니 배열에 담긴 상품 가격을 합산해 주문 전 총액을 보여 준다.",
      ["`reduce` 누적 계산을 이해한다.", "빈 장바구니 총액을 처리한다.", "Python 할인 계산과 연결한다."],
      "reduce는 장바구니 항목을 계산대 위로 하나씩 올리는 일",
      ["Python에서는 반복문으로 `total += price`를 썼다. JavaScript의 `reduce`는 같은 합산을 짧게 표현한다.",
       "필수 기능은 상품을 여러 번 담으면 각각 한 개씩 계산하는 단순 규칙이다."],
      [("시작 sum", "0"), ("노트", "+2000"), ("펜", "+1000"), ("총액", "3000")],
      "6주차 Python total 변화표 옆에 React cart sum 변화표를 동일하게 작성한다.",
      "장바구니 표시 아래 총액 한 줄을 추가한다.",
      """const total = cart.reduce((sum, item) => {
  return sum + item.price;
}, 0);

return (
  <aside>
    <h2>장바구니</h2>
    {cart.map((item, index) => (
      <p key={index}>{item.name} {item.price}원</p>
    ))}
    <strong>총액: {total.toLocaleString()}원</strong>
  </aside>
);""",
      "장바구니: 노트 2000원 / 펜 1000원\n총액: 3,000원",
      ["reduce의 sum은 0에서 시작한다.",
       "각 item의 price가 sum에 추가되어 최종 숫자가 total이 된다.",
       "cart가 비어 있으면 반복할 항목이 없어 total은 초기값 0이다."],
      "동일한 노트를 두 번 담았을 때 총액이 두 배가 되는지 먼저 예상하고 확인한다.",
      "누적 계산", "언어가 달라도 누적 합계를 추적하는 표는 똑같이 사용할 수 있다.",
      """const prices = [1200, 800, 1500];
const total = prices.reduce((sum, price) => sum + price, 0);
const discount = total >= 3000 ? 500 : 0;""",
      "`total`과 `discount`는 무엇인가?",
      "합계는 3500이고 3000 이상 조건을 만족하므로 discount는 500이다.",
      ["빈 장바구니에서 총액 0을 확인한다.",
       "상품 세 개를 담아 손계산과 화면 총액을 비교한다.",
       "6주차 할인 계산을 선택 기능으로 화면에 추가할 위치를 표시한다."],
      "주문 저장에는 cart의 각 상품 번호와 당시 가격이 필요하다.",
      "금요일: 장바구니 주문 저장",
      "사용자가 담은 상품의 결제 예정 총액을 표시한다.",
      ["총액 계산 코드", "손계산 대조 기록"]),

    L(11, 3, "React + API", "주문자 이름과 주문 요청 만들기",
      "장바구니와 주문자 이름을 API에 보낼 요청 데이터로 묶는다.",
      ["주문 입력값을 검증한다.", "보낼 JSON 구조를 이해한다.", "주문 저장 전 화면 데이터를 확인한다."],
      "주문 요청은 영수증 머리와 상품 줄을 한 봉투에 담은 것",
      ["customer_name은 orders 행에 들어갈 정보이고, cart 항목은 order_items 행들이 된다.",
       "장바구니가 비었거나 이름이 비어 있으면 주문을 보내지 않는다."],
      [("이름", "민지"), ("cart", "상품 두 개"), ("JSON", "주문 봉투"), ("API", "저장 요청")],
      "8주차 영수증 표 그림을 다시 꺼내 화면 JSON에서 어느 값이 어느 표로 갈지 색으로 연결한다.",
      "오늘은 요청 객체를 콘솔에 표시하고 검증 규칙을 완성한다.",
      """const [customerName, setCustomerName] = useState("");

function prepareOrder() {
  if (!customerName.trim() || cart.length === 0) {
    alert("이름과 상품을 확인하세요.");
    return;
  }

  const order = {
    customer_name: customerName,
    items: cart.map(item => ({
      product_id: item.product_id,
      quantity: 1,
      unit_price: item.price
    }))
  };
  console.log(order);
}""",
      "민지, 노트와 펜 담기 후 실행:\n{customer_name:'민지', items:[{product_id:..., quantity:1, unit_price:...}, ...]}",
      ["빈 문자열의 공백을 제거한 뒤 값이 없으면 요청하지 않는다.",
       "cart의 각 상품은 DB order_items에 필요한 값으로 변환된다.",
       "상품명 대신 product_id를 보내야 DB의 상품 행과 연결할 수 있다."],
      "상품명이 아닌 product_id가 저장 연결에 필요한 이유를 8주차 외래키 그림으로 설명한다.",
      "관계 데이터", "프로젝트 데이터 구조는 SQL의 orders/order_items 관계를 이해했을 때 읽을 수 있다.",
      """-- items 한 줄이 아래처럼 저장된다고 가정
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (5, 2, 1, 1000);""",
      "이 행은 어떤 내용을 뜻하는가?",
      "주문 번호 5에 상품 번호 2를 1개, 당시 단가 1000원으로 담은 상세 한 줄이다.",
      ["이름 없이 주문 버튼을 눌렀을 때 막히는지 확인한다.",
       "장바구니 없이 주문할 때 막히는지 확인한다.",
       "유효한 요청 객체의 items 수가 담은 상품 수와 같은지 확인한다."],
      "내일은 이 요청을 API가 받아 실제 orders와 order_items에 저장한다.",
      "금요일: 장바구니 주문 저장",
      "주문 API에 보낼 정확한 데이터 모양을 작성한다.",
      ["주문 JSON 확인", "외래키 연결 설명"]),

    L(11, 4, "React + API", "orders와 order_items에 저장하기",
      "주문 요청을 서버에 보내고 API가 주문 머리와 상세 줄을 순서대로 INSERT하도록 확인한다.",
      ["주문 저장 순서를 설명한다.", "API POST를 연결한다.", "JOIN으로 저장 결과를 검사한다."],
      "한 주문 저장은 머리 한 줄 다음 상세 여러 줄",
      ["서버는 먼저 orders에 주문자를 저장하여 새 주문 번호를 얻고, cart 상품마다 같은 번호로 order_items를 저장한다.",
       "서버 뼈대와 트랜잭션 처리는 강사가 제공한다. 학생은 두 INSERT의 역할과 화면의 POST 호출을 입력한다."],
      [("POST 주문", "JSON"), ("orders", "새 ID"), ("order_items", "여러 INSERT"), ("JOIN", "저장 확인")],
      "빈 영수증 상단에 주문번호를 찍은 뒤 상세 상품 줄마다 같은 번호를 복사해 쓰는 모습을 재현한다.",
      "React 주문 요청과 서버가 사용할 핵심 SQL을 나란히 확인한다.",
      """// React의 주문 전송 핵심
await fetch("http://localhost:8000/orders", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(order)
});

-- API 내부 핵심 SQL의 의미
INSERT INTO orders (customer_name) VALUES (?);
INSERT INTO order_items
    (order_id, product_id, quantity, unit_price)
VALUES (?, ?, ?, ?);""",
      "주문하기 클릭 -> 주문 완료 문구 표시\nSQL JOIN 조회 -> 주문자와 담은 상품 행 확인",
      ["첫 INSERT가 주문 한 건의 ID를 만든다.",
       "둘째 INSERT는 cart 항목 수만큼 실행되어 같은 order_id에 연결된다.",
       "실제 서버 코드에서는 드라이버에 맞는 매개변수 표시와 트랜잭션을 교사 뼈대가 처리한다."],
      "주문 실패 시 일부 상세만 저장되면 왜 문제인지 말하고, 트랜잭션이라는 용어를 메모한다.",
      "SQL 관계/보안", "주문 저장은 관계형 DB와 통합 구현을 한 장면에 보여 주며, 값 매개변수 사용도 유지한다.",
      """SELECT o.customer_name, p.name, i.quantity
FROM orders o
JOIN order_items i ON o.order_id = i.order_id
JOIN products p ON p.product_id = i.product_id
WHERE o.customer_name = '민지';""",
      "이 SQL은 무엇을 확인하기 위한 문장인가?",
      "민지라는 주문자가 주문한 상품 이름과 수량을 연결해 확인하는 조회다.",
      ["상품 두 개를 담아 주문 저장을 실행한다.",
       "JOIN SQL로 주문자가 선택한 상품이 저장됐는지 확인한다.",
       "주문 저장 중 실패 시 되돌려야 하는 이유를 한 문장으로 쓴다."],
      "금요일은 주문 저장과 조회 확인까지만 필수다. 결제나 로그인은 하지 않는다.",
      "금요일: 장바구니 주문 저장",
      "React 주문 버튼부터 PostgreSQL 주문 행까지 연결한다.",
      ["주문 저장 화면", "JOIN 저장 확인 결과"]),

    L(11, 5, "React + API", "완성: 장바구니에서 주문 저장까지",
      "상품 선택, 총액 확인, 주문자 입력, DB 저장과 SQL 확인까지 작은 구매 흐름을 시연한다.",
      ["주문 흐름 전체를 실행한다.", "데이터가 저장되는 표를 설명한다.", "입력 오류와 빈 장바구니를 검사한다."],
      "쇼핑몰의 구매 흐름이 처음 끝까지 이어지는 날",
      ["화려한 결제 화면보다 중요한 것은 선택한 상품이 정확한 가격과 수량으로 주문표에 남는가이다.",
       "오늘 시연은 화면과 SQL 결과를 함께 보여 주어 기능이 실제 저장으로 이어졌음을 확인한다."],
      [("목록", "상품 선택"), ("cart", "총액"), ("POST", "주문"), ("SQL", "내역 확인")],
      "시연 전에 입력값, 예상 총액, 저장될 상세 행을 종이에 적고 실제 결과와 하나씩 비교한다.",
      "주문 버튼 함수의 학생 이해 범위 핵심을 정리한다.",
      """async function submitOrder() {
  if (!customerName.trim() || cart.length === 0) {
    alert("주문자와 상품을 확인하세요.");
    return;
  }
  const order = {
    customer_name: customerName,
    items: cart.map(item => ({
      product_id: item.product_id,
      quantity: 1,
      unit_price: item.price
    }))
  };
  await fetch("http://localhost:8000/orders", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(order)
  });
  setCart([]);
  alert("주문이 저장되었습니다.");
}""",
      "장바구니에 상품 담기 -> 총액 표시 -> 이름 입력 -> 주문 저장됨 알림 -> 장바구니 비워짐",
      ["검증을 통과한 요청만 서버로 전송된다.",
       "주문 완료 뒤 화면 cart를 비우지만, DB orders와 order_items 데이터는 남아 있다.",
       "따라서 저장 확인은 화면이 아니라 SQL JOIN 결과로 한다."],
      "주문 완료 뒤 장바구니만 비어 있고 DB 주문은 남는 차이를 그림으로 표현한다.",
      "통합/SQL", "화면 상태와 영구 저장 데이터의 차이는 데이터 입출력과 DB 이해의 핵심이다.",
      """SELECT SUM(i.quantity * i.unit_price) AS total
FROM orders o
JOIN order_items i ON o.order_id = i.order_id
WHERE o.customer_name = '민지';""",
      "이 조회는 무엇을 계산하는가?",
      "민지의 주문상세 행 금액들을 합쳐 저장된 구매 총액을 계산한다.",
      ["상품 두 개를 담은 예상 총액을 적고 화면 총액과 맞춘다.",
       "주문 후 JOIN 조회와 SUM 조회 결과를 확인한다.",
       "빈 이름, 빈 장바구니 테스트를 기록한다."],
      "12주차에는 새 기능을 무리하게 추가하지 않고 오류 수정, 매출 조회, 설명에 집중한다.",
      "제출 작품: 장바구니 주문 저장",
      "구매 흐름이 작동하는 버전과 SQL 확인 결과를 제출한다.",
      ["주문 저장 동작 화면", "주문 SQL 확인표"]),

    L(12, 1, "통합", "전체 기능 지도와 C 복습",
      "마지막 주는 새 기능보다 완성도를 높인다. 쇼핑몰 기능을 점검하면서 C 코드 추적을 복습한다.",
      ["기능 체크리스트를 만든다.", "데이터 이동 흐름을 전체로 그린다.", "C 조건/반복/배열 문제를 다시 푼다."],
      "완성은 기능을 더하는 일이 아니라 흐름이 끊기지 않는지 보는 일",
      ["상품 목록, 등록, 담기, 주문, 조회의 각 지점에서 실패하는 입력을 시험한다.",
       "처음 두 주에 익힌 입력·조건·반복은 지금도 폼 검증과 목록 반복의 밑바탕이다."],
      [("상품", "GET"), ("등록", "POST/INSERT"), ("장바구니", "상태"), ("주문", "DB 저장")],
      "모든 화면과 DB 표를 큰 종이 한 장에 그리고 화살표마다 사용한 언어나 SQL을 적는다.",
      "오늘 코드는 프로젝트 수정 대신 C 실기형 추적 복습 코드로 직접 입력한다.",
      """#include <stdio.h>

int main(void) {
    int stock[3] = {2, 0, 3};
    int available = 0;
    for (int i = 0; i < 3; i++) {
        if (stock[i] > 0) {
            available += stock[i];
        }
    }
    printf("%d", available);
    return 0;
}""",
      "5",
      ["배열의 재고를 하나씩 읽는다.",
       "0보다 큰 2와 3만 available에 더한다.",
       "이 로직은 화면의 판매 가능 재고 표시와도 연결할 수 있다."],
      "조건을 `>= 0`으로 바꾸어도 합계가 같은 이유와, 카운트를 셀 때는 달라질 수 있는 이유를 적는다.",
      "C 종합", "기사 대비는 최종 작품 주에도 매일 한 언어씩 짧게 되짚어 감각을 유지한다.",
      """int data[4] = {1, 2, 3, 4};
int result = 0;
for (int i = 0; i < 4; i++) {
    if (i % 2 == 0) result += data[i];
}
printf("%d", result);""",
      "출력값은 무엇인가?",
      "짝수 인덱스 0과 2의 값 1과 3을 더하므로 `4`이다.",
      ["쇼핑몰 필수 기능 다섯 개를 직접 클릭해 성공/실패를 표시한다.",
       "C 배열/반복 문제 세 개를 손으로 푼다.",
       "현재 발견한 오류 한 건을 기록한다."],
      "버그를 찾는 것도 프로젝트 결과다. 수정 전 입력과 기대 결과를 반드시 남긴다.",
      "금요일: 우리 반 미니 쇼핑몰",
      "기능별 점검표와 데이터 흐름 전체 지도를 완성한다.",
      ["기능 점검표", "C 복습 답안"]),

    L(12, 2, "통합", "상품·장바구니 점검과 Java 복습",
      "상품 카드와 장바구니 계산 오류를 수정하고 Java 객체 실행 순서를 다시 추적한다.",
      ["상품 표시/담기/총액을 테스트한다.", "오류 재현과 수정을 기록한다.", "Java 객체·오버라이딩 문제를 복습한다."],
      "장바구니 상태도 객체의 필드처럼 변화 기록이 필요하다",
      ["담기 전후 화면의 cart 배열이 달라지고 총액이 재계산된다. 이는 Java 객체의 stock이나 balance를 추적하던 습관과 같다.",
       "품절인데 담기는 경우, 총액이 잘못 계산되는 경우를 일부러 시험한다."],
      [("클릭 전", "cart=[]"), ("담기", "상품 추가"), ("합계", "reduce"), ("표시", "총액")],
      "테스트 카드에 입력 행동, 예상 화면, 실제 화면, 수정 결과 네 칸을 만든다.",
      "Java 기사형 코드를 입력해 실제 출력과 손 추적을 비교한다.",
      """class Product {
    int stock = 2;
    void addCart() {
        if (stock > 0) stock--;
    }
}
public class Test {
    public static void main(String[] args) {
        Product p = new Product();
        p.addCart();
        p.addCart();
        p.addCart();
        System.out.println(p.stock);
    }
}""",
      "0",
      ["p 객체 하나가 stock 값 하나를 유지한다.",
       "앞 두 호출에서 2에서 1, 1에서 0으로 감소한다.",
       "세 번째에는 조건이 거짓이라 0이 유지된다."],
      "화면에서 품절 상품을 막는 조건과 Java 코드의 stock 조건을 나란히 적는다.",
      "Java 종합", "객체 상태 변화는 호출 순서대로 표를 만들면 안정적으로 풀이한다.",
      """class A { int value() { return 2; } }
class B extends A { int value() { return 5; } }
A x = new B();
System.out.print(x.value() * 2);""",
      "출력값은 무엇인가?",
      "실제 객체 B의 재정의 메서드가 5를 반환하므로 `10`이다.",
      ["품절 상품 카드가 담기 불가능한지 확인한다.",
       "상품 두 개 장바구니 총액을 손계산과 비교한다.",
       "Java 객체 문제 세 개를 해결한다."],
      "고친 오류는 발표 때 단순 자랑보다 프로그램 이해를 보여 주는 좋은 설명 소재다.",
      "금요일: 우리 반 미니 쇼핑몰",
      "상품 목록과 장바구니 기능의 테스트 기록 및 오류 수정을 마친다.",
      ["버그 수정 기록", "Java 복습 답안"]),

    L(12, 3, "통합", "주문·매출 점검과 Python 복습",
      "주문 저장과 집계 조회를 확인하면서 Python의 리스트, 함수, 누적 계산을 복습한다.",
      ["주문 저장 후 SQL로 검증한다.", "매출 조회 결과를 손계산과 비교한다.", "Python 함수 추적을 해결한다."],
      "화면 총액과 DB 매출은 같은 주문을 다른 위치에서 계산한 값",
      ["화면의 total은 주문 전 사용자에게 보여 주는 값이고, DB의 SUM은 저장 뒤 기록에서 다시 계산한 값이다.",
       "두 값이 다르면 주문 데이터나 계산 로직에 오류가 있다는 신호다."],
      [("cart total", "화면"), ("POST", "저장"), ("order_items", "기록"), ("SUM", "검증")],
      "같은 주문에 대해 화면 계산표와 SQL 계산표를 좌우로 쓰고 숫자가 일치하는지 선으로 연결한다.",
      "Python 추적 문제를 입력하며 장바구니 계산의 원형을 되새긴다.",
      """def cart_total(items):
    total = 0
    for item in items:
        total += item["price"] * item["count"]
    if total >= 5000:
        total -= 500
    return total

cart = [
    {"price": 1200, "count": 2},
    {"price": 1500, "count": 2}
]
print(cart_total(cart))""",
      "4900",
      ["첫 상품 소계는 2400, 둘째는 3000으로 할인 전 합계는 5400이다.",
       "5000 이상이므로 500을 빼 최종 4900이다.",
       "이전 Python 프로젝트의 할인 계산과 같은 형태다."],
      "할인 기능을 실제 React 필수 범위에 넣지 않았더라도 계산 함수가 어디에 들어갈 수 있을지 표시한다.",
      "Python 종합", "중첩된 딕셔너리/리스트 문제는 항목별 소계를 먼저 계산한다.",
      """data = [{"v": 2}, {"v": 4}, {"v": 1}]
result = 0
for item in data:
    if item["v"] > 1:
        result += item["v"]
print(result)""",
      "출력값은 무엇인가?",
      "2와 4만 조건을 만족해 더해지므로 `6`이다.",
      ["실제 주문 한 건의 화면 총액을 기록한다.",
       "저장 후 SQL SUM 결과가 같은지 확인한다.",
       "Python 문제 세 개를 손 추적한다."],
      "내일은 SQL과 입력 검증·안전성 설명을 정리하고 시연 데이터를 고정한다.",
      "금요일: 우리 반 미니 쇼핑몰",
      "주문 저장 및 매출 검증 테스트를 완료한다.",
      ["화면/DB 금액 검증표", "Python 복습 답안"]),

    L(12, 4, "통합", "SQL·보안 점검과 발표 리허설",
      "입력 검증과 안전한 SQL 사용을 확인하고 학생별 설명 부분을 연습한다.",
      ["JOIN/집계 SQL을 재작성한다.", "입력값 검증과 매개변수 SQL의 이유를 말한다.", "시연 실패에 대비한 순서를 준비한다."],
      "보안은 어려운 해킹보다 먼저 잘못된 입력을 믿지 않는 태도",
      ["상품 가격이 음수이거나 이름 칸에 이상한 입력이 들어오면 프로그램은 저장을 막아야 한다.",
       "SQL을 문자열 이어 붙이기로 만들지 않고 매개변수로 전달하는 이유를 자신의 프로그램 장면에서 설명한다."],
      [("사용자 입력", "검증"), ("API", "매개변수"), ("DB", "정상 행"), ("조회", "확인")],
      "문 앞 입력 검사원과 DB 저장 담당을 그려, 검사를 통과한 값만 저장 표로 가게 한다.",
      "오늘 직접 작성할 핵심은 최종 발표에서 실행할 매출 조회 SQL이다.",
      """SELECT p.name,
       SUM(i.quantity) AS sold_count,
       SUM(i.quantity * i.unit_price) AS sales
FROM products p
JOIN order_items i ON p.product_id = i.product_id
GROUP BY p.product_id, p.name
ORDER BY sales DESC;""",
      "상품별 판매수량과 매출이 매출이 높은 순으로 표시됨",
      ["order_items가 상품 판매의 실제 줄 데이터를 가진다.",
       "상품별로 묶은 후 수량 합계와 금액 합계를 계산한다.",
       "발표에서 어떤 상품이 많이 팔렸는지 결과표를 읽어 설명한다."],
      "시연 전에 테스트 주문 두 건을 미리 넣고 예상 매출표를 손으로 계산한다.",
      "SQL/보안 종합", "실기에서는 JOIN과 GROUP BY 문장 작성뿐 아니라 보안 용어와 입력 검증 개념도 연결해 정리한다.",
      """UPDATE products
SET stock = stock - 1
WHERE product_id = 1 AND stock > 0;""",
      "왜 `AND stock > 0` 조건이 중요한가?",
      "재고가 이미 0인 상품에서 또 감소하여 음수 재고가 되는 것을 막기 위한 조건이다.",
      ["상품별 매출 SQL을 직접 다시 입력한다.",
       "빈 상품명/음수 가격/빈 장바구니가 막히는지 확인한다.",
       "각 학생이 React 기능 1개와 SQL 문장 1개를 3분 안에 설명한다."],
      "발표에서는 숨겨 둔 복잡한 기능보다 검증한 필수 흐름을 정확히 보여 주는 것이 낫다.",
      "금요일: 우리 반 미니 쇼핑몰",
      "시연용 주문 데이터와 핵심 SQL, 입력 검증 체크를 확정한다.",
      ["최종 SQL 출력 결과", "발표 리허설 체크표"]),

    L(12, 5, "통합", "최종 발표: 우리 반 미니 쇼핑몰",
      "상품 등록부터 주문 저장과 매출 조회까지 시연하고 C, Java, Python, SQL의 학습 결과를 확인한다.",
      ["필수 쇼핑몰 흐름을 안정적으로 시연한다.", "자신의 코드와 SQL을 설명한다.", "기사형 종합 문제로 과정을 마무리한다."],
      "한 화면 뒤에 네 언어 학습의 흔적이 있다",
      ["C에서 입력·조건·반복을 익혔고, Java에서 상품의 값과 행동을 묶었으며, Python에서 장바구니 계산을 했고, SQL에서 상품과 주문을 저장했다.",
       "React 쇼핑몰은 새 마술이 아니라 앞선 개념들이 사용자에게 보이는 결과로 모인 작품이다."],
      [("C/Java/Python", "계산 감각"), ("SQL", "영구 저장"), ("React/API", "연결/화면"), ("시연", "설명")],
      "각 학생이 자신이 설명할 기능 카드를 들고, 화면 동작에서 DB 결과까지 한 줄의 흐름으로 연결한다.",
      "최종일의 코드는 새로 추가하는 코드가 아니라 발표 때 보여 줄 SQL과 확인 절차다.",
      """-- 시연 확인 1: 등록된 상품
SELECT product_id, name, price, stock
FROM products
ORDER BY product_id;

-- 시연 확인 2: 저장된 주문 내역
SELECT o.customer_name, p.name, i.quantity,
       i.quantity * i.unit_price AS subtotal
FROM orders o
JOIN order_items i ON o.order_id = i.order_id
JOIN products p ON p.product_id = i.product_id
ORDER BY o.order_id;

-- 시연 확인 3: 상품별 매출
SELECT p.name, SUM(i.quantity * i.unit_price) AS sales
FROM products p
JOIN order_items i ON p.product_id = i.product_id
GROUP BY p.product_id, p.name
ORDER BY sales DESC;""",
      "상품 등록 결과표 -> 주문 상세 결과표 -> 상품별 매출 결과표를 순서대로 시연",
      ["첫 조회는 React 상품 목록이 읽는 원본 데이터다.",
       "둘째 조회는 화면에서 저장한 주문이 올바른 상품에 연결됐는지 보여 준다.",
       "셋째 조회는 축적된 기록이 유용한 정보로 바뀌는 장면이다."],
      "발표 뒤 내가 가장 자신 있게 설명할 수 있는 코드 열 줄과 아직 복습할 개념 하나를 기록한다.",
      "종합 평가", "종합 평가는 언어별 긴 프로그램 작성보다 짧은 코드 추적과 SQL 작성, 본인 기능 설명을 함께 본다.",
      """-- 종합 SQL 문제
SELECT p.name, SUM(i.quantity) AS qty
FROM products p
JOIN order_items i ON p.product_id = i.product_id
GROUP BY p.product_id, p.name
HAVING SUM(i.quantity) >= 2;""",
      "이 SQL이 매출 조회와 다른 점을 설명하라.",
      "금액을 합하지 않고 상품별 판매 수량을 합하며, 총 판매 수량이 2개 이상인 상품만 결과에 남긴다.",
      ["상품 등록 -> 목록 확인 -> 장바구니 담기 -> 주문 저장 -> SQL 조회를 시연한다.",
       "C/Java/Python 코드 추적 각 1문제와 SQL 작성 2문제를 해결한다.",
       "프로젝트를 만들며 코드가 어디에 쓰였는지 다섯 문장으로 작성한다."],
      "학생이 프로그램을 전부 외웠는지가 아니라, 작동 흐름을 이해하고 작은 코드를 읽고 수정할 수 있는지가 수료 기준이다.",
      "최종 제출: 우리 반 미니 쇼핑몰",
      "12주 학습을 실제 화면과 데이터로 발표한다. 최종 작품과 종합 문제 답안을 함께 보관한다.",
      ["동작하는 최종 프로젝트 시연", "종합 테스트와 회고 기록"]),
]
