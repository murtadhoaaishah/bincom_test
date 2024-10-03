from collections import Counter
import statistics

from db_operations import connect_db, create_table, insert_color_data, close_connection

colors_week = [
    'GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN'.split(', '),
    'ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE'.split(', '),
    'GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE'.split(', '),
    'BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN'.split(', '),
    'GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE'.split(', ')
]

all_colors = [color for day_colors in colors_week for color in day_colors]
print(all_colors)

color_counts = Counter(all_colors)
print("Color Counts:", color_counts)
print(color_counts)

# Flatten the list of colors across the week
all_colors = [color for day_colors in colors_week for color in day_colors]

# Counter for color frequencies
color_counts = Counter(all_colors)
print("Color Counts:", color_counts)

# Assign numbers to colors
color_map = {color: idx for idx, color in enumerate(color_counts.keys())}
numeric_colors = [color_map[color] for color in all_colors]

# Find the mean and map it back to color
mean_color_idx = round(statistics.mean(numeric_colors))
mean_color = list(color_map.keys())[list(color_map.values()).index(mean_color_idx)]
print("Mean Color:", mean_color)

most_frequent_color = color_counts.most_common(1)[0][0]
print("Most Frequent Color:", most_frequent_color)

median_color_idx = round(statistics.median(numeric_colors))
median_color = list(color_map.keys())[list(color_map.values()).index(median_color_idx)]
print("Median Color:", median_color)

variance = statistics.variance(numeric_colors)
print("Variance of Colors:", variance)

total_colors = len(all_colors)
red_count = color_counts['RED']
probability_red = red_count / total_colors
print("Probability of Red:", probability_red)


# Database operations: Save color counts to PostgreSQL
conn, cur = connect_db()
if conn and cur:
    create_table(cur)
    for color, freq in color_counts.items():
        insert_color_data(cur, color, freq)

    # Commit changes and close the connection
    conn.commit()
    close_connection(conn, cur)