# %%writefile app.py
import pickle

import streamlit as st

# Load trained model
pickle_in = open("classifier.pkl", 'rb')
classifier = pickle.load(pickle_in)


@st.cache()
def prediction(loan_amnt, int_rate, annual_inc, dti, fico_range_low, pub_rec, revol_bal,
               revol_util, total_acc, mths_since_rcnt_il, mort_acc,
               mths_since_recent_bc, mths_since_recent_inq):
    prediction = classifier.predict([[loan_amnt, int_rate, annual_inc, dti, fico_range_low, pub_rec, revol_bal,
                                      revol_util, total_acc, mths_since_rcnt_il, mort_acc,
                                      mths_since_recent_bc, mths_since_recent_inq]])
    if prediction == 1:
        pred = "Fully Paid"
    else:
        pred = "Charged Off"
    return pred


# Main function:
def main():
    # Front end Elements:
    html_temp = """
    <div style ="padding:13px">
    <h1 style ="background:rgb(0,0,128,0.5);color:white;text-align:center;border-style:solid;border-radius:25px">Optimizing Bank's Financial Risk By Forecasting Future NPAs Using Machine Learning</h1>
    </div>
    """
    p = """<br>"""
    la = """
    <p style="color:white";text-align:left> Loan Amount </p>
    """
    ir = """
        <p style="color:white";text-align:left> Interest Rate </p>
        """
    ai = """
        <p style="color:white";text-align:left> Annual Income </p>
        """
    dti = """
        <p style="color:white";text-align:left> Debt To Income Ratio </p>
        """
    fico = """
        <p style="color:white";text-align:left> FICO Range(Low) </p>
        """
    dpr = """
        <p style="color:white";text-align:left> Number of derogatory public records </p>
        """
    crb = """
        <p style="color:white";text-align:left> Total Credit Revolving Balance </p>
        """
    rlur = """
        <p style="color:white";text-align:left> Revolving Line Utilization Rate </p>
        """
    tcl = """
        <p style="color:white";text-align:left> Total Number of Credit lines </p>
        """
    iao = """
        <p style="color:white";text-align:left> Months Since Most Recent Installment Accounts Opened </p>
        """
    ma = """
        <p style="color:white";text-align:left> Number of Mortgage Accounts </p>
        """
    bao = """
        <p style="color:white";text-align:left> Months Since Most Recent Bankcard Account Opened </p>
        """
    ri = """
        <p style="color:white";text-align:left> Months Since Most Recent Inquiry </p>
        """
    st.markdown(
        """
            <style>
                .reportview-container{
                background:url("https://wallpapercave.com/wp/wp6602995.jpg");
                background-repeat:no-repeat;
                background-size: cover;
                font-color:'white';
                }
                .reportview-container .main{
                color:white;
                }
                div[data-baseweb='input]>div{
                **color:'white';**
                }
            </style>
            """
        , unsafe_allow_html=True)
    footer = """
                <style> 
                footer{
                    visibility:hidden;
                }
                footer:after{
                    content: 'Developed By:  Aditya Iyengar, Aditya Kamat, Chaitanya Shukla and Drumil Joshi';
                    visibility:visible;
                    background-color: rgba(127, 150, 255, 0.5);
                    text-align: center;
                    bottom:0;
                    margin:auto;
                    display:block;
                    font-size:17px;
                    color:white;
                    padding:5px;
                    top:2px;
                    border-style:solid;
                    border-radius:25px;
                }
                </style>
                """
    st.markdown(footer, unsafe_allow_html=True)
    # Display aspect of front end
    st.markdown(html_temp, unsafe_allow_html=True)
    st.markdown(p, unsafe_allow_html=True)
    st.markdown(la, unsafe_allow_html=True)

    Loan_Amount = st.number_input("")
    st.markdown(p, unsafe_allow_html=True)
    st.markdown(ir, unsafe_allow_html=True)

    Interest_Rate = st.number_input(" ")
    st.markdown(p, unsafe_allow_html=True)
    st.markdown(ai, unsafe_allow_html=True)

    Annual_Income = st.number_input("  ")
    st.markdown(p, unsafe_allow_html=True)
    st.markdown(dti, unsafe_allow_html=True)

    Debt_To_Income_Ratio = st.number_input("   ")
    st.markdown(p, unsafe_allow_html=True)
    st.markdown(fico, unsafe_allow_html=True)

    fico_range_low = st.number_input("    ")
    st.markdown(p, unsafe_allow_html=True)
    st.markdown(dpr, unsafe_allow_html=True)

    Number_of_Derogatory_Public_Records = st.number_input("     ")
    st.markdown(p, unsafe_allow_html=True)
    st.markdown(crb, unsafe_allow_html=True)

    Total_credit_revolving_balance = st.number_input("      ")
    st.markdown(p, unsafe_allow_html=True)
    st.markdown(rlur, unsafe_allow_html=True)

    Revolving_line_utilization_rate = st.number_input("       ")
    st.markdown(p, unsafe_allow_html=True)
    st.markdown(tcl, unsafe_allow_html=True)

    total_number_of_credit_lines = st.number_input("        ")
    st.markdown(p, unsafe_allow_html=True)
    st.markdown(ri, unsafe_allow_html=True)

    Months_since_most_recent_installment_accounts_opened = st.number_input("         ")
    st.markdown(p, unsafe_allow_html=True)
    st.markdown(ma, unsafe_allow_html=True)

    Number_of_mortgage_accounts = st.number_input("          ")
    st.markdown(p, unsafe_allow_html=True)
    st.markdown(bao, unsafe_allow_html=True)

    Months_since_most_recent_bankcard_account_opened = st.number_input("           ")
    st.markdown(p, unsafe_allow_html=True)
    st.markdown(ri, unsafe_allow_html=True)

    Months_since_most_recent_inquiry = st.number_input("            ")
    result = ""

    # When Predict is clicked:
    st.markdown(""" <style>
    div.stButton > button:first-child {
    color:red;
    }
    </style>
    """,
                unsafe_allow_html=True)
    if st.button("Predict"):
        result = prediction(Loan_Amount, Interest_Rate, Annual_Income, Debt_To_Income_Ratio, fico_range_low,
                            Number_of_Derogatory_Public_Records, Total_credit_revolving_balance,
                            Revolving_line_utilization_rate,
                            total_number_of_credit_lines, Months_since_most_recent_installment_accounts_opened,
                            Number_of_mortgage_accounts, Months_since_most_recent_bankcard_account_opened,
                            Months_since_most_recent_inquiry)
        st.success(f"Your Loan is {result}")
        print(Loan_Amount)


if __name__ == '__main__':
    main()
