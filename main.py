import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import scipy.stats as stats
import math


def f(row):
    if row['Gender'] == 'M':
        return 0
    return 1

def clustering():
    print("Clustering 2")
    df = pd.read_csv("Ebenezer_Stats2016-2019_full.csv")


    male = df.loc[df['Gender'] == 'M']
    #female = df.loc[df['Gender'] == 'F']
    #male2016 = male.loc[male['Year'] == '2016']
    male2016 = male.query('Year == 2016')
    male2017 = male.query('Year == 2017')
    male2018 = male.query('Year == 2018')
    male2019 = male.query('Year == 2019')
    #print(male2016)


    #plt.bar(male['Year'], male['Age'])
    ax = plt.figure()
    min = df.loc[df['Age'].idxmin]
    print('Min Age:', min.Age, 'Year:', min.Year, 'Time:', min.Time, 'Gender:', min.Gender)
    max = df.loc[df['Age'].idxmax]
    print('Max Age:', max.Age, 'Year:', max.Year, 'Time:', max.Time, 'Gender:', max.Gender)

    averages = (df.groupby(['Year', 'Gender']).mean().groupby(['Year', 'Gender'])['Time'].mean())
    df['Age'] = round(df['Age']/5)*5
    total = (df.groupby(['Year', 'Age'])['Gender'].count()).unstack(0).fillna(0)
    speed = (df.groupby(['Year', 'Age'])['Time'].mean()).unstack(0).fillna(0)
    print(speed)
    #print(total)
    plt.xlabel('Count')
    plt.ylabel('Age Group (5-years)')
    ax = total.plot.barh()
    ax.set(xlabel = "Count")
    ax.set(ylabel="Age (5 Years)")


    plt.show()

    return;
    print(averages.unstack())
    averages.unstack().plot.barh()
    plt.xlabel('Average Time (minutes)')
    plt.ylabel('Year & Gender')
    plt.show()
    return
    print(averages['Year'])
    #plt.bar(averages['Year'], averages['Time'])

    #plt.show();
    return


    #plt.scatter(male['Time'], male['Age'], c='blue', alpha=0.2, s=120, edgecolors='none', label='Male')

    #plt.scatter(male['Time'], male['Age'], c='blue', alpha=0.2, s=120, edgecolors='none', label='Male')
    plt.scatter(male2016['Time'], male2016['Age'], c='blue', alpha=0.2, label='2016', s=50)
    plt.scatter(male2017['Time'], male2017['Age'], c='red', alpha=0.2, label='2017', s=50)
    plt.scatter(male2018['Time'], male2018['Age'], c='green', alpha=0.2, label='2018', s=50)
    plt.scatter(male2019['Time'], male2019['Age'], c='purple', alpha=0.2, label='2019', s=50)

    #plt.scatter(female['Time'], female['Age'], c='red', alpha=0.2, s=120, edgecolors='none', label='Female')
    plt.scatter(30.19, 36, s=120, marker='d', label='Schalk', edgecolors='black')
    plt.scatter(31.28, 33, s=120, marker='d', label='Tiaan', edgecolors='black')
    plt.scatter(38.24, 49, s=120, marker='d', label='Neal', edgecolors='black')
    plt.scatter(39.13, 40, s=120, marker='d', label='JP', edgecolors='black')
    plt.scatter(47.16, 42, s=120, marker='d', label='Johan', edgecolors='black')
    plt.ylabel('Age (Years)')
    plt.xlabel('Time (Minutes)')
    plt.legend();

    plt.show()






def main():
    print("Hello world")

    #print(reverse(123))
    #print(reverse_bits("00000010100101000001111010011100"))
    clustering()



if __name__ == "__main__":
    main()

