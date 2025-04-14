
import stream as st 
import pandas as pd 
import os 
from io import BytesIo 

st.set_page_config(page_title== "Data Sweeper",layout='wide' )

#custom css 
st.markdown(
    """
     <style>
    .stApp{
        background-color: black; 
        color: white;
       }
       </style> 
       """, 
       unsafe-allow-html=True
)

#title and description 
st.title("Datasweeper sterling integrator By Saima Majid")
st.write("Transform your files between CSV and Excel formats with bilt-in data cleaning and visualization Creating the project for qarter 3!")
uploaded_files = st.file_uploader("upload your files  (accepts CSV Excel):", type=["CVS","xlsx"], accepts_mutltiple_files=(True))



if file in uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext == "CSV":
            df = pd.read_CSV(file)
        elif file_ext == "xlsx":
            df = pd.read_excel(file) 
        else:
            st.error(f"unsupported file type: {file_ext}") 
            continue 

        #file details
        st.write("preview the head of the Dataframe") 
        st.dataframe(df.head())

        #data cleaning options
        st.subheader("Data cleaning options") 
        if s.checkbox(f"clen data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove duplicates from the file : {file.name}"):
                    df.drop_dplicates(inplace=True) 
                    st.write("Duplicates removed!") 

            with col2:
                if st.button(f"Fill missing values for {file.name}"):
                    numeric_ = df.select_dtypes(includes=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())                        
                    st.write("missing valus have been filled!")

        st.subheader("select columns to keep") 
        columns = st.multiselect(f"choose columns for {file.name}", df.columns, defalt=df.columns)
        df = df[columns]  


        #data  vissualization
        st.subheader("Data vissualizationl")
        if st.checkbox (f"show vissualizationl for {flie.name}"): 
            st.bar_chart(df.select_dtypes(includes='number').iloc[:, :2]) 

        #conversion options    

        st.subheader("Conversion options")
        Conversion_type = st.radio(f"Convert {file.name} to:" , ["CVS , "Excel], key=file.name)
        if st.button(f"conversion{file.name}"):
            buffer = BytesI0()
            if Conversion_type =="CSV":
                df.to.CSV(buffer, index=false)
                file_name =file_name.replace(file_ext, "CSV")
                mime_type = "text/CSV"

            elif Conversion_type == "Excel":
                df. to.to_Excel(buffer, index=False)
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)


            st.download_button(
                label=f"Download {file_name} as {Conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )

 st.success(" All files processed successfully!")           



