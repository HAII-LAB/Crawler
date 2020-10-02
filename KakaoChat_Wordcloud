from wordcloud import WordCloud

text = ""

with open("kakaotalk.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        if '] [' in line:
            text += line.split('] ')[2].replace('ㅋ','').replace('ㅠ','').replace('ㅜ','').replace('사진\n','').replace('이모티콘\n','').replace('삭제된 메시지입니다','')

font_path = 'C:/Windows/Fonts/gulim.ttc'

wc = WordCloud(font_path=font_path, background_color="white", width=600, height=400)
wc.generate(text)
wc.to_file("result.png")
