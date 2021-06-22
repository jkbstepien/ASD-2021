"""
Zadanie (impreza instytutowa II) - zbiór wierzchołków niezależnych.
Chcemy wybrać takie wierzchołki, których suma 'imprezowości' jest jak
największa, a jednocześnie nigdy nie chcemy wybrać dwóch wierzchołków połączonych krawędzią.
"""


class Employee:
    def __init__(self, name, fun):
        self.emp = []  # Employees.
        self.f = -1  # Value of f function.
        self.g = -1  # Value of g function.
        self.name = name
        self.fun = fun


def best_party_without_emp(v):
    """
    Utility function. Obtains value of best party without
    chosen employee 'v' in given subtree.
    """
    if v.g >= 0:
        return v.g

    # Calculate fun factor of every 'v' descendant.
    v.g = 0
    for u in v.emp:
        v.g += best_party(u)

    return v.g


def best_party(v):
    """
    Function calculates value of the best party in the tree,
    where no chosen nodes have a joint edge.

    Let:
        T - tree
        u - subordinate of 'v'
        g(v) = value of the best party without 'v' in subtree T_v.
        g(v) = Σ of u( f(u) )
        f(v) = value of the best party with 'v' in subtree T_v.
        f(v) = max( g(v), v.fun + Σ of u( g(u) ) )
    """
    if v.f >= 0:
        return v.f

    # Calculate total fun if decided to invite 'v'.
    party_fun = v.fun
    for u in v.emp:
        party_fun += best_party_without_emp(u)

    # Calculate total fun if 'v' is not invited and choose bigger value.
    party_fun_without_emp = best_party_without_emp(v)
    v.f = max(party_fun, party_fun_without_emp)

    return v.f


def main():
    # Tests for party planning.
    # Solution: f(root)
    boss = Employee('Boss', 100)
    boss.emp = [Employee('Paweł', 50), Employee('Marek', 51)]
    boss.emp[0].emp = [Employee('Zbychu', 10)]
    boss.emp[1].emp = [Employee('Krysia', 20), Employee('Kasia', 30)]
    print(best_party(boss))


if __name__ == "__main__":
    main()

