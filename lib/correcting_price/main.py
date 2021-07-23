import pandas as pd
source_file = pd.read_html('31103-plity-perekrytia-napr.html', header=0)
df = (source_file[0])
print(df)
df = df.set_index('Наименование')
df['Цена, руб.'] = df['Цена, руб.']*1.1
df['Цена, руб.'] = df['Цена, руб.'].round(0).astype(int)
df.to_html('result.html')
