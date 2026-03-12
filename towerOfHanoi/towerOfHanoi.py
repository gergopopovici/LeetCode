def tower_of_hanoi(n,source,target,helper):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    
    tower_of_hanoi(n-1, source,helper,target)

    print(f"Move disk {n} from {source} to {target}")

    tower_of_hanoi(n-1,helper,target,source)

tower_of_hanoi(5, 'A', 'C', 'B')