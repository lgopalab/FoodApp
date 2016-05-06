class PageRetrievalTests:
	@staticmethod
	def run_all(app):
		pages = ["/", "/home", "/login", "/register", "/search"]
		for page in pages:
			assert app.test_client().get(page).status_code == 200