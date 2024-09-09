class FizzBuzz:

    def main():
        for i in range(1, 100):
            divisible_by_3 = (i % 3 == 0)
            divisible_by_5 = (i % 5 == 0)

            if divisible_by_3 and divisible_by_5:
                print("Fizz Buzz")
            elif divisible_by_3:
                print("Fizz")
            elif divisible_by_5:
                print("Buzz")
            else:
                print(i)

if __name__ == "__main__":
    FizzBuzz.main()
