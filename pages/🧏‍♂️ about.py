import streamlit as st

st.set_page_config(layout='wide',
                   initial_sidebar_state='expanded',
                   page_title='index',
                   page_icon=':bar_chart:')


st.write("""
    <link href='https://fonts.googleapis.com/css?family=Playfair+Display' rel='stylesheet'>
    
    <style>
        h4, h3, h2, h1, p, a, .bold{
            font-family: 'Playfair Display', serif;
        }
        h3, h2, a.link {
            color: #F75d5d;
        }
        h4 {
            margin-top: -30px;
            font-weight: 300; /* Lighter weight */
            font-style: italic; /* Italic style */
        }
    </style>
    
    <h2>Hello 👋</h2>
    <h3>I am Ahmad Muhammad</h3>
    <h4 class='sub-title'>DATA ANALYST AND PYTHON DEVELOPER</h4>
    <a class='link' href="https://mavenanalytics.io/profile/Ahmad-Muhammad/182882912">
        🔗PORTFOLIO
    </a><br>
    <a class='link' href="https://www.linkedin.com/in/ahmadmuhammadgd/">
        🔗LINKEDIN
    </a>
    <p>AHMADMUHAMMADGD@GMAIL.COM</p>
    
""", unsafe_allow_html=True)


st.divider()

st.write("""  
        <style>
        p {
            line-height: 1.5;
        }

        .bold {
            font-weight: bold;
        }

        div.bold {
            display: inline;
        }
        </style>
         
        <h3>Skills 🤹🏼</h3>
        <p>
        <div class = 'bold'>Q</div>uerying data using <div class = 'bold'>SQL</div>.</br>
        <div class = 'bold'>C</div>leaning and <div class = 'bold'>a</div>utomating using <div class = 'bold'>python</div>.</br>
        <div class = 'bold'>V</div>isualizing and <div class = 'bold'>c</div>ommunicating using <div class = 'bold'>Python, PowerBI, and Tableau</div>.</br> 
        <div class = 'bold'>C</div>ollaborating with teams using <div class = 'bold'>Git</div>.</br>
        <div class = 'bold'>B</div>logging and <div class = 'bold'>D</div>ocumenting  at <div class = 'bold'>Linkedin</div>.</br>
        </p>
""", unsafe_allow_html=True)

st.divider()

st.write("""
         <h4>
            Feel free to reach out to me
         </h4>
         """, unsafe_allow_html=True)
# The rest of your Streamlit app code
