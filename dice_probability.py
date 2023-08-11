from itertools import combinations


def calculate_probability(total_dice, num_sides, target_sum):
    count_favorable = 0
    count_total = 0

    # Genera todas las combinaciones posibles de resultados de los dados
    dice_values = list(range(1, num_sides + 1))
    all_combinations = combinations(dice_values, total_dice)

    for combo in all_combinations:
        # Ordena los valores de los dados de menor a mayor
        sorted_combo = sorted(combo)

        # Suma los dos valores más bajos
        sum_lowest = sum(sorted_combo[:2])

        # Verifica si cumple con las condiciones adicionales
        if sum_lowest >= target_sum:
            count_favorable += 1
        count_total += 1

    # Calcula la probabilidad
    probability = count_favorable / count_total
    return probability


total_dice = 3
num_sides = 6
target_sum = 6

probability = calculate_probability(total_dice, num_sides, target_sum)
print(f"La probabilidad de obtener una sumatoria de {target_sum} o más es aproximadamente: {probability:.4f}")
