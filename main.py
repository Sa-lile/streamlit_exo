import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.subheader('This is a Streamlit & Python création ', divider='rainbow')
st.title('Streamlit is :blue[cool] :sunglasses:')

st.markdown("***Interactive Widgets*** &mdash;\
            :tulip::cherry_blossom::rose:")

text = st.text_input(
    'What is your hobby?',
)
'My hobby is ', text,


option = st.selectbox(
    'Which number do you like ?',
    list(range(1, 11))
)
'My favorite number is ', option,

with st.expander("Question1"):
    st.write('Answer1')
with st.expander("Question2"):
    st.write('Answer2')

with st.form("my_form"):
   st.write("Inside the form")
   my_number = st.slider('Pick a number', 1, 10)
   my_color = st.selectbox('Pick a color', ['red','orange','green','blue','violet'])
   st.form_submit_button('Submit my picks')

# This is outside the form
st.write(my_number)
st.write(my_color)


# st.write('')
st.markdown("***Display image*** &mdash;\
            :hibiscus::sunflower::blossom:")

if st.checkbox('show Image'):
    img = Image.open('sakura_mt.fuji.jpg')
    st.image(img, caption='sakura & Mt.Fuji', use_column_width=True)

# Latitude et longitude de Tokyo
df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon'],
)
# Latitude et longitude de Toulouse
# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [43.60, 1.44],
#     columns=['lat', 'lon'],
# )
st.map(df, size=30, color='#84abb5')

# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )

# must be version 11.0.0 or greater. Found version 9.0.0
# st.line_chart(df) 
# st.bar_chart(df) 
# st.area_chart(df)

# df = pd.DataFrame({
#     '1': [1, 2, 3, 4],
#     '2': [10, 20, 30, 40],
# })


# st.dataframe(df.style.highlight_max(axis=0))

# st.table(df.style.highlight_max(axis=0))


# """
# #  Lorem
# ## Lorem
# ### Lorem

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """
