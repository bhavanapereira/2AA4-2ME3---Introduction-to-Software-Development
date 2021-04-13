## @file test_driver.py
#  @author Your Name
#  @brief Tests implementation of SeqServicesLibrary and SetOfInt ADT
#  @date 03/04/2021

from SeqServicesLibrary import *
from SetOfInt import *

from itertools import permutations 

from pytest import *

## @brief Tests functions from SeqServicesLibrary.py
class TestSeqServices:

    # Test max_val
    def test_max_empty(self):
        with raises(ValueError):
            max_val([])

    def test_max_first(self):
        assert max_val([17, 15, -1]) == 17

    def test_max_last(self):
        assert max_val([1, 15, 17]) == 17

    def test_max_neg_val_first(self):
        assert max_val([-17, 15, -1]) == 17
                
    def test_max_neg_val_last(self):
        assert max_val([1, 15, -17]) == 17

    def test_max_repeated(self):
        assert max_val([-17, -17, 17]) == 17
        
    def test_max_one_element_list(self):
        assert max_val([-17]) == 17

    # Test count
    def test_count_empty(self):
        with raises(ValueError):
            count(5, [])

    def test_count_no_occurrences(self):
        assert count(0, [17, 17, -1]) == 0
        
    def test_count_one_occurrence(self):
        assert count(17, [17, -1, -1]) == 1

    def test_count_max_occurrence(self):
        assert count(-1, [-1, -1, -1]) == 3

    # Test spices    
    def test_spices_empty(self):
        with raises(ValueError):
            spices([])

    def test_spices_nutmeg(self):
        assert spices([-1, 0]) == ["nutmeg", "nutmeg"]

    def test_spices_nutmeg_largeNeg(self):
        assert spices([-1000, -10000]) == ["nutmeg", "nutmeg"]
        
    def test_spices_ginger(self):
        assert spices([17, 1]) == ["ginger", "ginger"]

    def test_spices_ginger_largePositive(self):
        assert spices([1000, 10000]) == ["ginger", "ginger"]
        
    def test_spices_both(self):
        assert spices([17, 0]) == ["ginger", "nutmeg"]

    def test_spices_singleton(self):
        assert spices([10]) == ["ginger"]

    def test_spices_large_seq(self):
        assert spices([-15, -10, -5, 0, 5, 10, 15]) == ["nutmeg", "nutmeg", "nutmeg", "nutmeg", "ginger", "ginger", "ginger"]
        
    # Test new_max_val    
    def test_new_empty(self):
        with raises(ValueError):
            new_max_val([], lambda x: x > 10)
            
    def test_new_empty_after_filter(self):
        with raises(ValueError):
            new_max_val([-1, -1, -1], lambda x: x > 10)

    def test_new_one_occurrence(self):
        assert new_max_val([17, 0], lambda x: x > 10) == 17
        
    def test_new_multiple_occurrence(self):
        assert new_max_val([17, 11, -9, 8], lambda x: x > 10) == 17

    def test_new_max_occurrence(self):
        assert new_max_val([17, 17, 17, 17], lambda x: x > 10) == 17

    def test_new_max_no_filter(self):
        assert new_max_val([-17, 1, 9, 16], lambda x: True) == 17


## @brief Tests functions from SetOfInt.py
class TestSetOfInt:

    # Test constructor and to_seq
    def test_constructor_empty(self):
        x = []
        S = SetOfInt(x)
        assert S.to_seq() == []

    def test_constructor_no_repeats(self):
        x = [1, 2, 3, 4]
        S = SetOfInt(x)
        y = tuple(S.to_seq())
        assert (y in permutations(x)) #in case output in different order

    def test_constructor_repeats(self):
        x = [1, 4, 4, 4]
        S = SetOfInt(x)
        assert (S.to_seq() == [1, 4]) or (S.to_seq() == [4, 1])

    # Test is_member
    def test_member_true(self):
    	x = [-1, -2, -3, 4, 5, 6]
    	S = SetOfInt(x)
    	assert S.is_member(-3)

    def test_member_false(self):
    	x = [-1, -2, -3, 4, 5, 6]
    	S = SetOfInt(x)
    	assert not(S.is_member(3))

    # Test union
    def test_union_both_empty(self):
    	S1 = SetOfInt([])
    	S2 = SetOfInt([])
    	S3 = S1.union(S2)
    	assert S3.to_seq() == []

    def test_union_fst_empty(self):
    	x = [-1, 2, 3]
    	S1 = SetOfInt([])
    	S2 = SetOfInt(x)
    	S3 = S1.union(S2)
    	y = tuple(S3.to_seq())
    	assert (y in permutations(x))

    def test_union_snd_empty(self):
    	x = [-1, 2, 3]
    	S1 = SetOfInt(x)
    	S2 = SetOfInt([])
    	S3 = S1.union(S2)
    	y = tuple(S3.to_seq())
    	assert (y in permutations(x))

    def test_union_disjoint(self):
    	x = [-1, -3]
    	y = [1, 3]
    	S1 = SetOfInt(x)
    	S2 = SetOfInt(y)
    	S3 = S1.union(S2)
    	z = tuple(S3.to_seq())
    	assert (z in permutations(x+y))

    def test_union_not_disjoint(self):
    	x = [-1, -3, 2]
    	y = [2, 1, 3]
    	S1 = SetOfInt(x)
    	S2 = SetOfInt(y)
    	S3 = S1.union(S2)
    	z = tuple(S3.to_seq())
    	assert (z in permutations([-1, -3, 2, 1, 3]))

    def test_union_same_sets(self):
    	x = [-1, -3, 2]
    	S1 = SetOfInt(x)
    	S2 = SetOfInt(x)
    	S3 = S1.union(S2)
    	y = tuple(S3.to_seq())
    	assert (y in permutations(x))

# Test diff
    def test_diff_both_empty(self):
    	S1 = SetOfInt([])
    	S2 = SetOfInt([])
    	S3 = S1.diff(S2)
    	assert S3.to_seq() == []

    def test_diff_fst_empty(self):
    	x = [-1, 2, 3]
    	S1 = SetOfInt([])
    	S2 = SetOfInt(x)
    	S3 = S1.diff(S2)
    	assert S3.to_seq() == []

    def test_diff_snd_empty(self):
    	x = [-1, 2, 3]
    	S1 = SetOfInt(x)
    	S2 = SetOfInt([])
    	S3 = S1.diff(S2)
    	y = tuple(S3.to_seq())
    	assert (y in permutations(x))

    def test_diff_disjoint(self):
    	x = [-1, -3]
    	y = [1, 3]
    	S1 = SetOfInt(x)
    	S2 = SetOfInt(y)
    	S3 = S2.diff(S1)
    	z = tuple(S3.to_seq())
    	assert (z in permutations(y))

    def test_diff_not_disjoint_x_y(self):
    	x = [-1, -3, 2]
    	y = [2, 1, 3]
    	S1 = SetOfInt(x)
    	S2 = SetOfInt(y)
    	S3 = S1.diff(S2)
    	z = tuple(S3.to_seq())
    	assert (z in permutations([-1, -3]))

    def test_diff_not_disjoint_y_x(self):
    	x = [-1, -3, 2]
    	y = [2, 1, 3]
    	S1 = SetOfInt(x)
    	S2 = SetOfInt(y)
    	S3 = S2.diff(S1)
    	z = tuple(S3.to_seq())
    	assert (z in permutations([1, 3]))

    def test_diff_same_sets(self):
    	x = [-1, -3, 2]
    	S1 = SetOfInt(x)
    	S2 = SetOfInt(x)
    	S3 = S1.diff(S2)
    	assert S3.to_seq() == []

    #Test size
    def test_size_empty(self):
    	S = SetOfInt([])
    	assert (S.size() == 0)

    def test_size_not_empty(self):
    	S = SetOfInt([1, 2, 3, 4, 5, 6, 7, 8, 9])
    	assert (S.size() == 9)

    #Test empty
    def test_empty_empty(self):
    	S = SetOfInt([])
    	assert (S.empty())

    def test_empty_not_empty(self):
    	S = SetOfInt([1, 2, 3, 4, 5, 6, 7, 8, 9])
    	assert (not(S.empty()))

    #Test equals
    def test_equals_both_empty_s1s2(self):
    	S1 = SetOfInt([])
    	S2 = SetOfInt([])
    	assert S1.equals(S2)

    def test_equals_both_empty_s2s1(self):
    	S1 = SetOfInt([])
    	S2 = SetOfInt([])
    	assert S2.equals(S1)

    def test_equals_fst_empty_s1s2(self):
    	x = [-1, 2, 3]
    	S1 = SetOfInt([])
    	S2 = SetOfInt(x)
    	assert not(S1.equals(S2))

    def test_equals_fst_empty_s2s1(self):
    	x = [-1, 2, 3]
    	S1 = SetOfInt([])
    	S2 = SetOfInt(x)
    	assert not(S2.equals(S1))

    def test_equals_disjoint_s1s2(self):
    	x = [-1, -3]
    	y = [1, 3]
    	S1 = SetOfInt(x)
    	S2 = SetOfInt(y)
    	assert not(S1.equals(S2))

    def test_equals_disjoint_s2s1(self):
    	x = [-1, -3]
    	y = [1, 3]
    	S1 = SetOfInt(x)
    	S2 = SetOfInt(y)
    	assert not(S2.equals(S1))

    def test_equals_not_disjoint_s1s2(self):
    	x = [-1, -3, 2]
    	y = [2, 1, 3]
    	S1 = SetOfInt(x)
    	S2 = SetOfInt(y)
    	assert not(S1.equals(S2))

    def test_equals_not_disjoint_s2s1(self):
    	x = [-1, -3, 2]
    	y = [2, 1, 3]
    	S1 = SetOfInt(x)
    	S2 = SetOfInt(y)
    	assert not(S2.equals(S1))

    def test_equals_same_sets_s1s2(self):
    	x = [-1, -3, 2]
    	S1 = SetOfInt(x)
    	S2 = SetOfInt(x)
    	assert S1.equals(S2)

    def test_equals_same_sets_s2s1(self):
    	x = [-1, -3, 2]
    	S1 = SetOfInt(x)
    	S2 = SetOfInt(x)
    	assert S2.equals(S1)