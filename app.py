import streamlit as st
from PIL import Image
from streamlit.components.v1 import html
import webbrowser
import base64
import requests

st.set_page_config(page_title = "Emir's Webpage", page_icon=":tada:", layout="wide")
st.subheader("Hi, I am Emir Tuna Korkmaz :wave:")
st.title("A Mechanical Engineer from Istanbul/Turkey")


#Use web CSS
def web_css(file_path):
    try:
        response = requests.get(f'https://raw.githubusercontent.com/emirtunaa/digital-resume/main/{file_path}')
        response.raise_for_status()  # Check for HTTP errors
        css_content = response.text
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching CSS file from GitHub: {e}")

# Usage
web_css("style/style.css")


#Use local CSS
def local_css(file_name):
    try:
        with open(file_name, 'r') as f:
            css_content = f.read()
            st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Error: CSS file not found at {file_name}")
    except Exception as e:
        st.error(f"Error reading CSS file: {e}")
        # Log additional information
        st.error(f"Additional information: {str(e)}")

# Usage
local_css("/Users/emirtuna/Desktop/apps/style/style.css")



#Images
l_bullet_image = Image.open("/Users/emirtuna/Desktop/apps/images/bullet1.jpeg")
l_resume_pic = Image.open("/Users/emirtuna/Desktop/apps/images/resume.png")

bullet_image = Image.open("images/bullet1.jpeg")
resume_pic = Image.open("images/resume.png")

# Header
#with open("/Users/emirtuna/Desktop/cv.pdf", "rb") as file:
 #   resume_data = base64.b64encode(file.read()).decode()
l_resume_path = "/Users/emirtuna/Desktop/cv.pdf"
resume_path = "cv.pdf"

with st.container():
    st.write("---")
    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(resume_pic)

    with text_column:
        st.subheader("About Me")
        st.success("I am a recent graduate with a bachelor's degree in mechanical engineering from Gebze Technical University with a strong passion for applying artificial intelligence and additive manufacturing to address engineering challenges. I have a keen interest in areas such as thermal analysis, explicit analysis, topology optimization, and the application of statistical tools to enhance engineering solutions. While I have a keen interest in these topics, I remain open to exploring innovative and research-based areas in the field.")
        
        st.subheader("My Github")   
        github_link = st.button("My Github Account", key='github')     
        st.write("It includes homeworks from my university classes and additional codes that I developed during my business life.")
        if github_link:
            webbrowser.open("https://github.com/emirtunaa")

        st.subheader("My Resume")        
        st.write("Download my resume for summarized 1 page pdf version of this website.")
        st.download_button(label="Download Resume",data='pdf', file_name=resume_path,mime="file/png")


st.write("<div id='detailed_description1'></div>", unsafe_allow_html=True)


with st.container():
    st.write("---")
    left_column, right_column = st.columns((2,2))
    with left_column:
        st.header("Work Experiences")
        
        
        with st.expander("Functional Safety Consultant"):
            st.write("**March 2023 - September 2023**") 
            st.write("""As a full-time Functional Safety Consultant, I took part in three distinct projects for TOGG,
                      consulting for ISO 26262 on the development of the gear shifter unit, camera module system, and electric tailgate.""")
            st.write("- Proficiency in ISO 26262, Automotive SPICE.") 
            st.write("""- Knowledge of:
    - Safety Plan
    - V Model
    - Item Definition
    - HARA
    - FuSa Requirements
    - Technical Safety Requirements
    - Safety Case""") 
            st.write("- Research in project management methodologies for applying to the development environment, including Six Sigma, Kanban, and Scrum.") 

            
        with st.expander("**Siemens - Strategic Procurement Working Student**"):
            st.write("**October 2022 - March 2023**")           
            st.write("As a part-time working student in the role of Strategic Procurement, I was actively involved in a variety of job responsibilities. They can be listed as:")
            st.write("- Involved in correcting invoice mistakes using SAP.")
            st.write("- Involved in control and tracking of contract agreements.")
            st.write("- Managed supplier evaluation procedure with collabration to all departments.")
            st.write("- Involved in alternative supplier sourcing for reducing TDC.")
            st.write("- Involved in quality management system (QMS) documents control and preperation for procurement department.")


        with st.expander("Real Estate Internship"):
            st.write("**July 2022 - August 2022**") 
            st.write("""As an intern, I played a role in a team of three interns tasked with the design and pre-development of a family house. 
                     My primary responsibility was focused on the selection, calculation, and pre-design of the mechanical systems, with a strong emphasis on achieving sustainable net-zero energy. 
                     This encompassed conducting detailed calculations for energy consumption, the heating and cooling systems of the house, and specifying essential components like batteries,
                      heat pumps, and solar panels. Additionally, I played a role in the pre-design of various house mechanical systems, including plumbing and equipment for the mechanical system room.""")
            st.write("- Took education on project management lifecycle.")
            st.write("- Involved in calculations and equipment choose for HVAC.")
            st.write("- Involved in providing net-zero energy for house.")
            st.write("- Calculating and minimizing total delivered cost (TDC).")
            # Add more information as needed
            
        with st.expander("Manufacturing Internship"):
            st.write("**August 2021 - September 2021**") 
            st.write("""As an intern, I had the opportunity to acquire knowledge of machining and casting manufacturing methods.
                      My responsibilities encompassed working in a calibration lab, where I gained hands-on experience with various measuring techniques,
                      measuring tools, and quality control procedures. I also contributed to the mechanical testing and analysis of manufactured parts.""")
            # Add more information as needed


# Placeholder buttons for detailed descriptions


# Project Header and Project 1
with st.container():
    st.write("---")
    st.header("Projects")
    st.write("##")

    image_column, text_column = st.columns((1, 2))
    
    with image_column:
        st.image(bullet_image)
    
    with text_column:
        st.subheader("Bullet Impact on Metal Plate")
        st.write("More info about bullet impact analysis.")
        
        detailed_link1 = st.button("For More Detail", key='project1')
    
    # Place the link next to the relevant project
        if detailed_link1:
            webbrowser.open("http://localhost:8501/apps/detailed_description1")

st.write("<div id='detailed_description1'></div>", unsafe_allow_html=True)


#Project2
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(bullet_image)
    with text_column:
        st.subheader("Another Project")
        st.write("More info about another project.")
        
        detailed_link2 = st.button("For More Detail", key='project2')
    
    # Place the link next to the relevant project
        if detailed_link2:
            webbrowser.open("http://localhost:8501/apps/detailed_description2")

st.write("<div id='detailed_description1'></div>", unsafe_allow_html=True)


with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = '''
    <form action="https://formsubmit.co/emir.tuna44@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Name" required>
     <input type="email" name="email" placeholder="Email" required>
     <textarea name="message" placeholder="A message to me" required></textarea>
     <button type="submit">Send</button>
    </form>
    '''

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()




