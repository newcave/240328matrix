import streamlit as st
import numpy as np

st.title('Tridiagonal Matrix Solver')

# Input fields for the diagonals and the solution vector
st.subheader('Enter the diagonals and the solution vector')
b_input = st.text_input('Main Diagonal (comma-separated, e.g. "5, 6, 6, 6, 6, 6, 6, 6, 5")', '5, 6, 6, 6, 6, 6, 6, 6, 5')
a_input = st.text_input('Lower Diagonal (comma-separated, starts with 0)', '0, 1, 1, 1, 1, 1, 1, 1, 1')
c_input = st.text_input('Upper Diagonal (comma-separated, ends with 0)', '1, 1, 1, 1, 1, 1, 1, 1, 0')
d_input = st.text_input('Solution Vector (comma-separated)', '3, 2, 1, 3, 1, 3, 1, 2, 3')

# Convert input strings to numpy arrays
b = np.fromstring(b_input, sep=',', dtype=float)
a = np.fromstring(a_input, sep=',', dtype=float)
c = np.fromstring(c_input, sep=',', dtype=float)
d = np.fromstring(d_input, sep=',', dtype=float)

if len(b) == len(a) == len(c) == len(d):
    n = len(d)
    # Create the matrix A from diagonals
    A = np.zeros((n, n))
    for i in range(n):
        A[i, i] = b[i]
        if i < n - 1:
            A[i, i + 1] = c[i + 1]
            A[i + 1, i] = a[i]

    # Display the matrix A and vector B
    st.subheader('Matrix A (constructed from input diagonals)')
    st.write(A)

    st.subheader('Vector B (Solution Vector)')
    st.write(d)

    # Solve the system using the provided algorithm
    newC = np.zeros(n, dtype=float)
    newD = np.zeros(n, dtype=float)
    x = np.zeros(n, dtype=float)

    newC[0] = c[0] / b[0]
    newD[0] = d[0] / b[0]
    for i in range(1, n):
        newC[i] = c[i] / (b[i] - a[i] * newC[i - 1])
        newD[i] = (d[i] - a[i] * newD[i - 1]) / (b[i] - a[i] * newC[i - 1])

    x[n - 1] = newD[n - 1]
    for i in reversed(range(n - 1)):
        x[i] = newD[i] - newC[i] * x[i + 1]

    # Solve using np.linalg.solve for comparison
    sol = np.linalg.solve(A, d)

    # Display the computed solution and comparison
    st.subheader('Computed Solution')
    st.write(x)
    
#    st.subheader('NumPy Solution for Comparison')
#    st.write(sol)
else:
    st.error('The lengths of the diagonals or the solution vector do not match the expected sizes. Please ensure all inputs have correct lengths.')
