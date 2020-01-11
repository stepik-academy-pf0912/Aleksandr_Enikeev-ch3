start_msg_to_user = '''Привет, это Stepik Media, портал видео посвященных программированию.
Введите 1, чтобы посмотреть видео;
Введите 2, чтобы найти видео;
Введите 3, чтобы посмотреть плейлисты;
Введите 0 или exit, чтобы выйти.\n'''

msg_to_user = ""

video_1_title = "Лекция №1"
video_1_link = "https://www.youtube.com/watch?v=KdZ4HF1SrFs&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0"

video_2_title = "#1 - Программирование на Python"
video_2_link = "https://www.youtube.com/watch?v=n0xtO0x81cg&list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu"

video_3_title = "#1 - основы"
video_3_link = "https://www.youtube.com/watch?v=PEKN8NtBDQ0&list=PLY4rE9dstrJyTdVJpv7FibSaXB4BHPInb"

videos = [video_1_title + " " + video_1_link, \
          video_2_title + " " + video_2_link, \
          video_3_title + " " + video_3_link]

search_video_list = []

playlist_1_title = "Алгоритмы на Python 3"
playlist_2_title = "Уроки Python для начинающих"
playlist_3_title = "Git - для новичков"

playlists = [playlist_1_title, playlist_2_title, playlist_3_title]

while True:
    user_command = input(start_msg_to_user)

    if user_command == '1':
        msg_to_user = "У нас нашлось {} видео:\n".format(len(videos))
        for video in videos:
            msg_to_user += video + "\n"

    if user_command == '2':
        search_command = input("Введите слово для поиска\n")
        for video in videos:
            if search_command in video:
                search_video_list.append(video)
        msg_to_user = "У нас нашлось {} видео по запросу '{}'\n".format(len(search_video_list), search_command)
        for video in search_video_list:
            msg_to_user += video + "\n"
        search_video_list = []

    elif user_command == '3':
        msg_to_user = "У нас нашлось {} плейлиста:\n".format(len(playlists))
        for playlist in playlists:
            msg_to_user += playlist + "\n"

    elif user_command == '0' or user_command == 'exit':
        break
    print(msg_to_user)
    msg_to_user = ""