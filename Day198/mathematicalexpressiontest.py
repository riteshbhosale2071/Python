import math

def mathematicalexpressiontest():
    print(" MATHEMATICAL EXPRESSION TEST SUITE :")

    test_results = []

    def run_test(name, expression, expected, actual):
        passed = actual == expected

        test_results.append({
            "name": name,
            "expression": expression,
            "expected": expected,
            "actual": actual,
            "passed": passed
        })

        print("\nTest:", name)
        print("Expression:", expression)
        print("Expected:", expected)
        print("Actual:", actual)
        print("Status:", "PASS" if passed else "FAIL")

    def safe_calculate(expression):
        allowed_characters = "0123456789+-*/().% "

        if not expression or any(
            character not in allowed_characters
            for character in expression
        ):
            raise ValueError("Expression contains unsupported characters.")

        if not any(character.isdigit() for character in expression):
            raise ValueError("Expression must contain a number.")

        try:
            result = eval(expression, {"__builtins__": {}}, {})
        except ZeroDivisionError:
            raise ZeroDivisionError("Division by zero is not allowed.")
        except Exception:
            raise ValueError("Invalid mathematical expression.")

        if not isinstance(result, (int, float)):
            raise ValueError("Expression must produce a numeric result.")

        if not math.isfinite(result):
            raise ValueError("Result is not finite.")

        return result

    print("\nAutomated Test Cases :")

    run_test("Addition", "5 + 3", 8, safe_calculate("5 + 3"))
    run_test("Subtraction", "10 - 4", 6, safe_calculate("10 - 4"))
    run_test("Multiplication", "6 * 7", 42, safe_calculate("6 * 7"))
    run_test("Division", "20 / 5", 4, safe_calculate("20 / 5"))
    run_test("Expression with brackets", "(2 + 3) * 4", 20,
             safe_calculate("(2 + 3) * 4"))
    run_test("Decimal calculation", "2.5 * 4", 10,
             safe_calculate("2.5 * 4"))
    run_test("Negative result", "5 - 12", -7,
             safe_calculate("5 - 12"))
    run_test("Modulo operation", "17 % 5", 2,
             safe_calculate("17 % 5"))

    print("\nError Handling Tests :")

    try:
        safe_calculate("10 / 0")
        run_test("Division by zero", "10 / 0", "Error", "No error")
    except (ValueError, ZeroDivisionError):
        run_test("Division by zero", "10 / 0", "Error", "Error")

    try:
        safe_calculate("5 +")
        run_test("Invalid expression", "5 +", "Error", "No error")
    except (ValueError, ZeroDivisionError):
        run_test("Invalid expression", "5 +", "Error", "Error")

    try:
        safe_calculate("abc + 5")
        run_test("Invalid characters", "abc + 5", "Error", "No error")
    except (ValueError, ZeroDivisionError):
        run_test("Invalid characters", "abc + 5", "Error", "Error")

    print("\nCustom Expression Test :")
    expression = input("Enter a mathematical expression: ").strip()

    try:
        result = safe_calculate(expression)
        print("Expression:", expression)
        print("Result:", result)
        print("Custom Test: PASS")
    except (ValueError, ZeroDivisionError) as error:
        print("Expression:", expression)
        print("Error:", error)
        print("Custom Test: FAIL")

    print("\n" + "=" * 50)
    print("             TEST SUITE SUMMARY")
    print("=" * 50)

    total_tests = len(test_results)
    passed_tests = sum(test["passed"] for test in test_results)
    failed_tests = total_tests - passed_tests

    print("Total Automated Tests:", total_tests)
    print("Passed Tests:", passed_tests)
    print("Failed Tests:", failed_tests)
    print("Success Rate:", round(passed_tests / total_tests * 100, 2), "%")

    if failed_tests == 0:
        print("Overall Status: ALL AUTOMATED TESTS PASSED")
    else:
        print("Overall Status: SOME TESTS FAILED")

    print("\nDetailed Test Report :")

    for test in test_results:
        status = "PASS" if test["passed"] else "FAIL"
        print(test["name"], ":", status)

    print("\nMathematical expression testing completed.")

mathematicalexpressiontest()