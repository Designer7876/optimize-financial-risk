# %%writefile app.py
import bz2
import pickle
import _pickle as cPickle
import streamlit as st

# Load trained model
def decompress_pickle(file):
    data = bz2.BZ2File(file, 'rb')
    data = cPickle.load(data)
    return data
classifier = decompress_pickle('forest.pbz2') 

@st.cache()
def prediction(term,issue_d,inq_last_6mths,mort_acc,open_acc,earliest_cr_year,
               fico_range,annual_inc,revol_bal,revol_util, dti,int_rate,
               loan_amnt,last_pymnt_amnt):
    prediction = classifier.predict([[term,issue_d,inq_last_6mths,mort_acc,open_acc,
                                      earliest_cr_year,fico_range,annual_inc,revol_bal,
                                      revol_util, dti,int_rate,loan_amnt,last_pymnt_amnt]])
    if prediction == 0:
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
    term = """
        <p style="color:white";text-align:left> Loan Term </p>
        """
    is_d = """
        <p style="color:white";text-align:left> Issue Year </p>
        """
    inq = """
        <p style="color:white";text-align:left> Months since last inquiry </p>
        """
    mor_ac = """
        <p style="color:white";text-align:left> No of mortgage accounts </p>
        """
    op_ac = """
        <p style="color:white";text-align:left> Total number of currently open accounts. </p>
        """
    ear_cr = """
        <p style="color:white";text-align:left> Year of the earliest line of credit </p>
        """
    fico = """
        <p style="color:white";text-align:left> FICO Range(LOW) </p>
        """
    an_inc = """
        <p style="color:white";text-align:left> Annual Income </p>
        """
    crb = """
        <p style="color:white";text-align:left> Total Credit Revolving Balance </p>
        """
    rlur = """
        <p style="color:white";text-align:left> Revolving Line Utilization Rate </p>
        """
    dti = """
        <p style="color:white";text-align:left> Debt To Income Ratio </p>
        """
    intr = """
        <p style="color:white";text-align:left> Interest Rate </p>
        """
    loan = """
        <p style="color:white";text-align:left> Loan Amount </p>
        """
    lpm = """
        <p style="color:white";text-align:left> Last Payment Amount </p>
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
    st.markdown(term, unsafe_allow_html=True)

    term = st.number_input("")
    st.markdown(p, unsafe_allow_html=True)
    st.markdown(is_d, unsafe_allow_html=True)

    issue_d = st.number_input(" ")
    st.markdown(p, unsafe_allow_html=True)
    st.markdown(inq, unsafe_allow_html=True)

    inq_last_6mths = st.number_input("  ")
    st.markdown(p, unsafe_allow_html=True)
    st.markdown(mor_ac, unsafe_allow_html=True)

    mort_acc = st.number_input("   ")
    st.markdown(p, unsafe_allow_html=True)
    st.markdown(op_ac, unsafe_allow_html=True)

    open_acc = st.number_input("    ")
    st.markdown(p, unsafe_allow_html=True)
    st.markdown(ear_cr, unsafe_allow_html=True)

    earliest_cr_year = st.number_input("     ")
    st.markdown(p, unsafe_allow_html=True)
    st.markdown(fico, unsafe_allow_html=True)

    fico = st.number_input("      ")
    st.markdown(p, unsafe_allow_html=True)
    st.markdown(an_inc, unsafe_allow_html=True)

    annual_inc = st.number_input("       ")
    st.markdown(p, unsafe_allow_html=True)
    st.markdown(crb, unsafe_allow_html=True)

    revol_bal = st.number_input("        ")
    st.markdown(p, unsafe_allow_html=True)
    st.markdown(rlur, unsafe_allow_html=True)

    revol_util = st.number_input("         ")
    st.markdown(p, unsafe_allow_html=True)
    st.markdown(intr, unsafe_allow_html=True)

    int_rate = st.number_input("          ")
    st.markdown(p, unsafe_allow_html=True)
    st.markdown(loan, unsafe_allow_html=True)

    loan_amnt = st.number_input("           ")
    st.markdown(p, unsafe_allow_html=True)
    st.markdown(lpm, unsafe_allow_html=True)

    last_pymnt_amnt = st.number_input("            ")
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
        result = prediction(term,issue_d,inq_last_6mths,mort_acc,open_acc,earliest_cr_year,
                            fico_range,annual_inc,revol_bal,revol_util, dti,int_rate,loan_amnt,last_pymnt_amnt)
        st.success(f"Your Loan is {result}")
        print(loan_amnt)


if __name__ == '__main__':
    main()
