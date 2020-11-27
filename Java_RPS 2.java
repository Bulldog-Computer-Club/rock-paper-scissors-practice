import java.util.Scanner;
import java.util.*;
import java.util.Random;

class Main {

  public static void tie (String user, String bot){
    if (user.compareTo(bot) == 0){
      System.out.println();
      System.out.println("It's a tie");
    }
  }

  public static void cpuWin (String user, String bot){
    if (user.equals("Rock") && bot.equals("Paper") || user.equals("Paper") && bot.equals("Scissors") || user.equals("Scissors") && bot.equals("Rock")){
      System.out.println();
      System.out.println("Progran Wins.");
    }
  }

  public static void humanWin (String user, String bot){
    if (user.equals("Rock") && bot.equals("Scissors") || user.equals("Paper") && bot.equals("Rock") || user.equals("Scissors") && bot.equals("Paper")){
      System.out.println();
      System.out.println("User Wins.");
    }
  }

  public static void main(String[] args) {
    ArrayList <String> options = new ArrayList <String>();
    options.add("Rock");
    options.add("Paper");
    options.add("Scissors");

    int index = new java.util.Random().nextInt(options.size());
    String cpu = options.get(index);

    Scanner input = new Scanner(System.in);
    String command = input.nextLine();

    while (!options.contains(command)){
      System.out.println("Enter your choice, Rock, Paper or Scissors! ");
      command = input.nextLine();
    }

    System.out.println("You chose: "+command);
    System.out.println("The program chose: " + cpu);

    tie (command,cpu);
    cpuWin (command,cpu);
    humanWin(command,cpu);
    
  }
}