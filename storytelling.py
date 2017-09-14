import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

pd.options.mode.chained_assignment = None
os.system('cls')
con = pd.read_csv("C:\\Users\\EricF\\Documents\\Competing through Business Analytics\\ConstructionTimeSeriesDataV2(1).csv", sep = ",")

con['Private %'] = con['Private Construction'] / con['Total Construction']
con['Public %'] = con['Public Construction'] / con['Total Construction']
con['Private Change'] = con['Month']
con['Private Change'][0] = None
con['Public Change'] = con['Month']
con['Public Change'][0] = None
con['Month-Abbrev'] = con['Month']
con['Abs Diff'] = con['Private Construction'] - con['Public Construction']
con['MonNum'] = None

for i in range(len(con['Month-Year'])):
    con['MonNum'][i] = str(con['Month-Year'][i]).split('-')[-1]

#print con['Month-Year'][len(con['Month-Year']) - 1]

x_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for i in range(len(con['Month-Abbrev'])):
    k = i % len(x_labels)
    con['Month-Abbrev'][i] = x_labels[k]

for i in range(len(con['Private Change'])):
    try:
        con['Private Change'][i + 1] = ((float(con['Private Construction'][i + 1]) - float(con['Private Construction'][i]))/float(con['Private Construction'][i + 1])) * 100
        con['Private Change'][i + 1] = round(con['Private Change'][i + 1], 2)
        con['Public Change'][i + 1] = ((float(con['Public Construction'][i + 1]) - float(con['Public Construction'][i]))/float(con['Public Construction'][i + 1])) * 100
        con['Public Change'][i + 1] = round(con['Public Change'][i + 1], 2)
    except:
        pass
#print con.head()
average_est = []
average_pub = []
for i in range(2, 15):
    average = []
    avg_pub = []
    #print int(con['MonNum'][i])
    for k in range(len(con['Month'])):
        if int(con['MonNum'][k]) == i:
            average.append(con['Private Construction'][k])
            avg_pub.append(con['Public Construction'][k])
    average_est.append((sum(average)/len(average)))
    average_pub.append((sum(avg_pub)/len(avg_pub)))

print average_pub
print average_est

fig, ax1 = plt.subplots(1, 1, figsize = (20, 10))
ax1.plot(range(2, 15), average_pub, label = 'Average Yearly Pubic')
ax1.plot(range(2, 15), average_est, label = 'Average Yearly Private')
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.legend(loc = 'upper right')
ax1.xaxis.set_label_text('Years', fontsize = 18)
ax1.yaxis.set_label_text('Average Spending', fontsize = 18)
fig.suptitle("Private/Public Average Annual Spending", fontsize = 25)
fig.savefig('C:\Users\EricF\Documents\Python\Python Work Dir\CBTA\Average Spending.png', format = 'png', dpi = 1000)
"""
print con['Private Change'].corr(con['Public Change'])

#(width, height)
fig1, ax11 = plt.subplots(1, 1, figsize = (20, 10), sharey = True)
#scat, axscat = plt.subplots(1, 1, figsize = (20, 10))
fig, (ax1, ax2) = plt.subplots(2, 1, figsize = (20, 10), sharey = True)

y1 = con['Total Construction']
y2 = con['Public Change']
a2 = con['Public Construction']
y3 = con['Private Change']
a3 = con['Private Construction']

#plt.plot(con['Month'], y1, label = 'Total Construction')
ax1.plot(con['Month'], y2, label = "Public Construction % Change")
ax2.plot(con['Month'], y3, label = "Private Construction % Change")
#axscat.scatter(y2, y3, label = "Public/Private Correlation")

ax11.plot(con['Month'], a2, label = "Public Construction")
ax11.plot(con['Month'], a3, label = "Private Construction")
#ax11.plot(con['Month'], y1, label = "Total Construction")
#ax11.plot(con['Month'], con['Abs Diff'], label = "Private/Public Difference")

for ax in fig.axes:
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks(np.arange(0, len(con['MonNum'])))
    ax.legend(loc = 'upper right')
    ax.xaxis.set_label_text('Month', fontsize = 18)
    ax.yaxis.set_label_text('% Change', fontsize = 18)
    ax.xaxis.set_ticklabels(con['Month-Year'])
    for label in ax.xaxis.get_ticklabels():
        label.set_visible(False)
    for tick in ax.xaxis.get_major_ticks():
        tick.set_visible(False)
    for label in ax.xaxis.get_ticklabels()[::6]:
        label.set_visible(True)
    for tick in ax.xaxis.get_major_ticks()[::6]:
        tick.set_visible(True)

for ax in fig1.axes:
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks(np.arange(0, len(con['MonNum'])))
    ax.legend(loc = 'upper right')
    ax.xaxis.set_label_text('Month', fontsize = 18)
    ax.yaxis.set_label_text('Spending', fontsize = 18)
    ax.xaxis.set_ticklabels(con['Month-Year'])
    for label in ax.xaxis.get_ticklabels():
        label.set_visible(False)
    for tick in ax.xaxis.get_major_ticks():
        tick.set_visible(False)
    for label in ax.xaxis.get_ticklabels()[::6]:
        label.set_visible(True)
    for tick in ax.xaxis.get_major_ticks()[::6]:
        tick.set_visible(True)


for ax in scat.axes:
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_label_text('Public Construction % Change', fontsize = 18)
    ax.yaxis.set_label_text('Private Construction % Change', fontsize = 18)

fig.suptitle("Public vs Private Construction Spending % Change", fontsize = 25)
fig1.suptitle("Public vs Private Construction Spending", fontsize = 25)
#scat.suptitle("Public/Private Correlation", fontsize = 25)

fig.savefig('C:\Users\EricF\Documents\Python\Python Work Dir\CBTA\Percent Change.png', format = 'png', dpi = 1000)
fig1.savefig('C:\Users\EricF\Documents\Python\Python Work Dir\CBTA\Construction.png', format = 'png', dpi = 1000)
#scat.savefig('C:\Users\EricF\Documents\Python\Python Work Dir\CBTA\Correlation.png', format = 'png', dpi = 1000)
"""
plt.show()
