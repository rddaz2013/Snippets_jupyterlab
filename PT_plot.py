fig=plt.figure(figsize=(7, 6), dpi= 100, facecolor='w', edgecolor='k')
Can_Temp = dat.myrecarray[ 'Can Temp' ]
Can_Pressure = dat.myrecarray[ 'Can Pressure' ]
plt.plot(Can_Temp, Can_Pressure,'b-',label='Gesamtverlauf der Messung')
Can_Temp = dat.myrecarray[ 'Can Temp' ][dat.myrecarray['Step']=='Track_1']
Can_Pressure = dat.myrecarray[ 'Can Pressure' ][dat.myrecarray['Step']=='Track_1']
plt.plot(Can_Temp, Can_Pressure,'r-',label='Reaktionsbereich')
plt.ylabel('Druck [bar]')
plt.xlabel('Temperatur [°C]')
plt.title(phitec_dat + 'PHITEC Druck/Temperatur')
plt.legend(prop={'size': 12})
plt.show()
