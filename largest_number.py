import streamlit as st

def main():
    st.title("Find the Largest Number")

    # Input fields for three numbers
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    # Find the largest number
    largest_number = max(num1, num2, num3)

    # Display the result
    if largest_number == num1 == num2 == num3:
        st.write("All numbers are equal.")
    else:
        st.write("The largest number is:", largest_number)

if __name__ == "__main__":
    main()
