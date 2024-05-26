import streamlit as sl
import pickle
import pandas as pd
import time
similarity=pickle.load(open("similarity.pkl",'rb'))
def recommend(movie):
    index = movies_list[movies_list['title'] == movie].index[0]
    # distances=similarity[index]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    l=[]
    for i in distances[1:6]:
        l.append(movies_list.iloc[i[0]].title)
    return l

movies_list_dict=pickle.load(open("movie_list_to_dict.pkl",'rb'))
movies_list=pd.DataFrame(movies_list_dict)
sl.title("Movies Recommender System")
#temp=sl.write("""##### Select Your Favourite Movie""")
sl.subheader(":blue[One point for your next binge watch]:sunglasses:")
option = sl.selectbox(
    "Select Your Favourite Movie",
    movies_list['title'].values)

sl.write("You selected:", option)
if sl.button("Recommend", type="primary"):
    sl.write("""#### Your Recommended Movies Are:
    """)
    time.sleep(3)
    result=recommend(option)
    for i in result:
        temp=i.upper()
        sl.write(temp)

