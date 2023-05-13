def solution():
    for S in range(1, 10):
        for E in range(10):
            if (E != S):
                for N in range(10):
                    if (N != S) and (N != E):
                        for D in range(10):
                            if (D != S) and (D != E) and (D != N):
                                for M in range(1, 10):
                                    if (M != S) and (M != E) and (M != N) and (M != D):
                                        for O in range(10):
                                            if (O != S) and (O != E) and (O != N) and (O != D) and (O != M):
                                                for R in range(10):
                                                    if (R != S) and (R != E) and (R != N) and (R != D) and (
                                                            R != M) and (R != O):
                                                        for Y in range(10):
                                                            if (Y != S) and (Y != E) and (Y != N) and (Y != D):
                                                                if (Y != M) and (Y != O) and (Y != R):
                                                                    if ((1000 * S + 100 * E + 10 * N + D)
                                                                            + (1000 * M + 100 * O + 10 * R + E)
                                                                            == (
                                                                                    10000 * M + 1000 * O + 100 * N + 10 * E + Y)):
                                                                        print("SEND=", 1000 * S + 100 * E + 10 * N + D)
                                                                        print("MORE=", 1000 * M + 100 * O + 10 * R + E)
                                                                        print("MONEY=", 10000 * M + 1000 * O +
                                                                              100 * N + 10 * E + Y)
                                                                        print("MONROE",
                                                                              100000 * M + 10000 * O + 1000 * N + 100 * R + 10 * O + E)


# solution : MONROE 106805
if __name__ == '__main__':
    solution()
