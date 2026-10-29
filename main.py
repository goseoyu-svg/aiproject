import streamlit as st
st.title('김서율똥!')
a=st.text_input('이름써')
b=st.selectbox('좋아하는 음식 선택',['김서율똥','마라탕','엽떡','허니콤보','공차','율똥'])
if st.button('인사말생성'):
 st.write('반갑티비')
