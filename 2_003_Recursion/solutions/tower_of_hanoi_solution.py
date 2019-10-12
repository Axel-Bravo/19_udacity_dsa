# Solution
def tower_of_Hanoi_soln(num_disks, source, auxiliary, destination):
    
    if num_disks == 0:
        return
    
    if num_disks == 1:
        print("{} {}".format(source, destination))
        return
    
    tower_of_Hanoi_soln(num_disks - 1, source, destination, auxiliary)
    print("{} {}".format(source, destination))
    tower_of_Hanoi_soln(num_disks - 1, auxiliary, source, destination)
    
def tower_of_Hanoi(num_disks):
    tower_of_Hanoi_soln(num_disks, 'S', 'A', 'D')