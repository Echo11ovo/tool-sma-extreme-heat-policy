from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc


def my_footer():
    return html.Footer(
        dmc.Container(
            dmc.Grid(
                [
                    dmc.Col(
                        dcc.Markdown(
                            """
                            [Click here to provide your feedback](https://sydney.au1.qualtrics.com/jfe/form/SV_3jAqlzAnAoAOU8S)
                            
                            Website authors: [Federico Tartarini](https://www.linkedin.com/in/federico-tartarini/), [Ollie Jay](https://au.linkedin.com/in/ollie-jay-793a1b11), and [James Smallcombe](https://twitter.com/smallcombe2?lang=en)
                            
                            © 2023 - Heat and Health Research Incubator, USyd
                            
                            Version: 0.0.3
                            
                            [Contact Us](mailto:federico.tartarini@sydney.edu.au)
                            """
                        ),
                        style={"color": "#eee", "inherit": "none"},
                        span=12,
                        md="auto",
                        className="markdown-footer",
                    ),
                    dmc.Col(
                        html.Img(
                            src="../assets/icons/usyd-logo.png",
                            width="125px",
                            height="43px",
                            alt="USYD logo icon",
                        ),
                        span="content",
                    ),
                ],
                justify="space-between",
            ),
            style={"flex": 1, "marginBottom": 20},
            className="p-2",
            size="xs",
        ),
        style={"background": "#215f93"},
        className="p-2",
    )
