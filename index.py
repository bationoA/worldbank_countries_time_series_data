from src.functions import *
default_pages_config()


if __name__ == '__main__':
    st.title("World-Bank Countries Time Series Data")
    with st.sidebar:
        population_size = st.number_input(label=f"Population size", min_value=0, value=30)
        level_of_confidence = st.slider(label=f"Level of confidence (%)", min_value=0, value=80,
                                        max_value=100)
        level_of_severity_of_an_error = st.slider(label=f"Level of severity of an error (%)",
                                                  value=50, max_value=100, min_value=0)

    # # Sample list of items
    # items = ['Apple', 'Banana', 'Orange', 'Mango', 'Pineapple']
    #
    # # Create a text input field for keywords
    # keywords = st.text_input('Enter keywords')
    #
    # # Filter the items based on the keywords
    # filtered_items = [item for item in items if all(keyword.lower() in item.lower() for keyword in keywords.split())]
    #
    # # Create a multiselect widget to select items
    # selected_items = st.multiselect('Select Items', items=filtered_items)
    #
    # # Display the selected items
    # st.write('Selected Items:', selected_items)

    countries_df = get_international_country_codes()
    country_names, country_codes = countries_df['Country'].tolist(), countries_df['Iso3code'].tolist()
    # st.dataframe(countries_df)

    selected_country = st.selectbox('Select country', country_names, index=0)
    # Get the corresponding value based on the selected option
    selected_country_index = country_names.index(selected_country)
    selected_country_code = country_codes[selected_country_index]

    st.write(f"selected_country_code: {selected_country_code}")

    cols = st.columns([1, 1, 1])

    # ------------------sample Size
    with cols[0]:
        st.header(f"Sample Size'")
        st.write(""" <table class='table'>
                            <tr><th>Header 1</th><th>Header 2</th> <th>Header 3</th></tr>
                            <tr><td>cell</td> <td>cell</td> <td>cell</td></tr>
                            <tr><td>cell</td> <td>cell</td> <td>cell</td></tr>
                            <tr><td>cell</td> <td>cell</td> <td>cell</td></tr>
                            <tr><td>cell</td> <td>cell</td> <td>cell</td></tr>
                        </table>
        """, unsafe_allow_html=True)

        st.subheader("To Do list")
    # ------------------------------

    # ------------------ Survey / Data collection Guide
    # with cols[1]:
    cols[1].header("Survey / Data collection Guide")
    is_business_objective_clearly_defined = cols[1].selectbox(
        label="Have you clearly defined the business objective?", options=["choose...", "Yes", "No"]
    )

    if is_business_objective_clearly_defined == "No":
        cols[1].write("""
            <span class='alert alert-primary' role='alert'>Clearly defining the objective should before sampling</span>
        """, unsafe_allow_html=True)
    elif is_business_objective_clearly_defined == "Yes":
        is_data_readily_available = cols[1].selectbox(
            label="Is data to support business objective readily available?", options=["choose...", "Yes", "No"]
        )

    is_data_well_aligned_with_objectives = cols[1].selectbox(
        label="His data well aligned with objectives?", options=["choose...", "Yes", "No"]
    )
    with cols[2]:
        # Create a text input field for keywords
        st.write(""" Keywords should be separated with commas (,)""", unsafe_allow_html=True)
        keywords = st.text_input('Enter keywords')
        st.write(f"""<span >You can gain powerful insights and make accurate conclusions when data is well-aligned to 
        business objectives. As a data analyst, alignment is something you will need to judge. Good alignment means 
        that the data is relevant and can help you solve a business problem or determine a course of action to 
        achieve a given business objective.</span> """, unsafe_allow_html=True)
