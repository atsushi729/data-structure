def loss(weight: float) -> float:
    return (weight - 3) ** 2


def gradient(weight: float) -> float:
    return 2 * (weight - 3)


weight = 10.0
learning_rate = 0.3

for epoch in range(20):
    grad = gradient(weight)
    current_loss = loss(weight)
    weight -= learning_rate * grad

    print(
        f"epoch={epoch + 1}, "
        f"loss={current_loss:.4f}, "
        f"gradient={grad:.4f}, "
        f"weight={weight:.4f}"
    )
