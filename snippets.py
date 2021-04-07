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