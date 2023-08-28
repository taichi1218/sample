import streamlit as st

st.title('売上可視化')
st.caption('売上を可視化するアプリです。')
st.subheader('サブヘッダー')
st.text('テキスト')

code = "これはコードです"

st.code(code, language='python')

with st.form(key='profile_form'):
    name = st.text_input('名前')
    address = st.text_input('住所')
    
    age_category = st.selectbox('年齢層', ('子ども(18歳未満)', '大人(18歳以上)'))
    
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    if submit_btn:
        st.text(f'ようこそ！{name}さん。{address}に書籍を送りました。')
        st.text(f'年齢層：{age_category}')