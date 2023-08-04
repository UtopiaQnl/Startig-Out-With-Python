def main():
    video_file = open("video_times.txt")

    total = 0

    count = 0

    print("Длительность всех видеоклипов:")

    for line in video_file:
        run_time = float(line)
        count += 1
        print(f"Видеоклип №{count}: {run_time}")

        total += run_time

    video_file.close()
    print(f"Общая длительность составляет {total} секунд.")


if __name__ == "__main__":
    main()
