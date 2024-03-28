import streamlit as st
import numpy as np
from scipy.linalg import solve_banded

# Streamlit interface for input
st.title('Solve Banded Matrix System')

# Input fields for diagonals and RHS vector
st.subheader('Enter the diagonals of the matrix')
lower_diag = st.text_input('Lower diagonal (comma-separated values)', '1, 1')
main_diag = st.text_input('Main diagonal (comma-separated values)', '3, -1, 1')
upper_diag = st.text_input('Upper diagonal (comma-separated values)', '1, 3')
rhs_vector = st.text_input('Right-hand side vector (comma-separated values)', '1, 6, 1')

# Convert input strings to numpy arrays
try:
    lower_diag = np.fromstring(lower_diag, dtype=np.float64, sep=',')
    main_diag = np.fromstring(main_diag, dtype=np.float64, sep=',')
    upper_diag = np.fromstring(upper_diag, dtype=np.float64, sep=',')
    rhs_vector = np.fromstring(rhs_vector, dtype=np.float64, sep=',')

    # Check if dimensions match
    if len(main_diag) - 1 == len(lower_diag) == len(upper_diag) and len(main_diag) == len(rhs_vector):
        # Arrange the matrix in the required format for solve_banded
        ab = np.vstack((np.append(0, upper_diag), main_diag, np.append(lower_diag, 0)))
        
        # Solve the system
        solution = solve_banded((1, 1), ab, rhs_vector)
        
        # Display the solution
        st.subheader('Solution')
        st.write(solution)
    else:
        st.error('The lengths of the diagonals or the RHS vector do not match the expected sizes.')
except ValueError as e:
    st.error(f'Input error: {e}')

