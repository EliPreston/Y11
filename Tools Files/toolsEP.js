// Function isEven takes an integer (a >=0) and returns True if even, and False if odd

function isEven(a) {
  if (a % 2 == 0) {
    return true;
  }
  return false;
}

// Test cases for function isEven
for (i = 0; i < 100; i = i + 1) {
  console.log(isEven(i));
}