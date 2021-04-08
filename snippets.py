base_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
    <link rel="stylesheet" href="style.css">
    <title>Fake Python Jobs</title>
</head>
<body>

<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Fake Python Jobs</a>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link" target="_blank" aria-current="page" href="https://www.realpython.com">Real Python</a>
          </li>
        </ul>
      </div>
    </div>
</nav>

<div id="ResultsContainer">
    {}
</div>
</body>
</html>"""

job_html = """<div class="card" style="width: 18rem;">
<div class="card-body">
<section class="card-content" data-jobid="4755ec59-d0db-4ce9-8385-b4df7c1e9f7c" onclick="MKImpressionTrackingMouseDownHijack(this, event)">
<div class="flex-row">
<div class="mux-company-logo thumbnail"></div>
<div class="summary">
<header class="card-header card-title">
<h2 class="title"><a data-bypass="true">{0}</a></h2>
</header>
<div class="card-body">
<div class="badge bg-light rounded-pill text-dark"><time datetime="{3}">{3}</time></div>
<div class="company">
<span class="name fs-3">{1}</span>
<ul class="list-inline">
</ul>
</div>
<div class="location">
<span class="name">
{2}
</span>
</div>
</div>
<div class="btn-group" role="group" aria-label="Basic example">
  <button type="button" class="btn btn-success btn-outline">Apply</button>
  <button type="button" class="btn btn-primary btn-outline">Save</button>
</div>
</div>
</div>
</section>
</div>
</div>
"""

page_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
    <link rel="stylesheet" href="style.css">
    <title>Fake Python Jobs</title>
</head>
<body>

<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Fake Python Jobs</a>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link" target="_blank" aria-current="page" href="https://www.realpython.com">Real Python</a>
          </li>
        </ul>
      </div>
    </div>
</nav>

<div class="container">
    {}
</div>
</body>
</html>
"""

bulma_html = """<!DOCTYPE html>
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

bulma_job = """<div class="column is-half">
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