
/* 	prompt user to enter father's age 
	collect father's  name from user assign it to a vraible fatherage
	prompt user to enter son's age
	collect son's  name from user  assign it to a variable sonage
	calculate twice the son age by multiplying the age by 2 and assign the result to variable twicesonage
	deduct twice the son age from the current father's age to get how many  years ago was he twice his son's age
	print the age the father was when he was twice his son's age
											*/


import java.util.Scanner;

public class TwiceAsOld{
	public static void main(String[] args){
	
		Scanner scanner = new Scanner(System.in);

		System.out.print("Enter current father's age: ");
		int fatherAge = scanner.nextInt();
		System.out.print("Enter current son's age: ");
		int sonAge = scanner.nextInt();
		 
		int twiceSonAge = sonAge * 2;
		int fatherTwiceSonAge = fatherAge - twiceSonAge;
		System.out.println("The father was twice his son's age " + fatherTwiceSonAge + "years ago.");
	}
}