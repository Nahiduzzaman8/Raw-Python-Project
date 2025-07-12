import sqlite3
con = sqlite3.connect("Youtube.db")
cur = con.cursor()

cur.execute(''' 
            CREATE TABLE IF NOT EXISTS video_list(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, 
            time TEXT NOT NULL )
''')



def List_videos():
    cur.execute("SELECT * FROM video_list")
    for row in cur.fetchall():
        print(row)
    


def Add_video():
    name = input("Enter video name: ")
    time = input("Enter the duration: ")
    cur.execute('''INSERT INTO video_list
                                (name,time)
                            VALUES(?,?)''',
                            (name,time))
    con.commit()



def Update_video():
    List_videos()
    try:
        id = int(input("Which video do you want to update: "))
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")
        return

    cur.execute('''SELECT * FROM video_list WHERE id = ?''',(id,))
    if cur.fetchone() is None:
        print("No video found with that ID.")
        return

    new_name = input("Enter video name: ")
    new_time = input("Enter video duration: ")
    cur.execute('''Update video_list SET name = ?,
                time = ? WHERE id = ?''', (new_name,new_time,id))
    con.commit()
    


def Delete_video():
    List_videos()
    try:
        id = int(input("Which video do you want to update: "))
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")
        return
    cur.execute('''SELECT * FROM video_list WHERE id = ?''',(id,))
    if cur.fetchone() is None:
        print("No video found with that ID.")
        return

    cur.execute('''DELETE FROM video_list 
                WHERE id = ?''',(id,))
    con.commit()



def main():
    while True:
        print("\nYouTube Video Manager | SQLite")
        print("1. List all videos.")
        print("2. Add video ")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit Program")
        choice = input("Enter your choice: ")
        match choice: 
                case '1': List_videos()
                case '2': Add_video()
                case '3': Update_video()
                case '4': Delete_video()
                case '5': 
                    con.close()
                    print("Program Terminated Successfully!!")
                    break
                case _: print('''Invalid selection !!!!
                              Enter a number between 1 to 5 !!''')

if __name__ == "__main__":
    main()