from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new_posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    cover_img = db.Column(db.String(250), nullable=False)
    description = db.Column(db.Text, nullable=False)
    page_img = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    lenght = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(250), unique=False, nullable=False)
# db.create_all()


post1 = BlogPost(
    title='デスノート Death Note',
    subtitle=' is a Japanese manga series written by Tsugumi Ohba and illustrated by Takeshi Obata.',
    cover_img='https://images.hdqwalls.com/download/death-note-manga-series-6f-1152x864.jpg',
    page_img='https://mobwallpapershd.com/wp-content/uploads/2021/06/Death-Note-Wallpapers-5-576x1024.jpg',
    description="The story follows Light Yagami, a teen genius who discovers a mysterious notebook: the "
                "'Death Note', which belonged to the Shinigami Ryuk, and grants the user the supernatural "
                "ability to kill anyone whose name is written in its pages. The series centers around Light's "
                "subsequent attempts to use the Death Note to carry out a worldwide massacre of individuals "
                "whom he deems immoral and to create a crime-free society, using the alias of a god-like "
                "vigilante named 'Kira', and the subsequent efforts of an elite Japanese police task force, "
                "led by enigmatic detective L, to apprehend him. Death Note ran in Shueisha's manga magazine"
                " Weekly Shōnen Jump from December 2003 to May 2006. Its 108 chapters were collected in 12 "
                "tankōbon volumes.",
    rating=9,
    lenght=5,
    type='fi'
)

post2 = BlogPost(
    title="Howl's Moving Castle ハウルの動く城",
    subtitle=' is a 2004 Japanese animated fantasy film written and directed by Hayao Miyazaki. It is loosely based on '
             'the 1986 novel of the same name by English author Diana Wynne Jones.',
    page_img='https://images6.alphacoders.com/739/739951.png',
    cover_img='https://w0.peakpx.com/wallpaper/160/415/HD-wallpaper-howl-anime-howl-pendragon-howls-moving-castle-studio-ghibli.jpg',
    description="The film is set in a fictional kingdom where both magic and early twentieth-century technology"
                " are prevalent, against the backdrop of a war with another kingdom. It tells the story of Sophie,"
                " a young milliner who is turned into an elderly woman by a witch who enters her shop and curses "
                "her. She encounters a wizard named Howl and gets caught up in his resistance to fighting for the king. "
                "Influenced by Miyazaki's opposition to the United States' invasion of Iraq in 2003, the film contains "
                "strong anti-war themes. Miyazaki stated that he 'had a great deal of rage' about the Iraq war, which "
                "led him to make a film which he felt would be poorly received in the United States. It also explores "
                "the theme of old age, depicting age positively as something which grants the protagonist freedom. "
                "The film contains feminist elements as well, and carries messages about the value of compassion.",
    rating=8,
    lenght=5,
    type='fi'
)

post3 = BlogPost(
    title='One-Punch Man ワンパンマン',
    subtitle='is a Japanese superhero manga series created by One. It tells the story of Saitama, '
             'a superhero who, because he can defeat any opponent with a single punch',
    cover_img='https://i.pinimg.com/originals/26/e5/ba/26e5ba4e44a69faf122a8f859ff811a9.jpg',
    page_img='https://c4.wallpaperflare.com/wallpaper/1006/84/906/anime-one-punch-man-garou-one-punch-man-moon-night-hd-wallpaper-preview.jpg',
    description="A digital manga remake began publication on Shueisha's Tonari no Young Jump website in June 2012. "
                "Written by One and illustrated by Yusuke Murata, its chapters are periodically compiled and "
                "published into individual tankōbon volumes. As of June 2022, 26 volumes have been released. "
                "In North America, Viz Media has licensed the remake manga for English language release and "
                "has serialized it in its Weekly Shonen Jump digital magazine. An anime adaptation produced "
                "by Madhouse was broadcast in Japan from October to December 2015. A second season, produced "
                "by J.C.Staff, was broadcast from April to July 2019. Licensed in North America by Viz Media, "
                "it premiered in the United States on Adult Swim's Toonami programming block in July 2016. "
                "The second season premiered in October 2019.",
    rating=7,
    lenght=4,
    type='fi'
)

post4 = BlogPost(
    title='The Garden of Words 言の葉の庭',
    subtitle='is a 2013 Japanese anime drama film written, directed and edited by Makoto Shinkai, animated by CoMix Wave Films and distributed by Toho.',
    cover_img='http://www.ty4k.cn/wp-content/uploads/2020/07/A077.jpg',
    page_img='https://images-na.ssl-images-amazon.com/images/I/91a61kAtRXL.jpg',
    description="The film focuses on Takao Akizuki, an aspiring 15-year-old shoemaker, and Yukari Yukino, a mysterious 27-year-old woman he keeps meeting at Shinjuku Gyoen National Garden on rainy mornings. While Takao is skipping his morning class to design shoes, Yukari is avoiding work due to personal problems in her professional life. Yukari tells Takao nothing about herself, including her name, while Takao opens up to her, sharing his passion for shoes by offering to make a pair for her. When Takao learns Yukari's identity, emotions come to a head as both learn that they have been teaching each other 'how to walk'. Shinkai wrote the story as a tale of 'lonely sadness', based on the meaning of the traditional Japanese word for 'love', and uses shoes as a metaphor for life. The story's motifs include rain, Man'yōshū poetry, and the Japanese garden. The age difference between the two main characters and their character traits demonstrate how awkwardly and disjointedly people mature, where even adults sometimes feel no more mature than teenagers, according to Shinkai.",
    rating=10,
    lenght=3,
    type='fi'
)

post5 = BlogPost(
    title='Spirited Away 千と千尋の神隠し',
    subtitle=' is a 2001 Japanese animated fantasy film written and directed by Hayao Miyazaki, animated by Studio Ghibli for Tokuma Shoten, Nippon Television Network, Dentsu, Buena Vista Home Entertainment, Tohokushinsha Film, and Mitsubishi and distributed by Toho.',
    cover_img='https://i.pinimg.com/originals/3c/7f/12/3c7f12426d3dad2ba4539b8a9cae9a89.jpg',
    page_img='https://www.whatspaper.com/wp-content/uploads/2021/12/spirited-away-wallpaper-whatspaper-9.jpg',
    description="The film features the voices of Rumi Hiiragi, Miyu Irino, Mari Natsuki, Takeshi Naito, Yasuko Sawaguchi, Tsunehiko Kamijō, Takehiko Ono, and Bunta Sugawara. Spirited Away tells the story of Chihiro Ogino (Hiiragi), a ten-year-old girl who, while moving to a new neighborhood, enters the world of Kami (spirits of Japanese Shinto folklore).[8] After her parents are turned into pigs by the witch Yubaba (Natsuki), Chihiro takes a job working in Yubaba's bathhouse to find a way to free herself and her parents and return to the human world.",
    rating=9,
    lenght=4,
    type='fi'
)


post6 = BlogPost(
    title='Hayao Miyazaki 宮崎 駿',
    subtitle='is a Japanese animator, director, producer, screenwriter, author, and manga artist. A co-founder of Studio Ghibli, he has attained international acclaim as a masterful storyteller and creator of Japanese animated feature films, and is widely regarded as one of the most accomplished filmmakers in the history of animation.',
    cover_img='https://c4.wallpaperflare.com/wallpaper/908/897/173/anime-studio-ghibli-hayao-miyazaki-wallpaper-preview.jpg',
    page_img='https://arthive.net/res/media/img/oy1200/article/543/287615@2x.jpg',
    description="Born in Bunkyō ward of Tokyo, Miyazaki expressed interest in manga and animation from an early age, and he joined Toei Animation in 1963. During his early years at Toei Animation he worked as an in-between artist and later collaborated with director Isao Takahata. Notable films to which Miyazaki contributed at Toei include Doggie March and Gulliver's Travels Beyond the Moon. He provided key animation to other films at Toei, such as Puss in Boots and Animal Treasure Island, before moving to A-Pro in 1971, where he co-directed Lupin the Third Part I alongside Takahata. After moving to Zuiyō Eizō (later known as Nippon Animation) in 1973, Miyazaki worked as an animator on World Masterpiece Theater, and directed the television series Future Boy Conan (1978). He joined Tokyo Movie Shinsha in 1979 to direct his first feature film The Castle of Cagliostro as well as the television series Sherlock Hound. In the same period, he also started writing and illustrating the manga Nausicaä of the Valley of the Wind (1982–1994), and he also directed the 1984 film adaptation produced by Topcraft.",
    rating=10,
    lenght=5,
    type='pe'
)

db.session.add(post1)
db.session.commit()