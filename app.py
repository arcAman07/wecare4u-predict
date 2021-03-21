# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegressionCV
page_bg_img = '''
<style>
body {
background-image: url("https://www.google.com/url?sa=i&url=http%3A%2F%2Fwallpaperswide.com%2Fbeige_simple_background-wallpapers.html&psig=AOvVaw1OG-KtBHNd577BnmQECf_2&ust=1616371855992000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCPDfl82MwO8CFQAAAAAdAAAAABAE");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

pickle_in = open("P3.pkl","rb")
classifier=pickle.load(pickle_in)
pickle1_in = open("P4.pkl","rb")
classifier1=pickle.load(pickle1_in)

def predict_menstruation_cycle(ReproductiveCategory,LengthofLutealPhase,LengthofMenses,MensesScoreDayOne,MensesScoreDayTwo,MensesScoreDayThree,MensesScoreDayFour,MensesScoreDayFive,NumberofDaysofIntercourse,IntercourseInFertileWindow,UnusualBleeding):
    prediction=classifier.predict([[ReproductiveCategory,LengthofLutealPhase,LengthofMenses,MensesScoreDayOne,MensesScoreDayTwo,MensesScoreDayThree,MensesScoreDayFour,MensesScoreDayFive,NumberofDaysofIntercourse,IntercourseInFertileWindow,UnusualBleeding]])
    print(prediction)
    return prediction
def predict_menstruation_cycle1(ReproductiveCategory,LengthofLutealPhase,LengthofMenses,MensesScoreDayOne,MensesScoreDayTwo,MensesScoreDayThree,MensesScoreDayFour,MensesScoreDayFive,NumberofDaysofIntercourse,IntercourseInFertileWindow,UnusualBleeding,LengthofCycle):
    prediction1=classifier1.predict([[ReproductiveCategory,LengthofLutealPhase,LengthofMenses,MensesScoreDayOne,MensesScoreDayTwo,MensesScoreDayThree,MensesScoreDayFour,MensesScoreDayFive,NumberofDaysofIntercourse,IntercourseInFertileWindow,UnusualBleeding,LengthofCycle]])
    print(prediction1)
    return prediction1
def main():
    st.title("WeCare ML Web App")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Menstruation Cycle Predictor </h2>
    </div>
    """
    Email = st.text_input("Email")
    Date = st.text_input("Date(dd-mm-yy)")
    ReproductiveCategory = st.text_input("Reproductive Category(0 or 1 or 2 or 9)","")
    LengthofLutealPhase = st.text_input("Length of Luteal Phase")
    LengthofMenses = st.text_input("Length of Menses")
    MensesScoreDayOne = st.text_input("Menses Score Day One (1 or 2 or 3)","")
    MensesScoreDayTwo = st.text_input("Menses Score Day Two (1 or 2 or 3)","")
    MensesScoreDayThree = st.text_input("Menses Score Day Three (1 or 2 or 3)","")
    MensesScoreDayFour = st.text_input("Menses Score Day Four (1 or 2 or 3)","")
    MensesScoreDayFive = st.text_input("Menses Score Day Five (1 or 2 or 3)","")
    NumberofDaysofIntercourse = st.text_input("Number of Days of Intercourse :")
    IntercourseInFertileWindow = st.text_input("Intercourse In Fertile Window(0 or 1)","")
    UnusualBleeding = st.text_input("Unusual Bleeding(0 or 1)","")
    result=""
    result1=""
    if st.button("Predict"):
        result=predict_menstruation_cycle(ReproductiveCategory,LengthofLutealPhase,LengthofMenses,MensesScoreDayOne,MensesScoreDayTwo,MensesScoreDayThree,MensesScoreDayFour,MensesScoreDayFive,NumberofDaysofIntercourse,IntercourseInFertileWindow,UnusualBleeding)
        result1=predict_menstruation_cycle1(ReproductiveCategory,LengthofLutealPhase,LengthofMenses,MensesScoreDayOne,MensesScoreDayTwo,MensesScoreDayThree,MensesScoreDayFour,MensesScoreDayFive,NumberofDaysofIntercourse,IntercourseInFertileWindow,UnusualBleeding,result)
    
        st.success('The length of the cycle is {}'.format(result))
        st.success('The estimated day of evolution is {}'.format(result1))
        L=Date.split('-')
        days=L[0]
        months=L[1]
        years=L[2]
        from ics import Calendar, Event
        def output(day, month, year, ml_output):
            day31 = [1, 3, 5, 7, 8, 10, 12]
            day30 = [4, 6, 9, 10]
            def day31f(day, month, year, ml_output):
                day += ml_output
                if day > 31:
                    day -= 31
                    month += 1
                if month > 12:
                    month = 1
                    year += 1
                return day, month, year
            def day30f(day, month, year, ml_output):
                day += ml_output
                if day > 30:
                    day -= 30
                    month += 1
                    if month > 12:
                        month = 1
                        year += 1
                return day, month, year
            def feb(day, month, year, ml_output):
                day += ml_output
                if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
                    if day > 29:
                        day -= 29
                        month += 1
                    if month > 12:
                        month = 1
                        year += 1
                else:
                    if day > 28:
                        day -= 28
                        month += 1
                    if month > 12:
                        month = 1
                        year += 1
                return day, month, year
            if month in day31:
                day, month, year = day31f(day, month, year, ml_output)
            elif month in day30:
                day, month, year = day30f(day, month, year, ml_output)
            else:
                day, month, year = feb(day, month, year, ml_output)

            return day, month, year
        final_d,final_m,final_y = output(days,months,years,result)
        final_d,final_m = str(final_d) , str(final_m)
        if len(final_d)==1:
            final_d = "0" + final_d
        if len(final_m)==1:
            final_m = "0" + final_m
        final = str(final_y) + "-" +str(final_m) + "-" +str(final_d) + " 00:00:00"
        print(final)
        c = Calendar()
        e = Event()
        e.name = "Predicted First Day of period"
        e.begin = final
        c.events.add(e)
        c.events
        with open('my.ics', 'w') as my_file:
            my_file.writelines(c)
        st.success('The starting day of your periods is {}'.format(Date))
        st.success('The estimated day of evolution is {}'.format(day+"-"+month+"-"+year))
        import calendar
        
        

        
 
import webbrowser

url = 'https://tripetto.app/run/85ZPL31A7Z'

if st.button('Review Form:Help us Improve'):
    webbrowser.open_new_tab(url)
        
if __name__=='__main__':
    main()
    
    