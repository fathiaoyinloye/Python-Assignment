/*	prompt user to enter three scores
	create a container total and assign zero to it
	create a container average and assign 0 to it
	create a container count and assign 1 to it
	Repeat the following process as long as variable count is less that 1 and count should increase at every repetition.
	collect the scores and assign  it to each variable
	total should increase by score 
	average should be total divided by 3
	if score is greater than and equal to 90, print A, if not
	if score is greater than and equal to 80, print B, if not
	if score is greater than and equal t0 60, print C, if not
	if score is less than 60, print F.
	At the end of the repeated process
	print average
							*/

import java.util.Scanner;

public class ThreeScore{
	public static void main(String[] args){
	
		Scanner scanner = new Scanner(System.in);
		int total = 0;
		int average = 0;
		for(int count = 1; count <= 3; count++){
			System.out.print("Enter student score: " );
			int score = scanner.nextInt();
			total = total + score;
			average = total/3;
			if(score >= 90){
				System.out.println("A");
			}

			else if(score >= 80){
				System.out.println("B");
			}	
			else if(score >= 70){
				System.out.println("C");
			}

			else if(score >= 60){
				System.out.println("D");
			}
			else{
				System.out.println("F");
			}
			
		}
		System.out.println("The average score is " + average);

	}
}