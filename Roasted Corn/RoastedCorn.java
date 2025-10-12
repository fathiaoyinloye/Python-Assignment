public class RoastedCorn{

	public static String oddIndex(String letters){
		String output = "";
		for (int count = 1; count < letters.length(); count+=2){
			output += letters.charAt(count);

		}
		return output;
		
	}

	public static String twoFirstLastCharacters(String letters){
		String output = "";

		if (letters.length() > 2)
			output = "" + letters.charAt(0) + letters.charAt(1) + letters.charAt(letters.length()-2) + letters.charAt(letters.length()-1);
		else
			output = "\"\"";	
		return output;

	}
	
	public static String addSuffix(String letters){
		String output = "";

		if (letters.length() < 3){
			output = letters;
		
		}
		while(letters.length() >= 3){
			String removeSuffix = "";
			String lastThreeCharacters = letters.substring(letters.length()-3, letters.length());
			String lastTwoCharacters = letters.substring(letters.length()-2, letters.length());

			if (!lastThreeCharacters.equalsIgnoreCase("ing") && !lastTwoCharacters.equalsIgnoreCase("ly")){
				output = letters + "ing";
			}
			else if (lastThreeCharacters.equalsIgnoreCase("ing")){
				removeSuffix = letters.substring(0, letters.length() - 3);
				output = removeSuffix + "ly";
			}
			else if (lastTwoCharacters.equalsIgnoreCase("ly")){
				removeSuffix = letters.substring(0, letters.length() - 2);
				output = removeSuffix + "ing";
			}

			break;
		}

		return output;
	
	}
	public static String getLongestWords(String[] words){
		String longestWords = words[0];
		int longest = words[0].length();
		for(int count = 1; count < words.length; count++){
			if (words[count].length() > longest){
				longest = words[count].length();
				longestWords = words[count];
			}
		}
		String result =  longest + "  "  + longestWords;
		return result;


	}
	public static String getWordsMultiples(String letters, double number){
		String output = "";
		if (number % 1 == 0){
			for (int count = 0; count < number; count++){
			output += letters;
			}
		}
		else
			output = letters;
	
		return	output;



	}
	public static int[] squareOfNumbers(int[] numbers){
		for (int count = 0; count < numbers.length; count++){
			numbers[count] = numbers[count] * numbers[count];


		}
		return numbers;


	}

	public static int sumOfSquareOfNumbers(int[] numbers){
		int sum = 0;
		for (int count = 0; count < numbers.length; count++){
			numbers[count] = numbers[count] * numbers[count];
			sum += numbers[count];

		}
		return sum;


	}


}