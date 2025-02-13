"""
SPDX-License-Identifier: Apache-2.0
Copyright Contributors to the ODPi Egeria project.



This module provides a set of utility functions to render Mermaid markdown in a Jupyter notebook.

A running Egeria environment is needed to run these functions.
These functions have been tested in a Jupyter notebook - but may work in other environments.

"""
import html
import os
import time

import nest_asyncio

nest_asyncio.apply()
from IPython.display import HTML, display
from rich.console import Console

from pyegeria import (
    AutomatedCuration,
    InvalidParameterException,
    PropertyServerException,
    UserNotAuthorizedException,
)

EGERIA_METADATA_STORE = os.environ.get("EGERIA_METADATA_STORE", "active-metadata-store")
EGERIA_KAFKA_ENDPOINT = os.environ.get("KAFKA_ENDPOINT", "localhost:9092")
EGERIA_PLATFORM_URL = os.environ.get("EGERIA_PLATFORM_URL", "https://localhost:9443")
EGERIA_VIEW_SERVER = os.environ.get("EGERIA_VIEW_SERVER", "view-server")
EGERIA_VIEW_SERVER_URL = os.environ.get(
    "EGERIA_VIEW_SERVER_URL", "https://localhost:9443"
)
EGERIA_INTEGRATION_DAEMON = os.environ.get("INTEGRATION_DAEMON", "integration-daemon")
EGERIA_ADMIN_USER = os.environ.get("ADMIN_USER", "garygeeke")
EGERIA_ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "secret")
EGERIA_USER = os.environ.get("EGERIA_USER", "erinoverview")
EGERIA_USER_PASSWORD = os.environ.get("EGERIA_USER_PASSWORD", "secret")
EGERIA_JUPYTER = bool(os.environ.get("EGERIA_JUPYTER", "False"))
EGERIA_WIDTH = int(os.environ.get("EGERIA_WIDTH", "200"))
EGERIA_MERMAID_FOLDER = os.environ.get("EGERIA_MERMAID_FOLDER", "./work/mermaid_graphs")


def load_mermaid():
    """Inject Mermaid.js library"""
    # Alternative CDN URL via unpkg
    mermaid_js = """
    <script src="https://unpkg.com/mermaid@11.4.1/dist/mermaid.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            mermaid.initialize({startOnLoad: true});
        });
    </script>

    """

    display(HTML(mermaid_js))


# def render_mermaid(mermaid_code):
#     """Function to display a Mermaid diagram in a Jupyter notebook"""
#     mermaid_html = f"""
#     <div class="mermaid">
#         {mermaid_code}
#     </div>
#     <script type="text/javascript">
#         if (window.mermaid) {{
#     mermaid.initialize({{startOnLoad: true}});
#     mermaid.contentLoaded();
#     }}
#     </script>
#     """
#     display(HTML(mermaid_html))
def render_mermaid(mermaid_code):
    return display(HTML(construct_mermaid_html(mermaid_code)))


def parse_mermaid_code(mermaid_code):
    parts = mermaid_code.split("---", maxsplit=3)
    if len(parts) == 3:
        full_title = parts[1].strip()
        title_l = full_title.split("[")[0]
        title = title_l.replace("title: ", "")
        guid = full_title.split("[")[1].split("]")[0]
        guid = " " if guid is None else guid
        mermaid_code = parts[2].strip()
    else:
        title = "Unlabeled diagram"
        guid = " "
    return title, guid, mermaid_code


def old_construct_mermaid_html(mermaid_str: str) -> str:
    """Function to display a HTML code in a Jupyter notebook"""
    title_label, guid, mermaid_code = parse_mermaid_code(mermaid_str)

    html_section1 = """
    <!DOCTYPE html>
    <html>
        <head>
          <style type="text/css">
            #mySvgId {
            width: 100%;
            height: 600px;
            overflow: scroll;
            border: 2px solid #ccc;
            position: relative;
            margin-bottom: 10px;
            }
            svg {
            cursor: grab;
            }
    
          </style>
        </head>
    """
    html_section2 = f"""
        <title>{title_label}</title>
        <h3>{title_label}</h3>
        GUID : {guid}

    """
    html_section3 = """
        <body>
        
          <div id="graphDiv"></div>
          <script src="https://bumbu.me/svg-pan-zoom/dist/svg-pan-zoom.min.js"></script>
          <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
    
            mermaid.initialize({startOnLoad: false});
            await mermaid.run({
              querySelector: '.mermaid',
              postRenderCallback: (id) => {
                const container = document.getElementById("diagram-container");
                const svgElement = container.querySelector("svg");
    
                // Initialize Panzoom
                const panzoomInstance = Panzoom(svgElement, {
                  maxScale: 5,
                  minScale: 0.5,
                  step: 0.1,
                });
    
                // Add mouse wheel zoom
                container.addEventListener("wheel", (event) => {
                  panzoomInstance.zoomWithWheel(event);
                });
              }
            });
    
    
            const drawDiagram = async function () {
              const element = document.querySelector('#graphDiv');
             const graphDefinition = `
    """

    html_section4 = r"""`;
              const {svg} = await mermaid.render('mySvgId', graphDefinition);
              element.innerHTML = svg.replace(/( )*max-width:( 0-9\.)*px;/i, '');
    
              var doPan = false;
              var eventsHandler;
              var panZoom;
              var mousepos;
    
              eventsHandler = {
                haltEventListeners: ['mousedown', 'mousemove', 'mouseup']
    
                , mouseDownHandler: function (ev) {
                  if (event.target.className == "[object SVGAnimatedString]") {
                    doPan = true;
                    mousepos = {x: ev.clientX, y: ev.clientY}
                  }
                  ;
                }
    
                , mouseMoveHandler: function (ev) {
                  if (doPan) {
                    panZoom.panBy({x: ev.clientX - mousepos.x, y: ev.clientY - mousepos.y});
                    mousepos = {x: ev.clientX, y: ev.clientY};
                    window.getSelection().removeAllRanges();
                  }
                }
    
                , mouseUpHandler: function (ev) {
                  doPan = false;
                }
    
                , init: function (options) {
                  options.svgElement.addEventListener('mousedown', this.mouseDownHandler, false);
                  options.svgElement.addEventListener('mousemove', this.mouseMoveHandler, false);
                  options.svgElement.addEventListener('mouseup', this.mouseUpHandler, false);
                }
    
                , destroy: function (options) {
                  options.svgElement.removeEventListener('mousedown', this.mouseDownHandler, false);
                  options.svgElement.removeEventListener('mousemove', this.mouseMoveHandler, false);
                  options.svgElement.removeEventListener('mouseup', this.mouseUpHandler, false);
                }
              }
              panZoom = svgPanZoom('#mySvgId', {
                zoomEnabled: true
                , controlIconsEnabled: true
                , fit: 1
                , center: 1
                , customEventsHandler: eventsHandler
              })
            };
            await drawDiagram();
          </script>
        </body>    
    """

    return html_section1 + html_section2 + html_section3 + mermaid_code + html_section4


def construct_mermaid_html(mermaid_str: str) -> str:
    """Function to display a HTML code in a Jupyter notebook

    Constructs HTML for a single Mermaid graph with pan and zoom support.
    Each call overwrites the previous graph.

    :param mermaid_code: The Mermaid code for the graph.
    :param graph_id: An optional unique graph ID (default is 'mermaid-graph').
    :return: The HTML content for the Mermaid graph with pan and zoom enabled.

    """
    title_label, guid, mermaid_code = parse_mermaid_code(mermaid_str)

    graph_id = title_label.replace(" ", "_")
    escaped_header = html.escape(title_label) if title_label else ""  # Sanitize the header safely

    header_html = f"<h2 class='diagram-header'>{escaped_header}</h2>\nGUID: {guid}" if title_label else ""

    # Construct the HTML content with Mermaid.js initialization and zoom/pan support
    mermaid_html = f"""
   <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mermaid Diagram with Centered Pan and Zoom</title>
        <!-- Load Mermaid.js -->
        <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
            .diagram-container {{
                width: 90%;
                max-width: 800px;
                padding: 20px;
                border: 1px solid #ddd;
                border-radius: 12px;
                background-color: white;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                text-align: center;
                position: relative;
            }}
            .diagram-header {{
                margin-bottom: 20px;
                font-size: 1.8rem;
                font-weight: bold;
                color: #007acc;
            }}
            .pan-zoom-container {{
                position: relative;
                width: 100%;
                height: 500px;
                overflow: hidden;
                border: 1px solid #ccc;
                background-color: #f9f9f9;
                cursor: grab;
            }}
            .pan-zoom-content {{
                position: absolute;
                transform-origin: 0 0;
                cursor: grab;
            }}
            .pan-zoom-content:active {{
                cursor: grabbing;
            }}
        </style>
    </head>
    <body>
        <div class="diagram-container">
            {header_html}
            <div class="pan-zoom-container">
                <div id="{graph_id}" class="mermaid pan-zoom-content">
                    {mermaid_code}
                </div>
            </div>
        </div>

        <script>
            document.addEventListener("DOMContentLoaded", function() {{
                // Initialize Mermaid.js
                console.log("Initializing Mermaid...");
                mermaid.initialize({{ startOnLoad: true }});

                const container = document.querySelector('.pan-zoom-container');
                const content = document.querySelector('.pan-zoom-content');
                let rect;      // Bounding box of the rendered diagram
                let scale = 1; // Current zoom level
                let panX = 0;  // Pan offset in X direction
                let panY = 0;  // Pan offset in Y direction
                let isDragging = false;
                let startX, startY;

                // Helper: Apply transformations
                const applyTransform = () => {{
                    content.style.transform = `translate(${{panX}}px, ${{panY}}px) scale(${{scale}})`;
                }};

                // Helper: Center the diagram and fit it to the container
                const centerAndFitDiagram = () => {{
                    rect = content.getBoundingClientRect();
                    const containerRect = container.getBoundingClientRect();

                    // Calculate the required scale to fit the diagram
                    scale = Math.min(
                        containerRect.width / rect.width,
                        containerRect.height / rect.height
                    );

                    // Adjust pan to center the diagram
                    panX = (containerRect.width - rect.width * scale) / 2;
                    panY = (containerRect.height - rect.height * scale) / 2;

                    applyTransform();
                    console.log("Diagram centered and fitted to container.");
                }};

                // Add pan/zoom functionality
                const zoomCenteredOnDiagram = (event, deltaZoom) => {{
                    rect = content.getBoundingClientRect();
                    const containerRect = container.getBoundingClientRect();

                    // Center of the diagram
                    const diagramCenterX = rect.left + rect.width / 2;
                    const diagramCenterY = rect.top + rect.height / 2;

                    const zoomX = (diagramCenterX - containerRect.left) * deltaZoom;
                    const zoomY = (diagramCenterY - containerRect.top) * deltaZoom;

                    panX -= zoomX;
                    panY -= zoomY;
                }};

                container.addEventListener('wheel', function(event) {{
                    event.preventDefault();
                    const zoomSpeed = 0.1;
                    const previousScale = scale;

                    // Zoom in or out
                    if (event.deltaY < 0) {{
                        scale = Math.min(scale + zoomSpeed, 4); // Limit zoom-in
                    }} else {{
                        scale = Math.max(scale - zoomSpeed, 0.5); // Limit zoom-out
                    }}

                    // Calculate deltaZoom and adjust pan
                    const deltaZoom = scale / previousScale - 1;
                    zoomCenteredOnDiagram(event, deltaZoom);

                    applyTransform();
                }});

                container.addEventListener('mousedown', function(event) {{
                    isDragging = true;
                    startX = event.clientX - panX;
                    startY = event.clientY - panY;
                    container.style.cursor = "grabbing";
                }});

                container.addEventListener('mousemove', function(event) {{
                    if (!isDragging) return;

                    panX = event.clientX - startX;
                    panY = event.clientY - startY;

                    applyTransform();
                }});

                container.addEventListener('mouseup', function() {{
                    isDragging = false;
                    container.style.cursor = "grab";
                }});

                container.addEventListener('mouseleave', function() {{
                    isDragging = false;
                    container.style.cursor = "grab";
                }});

                // Ensure Mermaid renders the diagram, then fit and center it
                setTimeout(centerAndFitDiagram, 100); // Delay to ensure Mermaid.js rendering is complete
            }});
        </script>
    </body>
    </html>
"""



    return mermaid_html



def save_mermaid_html(
    title: str, mermaid_str: str, folder: str = EGERIA_MERMAID_FOLDER
):
    """Save a Mermaid diagram to a file"""
    if not os.path.exists(folder):
        os.makedirs(folder)
    mermaid_file = os.path.join(folder, title + ".html")

    payload = construct_mermaid_html(mermaid_str)

    with open(mermaid_file, "w") as f:
        f.write(payload)
    return mermaid_file


def save_mermaid_graph(title, mermaid_str, folder: str = EGERIA_MERMAID_FOLDER):
    """Save a Mermaid diagram to a file"""
    if not os.path.exists(folder):
        os.makedirs(folder)
    mermaid_file = os.path.join(folder, title + ".html")

    title, mermaid_code = parse_mermaid_code(mermaid_str)

    html_prefix = """
    <html>
        <head>
          <style type="text/css">
            #mySvgId {
            width: 100%;
            height: 100%;
            overflow: hidden;
            border: 1px solid #ccc;
            position: relative;
            margin-bottom: 10px;
            }
            svg {
            cursor: grab;
            }
        
          </style>
        </head>
        
        <body>
          <div id="graphDiv"></div>
          <script src="https://bumbu.me/svg-pan-zoom/dist/svg-pan-zoom.min.js"></script>
          <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
        
            mermaid.initialize({startOnLoad: false});
            await mermaid.run({
              querySelector: '.mermaid',
              postRenderCallback: (id) => {
                const container = document.getElementById("diagram-container");
                const svgElement = container.querySelector("svg");
        
                // Initialize Panzoom
                const panzoomInstance = Panzoom(svgElement, {
                  maxScale: 5,
                  minScale: 0.5,
                  step: 0.1,
                });
        
                // Add mouse wheel zoom
                container.addEventListener("wheel", (event) => {
                  panzoomInstance.zoomWithWheel(event);
                });
              }
            });
        
        
            const drawDiagram = async function () {
              const element = document.querySelector('#graphDiv');
              const graphDefinition = `
    """

    html_postfix = r"""`;
              const {svg} = await mermaid.render('mySvgId', graphDefinition);
              element.innerHTML = svg.replace(/( )*max-width:( 0-9\.)*px;/i, '');
        
              var doPan = false;
              var eventsHandler;
              var panZoom;
              var mousepos;
        
              eventsHandler = {
                haltEventListeners: ['mousedown', 'mousemove', 'mouseup']
        
                , mouseDownHandler: function (ev) {
                  if (event.target.className == "[object SVGAnimatedString]") {
                    doPan = true;
                    mousepos = {x: ev.clientX, y: ev.clientY}
                  }
                  ;
                }
        
                , mouseMoveHandler: function (ev) {
                  if (doPan) {
                    panZoom.panBy({x: ev.clientX - mousepos.x, y: ev.clientY - mousepos.y});
                    mousepos = {x: ev.clientX, y: ev.clientY};
                    window.getSelection().removeAllRanges();
                  }
                }
        
                , mouseUpHandler: function (ev) {
                  doPan = false;
                }
        
                , init: function (options) {
                  options.svgElement.addEventListener('mousedown', this.mouseDownHandler, false);
                  options.svgElement.addEventListener('mousemove', this.mouseMoveHandler, false);
                  options.svgElement.addEventListener('mouseup', this.mouseUpHandler, false);
                }
        
                , destroy: function (options) {
                  options.svgElement.removeEventListener('mousedown', this.mouseDownHandler, false);
                  options.svgElement.removeEventListener('mousemove', this.mouseMoveHandler, false);
                  options.svgElement.removeEventListener('mouseup', this.mouseUpHandler, false);
                }
              }
              panZoom = svgPanZoom('#mySvgId', {
                zoomEnabled: true
                , controlIconsEnabled: true
                , fit: 1
                , center: 1
                , customEventsHandler: eventsHandler
              })
            };
            await drawDiagram();
          </script>
        </body>    
    """

    payload = html_prefix + mermaid_code + html_postfix

    with open(mermaid_file, "w") as f:
        f.write(payload)
    return mermaid_file


def generate_process_graph(
    process_guid: str,
    view_server: str = EGERIA_VIEW_SERVER,
    url: str = EGERIA_VIEW_SERVER_URL,
    user_id: str = EGERIA_USER,
    user_pass: str = EGERIA_USER_PASSWORD,
) -> str:
    """Generate Mermaid Markdown text reflecting the Egeria process graph identified by the GUID

    Parameters
        ----------
        process_guid: str
            The identity of the progress to generate a graph of.

        Returns
        -------
        str

        A Mermaid markdown string

        Raises
        ------

        InvalidParameterException
          If the client passes incorrect parameters on the request - such as bad URLs or invalid values
        PropertyServerException
          Raised by the server when an issue arises in processing a valid request
        NotAuthorizedException
          The principle specified by the user_id does not have authorization for the requested action

    """
    console = Console()
    a_client = AutomatedCuration(view_server, url, user_id, user_pass)
    token = a_client.create_egeria_bearer_token()
    try:
        start_time = time.perf_counter()
        response = a_client.get_gov_action_process_graph(process_guid)
        duration = time.perf_counter() - start_time

        if type(response) is dict:
            process_steps: [dict]
            step_links: [dict] = []
            gov_process_qn = response["governanceActionProcess"]["processProperties"][
                "qualifiedName"
            ]
            gov_process_dn = response["governanceActionProcess"]["processProperties"][
                "displayName"
            ]

            md = f"\n---\ntitle: {gov_process_dn}\n---\nflowchart LR\n"
            header = '%%{init: {"flowchart": {"htmlLabels": false}} }%%\n'
            md += header
            element = response["firstProcessStep"]["element"]
            qname = element["processStepProperties"]["qualifiedName"]
            dname = element["processStepProperties"]["displayName"]
            domain_id = element["processStepProperties"]["domainIdentifier"]
            guid = element["elementHeader"]["guid"]
            wait = element["processStepProperties"]["waitTime"]
            ignore_mult_trig = element["processStepProperties"][
                "ignoreMultipleTriggers"
            ]
            link = response["firstProcessStep"]["linkGUID"]

            md = f'{md}\nStep1("`**{dname}**\n*nwait_time*: {wait}\n*nmult_trig*: {ignore_mult_trig}`")'
            process_steps = {
                qname: {
                    "step": "Step1",
                    "displayName": dname,
                    "guid": guid,
                    "domain": domain_id,
                    "ignoreMultTrig": ignore_mult_trig,
                    "waitTime": wait,
                    "link_guid": link,
                }
            }
            next_steps = response.get("nextProcessSteps", None)
            if next_steps is not None:
                i = 1
                for step in next_steps:
                    i += 1
                    qname = step["processStepProperties"]["qualifiedName"]
                    dname = step["processStepProperties"]["displayName"]
                    wait = step["processStepProperties"]["waitTime"]
                    step = f"Step{i}"
                    md = f'{md}\n{step}("`**{dname}**\n*wait_time*: {wait}\n*mult_trig*: {ignore_mult_trig}`")'
                    process_steps.update(
                        {
                            qname: {
                                "step": step,
                                "displayName": dname,
                                "guid": guid,
                                "domain": domain_id,
                                "ignoreMultTrig": ignore_mult_trig,
                                "waitTime": wait,
                            }
                        }
                    )  # process_steps.append({qname: {"step": step,"displayName": dname, "waitTime": wait}})
            # print(md)
            # Now process the links
            process_step_links = response.get("processStepLinks", None)
            if process_step_links is not None:
                for slink in process_step_links:
                    prev_step_name = slink["previousProcessStep"]["uniqueName"]
                    next_step_name = slink["nextProcessStep"]["uniqueName"]
                    next_step_link_guid = slink["nextProcessStepLinkGUID"]
                    guard = slink["guard"]
                    mandatory_guard = slink["mandatoryGuard"]
                    # print(f"\n\n Links: prev_step: {prev_step_name}\t next_step: {next_step_name}\t next_step_link:
                    # {next_step_link_guid}\t Guard: {guard}\t mandatory_guard: {mandatory_guard}")
                    step_links.append(
                        {
                            next_step_link_guid: {
                                "prev_step_name": prev_step_name,
                                "next_step_name": next_step_name,
                                "guard": guard,
                                "mandatory_guard": mandatory_guard,
                            }
                        }
                    )
                    step_p = process_steps[prev_step_name]["step"]
                    step_n = process_steps[next_step_name]["step"]
                    if mandatory_guard:
                        link = f"Mandatory:{guard}"
                    else:
                        link = guard
                    md = f"{md}\n{step_p}-->|{link}|{step_n}"
                i = 1

            return md

        elif type(response) is str:
            console.log("\n\n" + response)
        assert True

    except (
        InvalidParameterException,
        PropertyServerException,
        UserNotAuthorizedException,
    ) as e:
        console.print_exception(show_locals=True)
        assert False, "Invalid request"

    finally:
        a_client.close_session()
