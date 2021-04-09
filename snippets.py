base_html = """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Fake Python</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.2/css/bulma.min.css">
  </head>
  <body>
  <section class="section">
    <div class="container mb-5">
      <h1 class="title is-1">
        Fake Python
      </h1>
      <p class="subtitle is-3">
        Fake Jobs for Your Web Scraping Journey
      </p>
    </div>
    <div class="container">
    <div id="ResultsContainer" class="columns is-multiline">
    {}
    </div>
    </div>
  </section>
  </body>
</html>
"""

job_html = """<div class="column is-half">
<div class="card">
  <div class="card-content">
    <div class="media">
      <div class="media-left">
        <figure class="image is-48x48">
          <img src="https://files.realpython.com/media/real-python-logo-thumbnail.7f0db70c2ed2.jpg?__no_cf_polish=1" alt="Real Python Logo">
        </figure>
      </div>
      <div class="media-content">
        <p class="title is-5">{0}</p>
        <p class="subtitle is-6 company">{1}</p>
      </div>
    </div>

    <div class="content">
      <p class="location">
        {2}
      </p>
      <p class="is-small has-text-grey">
        <time datetime="{3}">{3}</time>
      </p>
    </div>
    <footer class="card-footer">
        <a href="https://www.realpython.com" target="_blank" class="card-footer-item">Learn</a>
        <a href="{4}" target="_blank" class="card-footer-item">Apply</a>
    </footer>
  </div>
</div>
</div>
"""

job_detail_html = """<div class="box">
<h1 class="title is-2">{0}</h1>
<h2 class="subtitle is-4 company">{1}</h2>
<div class="content">
    <p>{4}</p>
    <p id="location"><strong>Location:</strong> {2}</p>
    <p id="date"><strong>Posted:</strong> {3}</p>
</div>
</div>
"""