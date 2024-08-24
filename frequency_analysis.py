from collections import Counter
import string
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def read_and_count(filename):
    with open(filename, 'r') as file:
        text = file.read().lower()

    text = ''.join(filter(lambda char: char in string.ascii_lowercase, text))

    letter_count = Counter(text)
    return letter_count

def calculate_stats(count):
    df = pd.DataFrame.from_dict(count, orient='index', columns=['frequency'])

    mean = df['frequency'].mean()
    median = df['frequency'].median()
    std = df['frequency'].std()
    min = df['frequency'].min()
    max = df['frequency'].max()

    return {
        'mean': mean,
        'median': median,
        'std': std,
        'min': min,
        'max': max
    }

def plot_frequencies(count):
    df = pd.DataFrame.from_dict(count, orient='index', columns=['frequency'])
    df.sort_index(inplace=True)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=df.index, y='frequency', data=df)
    plt.title('Letter Frequency Analysis')
    plt.xlabel('Letter')
    plt.ylabel('Frequency')
    plt.show()