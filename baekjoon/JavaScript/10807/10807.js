const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "./10807/input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");
const m = input[0];
const arr = input[1].split(" ")
const v = input[2];
let answer = 0;
console.log(arr.filter((x) => x === v).length);
