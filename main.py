from scripts.frequency_analysis import read_and_count, calculate_stats, plot_frequencies

if __name__ == "__main__":
    filename = 'data/doi.txt' # Insert text file
    count = read_and_count(filename)
    stats = calculate_stats(count)
    print("Stats:", stats)
    plot_frequencies(count)