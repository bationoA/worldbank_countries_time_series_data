from src.functions import *

default_pages_config()

if __name__ == '__main__':
    st.write("""
    <h1 class='h1 text-center'>World-Bank Countries Time Series Data</h1>
    """, unsafe_allow_html=True)
    with st.sidebar:
        countries_df = get_international_country_codes_df()
        country_names, country_codes = countries_df['Country'].tolist(), countries_df['Iso3code'].tolist()
        # st.dataframe(countries_df)

        selected_country_name = st.selectbox('Select country', country_names)
        # Get the corresponding value based on the selected option
        selected_country_index = country_names.index(selected_country_name)
        selected_country_code = country_codes[selected_country_index]

        # Select an indicator
        wb_indicators_key_df = get_world_bank_indicators_codes_df()
        indicator_codes = wb_indicators_key_df['indicatorID'].tolist()
        indicator_names = wb_indicators_key_df['indicator'].tolist()
        indicators_descriptions = wb_indicators_key_df['indicatorDesc'].tolist()

        selected_indicator_name = st.selectbox('Select indicator', indicator_names, index=0)
        # Get the corresponding value based on the selected option
        selected_indicator_index = indicator_names.index(selected_indicator_name)
        selected_indicator_code = indicator_codes[selected_indicator_index]
        selected_indicator_description = indicators_descriptions[selected_indicator_index]

        st.write(f"""<ul class='list-group'>
                    <li class='list-group-item fs-4'><span>{selected_indicator_name}</span></li>
                    <li class='list-group-item fs-5'>Indicator code: <span>{selected_indicator_code}</span></li>
                    </ul>""", unsafe_allow_html=True)

    cols = st.columns([1, 1])

    # ------------------sample Size
    time_series_df = None
    if selected_country_name and selected_indicator_name:
        time_series_df = get_time_series(
            country_code=selected_country_code.strip(), indicator=selected_indicator_code.strip())

    with cols[0]:
        cols0 = st.columns([3, 1])
        cols0[0].write(f"""
        <ul class='list-group'>
        <li class='list-group-item fs-2'>Country: <span class='font-weight-bold'>{selected_country_name}</span></li> 
        </ul>""", unsafe_allow_html=True)

        if time_series_df is None:
            st.write("""
            No data was found
            """)
        else:
            cols0[1].download_button(label='📥 Download the table',
                                           data=to_excel(df=time_series_df),
                                           file_name=f"{selected_country_name}_{selected_indicator_name}.xlsx")
            numRows = time_series_df.shape[0]
            st.dataframe(data=time_series_df, height=(numRows + 1) * 35 + 3, width=700, hide_index=True)
        # st.write(""" <table class='table'>
        #                     <tr><th>Header 1</th><th>Header 2</th> <th>Header 3</th></tr>
        #                     <tr><td>cell</td> <td>cell</td> <td>cell</td></tr>
        #                     <tr><td>cell</td> <td>cell</td> <td>cell</td></tr>
        #                     <tr><td>cell</td> <td>cell</td> <td>cell</td></tr>
        #                     <tr><td>cell</td> <td>cell</td> <td>cell</td></tr>
        #                 </table>
        # """, unsafe_allow_html=True)
    # ------------------------------

    # ------------------ Survey / Data collection Guide
    with cols[1]:
        st.write("""<h3 class='title'>
        Description of the indicator
        </h3>
        """, unsafe_allow_html=True)
        st.write(f"""<div class='border border-info rounded m-3 p-3'>
        <span class='h2'>{selected_indicator_description}
        </span> 
        </div>
""", unsafe_allow_html=True)
