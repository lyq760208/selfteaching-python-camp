#！/usr/bin/python
#-*-coding:UTF-8 -*-

import sys
sys.path.append('/Users/apple/Downloads/hello world/selfteaching-python-camp/exercises/1901090036/d07/mymodule/stats_word.py:/')
import mymodule.stats_word as stats_word

text1='''
愚公移山

太⾏，王屋⼆⼭的北⾯，住了⼀個九⼗歲的⽼翁，名叫愚公。⼆⼭佔地廣闊，擋住去路，使他 和家⼈往來極為不便。

⼀天，愚公召集家⼈說：「讓我們各盡其⼒，剷平⼆⼭，開條道路，直通豫州，你們認為怎 樣？」
⼤家都異⼝同聲贊成，只有他的妻⼦表示懷疑，並說：「你連開鑿⼀個⼩丘的⼒量都沒有，怎 可能剷平太⾏、王屋⼆⼭呢？況且，鑿出的⼟⽯⼜丟到哪裏去呢？」

⼤家都熱烈地說：「把⼟⽯丟進渤海裏。」
於是愚公就和兒孫，⼀起開挖⼟，把⼟⽯搬運到渤海去。
愚公的鄰居是個寡婦，有個兒⼦⼋歲也興致勃勃地⾛來幫忙。
寒來暑往，他們要⼀年才能往返渤海⼀次。

住在⿈河河畔的智叟，看⾒他們這樣⾟苦，取笑愚公說：「你不是很愚蠢嗎？你已⼀把年紀 了，就是⽤盡你的氣⼒，也不能挖去⼭的⼀⻆呢？」

愚公歎息道：「你有這樣的成⾒，是不會明⽩的。你⽐那寡婦的⼩兒⼦還不如呢！就算我死 了，還有我的兒⼦，我的孫⼦，我的曾孫⼦，他們⼀直傳下去。⽽這⼆⼭是不會加⼤的，總有 ⼀天，我們會把它們剷平。」

智叟聽了，無話可說：
⼆⼭的守護神被愚公的堅毅精神嚇倒，便把此事奏知天帝。天帝佩服愚公的精神，就命兩位⼤ ⼒神揹⾛⼆⼭。

How The Foolish Old Man Moved Mountains

Yugong was a ninety-year-old man who lived at the north of two high mountains, Mount Taixing and Mount Wangwu.

Stretching over a wide expanse of land, the mountains blocked yugong's way making it inconvenient for him and his family to get around.
One day yugong gathered his family together and said,"Let's do our best to level these two mountains. We shall open a road that leads to Yuzhou. What do you think?"

All but this wife agreed with him. 
"You don't have the strength to cut even a small mound,"muttered his wife. "How on earth do you suppose you can level Mount Taixin and Mount Wanwu? Moreover, where will alll the earth and rubble go?"
"Dump them into the sea of Bohai!"said everyone. 

Now Yugong's neighbour was a widow who had an only child eight years old. Evening the young boy offered his help eagerly.

Summer went by and winter came. It took Yugong and his crew a full year to travel back and forth once. 

On the bank of the yellow river dwelled an old man much respected for his wisdom. when he saw their back-breaking labour,he ridiculed yugong saying, “Aren't you foolish, my friend? you are very old now, and with whatever remains of your waning strength, you won't be able to remove even a corner of the mountain."

Yugong uttered a sigh and said,"A biased person like you will never understand. you can't even compare with the widow's little boy!"

"Even is i were dead, there will still be my children , my grandchildren, my great grandchildren. they descendants will go on forever. but these mountains will not grow any taler. we shall level them one day!" he declared with confidence.

The wise old man was totally silenced. 
When the guardian gods of the mountains saw how determined Yugong and his crew were,they were struck with fear and reported the incident to the emperor of heavens.

Filled with admiration for yugong, the emperor if heavens ordered two mighty gods to carry the mountains away. 
'''
def stats_text(text1):
    global counter
    counter=stats_word.stats_text(text1)
    print(counter)