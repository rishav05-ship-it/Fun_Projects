package lab2; 

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Random;
import java.util.Scanner;

public class MusicLibraryApp
{

    public static void main(String[] args) throws FileNotFoundException 
    {
        // Only this line is changed to use "song.txt" without a full path

    	File file = new File("song.txt");


        if (!file.exists()) 
        {
            System.out.println("File not found");
            return;
        }

        String randomly_picked_songs = "";
        int count = 0;
        Random rand = new Random();
        Scanner scan = new Scanner(file);
        System.out.println("All songs in the library:");

        while (scan.hasNextLine())
        {
            String activesongs = scan.nextLine();
            System.out.println(activesongs);
            count++;

            if (rand.nextInt(count) == 0) 
            {
                randomly_picked_songs = activesongs;
            }
        }

        scan.close(); // Closing scanner here

        if (!randomly_picked_songs.isEmpty()) 
        {
            // Extract just the song title from the full song information
            String selectedSongTitle = randomly_picked_songs.split(" by ")[0];
            System.out.println("**Playing Random Song**");
            System.out.println("Now playing: " + selectedSongTitle);
        } else 
        {
            System.out.println("No songs available to play.");
        }
    }
}

