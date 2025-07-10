import json

def Load_data():
    try : 
        with open("Video_list.txt", "r") as file: 
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def Save(videos):
    with open("Video_list.txt", "w") as file: 
        json.dump(videos,file)


def List_all_videos(videos):
    print("\n")
    print("These are the videos you have listed till now ")
    print("*"*50)
    for index, vid in enumerate(videos, start = 1):
        print(f"{index}. {vid['Name']} Duration:{vid['Time']}")  
    print("*"*50)
    

    #alternatively we can write
    #s = 1
    #for vid in videos:
    #    print(s,".","Name:",vid['Name'], "Time:",vid['Time'])
    #    s += 1


def Add_video(videos):
    Name = input("Enter video name: ")
    Time = input("Enter video time: ")
    videos.append({"Name":Name, "Time":Time})
    Save(videos)


def Update_video(videos):
    List_all_videos(videos)
    upd_ind = int(input("Which video do you want me to update: "))
    if upd_ind >=1 and upd_ind<=len(videos):
        name = input("Enter a new name: ")
        time = input("Enter a new time: ")
        videos[upd_ind-1] = {'Name':name , 'Time':time}
        Save(videos)
        print(upd_ind, "Number video Updated succesfully!!")
    



def Delete_video(videos):
    List_all_videos(videos)
    del_ind = int(input("Which video do you want me to delete: "))
    if del_ind >=1 and del_ind<=len(videos):
        con = input("Are you sure ?? Y/N : ")
        if con == "Y":
            del videos[del_ind-1]
            Save(videos)
            print("Video number",del_ind,"deleted succesfully!!")
        elif con == "N" : 
            print("Deleting process has been terminated. Thank you")
        else : 
            print("Invalid Selection. Select Y for Yes or N for No")
    


def main():
    videos = Load_data() # Will go to the file then fetch the data from that file
    hey = True
    while hey: 
        print("\nYoutube video manager")
        print("1. List all youtube videos")
        print("2. Add a video.")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")

        choice = input("Enter your choice:")
        
        match choice:
            case '1':
                List_all_videos(videos)
            case '2':
                Add_video(videos)
            case '3':
                Update_video(videos)
            case '4':
                Delete_video(videos)
            case '5':
                hey = False
            case _:
                print("Invalid Choice")


if __name__== "__main__":
    main()