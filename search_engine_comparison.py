"""
(very) simple job website lister (in one page)
v0.1 - basic version
"""

from string import Template
import yaml

import streamlit as st
import streamlit.components.v1 as components

DEF_SEARCH_TERMS = "data"
IFRAME_X, IFRAME_Y = 1200, 500


def main():
    """main"""
    # pylint: disable=C0201,C0206
    st.set_page_config(layout="wide", page_title="obar1 1P Job lister")
    st.title("Search Engine Comparison")
    st.header("Enter your search query:")
    input_txt = st.text_input("search term:", DEF_SEARCH_TERMS)

    search_engines: dict = get_engines()
    if st.button("Submit"):
        st.subheader(f"Search Results for '{input_txt}'")
        for k in search_engines.keys():
            get_container(
                input_txt, search_engines[k]["id"], search_engines[k]["template"]
            )


def get_engines() -> dict:
    """
    get the ingfo on engines to use
    use `$input_text` where to inject the search term

    Returns:
        dict: id and template are mandatory
    """
    with open("engines.yaml", "r") as file:
        engines = yaml.safe_load(file)

    for engine in engines.values():
        engine["template"] = Template(engine["template"])

    return engines


def get_container(input_text: str, jl_id: str, template: Template):
    """get container rendered html

    Args:
        input_text (str): the search term
        jl_id (str): some job lister id
        template (Template): a template to hold the metadata
    """
    src = template.safe_substitute(input_text=input_text)

    with st.container():
        col1, col2 = st.columns(
            [0.3, 0.7], gap="small", vertical_alignment="top", border=False
        )
        with col1:
            st.write(jl_id)
            st.link_button(label=src, url=src)
        with col2:
            components.iframe(
                src,
                width=IFRAME_X,
                height=IFRAME_Y,
                scrolling=True,
            )
        st.divider()


if __name__ == "__main__":
    main()
