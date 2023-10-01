import pandas as pd
import pm4py

if __name__ == "__main__":
    log = pm4py.format_dataframe(pd.read_csv("flight_event_log.csv", sep=","), case_id="Flight",
                                 activity_key="Activity", timestamp_key="Timestamp")
    pm4py.write_xes(log, "myfile.xes")
