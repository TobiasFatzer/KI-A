<script>
	import Router from "svelte-spa-router";
	import routes from "./routes";
</script>

<!-- This part is always displayed -->

<div class= "navigation container">
	<nav class="navbar nav-fill w-100 navbar-expand-lg navbar-light bg-light">
		<a class="navbar-brand" href="#/">
			<!-- <img
			  src="https://i.postimg.cc/wj3cS2Py/logo.png"
			  alt="Logo"
			  height="50"
			/> -->
			Pontonier Competition Management Tool</a
		  >
		  <button
			class="navbar-toggler"
			type="button"
			data-bs-toggle="collapse"
			data-bs-target="#navbarNav"
			aria-controls="navbarNav"
			aria-expanded="false"
			aria-label="Toggle navigation"
		  >	
			<span class="navbar-toggler-icon" />
		  </button>
		<div class="container-fluid">
			<div class="collapse navbar-collapse" id="navbarNavDropdown">
				<ul class="navbar-nav">
					<li class="nav-item">
						<a class="nav-link" href="#/">Home</a>
					</li>				
					<li class="nav-item">
						<a class="nav-link" href="#/ponti">Ponti Image Classification</a>
					</li>			
					<li class="nav-item">
						<a class="nav-link" href="#/webcam">Scan</a>
					</li>		
				</ul>
			</div>
		</div>
	</nav>

</div>

<div class="container mt-3">
	<!-- Here we load the page depending on the current URL -->
	<Router {routes} />
</div>