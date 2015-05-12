package arrays;

import static org.junit.Assert.*;

import org.junit.Test;

public class CArraysTest {

	@Test
	public void testsHasAllUniqueChars() {
		assertTrue(CArrays.hasAllUniqueChars("Thequickbrown"));
		assertTrue(CArrays.hasAllUniqueChars("Lazy123"));
		assertTrue(CArrays.hasAllUniqueChars("$12450"));
		assertFalse(CArrays.hasAllUniqueChars("Humpy dumpty"));
		assertFalse(CArrays.hasAllUniqueChars("wordlyworld"));
		assertFalse(CArrays.hasAllUniqueChars("#$#Money"));
	}
}
