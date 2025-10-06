public class MultiplesOfTwelve{
	public static int isMultipleOfTwelve(int number){
		
		if (number % 12 == 0)
		return 1;
		else
		return 0;

	}
	public static void main(String... args){

	System.out.print(isMultipleOfTwelve(5));

	}


}