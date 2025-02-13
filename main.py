import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import team, batter, bowler,points_table,stats,about

st.set_page_config(
    page_title="IPL Analysis",
)
# adding markdown for music button
st.sidebar.markdown('*Groove- Theme song*', unsafe_allow_html=False)

# adding music button in the sidebar
button= st.sidebar.button('Music', key=None, help=None, on_click=None, args=None, kwargs=None, disabled=False)

# if click on music button is clicked show audio controls for playback
if button:
     st.sidebar.audio(r'IPL-theme-RMX.wav', format="audio/wav", start_time=0)


# Sidebar theme image
image = Image.open(r'1.png')
st.sidebar.image(image, caption='Indian Premire League')


class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:
            app = option_menu(
                menu_title='IPL Analysis ',
                options=['Points Table','Team Analysis','Batting Analysis','Bowling Analysis','Stats','About'],
                # icons=['trophy-fill', 'house-fill', 'person-circle', 'chat-fill', 'info-circle-fill'],
                menu_icon='cricket',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "15px"},
                    "nav-link": {"color": "white", "font-size": "15px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "#02ab21"},
                    "nav-link-selected": {"background-color": "Blue"}, }
            )

        if app == 'Team Analysis':
            team.app()
        if app == 'Batting Analysis':
            batter.app()
        if app == 'Bowling Analysis':
            bowler.app()
        if app == 'Points Table':
            points_table.app()
        if app == 'Stats':
            stats.app()
        if app == 'About':
            about.app()

    run()