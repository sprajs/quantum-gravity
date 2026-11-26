"""Exact local heat-kernel and finite-dimensional D.9 checks. Uses Python 3."""

from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product


def trace_square(matrix):
    """Return Tr(M M), including the sign for a skew generator."""
    return sum(entry * matrix[j][i] for i, row in enumerate(matrix)
               for j, entry in enumerate(row))


def local_heat_coefficients(a, b):
    # Algebraic Euclidean Ricci-flat curvature in an orthonormal frame.
    # The six plane curvatures sum to zero in each Ricci component.
    axes = range(4)
    planes = list(combinations(axes, 2))
    sectional = dict(zip(planes, [a, b, -a - b, -a - b, b, a]))

    def curvature(i, j, k, l):
        if i == j or k == l or {i, j} != {k, l}:
            return 0
        return (1 if (i < j) == (k < l) else -1) * sectional[min(i, j), max(i, j)]

    assert all(sum(curvature(k, i, k, j) for k in axes) == 0
               for i, j in product(axes, repeat=2))
    norm = sum(curvature(*indices) ** 2 for indices in product(axes, repeat=4))
    symmetric = list(combinations_with_replacement(axes, 2))

    def component(i, j, basis):
        return int((min(i, j), max(i, j)) == basis)

    def potential(i, j, basis):
        return 2 * sum(curvature(i, k, j, l) * component(k, l, basis)
                       for k, l in product(axes, repeat=2))

    potential2 = trace_square([[potential(i, j, basis) for basis in symmetric]
                               for i, j in symmetric])
    vector_curvature2 = tensor_curvature2 = 0
    for mu, nu in planes:
        connection = [[curvature(i, j, mu, nu) for j in axes] for i in axes]
        vector_curvature2 += 2 * trace_square(connection)
        tensor_connection = [
            [sum(connection[i][k] * component(k, j, basis)
                 + connection[j][k] * component(i, k, basis) for k in axes)
             for basis in symmetric]
            for i, j in symmetric
        ]
        tensor_curvature2 += 2 * trace_square(tensor_connection)

    assert (potential2, tensor_curvature2, vector_curvature2) == (3*norm, -6*norm, -norm)
    tensor = Fraction(2*len(symmetric)*norm + 180*potential2 + 30*tensor_curvature2,
                      360*norm)
    vector = Fraction(2*len(axes)*norm + 30*vector_curvature2, 360*norm)
    return tensor, vector, tensor - 2*vector


def separate_linear_sources():
    # I(x;u,v) = (2 x1^2 + 2 x1 x2 + 2 x2^2)/2 + x1^4/24 + u x1 + v x2.
    # At u=v=0 the saddle is zero and the inverse Hessian is [[2,-1],[-1,2]]/3.
    inverse11 = Fraction(2, 3)
    inverse12 = Fraction(-1, 3)
    dx1_du, dx1_dv = -inverse11, -inverse12
    # Only the 11 element of K depends on the saddle, through x1^2/2.
    mixed_hessian11 = dx1_du * dx1_dv
    return inverse11 * mixed_hessian11


if __name__ == "__main__":
    for a, b in [(1, 0), (2, -3), (-4, 7)]:
        spin2, ghost, total = local_heat_coefficients(a, b)
        assert (spin2, ghost, total) == (Fraction(19, 18), Fraction(-11, 180),
                                          Fraction(53, 45))
    separate = separate_linear_sources()
    assert separate == Fraction(-4, 27)
    print(f"Ricci-flat local densities / Riemann^2: spin 2 {spin2}, vector {ghost}, "
          f"spin 2 minus two vectors {total}")
    print(f"Separate linear sources: explicit mixed contact 0, "
          f"Tr(K^-1 d_u d_v K) = {separate}")
