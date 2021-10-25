class Vector:
    x = ''
    y = ''
    z = ''

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __radd__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __rsub__(self, other):
        return Vector(other.x - self.x, other.y - self.y, other.z - other.z)

    def __str__(self):
        return '('+str(self.x)+'  '+str(self.y)+' '+str(self.z)+')'

    def __repr__(self):
        return 'Vector('+str(self.x)+', '+str(self.y)+', '+str(self.z)+')'

    def __mul__(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def __rmul__(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def __matmul__(self, other):
        return Vector(self.y*other.z - self.z*other.y, self.z*other.x - self.x*other.z, self.x*other.y - self.y*other.x)

    def __rmatmul__(self, other):
        return __matmul__(other, self)

#-- 2
def max_mod(lst):
    N = len(lst)
    mx = -1

    for vec in lst:
        if abs(vec) > mx:
            mx = abs(vec)
            max_vec = vec

    return max_vec

N = int(input())
vec_lst = []

for i in range(N):
    vec = input().split()
    vec_lst.append(Vector(vec[0], vec[1], vec[2]))

print("Наиболее удаленный вектор:", max_mod(vec_lst))
#--

#--3
def mass_center(vec_lst):
    N = len(vec_lst)
    sx, sy, sz = 0., 0., 0.

    for vec in vec_lst:
        sx += vec.x
        sy += vec.y
        sz += vec.z
    
    return Vector(sx/N, sy/N, sz/N)
#--

#--4
def volume(a, b, c):
    return a * (b @ c)
#--

#--5
def perim(a, b, c):
    return abs(a-b) + abs(b-c) + abs(c-a)

def area(a, b, c):
    return (a-b) * (a-c) / 2

def max_perim(lst):
    mx = 0
    N = len(lst)

    pass

def max_area(lst):
    pass




