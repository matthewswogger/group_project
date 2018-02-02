import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def import_clean_data(data, air, carr):
    f = "data/"
    df = pd.read_csv(f+data)
    airports = pd.read_csv(f+air)
    carriers = pd.read_csv(f+carr)

    df = df.merge(airports, how='inner', left_on="Origin", right_on="iata")
    df = df.merge(airports, how='inner', left_on="Dest", right_on="iata")
    df = df.merge(carriers, how='inner', left_on='UniqueCarrier', right_on='Code')
    df.drop(['FlightNum', 'TailNum', 'iata_x', 'iata_y',
             'UniqueCarrier', 'Code'], axis=1, inplace=True)
    df.rename(columns={'DayofMonth': 'Day',
                       'airport_x': 'origin_airport',
                       'city_x': 'origin_city',
                       'state_x': 'origin_state',
                       'country_x': 'origin_country',
                       'lat_x': 'origin_lat',
                       'long_x': 'origin_long',
                       'airport_y': 'dest_airport',
                       'city_y': 'dest_city',
                       'state_y': 'dest_state',
                       'country_y': 'dest_country',
                       'lat_y': 'dest_lat',
                       'long_y': 'dest_long'}, inplace=True)
    t_rep = 'US Airways Inc. (Merged with America West 9/05. Reporting for both starting 10/07.)'
    df.replace(t_rep, 'US Airways Inc.', inplace=True)
    del airports
    del carriers
    return df


def plotfunction(df, title, y_label, x_labels=None, simple=True,
                                                    r=0, l=None, a=.5):
    fig, ax = plt.subplots(figsize=(15,7))
    if simple:
        df.plot(kind='bar', ax=ax, color='#034e7b')
    else:
        df.plot(kind='bar', ax=ax, colormap='Blues')
    ax.set_xlabel('')
    ax.set_ylabel(y_label, fontsize=20)
    ax.set_title(title, fontsize=25)
    ax.tick_params('both', labelsize=17, rotation=r)
    if x_labels != None:
        ax.set_xticklabels(x_labels)
    if l != None:
        ax.legend(bbox_to_anchor=l)
    ax.grid(alpha=a)
