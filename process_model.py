import pm4py
if __name__ == "__main__":
    log = pm4py.read_xes("myfile.xes")
    map =pm4py.discover_heuristics_net(log)
    pm4py.view_heuristics_net(map)
"""
    process_tree = pm4py.discover_process_tree_inductive(log)
    bpmn = pm4py.convert_to_bpmn(process_tree)
    pm4py.view_bpmn(bpmn)
"""