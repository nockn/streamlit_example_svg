import re
import base64

import streamlit as st


def read_svg(path_svg):
    """Get a SVG file as HTML

    Args:
        path_svg(str): Path of a SVG file
    Returns:
        svg_logo(str): HTML <svg> element
    """

    try:
        with open(path_svg, "r") as file:
            svg_logo = file.read().splitlines()
            _maped_list = map(str, svg_logo)
            svg_logo = "".join(_maped_list)
            temp_svg_logo = re.findall("<svg.*</svg>", svg_logo, flags=re.IGNORECASE)
            svg_logo = temp_svg_logo[0]
    except:  # None
        svg_logo = '<svg xmlns="http://www.w3.org/2000/svg" width="150px" height="1px" viewBox="0 0 150 1"></svg>'

    return svg_logo


def render_svg(svg):
    """Rendering SVG on Streamlit

    Args:
        svg(str): HTML <svg> element
    Returns: None
    """
    b64 = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
    html = (
        r"""
        <div align="center">
        <img src="data:image/svg+xml;base64,%s" alt="SVG Image" style="width: 50em;"/>
        </div>
        """
        % b64
    )
    st.markdown(html, unsafe_allow_html=True)


st.set_page_config(page_title="How to display SVG Image on Streamlit", layout="wide")

st.header("How to display SVG Image on Streamlit")
st.markdown("<br>", unsafe_allow_html=True)
render_svg(read_svg(r"src/undraw_Decide_re_ixfw.svg"))
license_text = r"""
    <div align="right">
        by <a href="https://undraw.co/" target="_blank">unDraw</a>
    </div>
    """
st.markdown(license_text, unsafe_allow_html=True)

code = '''
    import re
    import base64

    import streamlit as st

    SVG_FILE=r"src/undraw_Decide_re_ixfw.svg"

    def read_svg(path_svg):
        try:
            with open(path_svg, "r") as file:
                svg_logo = file.read().splitlines()
                _maped_list = map(str, svg_logo)
                svg_logo = "".join(_maped_list)
                temp_svg_logo = re.findall("<svg.*</svg>", svg_logo, flags=re.IGNORECASE)
                svg_logo = temp_svg_logo[0]
        except:  # None
            svg_logo = '<svg xmlns="http://www.w3.org/2000/svg" width="150px" height="1px" viewBox="0 0 150 1"></svg>'

        return svg_logo


    def render_svg(svg):
        b64 = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
        html = (
            r"""
            <div align="center">
            <img src="data:image/svg+xml;base64,%s" alt="SVG Image" style="width: 50em;"/>
            </div>
            """
            % b64
        )
        st.markdown(html, unsafe_allow_html=True)

    render_svg(read_svg(SVG_FILE))
    '''

st.code(code, language="python")
