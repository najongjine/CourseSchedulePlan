import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import vm from "node:vm";

const ROOT = dirname(fileURLToPath(import.meta.url));
const source = readFileSync(join(ROOT, "lesson_data.py"), "utf8");

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function translateMultilineStrings(text) {
  let output = "";
  let index = 0;
  while (index < text.length) {
    if (text.slice(index, index + 3) === '"""') {
      const end = text.indexOf('"""', index + 3);
      if (end < 0) throw new Error("닫히지 않은 여러 줄 문자열이 있습니다.");
      const multiline = text.slice(index + 3, end).replaceAll("\\\\n", "\\n");
      output += JSON.stringify(multiline);
      index = end + 3;
    } else {
      output += text[index];
      index++;
    }
  }
  return output.replace(
    /\(\s*("(?:\\.|[^"\\])*")\s*,\s*("(?:\\.|[^"\\])*")\s*\)/g,
    "[$1, $2]"
  );
}

function extractExpression(startMarker, endMarker) {
  const start = source.indexOf(startMarker) + startMarker.length;
  const end = source.indexOf(endMarker, start);
  return source.slice(start, end).trim();
}

const weeksText = extractExpression("WEEKS =", "\n\n\ndef L");
const WEEKS = vm.runInNewContext(`(${translateMultilineStrings(weeksText)})`);

function lessonFromArgs(...args) {
  const [
    week, day, tech, title, intro, goals, sense_title, theory, diagram, gesture,
    typing_intro, code, output, walk, modify, exam_tag, exam_intro, exam_code,
    exam_question, exam_answer, tasks, task_answer, project, project_step, check
  ] = args;
  const flow = day === 5
    ? [["1교시", "핵심 문법 미니 테스트와 손 추적"], ["2교시", "완성 코드를 기능별로 입력"], ["3교시", "실행, 오류 수정, 선택 기능"], ["4교시", "시연하고 자기 코드 설명"]]
    : [["1교시", "개념을 그림과 코드로 이해"], ["2교시", "예제를 직접 입력하고 실행"], ["3교시", "금요일 작품 기능 한 조각 작성"], ["4교시", "값을 바꾸고 손 추적 연습"]];
  return {
    week, day, tech, title, intro, goals, flow, sense_title, theory, diagram,
    gesture, typing_intro, code, output, walk, modify, exam_tag, exam_intro,
    exam_code, exam_question, exam_answer, tasks, task_answer, project,
    project_step, check
  };
}

function extractLessonCalls() {
  const start = source.indexOf("LESSONS =");
  const calls = [];
  let cursor = start;
  while ((cursor = source.indexOf("L(", cursor)) >= 0) {
    let depth = 0;
    let inString = false;
    let triple = false;
    let quote = "";
    let escaped = false;
    let end = cursor;
    for (; end < source.length; end++) {
      const current = source[end];
      const nextThree = source.slice(end, end + 3);
      if (triple) {
        if (nextThree === '"""') {
          triple = false;
          inString = false;
          end += 2;
        }
        continue;
      }
      if (inString) {
        if (escaped) {
          escaped = false;
        } else if (current === "\\") {
          escaped = true;
        } else if (current === quote) {
          inString = false;
        }
        continue;
      }
      if (nextThree === '"""') {
        inString = true;
        triple = true;
        end += 2;
      } else if (current === '"' || current === "'") {
        inString = true;
        quote = current;
      } else if (current === "(") {
        depth++;
      } else if (current === ")") {
        depth--;
        if (depth === 0) {
          calls.push(source.slice(cursor, end + 1));
          cursor = end + 1;
          break;
        }
      }
    }
    if (end >= source.length) throw new Error("닫히지 않은 L(...) 수업 데이터가 있습니다.");
  }
  return calls;
}

const LESSONS = extractLessonCalls().map(call => vm.runInNewContext(
  translateMultilineStrings(call),
  { L: lessonFromArgs }
));

function filename(week, day) {
  return `${String(week).padStart(2, "0")}주차_${String(day).padStart(2, "0")}일.html`;
}

function badge(text, extra = "") {
  return `<span class="badge ${extra}">${escapeHtml(text)}</span>`;
}

function renderSide(lesson, index) {
  const sections = [
    ["#goals", "오늘의 목표"], ["#flow", "4시간 흐름"], ["#sense", "감각으로 이해하기"],
    ["#typing", "직접 따라치기"], ["#trace", "기사형 코드 추적"],
    ["#practice", "손으로 푸는 연습"], ["#project", "금요일 프로젝트 연결"]
  ];
  const links = sections.map(([href, text]) => `<a href="${href}">${text}</a>`).join("");
  const previous = index ? filename(LESSONS[index - 1].week, LESSONS[index - 1].day) : "index.html";
  const next = index < LESSONS.length - 1 ? filename(LESSONS[index + 1].week, LESSONS[index + 1].day) : "index.html";
  return `<aside class="side"><strong>${lesson.week}주차 ${lesson.day}일차</strong>${links}<div class="move"><a href="${previous}">이전</a><a href="${next}">다음</a></div></aside>`;
}

function renderLesson(lesson, index) {
  const goals = lesson.goals.map(item => `<li>${escapeHtml(item)}</li>`).join("");
  const flow = lesson.flow.map(([head, text]) => `<div><b>${head}</b>${text}</div>`).join("");
  const diagram = lesson.diagram.map(([head, text]) => `<span class="node"><strong>${escapeHtml(head)}</strong>${escapeHtml(text)}</span>`).join('<span class="arrow">→</span>');
  const theory = lesson.theory.map(item => `<p>${escapeHtml(item)}</p>`).join("");
  const walk = lesson.walk.map(item => `<li>${escapeHtml(item)}</li>`).join("");
  const tasks = lesson.tasks.map(item => `<li>${escapeHtml(item)}</li>`).join("");
  const checks = lesson.check.map(item => `<div class="check">${escapeHtml(item)}</div>`).join("");
  const previous = index ? filename(LESSONS[index - 1].week, LESSONS[index - 1].day) : "index.html";
  const next = index < LESSONS.length - 1 ? filename(LESSONS[index + 1].week, LESSONS[index + 1].day) : "index.html";
  return `<!doctype html>
<html lang="ko">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>${lesson.week}주차 ${lesson.day}일 - ${escapeHtml(lesson.title)}</title><link rel="stylesheet" href="styles.css"></head>
<body>
<header class="site-head"><a class="course" href="index.html">정보처리기사 준비 + 미니 쇼핑몰</a><nav><a href="index.html">전체 차시</a><a href="#project">오늘 산출물</a></nav></header>
<main class="page">
<section class="hero"><div class="badges">${badge(lesson.tech)}${badge(`${lesson.week}주차 ${lesson.day}일차`, "gold")}${badge(lesson.exam_tag, "gray")}</div><h1>${escapeHtml(lesson.title)}</h1><p>${escapeHtml(lesson.intro)}</p></section>
<div class="lesson-grid">${renderSide(lesson, index)}<article class="content">
<section class="panel" id="goals"><h2>오늘의 목표</h2><ul class="goals">${goals}</ul></section>
<section class="panel" id="flow"><h2>오늘 4시간의 흐름</h2><div class="timeline">${flow}</div></section>
<section class="panel sense" id="sense"><h2>먼저 감각으로 이해하기</h2><h3>${escapeHtml(lesson.sense_title)}</h3>${theory}<div class="diagram">${diagram}</div><p class="note">손가락 실습: ${escapeHtml(lesson.gesture)}</p></section>
<section class="panel typing" id="typing"><h2>직접 따라치기</h2><div class="typing-body"><p>${escapeHtml(lesson.typing_intro)}</p><h3>코드를 입력한 뒤 반드시 실행한다</h3></div><pre><code>${escapeHtml(lesson.code.trim())}</code></pre><div class="typing-body"><h3>실행 결과 예</h3><div class="output">${escapeHtml(lesson.output)}</div><h3>한 줄씩 읽어 보기</h3><ol class="tasks">${walk}</ol><details><summary>입력한 뒤 바꾸어 볼 값</summary><p>${escapeHtml(lesson.modify)}</p></details></div></section>
<section class="panel exam" id="trace"><h2>손으로 추적하는 문제</h2><p>${escapeHtml(lesson.exam_intro)}</p><pre><code>${escapeHtml(lesson.exam_code.trim())}</code></pre><p><strong>문제.</strong> ${escapeHtml(lesson.exam_question)}</p><details><summary>정답과 풀이 열기</summary><p>${escapeHtml(lesson.exam_answer)}</p></details></section>
<section class="panel practice" id="practice"><h2>감각을 굳히는 연습</h2><p>먼저 종이에 예상 결과를 적고, 그 다음 코드를 바꾸어 실행해서 확인한다. 틀렸다면 틀린 이유가 학습 기록이다.</p><ol class="tasks">${tasks}</ol><details><summary>연습 확인 포인트</summary><p>${escapeHtml(lesson.task_answer)}</p></details></section>
<section class="panel project" id="project"><div class="badges">${badge("금요일 작품으로 연결", "gold")}</div><h2>${escapeHtml(lesson.project)}</h2><p>${escapeHtml(lesson.project_step)}</p><h3>오늘 저장할 것</h3><div class="checkpoint">${checks}</div></section>
</article></div>
<nav class="footer-nav"><a href="${previous}">← 이전 수업</a><a href="${next}">다음 수업 →</a></nav>
</main></body></html>`;
}

function renderIndex() {
  const cards = WEEKS.map(week => {
    const days = LESSONS.filter(lesson => lesson.week === week.week)
      .map(lesson => `<a href="${filename(lesson.week, lesson.day)}">${lesson.day}일</a>`).join("");
    return `<section class="week-card"><div class="badges">${badge(week.tech)}</div><h2>${week.week}주차. ${escapeHtml(week.title)}</h2><p>${escapeHtml(week.project)}</p><div class="days">${days}</div></section>`;
  }).join("");
  return `<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>정보처리기사 준비 + React 미니 쇼핑몰 상세 교재</title><link rel="stylesheet" href="styles.css"></head>
<body><header class="site-head"><a class="course" href="index.html">정보보안_2606 상세 교재</a><nav><a href="#weeks">60차시 보기</a></nav></header>
<main class="page"><section class="hero"><div class="badges">${badge("비전공자 4명")}${badge("12주 x 5일", "gold")}${badge("1일 4시간", "gray")}</div><h1>코드를 읽고, 직접 치고,<br>작동하는 쇼핑몰까지</h1><p>C, Java, Python, 표준 SQL 중심의 PostgreSQL을 먼저 익히고 React 화면을 붙입니다. 매일 자료에는 개념 설명, 시각적 흐름, 따라치기 코드, 기사형 손 추적 문제, 프로젝트 산출물이 들어 있습니다.</p></section>
<section class="panel" style="margin-top:24px"><h2>사용 방법</h2><p><a href="수업준비.html">수업 전 환경 준비와 교사용 공통 뼈대 확인하기 →</a></p><div class="timeline"><div><b>먼저 보기</b>도식에서 값이 이동하는 모습을 말로 설명한다.</div><div><b>직접 입력</b>코드는 복사하지 않고 한 줄씩 입력한다.</div><div><b>손 추적</b>실행 전에 결과를 종이에 예상한다.</div><div><b>금요일 완성</b>나흘의 조각을 합쳐 시연한다.</div></div></section><div class="week-cards" id="weeks">${cards}</div></main></body></html>`;
}

if (LESSONS.length !== 60) {
  throw new Error(`12주 x 5일은 60개 수업이어야 합니다. 현재 ${LESSONS.length}개입니다.`);
}

writeFileSync(join(ROOT, "index.html"), renderIndex(), "utf8");
for (const [index, lesson] of LESSONS.entries()) {
  writeFileSync(join(ROOT, filename(lesson.week, lesson.day)), renderLesson(lesson, index), "utf8");
}
console.log(`${LESSONS.length}개 차시와 index.html을 생성했습니다.`);
