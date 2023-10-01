import pm4py
import pandas as pd
import datetime as dt
log = pm4py.format_dataframe(pd.read_csv("flight_event_log.csv", sep=","), case_id="Flight",
                             activity_key="Activity", timestamp_key="Timestamp")
filtered = pm4py.filter_start_activities(log, {"Check-in"})

# filtered1 = pm4py.filter_end_activities(log,{"Landing"})
# print(filtered1)
filtered2 = pm4py.filter_event_attribute_values(log, "City", {"New York", "Munich"}, level="event")
# print(filtered2)
filtered3 = pm4py.filter_directly_follows_relation(log, [["Check-in", "Boarding", "Take off", "Landing", "Baggage claim"]])
#print(filtered3)
filtered4= pm4py.filter_time_range(log,dt.datetime(2019,1,1),dt.datetime(2019,2,28), mode="events")
print(filtered4)