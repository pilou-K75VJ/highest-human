import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('./missions.csv', parse_dates=['launch', 'touchdown'])
    df = df.loc[~df.touchdown.isna()]

    dt_0 = df.launch.dt
    dt_1 = df.touchdown.dt

    launch_decimal = dt_0.year + dt_0.dayofyear / (365. + dt_0.is_leap_year)
    touchdown_decimal = dt_1.year + dt_1.dayofyear / (365. + dt_1.is_leap_year)
    date_decimal = (launch_decimal + touchdown_decimal) / 2.

    grouped_0 = df.altitude.groupby(dt_0.year).max()
    grouped_1 = df.altitude.groupby(dt_1.year).max()
    grouped = pd.concat((grouped_0, grouped_1), axis='index').groupby(level=0).max()

    _, ax = plt.subplots(figsize=(5, 1254 * 5 / 705))
    ax.bar(grouped.index, grouped.values,
           color='xkcd:night blue', align='edge', width=1. - 61./705.)
    # ax.plot(date_decimal, df.altitude, '.b')
    ax.set_ylim(-10000,)
    plt.savefig('full_.png')
    # plt.show()

    # _, ax = plt.subplots(figsize=(10, 30))
    # ax.bar(grouped.index, grouped.values.clip(max=2000.),
    #        color='xkcd:night blue', align='edge', width=1. - 61./705.)
    # # ax.plot(date_decimal, df.altitude.clip(upper=2000), '.b')
    # ax.set_ylim(-50,)
    # plt.savefig('cropped_.png')
    # # plt.show()
