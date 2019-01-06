from subprocess import call
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from nmlu.qinspect.console import df_peek


INPUT_DIR = './example_data/titanic/'

print("\n--- INPUT:")
call(['ls', '-lah', INPUT_DIR])

# load
df_raw = pd.read_csv(f'{INPUT_DIR}train.csv', low_memory=False)

# Peek
df_peek(df_raw, 'df_raw')
