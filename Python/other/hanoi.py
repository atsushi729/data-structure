def hanoi(disk: int, src: str, dest: str, center: str):
    if disk < 1:
        return

    hanoi(disk - 1, src, center, dest)
    print(f'move {disk} from {src} to {dest}')
    hanoi(disk - 1, center, dest, src)


if __name__ == "__main__":
    hanoi(3, 'A', 'B', 'C')
