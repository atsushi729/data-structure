def buddyStrings(s: str, goal: str) -> bool:
    s_list = list(s)
    goal_list = list(goal)
    swap_times = 2

    if len(s_list) != len(goal_list):
        return False

    for i in range(len(s_list)):
        if s_list[i] != goal_list[i]:
            swap_times -= 1

        if swap_times == 0:
            return False

    return True


if __name__ == "__main__":
    s = "aaaaaaabc"
    goal = "aaaaaaacb"
    print(buddyStrings(s, goal))
