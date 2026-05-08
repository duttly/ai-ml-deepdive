class Node:
    def __init__(self, data, _children=(), label=None, op=None):
        self.data = data
        self.label = label
        self.op = op
        self.gradient = 0
        self._backprop = lambda: None
        self._prev = set(_children)

    def doBackProp(self):
        # topological order all of the children in the graph
        topo = []
        visited = set()
        def build_topo(v):
            if v not in visited:
                # print("visiting ", str(v.label))
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
                # print("adding ", str(v.label))
        build_topo(self)

        # go one variable at a time and apply the chain rule to get its gradient
        # print(topo)
        self.gradient = 1
        for v in reversed(topo):
            v._backprop()
            print("gradient of ", str(v.label), " is ", str(v.gradient))

    def __add__(self, other):
        if not isinstance(other, Node):
            other = Node(other)
        out = Node(self.data + other.data, (self, other), op='+')

        def _backprop():
            self.gradient += 1.0 * out.gradient
            other.gradient += 1.0 * out.gradient

        out._backprop = _backprop
        return out

    def __mul__(self, other):
        if not isinstance(other, Node):
            other = Node(other)
        out = Node(self.data * other.data, (self, other), op='*')

        def _backprop():
            self.gradient += other.data * out.gradient
            other.gradient += self.data * out.gradient

        out._backprop = _backprop
        return out

    def __repr__(self):
        label = "" if self.label is None else str(self.label)
        op = "" if self.op is None else str(self.op)
        return f"({label}: {self.data}, gradient: {self.gradient}, created by op:{op})"
    
    def __neg__(self): # -self
        return self * -1

    def __radd__(self, other): # other + self
        return self + other

    def __sub__(self, other): # self - other
        return self + (-other)

    def __rsub__(self, other): # other - self
        return other + (-self)

    def __rmul__(self, other): # other * self
        return self * other
