import mysql.connector
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

def render_about():
    st.title("ABOUT US")
    st.success("[Find out more at https://www.phonepe.com/](https://www.phonepe.com/)")


    st.write("""<font color=purple size=+6> As India’s largest payments platform we’re helping over 46 crore users and 2.5 crore merchants send, receive, and invest their money, conveniently and securely. India's #1️⃣ Trusted Digital Payments Brand in 2022 & 2023! 🥳🎉 """, unsafe_allow_html=True)
    st.success("Excellence in Insurtech : Excellence in Insurtech category at Assocham's Fintech & Digital Payments Awards 2021")
    st.success("Excellence in WealthTech : Third ET BFSI Innovation Tribe Virtual Summit & Awards (APAC edition)")
    st.success("Telecom & Technology : Best campaign under the Telecom & Technology category at the IndIAA Awards 2018")
    st.success("India Retail and e- Retail : PhonePe announced as a winner at 8th Annual India Retail and e- Retail Awards 2019")
    st.success("IAMAI Digital Award 2019 : IAMAI 9th India Digital Awards 2019")

def render_home():

    st.title('Welcome to the world of PhonePe on our :blue[Phonepe Streamlit Website!] :sunglasses:')
    st.markdown('<font color=PURPLE size=+7> Simple, Fast & Secure </font>', unsafe_allow_html=True)
    st.video("C:/Users/mrk30/MY DATA SCIENCE/PHONE PE/home-fast-secure-v3.mp4")
    st.image(Image.open("C:/Users/mrk30/MY DATA SCIENCE/PHONE PE/featured-image.png"),width = 500)

    st.title("One app for all things money.")
    st.success("Pay bills, recharge, send money, buy gold, invest and shop at your favourite stores.")
    st.title("Pay whenever you like, wherever you like.")
    st.success("Choose from options like UPI, the PhonePe wallet or your Debit and Credit Card.")
    st.title("Find all your favourite apps on PhonePe Switch.")
    st.success("Book flights, order food or buy groceries. Use all your favourite apps without downloading them.")
    
def render_basic_insights(cursor):
    st.markdown('<font color=PURPLE size=+7> The 10 Different facts </font>', unsafe_allow_html=True)

    options = {
        "Top 10 states based on year and amount of transaction":
            "SELECT DISTINCT States, Transaction_Year, SUM(Transaction_Amount) AS Total_Transaction_Amount FROM top_tran GROUP BY States, Transaction_Year ORDER BY Total_Transaction_Amount DESC LIMIT 10",

        "List 10 states based on type and amount of transaction":
                "SELECT DISTINCT States, SUM(Transaction_Count) AS Total FROM top_tran GROUP BY States ORDER BY Total ASC LIMIT 10",
    
            "Top 5 Transaction_Type based on Transaction_Amount":
                "SELECT DISTINCT Transaction_Type, SUM(Transaction_Amount) AS Amount FROM agg_user GROUP BY Transaction_Type ORDER BY Amount DESC LIMIT 5",
    
            "Top 10 Registered-users based on States and District":
                "SELECT DISTINCT State, District, SUM(RegisteredUsers) AS Users FROM top_user GROUP BY State, District ORDER BY Users DESC LIMIT 10",
    
            "Top 10 Districts based on states and Count of transaction":
                "SELECT DISTINCT States, District, SUM(Transaction_Count) AS Counts FROM map_tran GROUP BY States, District ORDER BY Counts DESC LIMIT 10",
    
            "List 10 Districts based on states and amount of transaction":
                "SELECT DISTINCT States, Transaction_year, SUM(Transaction_Amount) AS Amount FROM agg_trans GROUP BY States, Transaction_year ORDER BY Amount ASC LIMIT 10",
    
            "List 10 Transaction_Count based on Districts and states":
                "SELECT DISTINCT States, District, SUM(Transaction_Count) AS Counts FROM map_tran GROUP BY States, District ORDER BY Counts ASC LIMIT 10",
    
            "Top 10 RegisteredUsers based on states and District":
                "SELECT DISTINCT States, District, SUM(RegisteredUsers) AS Users FROM map_user GROUP BY States, District ORDER BY Users DESC LIMIT 10"
           

    }

    select= st.selectbox("Select the option", list(options.keys()))

    query= options[select]
    cursor.execute(query)
    df =pd.DataFrame(cursor.fetchall(), columns=cursor.column_names)

    fig =px.bar(df, x=df.columns[0], y=df.columns[-1])
    fig.update_xaxes(title_text="X-label")
    fig.update_yaxes(title_text="Y-label")

    st.write(df)
    st.title(select)
    st.plotly_chart(fig)

def render_contact():
    st.subheader("CONTACT INFO")
    st.markdown('<font color=green size=+7> We are here to help you!</font>', unsafe_allow_html=True)
    st.markdown('<font color=PURPLE size=+7>Customer Support</font>', unsafe_allow_html=True)
    st.success("To get instant help, tap  on your PhonePe app home screen & select the relevant topic.")
    st.markdown('<font color=PURPLE size=+7>Registered Address</font>', unsafe_allow_html=True)
    st.success("""PhonePe Private Limited
                (Formerly known as FX Mart Private Ltd. ),
                Unit No.001, Ground Floor, Boston House,
                Suren Road, Off. Andheri-Kurla Road,
                Andheri(East) Mumbai, Maharashtra, India, Pincode- 400093""")
    st.markdown('<font color=PURPLE size=+7>Mailing  Address</font>', unsafe_allow_html=True)
    st.success("""PhonePe Private Limited
                Office-2, Floor 4,5,6,7, Wing A, Block A,
                Salarpuria Softzone, Service Road,
                Green Glen Layout, Bellandur
                Bengaluru, Karnataka-KA, Pincode- 560103""")
    st.markdown('<font color=PURPLE size=+7>Social Media Links</font>', unsafe_allow_html=True)            
    st.write("[Phonepe Youtube Channel Link](https://www.youtube.com/@PhonePe_/videos)")
    st.write("[Phonepe Facebook Link](https://www.facebook.com/OfficialPhonePe)")
    st.write("[Phonepe twitter Link](https://twitter.com/PhonePe)")
    st.write("[Phonepe Instagram Link](https://www.instagram.com/phonepe/)")
    st.write("[Phonepe Linked in Link](https://www.linkedin.com/company/phonepe-internet/)")

def trust():
    st.video("C:/Users/mrk30/MY DATA SCIENCE/PHONE PE/safety-herobanner.mp4")
    st.image(Image.open("C:/Users/mrk30/MY DATA SCIENCE/PHONE PE/e1rhrsnf.png"),width = 400)
    st.write("That’s why we have an advanced security infrastructure to keep your transactions safe. We do what it takes to earn the trust that you and 25 crore Indians have placed in us.")
    st.image(Image.open("C:/Users/mrk30/MY DATA SCIENCE/PHONE PE/secure.png"),width = 70)
    st.markdown('<font color=PURPLE size=+7>Secure from the start</font>', unsafe_allow_html=True)
    st.write("Every transaction on PhonePe needs your fingerprint/face ID, UPI PIN and password for authentication.")

    st.image(Image.open("C:/Users/mrk30/MY DATA SCIENCE/PHONE PE/privecy.png"),width = 70)
    st.markdown('<font color=PURPLE size=+7>Payment Privacy</font>', unsafe_allow_html=True)
    st.write("Only you and the person you are transacting with will be able to see the details of your payment.")
    
    st.image(Image.open("C:/Users/mrk30/MY DATA SCIENCE/PHONE PE/risk.png"),width = 70)
    st.markdown('<font color=PURPLE size=+7>Risk assessment</font>', unsafe_allow_html=True)
    st.write("Our security teams monitor all transactions in real-time to block any suspicious activity. We also report fraud complaints & block fraudulent users from accessing the PhonePe platform")

    st.image(Image.open("C:/Users/mrk30/MY DATA SCIENCE/PHONE PE/protection.png"),width = 70)
    st.markdown('<font color=PURPLE size=+7>Partners in protection</font>', unsafe_allow_html=True)
    st.write("To aid safe transactions, we have partnered with cyber-crime cells of government law enforcement and security agencies, such as National Cybercrime Portal, CyCord and CyberSafe.")






def main():
    options =["HOME","DATA FACTS","TRUST & SAFETY","ABOUT","CONTACT"]
    default_index = 1  # Set the default index to Home

    st.image(Image.open("C:/Users/mrk30/MY DATA SCIENCE/PHONE PE/download_page-0001.JPG"),width = 400)

    st.markdown(
        """
        <style>
        .stSelectbox {
            color: blue;
            font-size: 20px;
            font-weight: bold;
            background-color: #F5F5F5;
            padding: 10px;
            width: 200px;
        }
        .stButton {
            background-color: #6F36AD;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    selected_option = st.sidebar.selectbox("Select a view", options, index=default_index)

    if selected_option=="ABOUT":
        render_about()
        st.snow()

        
        
    elif selected_option== "HOME":
        render_home()
        
    elif selected_option =="DATA FACTS":
        render_basic_insights(cursor)
    elif selected_option =="CONTACT":
        render_contact()
    elif selected_option=="TRUST & SAFETY":
        trust()

# Connect to the database
conn = mysql.connector.connect(user='root', password='12345', host='localhost', port=3306, database='neww')
cursor = conn.cursor()

if __name__ == "__main__":
    main()
