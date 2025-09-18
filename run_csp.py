from cs4300_csp_parser import parse_cs4300
from cs4300_csp import solve_backtracking

def _pp_grid(sol):
    # detect size by scanning variables like R1C1..R9C9 (or R1C1..R4C4)
    rows = {int(k[1]) for k in sol if k.startswith("R")}
    cols = {int(k[k.index('C')+1:]) for k in sol if 'C' in k}
    n = max(max(rows), max(cols))
    for r in range(1, n+1):
        line = []
        for c in range(1, n+1):
            v = sol.get(f"R{r}C{c}", 0)
            line.append(str(v) if v else ".")
        print(" ".join(line))



if __name__ == "__main__":
    import sys, time
    if len(sys.argv) != 2:
        print("Usage: python run_csp.py <problem.csp>")
        sys.exit(1)
    csp = parse_cs4300(sys.argv[1])
    any_sol = False
    t0 = time.perf_counter()
    for i, sol in enumerate(solve_backtracking(csp, use_mrv=True), 1):
        any_sol = True
        _pp_grid(sol)
    if not any_sol:
        print("No solutions.")
    print(f"Runtime: {time.perf_counter() - t0:.3f}s")



