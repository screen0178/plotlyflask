"""Plotly Dash HTML layout override."""

html_layout_original = '''
<!DOCTYPE html>
    <html>
        <head>
            {%metas%}
            <title>{%title%}</title>
            {%favicon%}
            {%css%}
        </head>
        <body class="dash-template">
            <header>
              <div class="nav-wrapper">
                <a href="/">
                    <img src="/static/img/logo.png" class="logo" />
                    <h1>Plotly Dash Flask Tutorial</h1>
                  </a>
                <nav>
                </nav>
            </div>
            </header>
            {%app_entry%}
            <footer>
                {%config%}
                {%scripts%}
                {%renderer%}
            </footer>
        </body>
    </html>
'''
html_layout = '''
<!DOCTYPE html>
    <html>
        <head>
            {%metas%}
            <title>{%title%}</title>
            {%favicon%}
            {%css%}
            <style>
                /* The side navigation menu */
                .sidebar {
                margin: 0;
                padding: 0;
                width: 200px;
                background-color: #fff;
                position: fixed;
                height: 100%;
                overflow: auto;
                }

                /* Sidebar links */
                .sidebar a {
                display: block;
                color: black;
                padding: 16px;
                text-decoration: none;
                }

                /* Active/current link */
                .sidebar a.active {
                background-color: #3F51B5;
                color: white;
                }

                /* Links on mouse-over */
                .sidebar a:hover:not(.active) {
                background-color: #2196F3;
                color: white;
                }

                /* Page content. The value of the margin-left property should match the value of the sidebar's width property */
                div.content {
                margin-left: 200px;
                padding: 1px 16px;
                height: 1000px;
                }

                /* On screens that are less than 700px wide, make the sidebar into a topbar */
                @media screen and (max-width: 700px) {
                    .sidebar {
                        width: 100%;
                        height: auto;
                        position: relative;
                    }
                    .sidebar a {float: left;}
                    div.content {margin-left: 0;}
                }

                /* On screens that are less than 400px, display the bar vertically, instead of horizontally */
                @media screen and (max-width: 400px) {
                    .sidebar a {
                        text-align: center;
                        float: none;
                    }
                }
            </style>
        </head>
        <body class="dash-template">
            <!-- <header>
              <div class="nav-wrapper">
                <a href="/">
                    <img src="/static/img/logo.png" class="logo" />
                    <h1>Plotly Dash Flask Tutorial</h1>
                </a> 
                <nav>
                </nav>
            </div> -->
            </header>
            <div class="sidebar">
                <a href="/likeDashboard/">Like Analysis</a>
                <a href="/commentDashboard/">Comment Analysis</a>
                <a href="/responseDashboard/">Response Analysis</a>
                <a href="/postDashboard/">Post Analysis</a>
            </div>
            <div class="content">
                {%app_entry%}
            </div>
            <footer>
                {%config%}
                {%scripts%}
                {%renderer%}
            </footer>
        </body>
    </html>
'''
