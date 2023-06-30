def is_prime(number: int) -> bool:
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


if __name__ == "__main__":
    print(is_prime(2))
