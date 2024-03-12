#!/usr/bin/node
function findSecondBiggest (args) {
  if (args.length < 3) {
    return 0;
  }
  const numbers = args.slice(2).map(Number);
  numbers.sort((a, b) => b - a);
  return numbers[1];
}

const secondBiggest = findSecondBiggest(process.argv);
console.log(secondBiggest);
