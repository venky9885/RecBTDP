
#!  A - B using C
#!  A  - C
#!  B - C using A
def hanoi(disk, source, middle, destination):

    if disk == 0:
        print('at 0 Disk %s from %s to %s' % (disk, source, destination))
        return

    hanoi(disk-1, source, destination, middle)

    print('After Disk %s from %s to %s' % (disk, source, destination))
    hanoi(disk-1, middle, source, destination)


hanoi(2, 'A', 'B', 'C')
