import math

def pythagorean(n):
    for adj in range(1, n - 1):
        for opp in range(adj + 1, n):
            for hypo in range(opp + 1, n + 1):
                if (math.sqrt((adj * adj) + (opp * opp))) == hypo:
                    print(f'{adj}\t\t\t{opp}\t\t\t{hypo}')


print(f'''_____________________________________
Adjacent\tOpposite\tHypotenuse
_____________________________________''')
pythagorean(20)
