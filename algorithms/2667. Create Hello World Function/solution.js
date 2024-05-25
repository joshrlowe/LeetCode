/**
 * @return {Function}
 */
var createHelloWorld = function () {
  return function (...args) {
    return "Hello World";
  };
};

function test_createHelloWorld() {
  // Test Case 1: Basic functionality
  console.log("Test Case 1: Basic functionality");
  const helloWorldFunc1 = createHelloWorld();
  const result1 = helloWorldFunc1();
  const expected1 = "Hello World";
  console.assert(
    result1 === expected1,
    `Test Case 1 Failed: Expected ${expected1}, got ${result1}`,
  );
  console.log("Passed");

  // Test Case 2: Function with arguments
  console.log("Test Case 2: Function with arguments");
  const helloWorldFunc2 = createHelloWorld();
  const result2 = helloWorldFunc2(1, 2, 3);
  const expected2 = "Hello World";
  console.assert(
    result2 === expected2,
    `Test Case 2 Failed: Expected ${expected2}, got ${result2}`,
  );
  console.log("Passed");

  // Test Case 3: Function with string arguments
  console.log("Test Case 3: Function with string arguments");
  const helloWorldFunc3 = createHelloWorld();
  const result3 = helloWorldFunc3("foo", "bar");
  const expected3 = "Hello World";
  console.assert(
    result3 === expected3,
    `Test Case 3 Failed: Expected ${expected3}, got ${result3}`,
  );
  console.log("Passed");

  // Test Case 4: Function with no arguments
  console.log("Test Case 4: Function with no arguments");
  const helloWorldFunc4 = createHelloWorld();
  const result4 = helloWorldFunc4();
  const expected4 = "Hello World";
  console.assert(
    result4 === expected4,
    `Test Case 4 Failed: Expected ${expected4}, got ${result4}`,
  );
  console.log("Passed");

  // Test Case 5: Function with object arguments
  console.log("Test Case 5: Function with object arguments");
  const helloWorldFunc5 = createHelloWorld();
  const result5 = helloWorldFunc5({ key: "value" });
  const expected5 = "Hello World";
  console.assert(
    result5 === expected5,
    `Test Case 5 Failed: Expected ${expected5}, got ${result5}`,
  );
  console.log("Passed");
}

test_createHelloWorld();
