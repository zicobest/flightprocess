import pandas as pd
import pm4py


def import_file(file_path):
    log = pd.read_csv("flight_event_log.csv", sep=",")
    log = pm4py.format_dataframe(log, case_id="Flight", activity_key="Activity", timestamp_key="Timestamp")

    start = pm4py.get_start_activities(log)

    end = pm4py.get_end_activities(log)
    print("Start of activity:{}\n End of activity:{}".format(start, end))
if __name__=="__main__":
    import_file("flight_event_log.csv")