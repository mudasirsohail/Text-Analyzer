import streamlit as st

def analyze_text(text):
    # Word and Character Count
    word_count = len(text.split())
    char_count = len(text)
    
    # Vowel Count
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)
    
    # Search and Replace
    search_word = st.text_input("Enter word to search:")
    replace_word = st.text_input("Enter word to replace with:")
    modified_text = text.replace(search_word, replace_word) if search_word else text
    
    # Uppercase and Lowercase Conversion
    uppercase_text = modified_text.upper()
    lowercase_text = modified_text.lower()
    
    # Operators
    contains_python = "python" in modified_text.lower()
    avg_word_length = char_count / word_count if word_count > 0 else 0
    
    # Display Results
    st.write(f"Total Words: {str(word_count)}")
    st.write(f"Total Characters: {str(char_count)}")
    st.write(f"Total Vowels: {str(vowel_count)}")
    st.write(f"Contains 'Python'?: {'Yes' if contains_python else 'No'}")
    st.write(f"Average Word Length: {avg_word_length:.2f}")
    
    st.subheader("Modified Text")
    st.write(modified_text)
    
    st.subheader("Uppercase Text")
    st.write(uppercase_text)
    
    st.subheader("Lowercase Text")
    st.write(lowercase_text)
    
# Streamlit UI
st.title("Text Analyzer")
text_input = st.text_area("Enter a paragraph:")
if text_input.strip():
    analyze_text(text_input)
else:
    st.warning("Please enter some text to analyze.")

st.write("-----")
st.write("Made with ❤️ by [Mudasir Sohail](https://www.linkedin.com/in/mudasir-sohail-98b399257/) ")
