import streamlit as st
import requests
import datetime
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.colored_header import colored_header
from streamlit_extras.badges import badge

# Configuration
st.set_page_config(
    page_title="🌍 AI Travel Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for better styling
st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
        }
        .stTextInput > div > div > input {
            border-radius: 20px;
            padding: 10px 15px;
        }
        .stButton > button {
            width: 100%;
            border-radius: 20px;
            background: linear-gradient(90deg, #4F46E5 0%, #7C3AED 100%);
            color: white;
            font-weight: 600;
            border: none;
            padding: 0.75rem 1.5rem;
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
        }
        .chat-message {
            padding: 1.5rem;
            border-radius: 1rem;
            margin-bottom: 1rem;
            display: flex;
            max-width: 80%;
        }
        .user-message {
            background-color: #4F46E5;
            color: white;
            margin-left: auto;
            border-bottom-right-radius: 0.25rem;
        }
        .bot-message {
            background-color: #f1f5f9;
            color: #1e293b;
            margin-right: auto;
            border-bottom-left-radius: 0.25rem;
        }
        .trip-card {
            background: white;
            border-radius: 1rem;
            padding: 1.5rem;
            margin: 1rem 0;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            border: 1px solid #e2e8f0;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your AI travel assistant. Where would you like to go? 🗺️"}
    ]

# Sidebar with trip preferences
def show_sidebar():
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/000000/beach-umbrella.png", width=80)
        st.title("✈️ Travel Preferences")
        
        with st.form("preferences_form"):
            st.subheader("Trip Details")
            destination = st.text_input("Destination")
            start_date = st.date_input("Start Date", min_value=datetime.date.today())
            end_date = st.date_input("End Date", min_value=datetime.date.today())
            budget = st.selectbox("Budget Range", ["💰 Budget", "💰💰 Mid-range", "💰💰💰 Luxury"])
            travel_style = st.multiselect(
                "Travel Style",
                ["🏖️ Beach", "🏙️ City", "🏞️ Nature", "🎭 Culture", "🍜 Food"]
            )
            
            if st.form_submit_button("Update Preferences", type="primary"):
                st.session_state.preferences = {
                    "destination": destination,
                    "start_date": start_date,
                    "end_date": end_date,
                    "budget": budget,
                    "travel_style": travel_style
                }
                st.success("Preferences updated!")
        
        st.markdown("---")
        st.subheader("Quick Actions")
        if st.button("🌤️ Check Weather"):
            st.session_state.messages.append({"role": "user", "content": "Check weather for my trip"})
        if st.button("🏨 Find Hotels"):
            st.session_state.messages.append({"role": "user", "content": "Show hotel options"})
        if st.button("🍽️ Restaurant Suggestions"):
            st.session_state.messages.append({"role": "user", "content": "Suggest restaurants"})

# Main app
def main():
    st.title("🌍 AI Travel Planner")
    st.caption("Your personal travel assistant for creating perfect itineraries")
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Where would you like to go?"):
        # Add user message to chat
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").markdown(prompt)
        
        # Get AI response
        with st.spinner("Planning your perfect trip..."):
            try:
                response = requests.post(
                    "http://localhost:8000/query",
                    json={"question": prompt}
                )
                
                if response.status_code == 200:
                    answer = response.json().get("answer", "I couldn't generate a response. Please try again.")
                    
                    # Format the response with better styling and dark mode support
                    formatted_response = f"""
                    <div style="
                        background: var(--background-color);
                        color: var(--text-color);
                        padding: 1.5rem;
                        border-radius: 0.5rem;
                        margin: 1rem 0;
                        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                        border: 1px solid var(--border-color);
                    ">
                        <h3 style="color: var(--primary-color); margin-top: 0;">✨ Your Personalized Itinerary</h3>
                        <p style="color: var(--text-color); opacity: 0.8;">
                            Generated on {datetime.datetime.now().strftime("%B %d, %Y at %I:%M %p")}
                        </p>
                        <hr style="border-color: var(--border-color); margin: 1rem 0;">
                        <div style="color: var(--text-color);">
                            {answer}
                        </div>
                        <hr style="border-color: var(--border-color); margin: 1rem 0;">
                        <p style="font-size: 0.9em; color: var(--text-color); opacity: 0.7; margin-bottom: 0;">
                            <i>This travel plan was generated by AI. Please verify all information before your trip.</i>
                        </p>
                    </div>
                    """
                    
                    # Add CSS for dark/light mode support
                    st.markdown("""
                    <style>
                        :root {
                            --background-color: #ffffff;
                            --text-color: #1a1a1a;
                            --border-color: #e0e0e0;
                            --primary-color: #4F46E5;
                        }
                        @media (prefers-color-scheme: dark) {
                            :root {
                                --background-color: #262730;
                                --text-color: #f0f2f6;
                                --border-color: #444;
                                --primary-color: #7C3AED;
                            }
                        }
                    </style>
                    """, unsafe_allow_html=True)
                    
                    # Add assistant response to chat
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                    with st.chat_message("assistant"):
                        st.markdown(formatted_response, unsafe_allow_html=True)
                else:
                    error_msg = "I'm having trouble connecting to the travel assistant. Please try again later."
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})
                    st.chat_message("assistant").error(error_msg)
                    
            except Exception as e:
                error_msg = f"An error occurred: {str(e)}"
                st.session_state.messages.append({"role": "assistant", "content": error_msg})
                st.chat_message("assistant").error(error_msg)

# Run the app
if __name__ == "__main__":
    show_sidebar()
    main()