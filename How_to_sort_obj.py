from operator import itemgetter, attrgetter
class Obj(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def toStr(o):
    return '(' + str(o.x) + ', ' + str(o.y) + ')'


arr = [
     Obj(0, 1), Obj(1, 5), Obj(2, 8),
     Obj(3, 9), Obj(4, 6), Obj(5, 7),
     Obj(6, 3), Obj(7, 4), Obj(8, 2),
     Obj(9, 0)]

arr.sort(key=attrgetter('y'))
print(' '.join(map(toStr, arr)))

arr.sort(key=lambda obj: obj.y)
print(' '.join(map(toStr, arr)), "\n")

arr = [
     Obj(3, 1), Obj(1, 5), Obj(1, 8),
     Obj(2, 9), Obj(1, 6), Obj(2, 7),
     Obj(3, 3), Obj(3, 4), Obj(2, 2),
     Obj(4, 0)]

arr.sort(key=attrgetter('x', 'y'))
print(' '.join(map(toStr, arr)))

arr.sort(key=lambda obj: (obj.x, obj.y))
print(' '.join(map(toStr, arr)), "\n")

arr = [(1, 0), (0, 0), (0, 2), (0, -1), (1, 0)]
arr.sort(key=lambda obj: (obj[0], obj[1]))
print(arr, "\n")
