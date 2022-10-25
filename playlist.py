#!/usr/bin/python3
'''
             My First Python Project Using 
                         OOP
              --------------------------       

      How the programm works:

      - Create your playlist 
      - Add  Songs to it
      - Play the playlist and enjoy the songs :)
      - Move to next song
      - Back to previous song
      - Search for a specific song if available
      - Delete a song for the playList
      - Exit the programm

      Concepts used in the project:
      - Classes
      - Modules 
      - Instance variable
      - Exceptions
      - Object Generator
      - Basic concepts

                  ENJOY CODING
                  ------------
'''
import time 
class Song:
      def __init__(self,name:str):
            self.name = name
            
      def __str__(self):
            return self.name
         
     
class PlayList:
      def __init__(self,name:str):
            self.name = name
            self.playlist = []
            self.index = -1 

                  
      def add_song(self,song:Song):
                self.playlist.append(song)
              

      def remove_song(self,sng_name:str):
             self.playlist.remove(sng_name)
        
      def __iter__(self):
           return self 
           

      def __next__(self):
             self.index +=1 
             if self.index >= len(self.playlist):
                  self.index = -1 
                  raise StopIteration
             else:
                 return self.playlist [self.index]

      def __reversed__(self):
            self.index -=1 
            if self.index >= len(self.playlist):
                  self.index = +1 
                  raise IndexError
            else:
                 return self.playlist [self.index]

      def search_song(self,sng_name:str):
            if sng_name in self.playlist:
                     print("Song found >>>",sng_name,"<<<")
            else:
                     print(sng_name ," is not in the playlist")
      
      def remove_song(self,sng_name:str):
             self.playlist.remove(sng_name)
             print(sng_name,"REMOVED")

      def play_pl(self):
            for songs in self.playlist:
                  print(songs)
                  self.display_dots()
                  
      def display_lst(self):
            return f">>>{self.playlist }<<<"

      def display_dots(self):
            time.sleep(0.8)
            print(".",end="")
            time.sleep(0.8)
            print("..",end ="")
            time.sleep(0.8)
            print("...")
      
if __name__ == "__main__": 
      def prnt_menu():              
          print("1 - Create Playlist\n2 - Add a Song \n3 - PLAY Playlist \n4 - Play Next Song\n5 - Play Previous Song\n6 - Search a Song\n7 - Remove a Song\n8 - EXIT")
          
      prnt_menu()
      print("*"*23)

      pl_lst = True
      while pl_lst:
          try:  
                  s = int(input("Enter numer: "))
                  assert isinstance(s,int)
                  if s == 1:
                        list_name = input("Create your PlayList: ")
                        p = PlayList(list_name)
                        print("Add Songs to enjoy listening")
                        print()
                        prnt_menu()
                  elif s == 2:
                        n = input("Enter song name ").upper()
                        p.add_song(n)   
                  elif s == 3:
                        print(p.display_lst())
                        p.play_pl()
                  elif s == 4:
                        rnd = iter(p)
                        print(next(rnd))
                        p.display_dots()
                  elif s == 5:
                        print(reversed(p))
                        p.display_dots()
                  elif s == 6:
                        s_lst = input("Search a Song: ").upper()
                        p.search_song(s_lst)
                  elif s == 7:
                        s_lst = input("Enter Song Name to remove: ").upper()
                        p.remove_song(s_lst)
                  elif s == 8:
                        pl_lst = False
                  else:
                        print("Enter a valid number between 1 - 8")

          except (AssertionError,ValueError):
                 print("Enter a valid number ")
          except (StopIteration,IndexError):
                print("No more songs to play ")
          except NameError:
                print("Create a playlist to Add songs")
          finally:      
                 print("ENJOY LISTENING")
    
