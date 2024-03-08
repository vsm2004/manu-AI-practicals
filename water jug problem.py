def water_jug_problem(jug1_capacity, jug2_capacity, target):
    jug1 = 0
    jug2 = 0
    while jug1 != target and jug2 != target:
        if jug2 == jug2_capacity:
            jug2 = 0
        elif jug1 == 0:
            jug1 = jug1_capacity
        else:
            amount_to_pour = min(jug1, jug2_capacity - jug2)
            jug1 -= amount_to_pour
            jug2 += amount_to_pour
    return jug1, jug2
if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    target = 2
    jug1_final, jug2_final = water_jug_problem(jug1_capacity, jug2_capacity, target)
    print(f"Final state: Jug1: {jug1_final} gallons, Jug2: {jug2_final} gallons")
