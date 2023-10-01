import pandas as pd


def import_csv(file_path):
    event_log = pd.read_csv(file_path, sep=",")
    num_event = len(event_log)
    num_fli = len(event_log.Flight.unique())
    print("Number of event:{}\n Number of flight:{}".format(num_event, num_fli))


if __name__ == "__main__":
    import_csv("flight_event_log.csv")
