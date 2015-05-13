package arrays;

import static org.junit.Assert.*;

import org.junit.Test;

public class CArraysTest {
	
	private String STRING_THE_QUICK_BROWN = new String("Thequickbrown");
	private String STRING_HUMPTY_DUMPTY = new String("Humpty dumpty");

	@Test
	public void testsHasAllUniqueChars() {
		assertTrue(CArrays.hasAllUniqueChars(STRING_THE_QUICK_BROWN));
		assertTrue(CArrays.hasAllUniqueChars("Lazy123"));
		assertTrue(CArrays.hasAllUniqueChars("$12450"));
		assertFalse(CArrays.hasAllUniqueChars(STRING_HUMPTY_DUMPTY));
		assertFalse(CArrays.hasAllUniqueChars("wordlyworld"));
		assertFalse(CArrays.hasAllUniqueChars("#$#Money"));
	}
	
	@Test
	public void testsCStyleReverse() {
		String reverseTheQuickBrown = CArrays.cStyleReverse(STRING_THE_QUICK_BROWN);
		assertEquals(reverseTheQuickBrown, "nworbkciuqehT\u0000");
		assertEquals(reverseTheQuickBrown.length(), STRING_THE_QUICK_BROWN.length()+1);
		
		String reverseHumptyDumpty = CArrays.cStyleReverse(STRING_HUMPTY_DUMPTY);
		assertEquals(reverseHumptyDumpty, "ytpmud ytpmuH\u0000");
		assertEquals(reverseHumptyDumpty.length(), STRING_HUMPTY_DUMPTY.length()+1);
	}
}
