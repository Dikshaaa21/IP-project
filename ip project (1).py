import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
def login():
    df=pd.read_csv("C:/ugh/users.csv")
    df['Username']=df['Username'].astype(str).str.strip()
    df['Password']=df['Password'].astype(str).str.strip()
    
    u=input('enter username-').strip()
    p=input('enter password-').strip()
    if ((df['Username']==u) & (df['Password']==p)).any():
        print(' LOGIN SUCCESSFUL! ')
        return True
    else:
        print('invalid username or password')
        return False

def add_user():
    while True:
        df=pd.read_csv("C:/ugh/users.csv")
        new_user=input('enter new username-')
        new_pass=input('enter new password-')
        if new_user in df['Username'].values:
            print("user already exists")
        else:
            df.loc[len(df)]=[new_user,new_pass]
            df.to_csv("C:/ugh/users.csv",index=False)
            print('new user added')
            print('1.add another user')
            print('2.Back to main menu')
            choice=input('enter your choice')
            if choice=='2':
                break


def recommend_songs():
    while True:
        songs_df = pd.read_csv("C:/ugh/songs.csv")
        mood = input("Enter your mood (happy, sad, calm, energetic,romantic,roadtrip): ").lower()

        match = songs_df[songs_df['Mood'].str.lower()== mood]
        if not match.empty:
            print(f"\n Songs for mood '{mood}':\n")
            for i, song in enumerate(match['Song'], start=1):
                print(f"{i}. {song}")
            
        else:
            print("Mood not found. Please try again.\n")
            
        print('1.Try again')
        print('2.Back to main menu')
        choice=input('enter your choice')
        if choice=='2':
            break

        

#View All Mood Categories
def view_categories():
    while True:
        songs_df = pd.read_csv("C:/ugh/songs.csv")
        moods = songs_df['Mood'].unique()
        print("\n Mood Categories Available:")
        for mood in moods:
            print("-", mood)
        print('1.refresh list')
        print('2.Back to main menu')
        choice=input('enter your choice')
        if choice=='2':
            break

#Add New Song
def add_song():
    songs_df = pd.read_csv("C:/ugh/songs.csv")
    while True:
        mood = input("Enter mood for the new song: ").lower()
        song = input("Enter song name: ")

        songs_df.loc[len(songs_df)] = [mood, song]
        songs_df.to_csv("songs.csv", index=False)
        print("Song added successfully!\n")

        print("1. Add another song")
        print("2. Back to main menu")
        choice = input("Enter your choice: ")
        if choice == "2":
            break

# Remove Existing Song
def remove_song():
    songs_df = pd.read_csv("C:/ugh/songs.csv")
    while True:
        print("\n Existing Songs:")
        print(songs_df)
        remove= input("Enter exact name of song to remove: ")

        if remove in songs_df['Song'].values:
            songs_df = songs_df[songs_df['Song'] != remove]
            songs_df.to_csv("songs.csv", index=False)
            print("Song removed successfully!\n")
        else:
            print("Song not found.\n")

        print("1. Remove another song")
        print("2. Back to main menu")
        choice = input("Enter your choice: ")
        if choice == "2":
            break

#  Show All Songs in Table Format
def show_all_songs():
    
    songs_df = pd.read_csv("C:/ugh/songs.csv")
    print("\n All Songs in the Database:\n")
    print(tabulate(songs_df, headers='keys',tablefmt='fancy_grid',
            showindex=False,numalign='center', stralign='center'))

#Pie Chart
def piechart():
    df = pd.read_csv("C:/ugh/songs.csv")
    mood_counts = df['Mood'].value_counts()
    colors = ['#FFD700', '#FF69B4', '#87CEFA', '#90EE90', '#FFB6C1', '#FFA07A', '#BA55D3',
                  '#40E0D0']
    plt.figure(figsize=(7,7))
    plt.pie(mood_counts,labels=mood_counts.index,autopct='%1.1f%%',startangle=90,
            colors=colors,textprops={'fontsize': 12, 'weight': 'bold'})
    plt.title("Mood Distribution of Listeners ", fontsize=16, fontweight='bold')
    plt.axis('equal')  
    plt.tight_layout()
    plt.show()

#Bar chart
def bar_graph():
    df = pd.read_csv("C:/ugh/songs.csv",names=["Mood","Song"], header= None)
    df["Singer"]=df["Song"].str.extract(r' by (.*)', expand= False)
    singer_counts = df['Singer'].value_counts().head(6)
    plt.figure(figsize=(8, 6))
    plt.bar(singer_counts.index,singer_counts.values,
            color=['r','c','y','m','b','g'],
            edgecolor='black')
    plt.title("Top 6 Most Listened Singers (This Week)",fontsize=16, fontweight='bold')
    plt.xlabel("Singer", fontsize=12, fontweight='bold')
    plt.ylabel("Number of Listens", fontsize=12, fontweight='bold')
    plt.xticks(rotation=20, ha='right', fontsize=11, fontweight='bold')
    plt.yticks(fontsize=11, fontweight='bold')
    plt.tight_layout()
    plt.show()

# Main Menu
def main_menu():
    while True:
        print("\n Welcome to the Mood-Based Song Recommender")
        print("1. Detect Mood & Recommend Songs")
        print("2. View Song Categories")
        print("3. Add New User")
        print("4. Exit")
        print("5. Add a New Song")
        print("6. Remove an Existing Song")
        print("7. Show All Songs")
        print("8. Show Piechart")
        print("9.Show Bargraph")

        
        choice = input("Enter your choice (1–9): ")

        if choice == "1":
            recommend_songs()
        elif choice == "2":
            view_categories()
        elif choice == "3":
            add_user()
        elif choice == "4":
            print("Thank you for using the Song Recommender!")
            break
        elif choice == "5":
            add_song()
        elif choice == "6":
            remove_song()
        elif choice == "7":
            show_all_songs()
        elif choice=="8":
            piechart()
        elif choice=="9":
            bar_graph()
        else:
            print(" Invalid choice. Please enter 1–8.\n")




if login():
    main_menu()















              
