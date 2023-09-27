from pathlib import Path
from streamlit_lottie import st_lottie

import requests
import streamlit as st
from PIL import Image

from streamlit_autorefresh import st_autorefresh



# ---- PATH SETTINGS ----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd
css_file = current_dir / "style" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "pic.png"



# ---- LOTTIE ANIMATION ----
def load_lottie(url):
	r = requests.get(url)
	if r.status_code != 200:
		return None
	return r.json()

pfp = load_lottie("https://lottie.host/912919eb-2c96-4d58-92b7-59c42fd5b854/rdiHoFXsFZ.json")
mail_anim = load_lottie("https://lottie.host/ec42a73a-f99c-49f9-937d-d8f70db818d7/bZCydEDqxG.json")
code_anim = load_lottie("https://lottie.host/880a7ca2-5837-4430-b897-494b22113f58/OTRjtwJ1XJ.json")



# ---- Genera; Settings -----------
# color = "#F5F5F5"
PAGE_TITLE = "Digital CV | Jayesh Jha"
PAGE_ICON = None
NAME = ":gray[Jayesh Nath Jha]"
Description= """
I am a recent CSE:computer: graduate... an aspiring Data Scientist with a good understanding of Data Analysis techniques, and keen interest in Machine Learning.
"""

EMAIL = ":e-mail: jayeshnathjha@gmail.com"
SOCIAL_MEDIA = {
	"LinkedIn" : "https://www.linkedin.com/in/jayesh-nath-jha/",
	"GitHub"   : "https://github.com/jayesh-jha",
	"LeetCode" : "https://leetcode.com/jayesh_jha/"
}

PROJECTS = {
	":video_game: AI Tic-Tac-Toe : A game of tic-tac-toe, powered by Minimax algorithm": "https://jayesh-jha.github.io/tic-tac-toe/",
	":cityscape: Bengauluru House Price Prediction : Using Linear Regression": "https://blr-house-price-prediction.onrender.com",
	":male-detective: Cybercrime Data Analysis of India: Year 2017 to 2021": "https://www.linkedin.com/in/jayesh-nath-jha/",
	":chart_with_upwards_trend: Crypto Analysis : Live Crypto-data analysis": "https://www.linkedin.com/in/jayesh-nath-jha/"
}



st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

st.markdown("""
        <style>
               .block-container {
                    padding-top: 5rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)


# ---- LOAD CSS, PDF & PROFILE PIC ----
with open(css_file) as f:
	st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
	PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)


# ---- HERO SECTION ----
with st.container():
	col1, col2, col3 = st.columns([1,2,1], gap="small")

	with col1:
		st_lottie(pfp, height=300, width=300)

	with col2:
		st.title(NAME)
		st.write(Description)
		st.download_button(
			label="Download Resume",
			data=PDFbyte,
			file_name=resume_file.name,
			mime="application/octet-stream",
		)
		st.write(EMAIL)




# ---- SOCIAL LINKS ----
with st.container():
	col_R, col_C, col_L = st.columns([1,2.5,1])
	with col_C:
		cols = st.columns(len(SOCIAL_MEDIA)+1)
		for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
			cols[index].write(f"[{platform}]({link})")





# ---- PROJECTS ----
with st.container():
	col_R, col_C, col_L = st.columns([1,5,1])
	with col_C:
		st.write("#")
		st.subheader("Projects")
		st.write("---")
		for project, link in PROJECTS.items():
			st.write(f"[{project}]({link})")

		st.write("##")




# ---- SKILLS ----
col4, col5 = st.columns(2, gap='small')
with col4:
	st.write("#")
	st.subheader("Skills")
	st.write("---")
	st.write(
		"""
		- Programming: Python (Scikit-learn, Pandas, NumPy), SQL, PostgreSQL
		- Data Visualization: Power BI, MS Excel, Plotly, Seaborn
		- Modeling: Logistic Regression, Linear Regression, Decision Trees
		"""
	)
with col5:
	st_lottie(code_anim, height=250)




# ---- EXPERIENCE & QUALIFICATIONS ----
with st.container():
	col_R, col_C, col_L = st.columns([1,5,1])
	with col_C:
		st.write("#")
		st.subheader("Experience & Qualifications")
		st.write(
		"""
		- Bachelor of Technology (2019-23)
		- Freelance:
			- 3 months of freelancing as a web developer; 
			- utilized p5 library of JavaScript, known for its emphasis on creative coding;
			- Fixed 75% of previously existing bugs.
		"""
		)
		st.write("#")




# ---- CONTACT SECTION ----
with st.container():
	st.header("Get In Touch With Me!")
	st.write("---")
	st.write("##")

# ---- Contact Form: formsubmit.co ----
	contact_form = """
	<form action="https://formsubmit.co/jayeshnathjha@gmail.com" method="POST">
	     <input type="hidden" name="_captcha" value="false"
	     <input type="text" name="name" placeholder="Your Name" required>
	     <input type="email" name="email" placeholder="Your email" required>
	     <textarea name="message" placeholder="Your message here.." required></textarea>
	     <button type="submit">Send</button>
	</form>
	"""

	left_column, right_column = st.columns(2)
	with left_column:
		st.markdown(contact_form, unsafe_allow_html=True)
	with right_column:
		st_lottie(mail_anim, height=350, key='mail')

# Set the autorefresh interval
st_autorefresh(interval=14 * 60 * 1000, key='mail1')
