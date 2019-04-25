import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import scipy.stats as stats
import math

df = pd.read_csv("Ebenezer_Stats2016-2019_full.csv")
male = df.loc[df['Gender'] == 'M']
female = df.loc[df['Gender'] == 'F']
male = male.query('Age < 80')

male2016 = male.query('Year == 2016')
male2017 = male.query('Year == 2017')
male2018 = male.query('Year == 2018')
male2019 = male.query('Year == 2019')


def f(row):
    if row['Gender'] == 'M':
        return 0
    return 1

def clustering():
    print("Clustering 2")

    #male2016 = male.loc[male['Year'] == '2016']
    #print(male2016)


    #plt.bar(male['Year'], male['Age'])
    ax = plt.figure()


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







def scatter():
    print('hello')

    plt.scatter(male['Time'], male['Age'], c='blue', alpha=0.2, s=120, edgecolors='none', label='Male')
    plt.scatter(female['Time'], female['Age'], c='red', alpha=0.1, s=120, edgecolors='none', label='Female')

    #plt.scatter(male2016['Time'], male2016['Age'], c='blue', alpha=0.2, label='2016', s=50)
    #plt.scatter(male2017['Time'], male2017['Age'], c='red', alpha=0.2, label='2017', s=50)
    #plt.scatter(male2018['Time'], male2018['Age'], c='green', alpha=0.2, label='2018', s=50)
    #plt.scatter(male2019['Time'], male2019['Age'], c='purple', alpha=0.2, label='2019', s=50)

    # plt.scatter(female['Time'], female['Age'], c='red', alpha=0.2, s=120, edgecolors='none', label='Female')
    plt.scatter(31.28, 33, s=120, marker='d', label='Me', edgecolors='black')
    plt.scatter(30.19, 36, s=120, marker='d', label='Friend1', edgecolors='black') # Schalk
    plt.scatter(38.24, 49, s=120, marker='d', label='Friend2', edgecolors='black') # Neal
    plt.scatter(39.13, 40, s=120, marker='d', label='Friend3', edgecolors='black') # JP
    plt.scatter(47.16, 42, s=120, marker='d', label='Friend4', edgecolors='black') # Johan
    plt.ylabel('Age (Years)')
    plt.xlabel('Time (Minutes)')
    plt.title('Ebenezer 2018 - Male/Female Age/Time')
    plt.legend();
    plt.show()

def minmax():
    min = df.loc[df['Age'].idxmin]
    print('Min Age:', min.Age, 'Year:', min.Year, 'Time:', min.Time, 'Gender:', min.Gender)
    max = df.loc[df['Age'].idxmax]
    print('Max Age:', max.Age, 'Year:', max.Year, 'Time:', max.Time, 'Gender:', max.Gender)

def count():
    averages = (df.groupby(['Year', 'Gender']).mean().groupby(['Year', 'Gender'])['Time'].mean())
    print(averages.unstack())
    df['Age'] = round(df['Age'] / 5) * 5
    total = (df.groupby(['Year', 'Age'])['Gender'].count()).unstack(0).fillna(0)
    speed = (df.groupby(['Year', 'Age'])['Time'].mean()).unstack(0).fillna(0)

    #print(speed)
    print(total)
    #plt.xlabel('Count')
    #plt.ylabel('Age Group (5-years)')
    #plt.plot(total, speed, 'o');
    plt.legend();

    ax = total.plot.bar()
    ax.set(xlabel="Age (5 Year Buckets)")
    ax.set(ylabel="Count")
    plt.show()

def averages():
    averagesF = (df.query("Gender == 'F'").groupby(['Year', 'Gender']).mean().groupby(['Year', 'Gender'])['Time'].mean())
    averagesM = (df.query("Gender == 'M'").groupby(['Year', 'Gender']).mean().groupby(['Year', 'Gender'])['Time'].mean())
    #print(averages.unstack())
    plt.plot(averagesF.unstack(), label='Female')
    plt.plot(averagesM.unstack(), label='Male')

    plt.xlabel('Year')
    plt.ylabel('Average Time (minutes)')
    print(np.arange(2016, 2019 + 1, 1.0))
    plt.xticks(np.arange(2016, 2019 + 1, 1.0))
    plt.legend()

    plt.show()

def trend():
    averagesF = (df.query("Gender == 'F' and Age > 10 and Age < 80 and Time < 55").groupby(['Age']))['Time'].mean().reset_index()
    averagesM = (df.query("Gender == 'M' and Age > 10 and Age < 80").groupby(['Age']))['Time'].mean().reset_index()
    plt.plot(averagesM['Age'], averagesM['Time'], 'o', alpha=0.5, label='Male')
    plt.plot(averagesF['Age'], averagesF['Time'], 'x', alpha=0.5, label='Female')

    z = np.polyfit(averagesM['Age'], averagesM['Time'], 3)
    p = np.poly1d(z)
    plt.plot(averagesM['Age'], p(averagesM['Age']), "b--", label='Male')

    z = np.polyfit(averagesF['Age'], averagesF['Time'], 3)
    p = np.poly1d(z)
    plt.plot(averagesF['Age'], p(averagesF['Age']), "r--", label='Female')
    plt.legend()
    plt.show()

def main():
    print("Hello world")

    #print(reverse(123))
    #print(reverse_bits("00000010100101000001111010011100"))
    #scatter()
    trend()



if __name__ == "__main__":
    main()

