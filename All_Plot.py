# 26.08.2018
timeline = dat.myrecarray['Time_s']
Can_Temp = dat.myrecarray[ 'Can Temp' ]
Can_Pressure = dat.myrecarray[ 'Can Pressure' ]
Can_Side = dat.myrecarray['Temperature(side)']
Heater = dat.myrecarray['Can Heater Power (W)']

f, axarr = plt.subplots(2,sharex=True,figsize=(9, 8), dpi=120)
axarr[1].grid(True)
axarr[0].grid(True)

# Box um den Reaktionsbereich Zeichenen
def Get_timeT(data,wo_her):
    
    timeline2 = data.myrecarray['Time_s'][data.myrecarray['Step']==wo_her]
    Can_Temp2 = data.myrecarray[ 'Can Temp' ][data.myrecarray['Step']==wo_her]
    P1 = (np.min(timeline2)/60.,np.min(Can_Temp2)-5)
    P2 = ((np.max(timeline2)+10)/60.,np.max(Can_Temp2)+10)
    return (P1+P2)

xc = Get_timeT(dat,'Track_1')
    
rect = patches.Rectangle((xc[0],xc[1]),xc[2]-xc[0],xc[3]-xc[1],linewidth=1,edgecolor='r',facecolor='none')
axarr[0].text((xc[0]+xc[2])/2.,xc[1]-7,'Reaktionsbereich',fontsize=8,verticalalignment='center', 
              bbox={'facecolor':'red', 'alpha':0.5, 'pad':3})
axarr[0].add_patch(rect)

# Temp/Druck Plot

line, = axarr[0].plot(timeline/60., Can_Temp, linewidth=2.0, linestyle="-", picker=2,label='Probe Temp.')
line, = axarr[0].plot(timeline/60., Heater, linewidth=0.5, linestyle="-.", picker=2,label='direkte Heizung [W]')
line, = axarr[0].plot(timeline/60., Can_Side, linewidth=1.0, linestyle=":", picker=2,label='Heizblock Temp.')
axarr[0].legend(prop={'size': 12})
axarr[0].set_title(phitec_dat + 'PHITEC Zeit - Temperatur/Druck')
axarr[1].plot(timeline/60., Can_Pressure,label='Probe Druck',color='green',linewidth=1.0)
axarr[1].legend(prop={'size': 12})
axarr[1].set_xlabel('Zeit [min]')
axarr[0].set_ylabel('Temperatur [°C]')
axarr[1].set_ylabel('Druck [bar]')

# Layout enger als bisher
f.tight_layout() 
plt.subplots_adjust(hspace = .001)

plt.show()
