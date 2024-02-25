// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {
	vscode.debug.onDidChangeActiveDebugSession((session) => {
		console.log("debug session changed");
	});
	const anotherDisposable = vscode.commands.registerCommand('yourExtension.showSidebar', async function () {
        const panel = vscode.window.createWebviewPanel(
            'ChatGDP', 
            'Your Sidebar Title', 
            vscode.ViewColumn.Two, 
            {}
        );

        panel.webview.html = await getWebviewContent(); // Your HTML content
    });

    context.subscriptions.push(anotherDisposable);
	// async function networkSearch() {
	// 	const rep = await fetch("https://dog.ceo/api/breeds/image/random")
	// 	const response = await fetch("http://127.0.0.1:5000/test_with_pyshark");
	// 	const text = await response.text();
	// 	console.log(text);
	// }
	
	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension "chatgdp" is now active!');

	// The command has been defined in the package.json file
	// Now provide the implementation of the command with registerCommand
	// The commandId parameter must match the command field in package.json
	let disposable = vscode.commands.registerCommand('chatgdp.helloWorld', () => {
		//networkSearch();
		vscode.window.showInformationMessage('Hello World from ChatGDP!');
	});
	
	context.subscriptions.push(disposable);
}
let data;
async function sqlSearch() {
	const response = await fetch("http://127.0.0.1:5000/incrementPricing");
	data = await response.text();
	//console.log(data);
	return data;
}

async function getWebviewContent() {
	console.log('hii');
	let text = await sqlSearch();
	let data = JSON.parse(text);
	console.log(data[0]);
	//let text = "model 1";
    return `<!DOCTYPE html>
	<html lang="en">
	<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Product Listings</title>
	<style>
	  body {
		font-family: 'Itim', sans-serif;
		max-width: 480px;
		margin: auto;
		background-color: #1b1b1d;
		color: #fff;
		padding: 36px 24px;
	  }
	  .title {
		color: #00a67e;
		text-align: center;
		font-size: 32px;
		font-family: "Dosis", sans-serif;
  		font-optical-sizing: auto;
  		font-weight: 700;
  		font-style: normal;
	  }
	  .product-card {
		text-align: center;
		font-size: 20px;
		font-family: "Dosis", sans-serif;
  		font-optical-sizing: auto;
  		font-weight: 400;
  		font-style: normal;
		background-color: rgba(0, 166, 126, 1);
		border-radius: 10px;
		box-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
		padding: 17px;
		margin-top: 20px;
	  }
	  .product-name {
		margin-top: 16px;
		background-color: #1e1e1e;
		padding: 20px;
		border-radius: 16px;
	  }
	  .product-name, .product-price, .product-type {
		margin-top: 16px;
		background-color: #1e1e1e;
		padding: 20px;
		border-radius: 16px;
	  }
	  .visually-hidden {
		position: absolute;
		width: 1px;
		height: 1px;
		margin: -1px;
		border: 0;
		padding: 0;
		white-space: nowrap;
		clip-path: inset(50%);
		clip: rect(0 0 0 0);
		overflow: hidden;
	  }
	</style>
	</head>
	<body>
	<header class="title">ChatGDP</header>
	<section class="product-card">
	  <div class="product-name"><span>${data[0][0]}</span></div>
	  <div class="product-price"><span>$${data[0][2]}</span></div>
	  <div class="product-type"><span>${data[0][1]}</span></div>
	</section>
	<section class="product-card">
	  <div class="product-name"><span>${data[1][0]}</span></div>
	  <div class="product-price"><span>$${data[1][2]}</span></div>
	  <div class="product-type"><span>${data[1][1]}</span></div>
	</section>
	<section class="product-card">
	  <div class="product-name"><span>${data[2][0]}</span></div>
	  <div class="product-price"><span>$${data[2][2]}</span></div>
	  <div class="product-type"><span>${data[2][1]}</span></div>
	</section>
	<section class="product-card">
	  <div class="product-name"><span>${data[3][0]}</span></div>
	  <div class="product-price"><span>$${data[3][2]}</span></div>
	  <div class="product-type"><span>${data[3][1]}</span></div>
	</section>
	</body>
	</html>`;
}

// This method is called when your extension is deactivated
export function deactivate() {}
