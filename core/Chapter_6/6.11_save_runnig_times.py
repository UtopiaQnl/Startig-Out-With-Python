def main():
    num_videos = int(input("Сколько видеоклипов в проекте? "))

    video_file = open("video_times.txt", "w")

    print("Введите длительность каждого видеоклипа.")
    for count in range(1, num_videos + 1):
        run_time = float(input(f"Видеоклип №{count}: "))
        video_file.write(f"{run_time}\n")

    video_file.close()
    print("Времена сохранены в video_times.txt")


if __name__ == "__main__":
    main()
