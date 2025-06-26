def arit_prog(num_min: float, num_max: float, interar:float = 0.5) -> list[float]:
    result :list[float] = []
    total = 0.0

    while num_min < num_max:
        result.append(float(num_min))
        num_min += interar

    return result