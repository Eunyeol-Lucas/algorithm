// 시간 초과

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");
const [n, m] = input[0].split(" ").map((v) => +v);
const graph = Array.from({ length: n + 1 }, () => []);
for (let i = 1; i < m + 1; i++) {
  const [x, y] = input[i].split(" ").map((v) => +v);
  graph[x].push(y);
  graph[y].push(x);
}
const q = +input[m + 1];
for (let i = m + 2; i < m + 2 + q; i++) {
  const [x, y, z] = input[i].split(" ").map((v) => +v);
  if (x === 1) {
    graph[y].push(z);
    graph[z].push(y);
  } else {
    graph[y] = graph[y].filter((x) => x !== z);
    graph[x] = graph[x].filter((x) => x !== y);
  }
  const arr = [];
  for (let i = 1; i < n + 1; i++) {
    const q = [];
    const ch = Array.from({ length: n + 1 }, () => 1e9);
    ch[i] = 0;
    for (const k of graph[i]) {
      q.push(k);
      ch[k] = 1;
    }
    while (q.length) {
      const k = q.shift();
      if (k === 1) {
      }
      for (const w of graph[k]) {
        if (ch[w] > ch[k] + 1) {
          ch[w] = ch[k] + 1;
          q.push(w);
        }
      }
    }

    if (ch[1] !== 1e9) {
      arr.push(ch[1]);
    } else arr.push(-1);
  }
  console.log(arr.join(" "));
}
