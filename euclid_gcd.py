# Euclid's algorithm to find GCD
def euclid_gcd(m, n):
    # Assume m to be highest of the two inputs
    if m < n:
        (m, n) = (n, m)

    # return the GCD when m%n == 0
    if (m%n) == 0:
        return n
    else:
        diff = m-n
        return euclid_gcd(max(diff, n), min(diff, n))


# This below is the improved version of the euclid's algorithm
def updated_euclid_gcd(m, n):
    if m < n:
        (m, n) = (n, m)

    if (m%n) == 0:
        return n
    else:
        # instead of giving n=difference of m and n
        # give the remainder
        return updated_euclid_gcd(n, m%n)


print("Base Euclid's algo")
print(euclid_gcd(10, 2))
print(euclid_gcd(999999999999999999, 1000000000000000000))
print(euclid_gcd(247, 33))
print(euclid_gcd(11, 22))


print("Updated Euclid's algo")
print(updated_euclid_gcd(10, 2))
print(updated_euclid_gcd(999999999999999999, 1000000000000000000))
print(updated_euclid_gcd(247, 33))
print(updated_euclid_gcd(11, 22))
