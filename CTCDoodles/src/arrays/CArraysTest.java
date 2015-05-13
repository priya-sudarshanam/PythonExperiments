package arrays;

import static org.junit.Assert.*;

import org.junit.Test;

public class CArraysTest {

	private String STRING_THE_QUICK_BROWN 	= new String("Thequickbrown");
	private String STRING_HUMPTY_DUMPTY 	= new String("Humpty dumpty");
	private String STRING_WORLDLY_WORLD 	= new String("worldlyworld");

	@Test
	public void testsHasAllUniqueChars() {
		assertTrue(CArrays.hasAllUniqueChars(STRING_THE_QUICK_BROWN));
		assertFalse(CArrays.hasAllUniqueChars(STRING_HUMPTY_DUMPTY));
		assertFalse(CArrays.hasAllUniqueChars(STRING_WORLDLY_WORLD));
		assertTrue(CArrays.hasAllUniqueChars("Lazy123"));
		assertTrue(CArrays.hasAllUniqueChars("$12450"));
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

	@Test
	public void testsRemoveDuplicateChars() {
		assertEquals(CArrays.removeDuplicateChars(STRING_THE_QUICK_BROWN), STRING_THE_QUICK_BROWN);
		assertEquals(CArrays.removeDuplicateChars(STRING_HUMPTY_DUMPTY), "Humpty d");
		assertEquals(CArrays.removeDuplicateChars(STRING_WORLDLY_WORLD), "worldy");
		assertEquals(CArrays.removeDuplicateChars("     "), " ");
	}
}
