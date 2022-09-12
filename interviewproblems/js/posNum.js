// Jordan - // * In JavaScript, create a function that receives an array of numbers and returns an array containing only the positive numbers *

const numbers = [
  2, -5, 6, 4, -57, 7, -78, 98, -345, 234, -22, 15, -14, 56,
].filter(positiveNums);

function positiveNums(numbers) {
  // for (let i = 0; i < nums.length; i++) console.log(nums[i]);
  return numbers > -1;
}

positiveNums(numbers);
