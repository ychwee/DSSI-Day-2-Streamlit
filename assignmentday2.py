import streamlit as st
# other libs
import numpy as np
import pandas as pd
import pickle

with open('logr.pkl', "rb") as f:
	model = pickle.load(f)


# Streamlit provides a caching mechanism that allows your app to stay performant 
# even when loading data from the web, manipulating large datasets, 
# or performing expensive computations. This is done with the @st.cache decorator.
@st.cache()

def prediction(X):
	# Making predictions
	prediction = model.predict([[X]])
	if prediction == 0:
		pred = 'Non cancerous'
	else:
		pred = 'Cancerous'
	return pred

# putting the app related codes in main()
def main():
	# -- Set page config
	apptitle = 'DSSI CH Assignment'
	st.set_page_config(page_title=apptitle, page_icon='random', 
		layout= 'wide', initial_sidebar_state="expanded")
	# random icons in the browser tab

	# give a title to your app
	st.title('DSSI CH Assignment')
	#front end elements of the web page 
	# pick colors from: https://www.w3schools.com/tags/ref_colornames.asp
	html_temp = """ <div style ="background-color:AntiqueWhite;padding:15px"> 
       <h1 style ="color:black;text-align:center;">A Cancerous Cell Assessment</h1> 
       </div> <br/>"""

    #display the front end aspect
	st.markdown(html_temp, unsafe_allow_html = True)
	# let us make infrastructure to provide inputs
	# we will add the inputs to side bar
	st.sidebar.info('Provide input using the panel')
	st.info('Click Assess button below')
	
	X = st.sidebar.number_input('Insert cancer cell length between 0 to 10cm')
	st.write('The current number is ', X)  
	
	result =""
	# assessment button
	if st.button("Predict"):
		assessment = prediction(X)
		st.success('**System assessment says:** {}'.format(assessment))

	# if st.button("Reset"):
	# 	pyautogui.hotkey("ctrl","F5")

	# st.balloons()
	st.success("App is working!!") # other tags include st.error, st.warning, st.help etc.

if __name__ == '__main__':
	main()
