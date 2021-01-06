import pandas as pd

df = pd.read_csv(
  filepath_or_buffer='data/training.1600000.processed.noemoticon.csv',
  encoding="ISO-8859-1",
  usecols=[0, 5],
  names=['target', 'text'],
  engine='python',
  error_bad_lines=False,
)

df['target'].value_counts().plot(kind='bar')
