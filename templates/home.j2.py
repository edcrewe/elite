<html>
                <head>
                <link rel="stylesheet" type="text/css" href="static/elite.css" />
                </head>
                <body>
                <h1>Elite</h1>
                <table>
                <tr><th>date</th><th>calories</th><th>distance</th><th>speed</th><th>heartrate</th></tr>
                {% for run in runs %}
                    <tr><td>{{ run.datetime }}</td><td>{{ run.calories }}</td><td>{{ run.distance }}</td><td>{{ run.speed }}</td><td>{{ run.heartrate }}</td></tr>
                    {% endfor %}
                    </table>
                </body>
            </html>
