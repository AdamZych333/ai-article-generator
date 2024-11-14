const articleContainer = document.body;

function loadArticle(path) {
	return fetch(path)
		.then((res) => res.text())
		.catch((err) => console.error(err));
}

function appendArticle(content) {
	articleContainer.innerHTML = content;
}

loadArticle("artykul.html").then(appendArticle);
