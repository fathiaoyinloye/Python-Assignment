
public class RoastedCornTest{
	public static void main(String[] args){
	String [] words = {"father", "happiness", "big"};
	System.out.println(RoastedCorn.oddIndex("Semicolon"));
	System.out.println(RoastedCorn.twoFirstLastCharacters("on"));
	System.out.println(RoastedCorn.addSuffix("oneing"));
	System.out.println(RoastedCorn.getLongestWords(words));
	System.out.println(RoastedCorn.getWordsMultiples("words", 5));
	int [] numbers = {1,2,3,4,5};
	int [] number = {1,2,3,4,5};

			RoastedCorn.squareOfNumbers(numbers);
			for (int count = 0; count < numbers.length; count++){
				System.out.print((numbers[count] + " "));

			}
			System.out.println();
		System.out.print(RoastedCorn.sumOfSquareOfNumbers(number));

	}

}