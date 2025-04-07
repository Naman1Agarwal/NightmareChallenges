import angr
import claripy

proj = angr.Project("future", auto_load_libs=False)

state = proj.factory.entry_state()

input_size = 25
sym_input = claripy.BVS("flag", 8 * input_size)
state = proj.factory.entry_state(stdin=angr.storage.file.SimFile("stdin", content=sym_input, has_end=True))

simgr = proj.factory.simulation_manager(state)

target_addr = 0x4007a1

simgr.explore(find=target_addr)

if simgr.found:
    solution_state = simgr.found[0]
    solution = solution_state.solver.eval(sym_input, cast_to=bytes)
    print("Found solution:", solution)
else:
    print("No solution found.")

