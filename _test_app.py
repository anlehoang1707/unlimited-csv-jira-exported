import streamlit as st

# Initialize the key in session state
'''if 'clicked' not in st.session_state:
    st.session_state.clicked = {1:False,2:False}

# Function to update the value in session state
def clicked(button):
    st.session_state.clicked[button] = True

# Button with callback function
st.button('First Button', on_click=clicked, args=[1])

# Conditional based on value in session state, not the output
if st.session_state.clicked[1]:
    st.write('The first button was clicked.')
    st.button('Second Button', on_click=clicked, args=[2])
    if st.session_state.clicked[2]:
        st.write('The second button was clicked')
        
        '''
#----------------------------------------------------------       
import streamlit as st

# create a function that sets the value in state back to an empty list
def clear_multi():
    st.session_state.multiselect = []
    return

st.title("Clear multiselect with stateful button")

# create multiselect and automatically put it in state with its key parameter
multi = st.multiselect("Pick an option", ["a","b","c","d"], key="multiselect")

# check state
st.session_state

#create your button to clear the state of the multiselect
st.button("Clear multiselect", on_click=clear_multi)

#------------------------------------------

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def set_clicked():
    st.session_state.clicked = True

st.button('Button', on_click=set_clicked)
if st.session_state.clicked:
    options = st.multiselect('Choose letter', ['a', 'b', 'c'])
    st.write(options)
    
    
#---------------
import streamlit as st

def on_change_checkbox(filter_id):
    print(filter_id)

for i in range(0,10):
    #st.checkbox(str(i), on_change=on_change_checkbox(i))
    st.checkbox(str(i), on_change=on_change_checkbox, args=(i,))
    
mulittest = st.multiselect(label = "Multi test",options = [1,2,3,4,"hi"],key="multi_test")

print(type(mulittest)) 
print(mulittest)
st.write(type(mulittest))