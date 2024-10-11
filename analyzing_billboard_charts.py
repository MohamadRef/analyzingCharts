# 6/9/2023
# Mohamad Hussam Refaai (301603558)
# [Coding Exercise 4] Billboard Top 100 Songs Charts

def welcome_message():
    print("Welcome to the Billboard Top 100 App!")
    print("PART 1\n======\n")


def read_chart_data(file_name):
    with open(file_name, 'r') as file:
        next(file)  # Skip header
        return [line.strip().split(",") for line in file]


def analyze_songs(data):
    stats = {
        "number_of_songs_with_love": 0,
        "number_of_songs_in_rank_1_or_2": 0,
        "songs_less_in_rank": 0,
        "total_weeks_on_board": 0,
        "count_lines": len(data),
        "list_rank_songs": [],
        "list_names_A": []
    }

    for line in data:
        rank = int(line[1])
        previous_rank = int(line[4])
        weeks_on_board = int(line[6])

        if "love" in line[2].lower():
            stats["number_of_songs_with_love"] += 1
        if rank in [1, 2]:
            stats["number_of_songs_in_rank_1_or_2"] += 1
            stats["list_rank_songs"].append(line[2])
        if line[3][0].lower() == "a":
            stats["list_names_A"].append(line[3])
        if rank < previous_rank:
            stats["songs_less_in_rank"] += 1

        stats["total_weeks_on_board"] += weeks_on_board

    return stats


def display_part1_results(stats):
    print(f"Number of songs in rank 1 or 2: {stats['number_of_songs_in_rank_1_or_2']}")
    for song in stats['list_rank_songs']:
        print(song)

    print("\nArtists names starting with 'A':")
    for name in stats['list_names_A']:
        print(name)

    print(f"\nNumber of songs containing the word 'love': {stats['number_of_songs_with_love']}")
    print(f"\nNumber of songs that are less in the rank compared to the previous week: {stats['songs_less_in_rank']}")

    average_weeks_on_board = stats['total_weeks_on_board'] / stats['count_lines']
    print(f"\nAverage weeks on board all songs: {average_weeks_on_board:.2f}")


def artist_songs_query(data):
    artist_name = input("\nArtist name (may be part of the name) --> ").strip(".,?!").lower()
    print("\nArtist".ljust(60), "Song".ljust(30), "Date".ljust(30), "Rank".ljust(25), "Previous Rank".ljust(35))
    
    count = 0
    for line in data:
        if artist_name in line[3].lower():
            print(f"{line[3].ljust(60)}{line[2].ljust(30)}{line[0].ljust(30)}{line[1].ljust(25)}{line[4].ljust(35)}")
            count = 1

    if count == 0:
        print("\nThere is no such artist in the file.")


def song_weeks_on_board_query(data):
    song_title = input("\nSong title (may be part of the title) ----> ").strip(".,?!").lower()
    requested_weeks = None

    print("\nRequested Song".ljust(60), "Date".ljust(30), "Weeks on Board")
    
    for line in data:
        if song_title in line[2].lower():
            print(f"{line[2].ljust(60)}{line[0].ljust(30)}{line[6]}")
            requested_weeks = int(line[6])
            break

    if requested_weeks is None:
        print("\nNo matching song found.")

    return requested_weeks


def display_songs_with_extra_weeks(data, requested_weeks):
    if requested_weeks is not None:
        print("\nSongs with more weeks on board than the requested song")
        print("Song".ljust(60), "Date".ljust(30), "Extra Weeks on Board")

        for line in data:
            if int(line[6]) > requested_weeks:
                extra_weeks = int(line[6]) - requested_weeks
                print(f"{line[2].ljust(60)}{line[0].ljust(30)}{extra_weeks}")


def main():
    welcome_message()
    chart_data = read_chart_data('charts.csv')
    stats = analyze_songs(chart_data)
    display_part1_results(stats)
    
    print("\nPART 2\n======\n")
    artist_songs_query(chart_data)
    requested_weeks = song_weeks_on_board_query(chart_data)
    
    if requested_weeks is not None:
        display_songs_with_extra_weeks(chart_data, requested_weeks)
    
    print("\nBye! End of app!")


if __name__ == "__main__":
    main()
