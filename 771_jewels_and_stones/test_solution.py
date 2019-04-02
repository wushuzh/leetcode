import pytest
import hypothesis as ht
import hypothesis.strategies as st
import random

from solution import num_jewels_in_stones_v1

# totally 100 distinct chars

# https://en.wikipedia.org/wiki/ASCII#Printable_characters
# there are 95 printable chars in ASCII
min_prt_ascii_codepoint = ord(' ')  # space
max_prt_ascii_codepoint = ord('~')  # tilde

#  https://en.wikipedia.org/wiki/Greek_alphabet#Greek_in_Unicode
#   upper case range 0x0391 - 0x03A1, 0x03A3 - 0x03A9
#   lower case range 0x03B1 - 0x03C1, 0x03C3 - 0x03C9
# I select a few greek alphabet, appearance must do not look like ascii at all
# http://kestrel.nmt.edu/~raymond/software/howtos/greekscape.xhtml
# 3rd Greek char
upper_gamma = chr(int('0x0393', 16))  # 'Γ'
lower_gamma = chr(int('0x03B3', 16))  # 'γ'
# 4th Greek char
upper_delta = chr(int('0x0394', 16))  # 'Δ'
lower_delta = chr(int('0x03B4', 16))  # 'δ'
# 24th Greek char
upper_omega = chr(int('0x03A9', 16))  # 'Ω'
lower_omega = chr(int('0x03C9', 16))  # 'ω'
extra_charset = upper_gamma + lower_gamma + upper_delta + lower_delta + upper_omega + lower_omega


@st.composite
def jewels_stones_jcount_data(draw):
    # jewels
    js = draw(
        st.lists(
            st.characters(
                min_codepoint=min_prt_ascii_codepoint,
                max_codepoint=min_prt_ascii_codepoint + 50),
            max_size=50))
    count = len(js)
    # stones are generated from another not-overlapping charset
    plain_stones = draw(
        st.lists(
            st.characters(
                min_codepoint=min_prt_ascii_codepoint + 51,
                max_codepoint=max_prt_ascii_codepoint,
                whitelist_characters=extra_charset),
            max_size=50 - count))
    mix = js + plain_stones
    random.shuffle(mix)
    return (''.join(js), ''.join(mix), count)


@ht.given(jsc=jewels_stones_jcount_data())
def test_with_ascii(jsc):
    js, ss, c = jsc
    assert num_jewels_in_stones_v1(js, ss) == c
