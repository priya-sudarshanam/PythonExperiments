package arrays;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Contains implementation of CTC's Chapter 1
 * on Arrays and Strings. 
 * 
 * @author dangiankit 
 * Created on: May 12, 2015
 */
public class CArrays {
	
	/**
	 * Initiates the execution of the program.
	 * 
	 * @param args - command line arguments
	 */
	public static void main(String[] args) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String string = new String();
		try {
			string = br.readLine();
		} catch (IOException ioException) {
			ioException.printStackTrace();
		}
		System.out.println(CArrays.hasAllUniqueChars(string));
		System.out.println(CArrays.removeDuplicateChars(string));
	}

	/**
	 * Determines whether or not the given <code>string</code>
	 * has all unique characters.
	 * 
	 * @param string - the string to check for unique characters
	 * @return <code>true</code> if the given <code>String</code> 
	 * contains unique characters, <code>false</code> otherwise.
	 */
	public static Boolean hasAllUniqueChars(String string) {
		boolean[] asciiTable = new boolean[Byte.MAX_VALUE];
		for(int i=0, asciiIndex=0; i<string.length(); i++) {
			asciiIndex = (int) (string.charAt(i));
			if(asciiTable[asciiIndex]) { 
				return (Boolean.FALSE); 
			}
			asciiTable[asciiIndex] = Boolean.TRUE;
		}
		return (Boolean.TRUE);
	}
	
	/**
	 * Reverses the given <code>string</code> as a C-Style string
	 * including a null character at the end. 
	 * 
	 * @param string - the string to reverse
	 * @return the reversed <code>String</code> including a null character.
	 */
	public static String cStyleReverse(String string) {
		char NULL_CHARACTER = '\u0000';
		String reverseString = new String();
		for(int i=string.length()-1; i>=0; i--) {
			reverseString += string.charAt(i);
		}
		reverseString += NULL_CHARACTER;
		return (reverseString);
	}
	
	/**
	 * Removes the duplicate characters from the given <code>string</code>.
	 * 
	 * @param string - the string from which the duplicate 
	 * characters need to be removed
	 * 
	 * @return a <code>String</code> that contains all 
	 * unique characters of the given <code>string</code>. 
	 */
	public static String removeDuplicateChars(String string) {
		String uniqueCharsString = new String("");
		for(int i=0; i<string.length(); i++) {
			char c = string.charAt(i);
			if(!uniqueCharsString.contains(String.valueOf(c)))
				uniqueCharsString += c;
		}
		return (uniqueCharsString);
	}
}
