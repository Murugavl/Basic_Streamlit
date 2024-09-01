import streamlit as st
import pandas as pd
from PIL import Image
st.set_page_config(page_title='Murugavel App')
st.header("STREAMLIT")

st.subheader("Linear Regression")

st.latex("y=mx+c")

st.markdown("_With simple linear regression when we have a single input, we can use statistics to estimate the coefficients. This requires that you calculate statistical properties from the data such as means, standard deviations, correlations and covariance.  All of the data must be available to traverse and calculate statistics._")
# we can change the text which we given in the markdown

st.text("Just like a text")
# we cannot change the text which we given in the text

st.caption("Just a caption")

st.code('''for i in range(1,5):
    print(vel)''',language="java")
#in the code function we can declare our code 

st.markdown("_HOMPRICES DATASET_")
df=pd.read_csv("homeprices.csv")
st.dataframe(df)
# if we use dataset in the dataframe function we select,download

st.text("IN TABLE FORMAT")
st.table(df)
# if we use dataset in the table function we cannnot do anything as we do in the dataframe function

st.markdown("JSON FILE")
json={'a':[1,2,3],'b':[23,2,4]}
st.json(json)

st.markdown("_METRIC_")
col1,col2=st.columns(2)
with col1:
    st.metric("AAPL","$40",'+4%')
with col2:
    st.metric("ASDF","$203","-43%")


st.markdown("_INPUT WIDGETS_")
submit=st.button("Submit")
# button function is used for the button option in app

if submit:
    st.dataframe(df)
    st.radio("Choose one:",('a','b','c'))
    # radio functio is used for the radio button actions
# if we use button() to get the input from the user then if the click the radio button means the dataframe will disappear
# in that case we use the checkbox()

submit=st.checkbox("Submit")
if submit:
    st.dataframe(df)
    st.radio("Choose one:",('a','b','c'))

st.markdown("_SELECT BOX_")
cols=list(df.columns)
name=st.selectbox("Choose a feature:",cols)
# selectbox is used for select a option in drop down menu
st.write("The selectd column is :",name)

if name=='price':
    st.write(df['price'])
elif name=='area':
    st.write(df['area'])
else:
    st.write(df['town'])

st.markdown("_NUMBER INPUT_")
col1,col2=st.columns(2)

with col1:
    a= st.number_input("Enter a 1st number:")
with col2:
    b= st.number_input("Enter a 2nd number:")
submit=st.button('ADD')
if submit:
    st.write("The Addition of two numbers is:",a+b)

st.markdown("_SLIDER INPUT_")
col3,col4=st.columns(2)

with col3:
    a1= st.slider("Enter a 1st number:")
with col4:
    b1= st.slider("Enter a 2nd number:")
submit1=st.checkbox('ADD')
if submit1:
    st.write("The Addition of two numbers is:",a1+b1)

st.write("_MULTIPLE SELECTING_")
option=st.multiselect('choose your variable',cols)
st.write('your selection:',option)

st.markdown("_IMAGE SHOWING_")
submit=st.checkbox('show image')
if submit:
    img=Image.open("image.jpg")
    st.image(img)

st.markdown("_VIDEO SHOWING_")
submit=st.checkbox("show video")
if submit:
    vid=open("video.mp4",'rb')
    st.video(vid,format='video/mp4')

st.markdown("_AUDIO SHOWING_")
submit=st.checkbox("play audio")
if submit:
    aud=open("song.mp3",'rb')
    st.audio(aud,format='Audio/mp3')


# graph
# st.markdown("_PLOTLY CHARTS_")
# df1=pd.read_excel("Cotton_Purchase_Details.xlsx")

# st.dataframe(df1.head())

# columns=list(df1.columns)
# target=st.selectbox("Choose a target",columns)
# col2=columns.copy()
# col2.remove(target)

# x_var=st.selectbox("Choose a X variable ",col2)
# y_var=st.selectbox("Choose a y variable ",col2)

# st.markdown("_SCATTER PLOT_")
# fig=px.scatter(df1,x=x_var,y=y_var,color=target)
# st.plotly_chart(fig)


# data=pd.DataFrame(np.random.randn(100,3),columns=['A','B','C'])
# st.markdown("_LINE CHART_")
# st.line_chart(data,use_container_width=True)

# st.markdown("_BAR CHART_")
# st.bar_chart(data,use_container_width=True)

# st.markdown("_AREA CHART_")
# st.area_chart(data,use_container_width=True)

# st.text("STATUS ELEMENTS")

# st.success("This is a success element.")

# st.info("This is a info elements.")

# st.warning("This is a warning element.")

# st.error("This is a error element.")

# st.exception("This is a exception element.")