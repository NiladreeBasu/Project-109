import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics as st
import plotly.graph_objects as go
import pandas as pd
import csv

df = pd.read_csv("StudentsPerformance.csv")
mathscore = df['mathScore'].tolist()

mean = st.mean(mathscore)
median = st.median(mathscore)
mode = st.mode(mathscore)
sd = st.stdev(mathscore)

print(mean,mode,median,sd)

sd1start,sd1end = mean-sd,mean+sd
sd2start,sd2end = mean-(2*sd),mean+(2*sd)
sd3start,sd3end = mean-(3*sd),mean+(3*sd)

fig = ff.create_distplot([mathscore],['Result'],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode='lines', name = 'mean'))
fig.add_trace(go.Scatter(x = [sd1start,sd1start], y = [0,0.17], mode='lines', name = 'sd1'))
fig.add_trace(go.Scatter(x = [sd1end,sd1end], y = [0,0.17], mode='lines', name = 'sd1'))
fig.add_trace(go.Scatter(x = [sd2start,sd2start], y = [0,0.17], mode='lines', name = 'sd2'))
fig.add_trace(go.Scatter(x = [sd2end,sd2end], y = [0,0.17], mode='lines', name = 'sd2'))
fig.add_trace(go.Scatter(x = [sd3start,sd3start], y = [0,0.17], mode='lines', name = 'sd3'))
fig.add_trace(go.Scatter(x = [sd3end,sd3end], y = [0,0.17], mode='lines', name = 'sd3'))
fig.show()

listofdatawithinsd1 = [Result for Result in mathscore if Result > sd1start and Result < sd1end]
listofdatawithinsd2 = [Result for Result in mathscore if Result > sd2start and Result < sd2end]
listofdatawithinsd3 = [Result for Result in mathscore if Result > sd3start and Result < sd3end]

print('{}% of data lies within sd1'.format(len(listofdatawithinsd1)*100.0/len(mathscore)))
print('{}% of data lies within sd2'.format(len(listofdatawithinsd2)*100.0/len(mathscore)))
print('{}% of data lies within sd3'.format(len(listofdatawithinsd3)*100.0/len(mathscore)))