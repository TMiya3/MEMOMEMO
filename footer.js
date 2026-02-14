document.addEventListener("DOMContentLoaded", () => {
	console.log(location.pathname)
 	// 現在のページのパスを取得
 	const depth = location.pathname.split("/").length - 2;

 	// 階層に応じて ../ を生成
 	const prefix = "../".repeat(depth);

	console.log(prefix)
	// footer.html を読み込む
	fetch("../footer.html")
		.then(res => res.text())
		.then(html => {
		document.getElementById("footer").innerHTML = html;
	});
});
