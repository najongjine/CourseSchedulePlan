import { existsSync, readdirSync, readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = dirname(fileURLToPath(import.meta.url));
const htmlFiles = readdirSync(root).filter(name => name.endsWith(".html"));
const lessonPages = htmlFiles.filter(name => /^\d{2}주차_\d{2}일\.html$/.test(name));
const requiredSections = ["goals", "flow", "sense", "typing", "trace", "practice", "project"];
const errors = [];

if (lessonPages.length !== 60) {
  errors.push(`수업 페이지 개수: 예상 60, 실제 ${lessonPages.length}`);
}
if (!existsSync(join(root, "index.html")) || !existsSync(join(root, "styles.css"))) {
  errors.push("index.html 또는 styles.css가 없습니다.");
}

for (const page of htmlFiles) {
  const html = readFileSync(join(root, page), "utf8");
  for (const match of html.matchAll(/href="([^"#]+\.html)(?:#[^"]*)?"/g)) {
    if (!existsSync(join(root, match[1]))) {
      errors.push(`${page}: 연결 대상 없음 ${match[1]}`);
    }
  }
  if (/^\d{2}주차_\d{2}일\.html$/.test(page)) {
    for (const section of requiredSections) {
      if (!html.includes(`id="${section}"`)) {
        errors.push(`${page}: #${section} 섹션 누락`);
      }
    }
    if (!html.includes("<pre><code>") || !html.includes("정답과 풀이 열기")) {
      errors.push(`${page}: 코드 예제 또는 풀이 블록 누락`);
    }
  }
}

if (errors.length) {
  console.error(errors.join("\n"));
  process.exit(1);
}

console.log(`검증 완료: 수업 ${lessonPages.length}개, HTML ${htmlFiles.length}개, 내부 링크와 필수 학습 섹션 정상`);
