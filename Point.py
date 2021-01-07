class Point:
    def __init__(self, x, y, z = None):
        self.x = x
        self.y = y
        self.z = z

    def ToString(self):
        if self.z:
            print('P({:.2f} , {:.2f} , {:.2f})'.format(self.x, self.y, self.z))
        else:
            print('P({:.2f} , {:.2f})'.format(self.x, self.y))
