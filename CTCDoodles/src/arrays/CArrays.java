package arrays;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Contains implementation of CTC's Chapter 1
 * on Arrays and Strings. 
 * 
 * @author dangiankit 
 * Last modified on: May 12, 2015
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
	}

	/**
	 * Determines whether or not the given <code>string</code>
	 * has all unique characters.
	 * 
	 * @param string - the string to check for unique characters
	 * @return <code>true</code> if the given <code>String</code> 
	 * contains unique characters, <code>false</code> otherwise.
	 */
	private static Boolean hasAllUniqueChars(String string) {
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
}
