def TOH(n, from_rod, to_rod,aux_rod):
    if n==0:
        return
    TOH(n-1, from_rod, aux_rod, to_rod)        
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TOH(n-1,aux_rod, to_rod, from_rod)
n=3
TOH(n, 'A', 'B', 'C')
# def tower_of_hanoi(n, source, auxiliary, target):
#     if n == 1:
#         print(f"Move disk 1 from {source} to {target}")
#         return
#     tower_of_hanoi(n - 1, source, target, auxiliary)
#     print(f"Move disk {n} from {source} to {target}")
#     tower_of_hanoi(n - 1, auxiliary, source, target)

# # Example: Move 3 disks from peg 'A' to peg 'C' using peg 'B' as an auxiliary peg
# tower_of_hanoi(3, 'A', 'B', 'C')

