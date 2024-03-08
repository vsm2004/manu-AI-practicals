def towers_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    towers_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    towers_of_hanoi(n-1, auxiliary, target, source)

# Example usage
if __name__ == "__main__":
    num_disks = 3
    towers_of_hanoi(num_disks, 'A', 'C', 'B')
