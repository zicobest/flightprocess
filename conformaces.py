import pandas as pd
import pm4py

df = pm4py.format_dataframe(pd.read_csv("flight_event_log.csv", sep=","), case_id="Flight", activity_key="Activity",
                            timestamp_key="Timestamp")





pn, im, fm = pm4py.discover_petri_net_inductive(df)
pm4py.view_petri_net(pn, im, fm)

pm4py.fitness_token_based_replay(df, pn, im, fm)
