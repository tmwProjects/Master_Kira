#Front ändern
sns.set_theme(style="whitegrid", font_scale=1)
paletteB = ['#CD4F39', '#CD69C9', '#C6E2FF', '#7FFFD4', '#CAFF70']

sns.set_palette(paletteB)
#Plot laden mit entsprechender X und Y Achse
BD=sns.catplot(data=FTD, x="PN-Stelle", y="ermB", kind="box", hue='PN-Stelle')

#BD.legend.remove()

plt.title("ermB", weight='bold', fontstyle='italic', fontsize='15')

#Log Skalierung erstellen
plt.yscale('log')
#Achsenbeschriftung
BD.set(xlabel='',ylabel='Gene concentration\n [copies/100 mL]')

#Speichern
plt.savefig(r'C:\Users\kirak\OneDrive\Desktop\UNI Bonn\Master\ARG_Kira\grafics\Braunschweig_ermB.jpg')






#Front ändern
sns.set_theme(style="whitegrid", font_scale=1)

#Plot laden mit entsprechender X und Y Achse
BD=sns.catplot(data=FTD, x="PN-Stelle", y="blaTEM", kind="box", hue='PN-Stelle')
#BD.legend.remove()
plt.title("$bla_{TEM}$", weight='bold', fontstyle='italic', fontsize='15')



#Log Skalierung erstellen
plt.yscale('log')

#Achsenbeschriftung
BD.set(xlabel='',ylabel='Gene concentration\n [copies/100 mL]')

#Speichern
plt.savefig(r'C:\Users\kirak\OneDrive\Desktop\UNI Bonn\Master\ARG_Kira\grafics\Braunschweig_blaTEM.jpg')




#Front ändern
sns.set_theme(style="whitegrid", font_scale=1)

#Plot laden mit entsprechender X und Y Achse
BD=sns.catplot(data=FTD, x="PN-Stelle", y="blaNDM-1", kind="box", hue='PN-Stelle')
#BD.legend.remove()
plt.title("$bla_{NDM-1}$", weight='bold', fontstyle='italic', fontsize='15')


#Log Skalierung erstellen
plt.yscale('log')

#Achsenbeschriftung
BD.set(xlabel='',ylabel='Gene concentration\n [copies/100 mL]')

#Speichern
plt.savefig(r'C:\Users\kirak\OneDrive\Desktop\UNI Bonn\Master\ARG_Kira\grafics\Braunschweig_blaNDM-1.jpg')





#Front ändern
sns.set_theme(style="whitegrid", font_scale=1)

#Plot laden mit entsprechender X und Y Achse
BD=sns.catplot(data=FTD, x="PN-Stelle", y="mcr-1", kind="box", hue='PN-Stelle')
#BD.legend.remove()
plt.title("mcr-1", weight='bold', fontstyle='italic', fontsize='15')


#Log Skalierung erstellen
plt.yscale('log')

#Achsenbeschriftung
BD.set(xlabel='',ylabel='Gene concentration\n [copies/100 mL]')

#Speichern
plt.savefig(r'C:\Users\kirak\OneDrive\Desktop\UNI Bonn\Master\ARG_Kira\grafics\Braunschweig_mcr1.jpg')





#Front ändern
sns.set_theme(style="whitegrid", font_scale=1)

#Plot laden mit entsprechender X und Y Achse
BD=sns.catplot(data=FTD, x="PN-Stelle", y="norm. ermB", kind="box", hue='PN-Stelle')
#BD.legend.remove()
plt.title("Normalized ermB", weight='bold', fontsize='15')



#Log Skalierung erstellen
plt.yscale('log')

#Achsenbeschriftung
BD.set(xlabel='',ylabel='Gene concentration\n [copies/100 mL]')

#Speichern
plt.savefig(r'C:\Users\kirak\OneDrive\Desktop\UNI Bonn\Master\ARG_Kira\grafics\Braunschweig__norm_ermB.jpg')





#Front ändern
sns.set_theme(style="whitegrid", font_scale=1)

#Plot laden mit entsprechender X und Y Achse
BD=sns.catplot(data=FTD, x="PN-Stelle", y="norm. blaTEM", kind="box", hue='PN-Stelle')
#BD.legend.remove()
plt.title(r"$\bf{Normalized}$" + " " + "$bla_{TEM}$", weight='bold', fontsize='15')


#Log Skalierung erstellen
plt.yscale('log')


#Achsenbeschriftung
BD.set(xlabel='',ylabel='Gene concentration\n [copies/100 mL]')

#Speichern
plt.savefig(r'C:\Users\kirak\OneDrive\Desktop\UNI Bonn\Master\ARG_Kira\grafics\Braunschweig_norm_blaTEM.jpg')





#Front ändern
sns.set_theme(style="whitegrid", font_scale=1)

#Plot laden mit entsprechender X und Y Achse
BD=sns.catplot(data=FTD, x="PN-Stelle", y="norm. blaNDM-1", kind="box", hue='PN-Stelle')
#BD.legend.remove()
plt.title("Normalized $bla_{NDM-1}$", weight='bold', fontstyle='italic', fontsize='15')


#Log Skalierung erstellen
plt.yscale('log')

#Achsenbeschriftung
BD.set(xlabel='',ylabel='Gene concentration\n [copies/100 mL]')

#Speichern
plt.savefig(r'C:\Users\kirak\OneDrive\Desktop\UNI Bonn\Master\ARG_Kira\grafics\Braunschweig_Norma_blaNDM-1.jpg')





#Front ändern
sns.set_theme(style="whitegrid", font_scale=1)

#Plot laden mit entsprechender X und Y Achse
BD=sns.catplot(data=FTD, x="PN-Stelle", y="norm. mcr-1", kind="box", hue='PN-Stelle')
#BD.legend.remove()
plt.title("Normalized mcr-1", weight='bold', fontstyle='italic', fontsize='15')


#Log Skalierung erstellen
plt.yscale('log')

#Achsenbeschriftung
BD.set(xlabel='',ylabel='Gene concentration\n [copies/100 mL]')

#Speichern
plt.savefig(r'C:\Users\kirak\OneDrive\Desktop\UNI Bonn\Master\ARG_Kira\grafics\Braunschweig_Norm_mcr1.jpg')





MNG = pd.read_csv(r"/home/timm/PycharmProjects/ARG_Kira/data/raw/Gene_MoNette.csv", sep=';')

paletteMN = ["#FF6347", "#b8e994"]

gene_names = ['mcr-1', 'blaNDM-1', 'ermB', 'blaTEM', 'tetM', 'sul1', 'blaCMY', 'blaCTX-M', 'mecA', 'vanA', 'blaKPC']
norm_gene_names = ['KAA mcr-1', 'KAA blaNDM-1', 'ermB KAA', 'blaTEM KAA', 'tetM KAA', 'sul1 KAA', 'blaCMY KAA', 'blaCTX-M KAA', 'mecA KAA', 'vanA KAA', 'blaKPC KAA']

# Initialisieren eines leeren DataFrame für die umstrukturierten Daten
long_df = pd.DataFrame()

for gen_name, norm_gen_name in zip(gene_names, norm_gene_names):
    # Daten für das normale Gen
    temp_df = pd.DataFrame({
        'Gen': gen_name,
        'Typ': 'AVK',
        'Wert': MNG[gen_name]
    })

    # Daten für das normalisierte Gen
    temp_norm_df = pd.DataFrame({
        'Gen': gen_name,
        'Typ': 'KAA',
        'Wert': MNG[norm_gen_name]
    })

    # Zusammenführen in ein langes DataFrame
    long_df = pd.concat([long_df, temp_df, temp_norm_df])    

# Boxplots zeichnen
sns.set_theme(style="whitegrid", font_scale=1)
sns.set_palette(paletteMN)
plt.figure(figsize=(12, 6))
ax = sns.boxplot(x='Gen', y='Wert', hue='Typ', data=long_df)


#plt.title('Boxplots für zulauf und ablauf Werte pro Gen')
plt.xlabel(None)
plt.ylabel('Gene concentration\n [copies/100 mL]')
ax.set_yscale('log')
plt.savefig(r'/home/timm/PycharmProjects/ARG_Kira/grafics/monette.jpg')
plt.show()