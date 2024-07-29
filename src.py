import folium.elements
import pandas as pd
import folium
import urllib.request, json
import requests

df = pd.read_csv('./datas/processed.csv')

loc = [36.16260, 127.4619] #금산구 위도 경도
colors = ['green', 'blue', 'gray', 'red', 'purple', 'pink', 'darkblue']

# 맵 , 마커 생성
m = folium.Map(location=loc, zoom_start=10)   

folium.Marker(
    location=loc,
    tooltip="금산군",
    popup="금산군",
    icon=folium.Icon(color="beige", icon="star"),
).add_to(m)

# 소개 ( popup ) 짧게
def shorten_string(input_string, limit=140):
    if len(input_string) > limit:
        return input_string[:limit] + '...'
    else:
        return input_string
    
# 금산군 문화재 위치 추가

eras = list(df['시대'].unique())
e = 0
for i, row in df.iterrows(): #i = index int, row = 내용
    
    e = eras.index(row['시대']) #시대별 색상 지정 인덱싱
    c = colors[e] #시대별 색상 지정
    
    folium.Marker(
        location= [ df['위도'][i], df['경도'][i] ],
        tooltip = df['문화재명'][i],
        popup= folium.Popup(shorten_string(df['소개'][i]), parse_html=True, max_width= 150),
        icon=folium.Icon(color=c, icon="circle")
    ).add_to(m)
    
legend_tag = '''
    <div class="legend">
        <div class="content">
            <div class="bars elems">
                <div class="bar">조선 시대</div>
                <div class="bar">미제공</div>
                <div class="bar">삼국 시대</div>
                <div class="bar">고려 시대</div>
                <div class="bar">현대</div>
                <div class="bar">임시정부</div>
                <div class="bar">청동기</div>
            </div>
        </div>
    </div>
'''
<<<<<<< Updated upstream

m.get_root().header.add_child(folium.CssLink('style.css'))
=======
>>>>>>> Stashed changes
m.get_root().html.add_child(folium.Element(legend_tag))
m.get_root().html.add_child(folium.CssLink('./style.css'))
# 저장
m.save('index.html')