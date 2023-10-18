def max(num1, num2):
    if num1 >= num2:
        print("1:", num1)
        return num1
    print("2:", num2)
    return num2

def main():
    larger = max(1, 5)
    print(larger)


if __name__ == "__main__":
    main()