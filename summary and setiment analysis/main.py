import tkinter as tk
import nltk
from textblob import TextBlob
from  newspaper import Article

def summarize():
    url = utext.get('1.0','end').strip()

    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    title.config(state='normal')
    Author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    semtiment.config(state='normal')

    title.delete('1.0','end')
    title.insert('1.0',article.title)

    Author.delete('1.0','end')
    Author.insert('1.0',article.authors)

    publication.delete('1.0','end')
    publication.insert('1.0',article.publish_date)

    summary.delete('1.0','end')
    summary.insert('1.0',article.text)

    analysis = TextBlob(article.text)
    semtiment.delete('1.0','end')
    semtiment.insert("1.0",f"polarity : {analysis.polarity}, sentiment : {'positive' if analysis.polarity > 0 else 'negative' if analysis.polarity < 0 else 'neutral'}")

    title.config(state='disabled')
    Author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    semtiment.config(state='disabled')



root = tk.Tk()
root.title("news summarizer")
root.geometry("1200x600")

tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1 ,width=140)
title.config(state="disabled")
title.pack()

alabel = tk.Label(root, text='Author')
alabel.pack()

Author = tk.Text(root, height=1 ,width=140)
Author.config(state="disabled")
Author.pack()

plabel = tk.Label(root, text='publishing date')
plabel.pack()

publication = tk.Text(root, height=1 ,width=140)
publication.config(state="disabled")
publication.pack()

slabel = tk.Label(root, text='summary')
slabel.pack()

summary = tk.Text(root, height=20 ,width=140)
summary.config(state="disabled")
summary.pack()

selabel = tk.Label(root, text='Sentiment analysis')
selabel.pack()

semtiment = tk.Text(root, height=1 ,width=140)
semtiment.config(state="disabled")
semtiment.pack()

ulabel = tk.Label(root, text='URL')
ulabel.pack()

utext = tk.Text(root, height=1 ,width=140)
utext.pack()

btn = tk.Button(root, text='Summarize' , command=summarize)
btn.pack()






root.mainloop()