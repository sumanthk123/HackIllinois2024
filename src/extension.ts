// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {
	vscode.debug.onDidChangeActiveDebugSession((session) => {
		console.log("debug session changed");
	});
	async function networkSearch() {
		const rep = await fetch("https://dog.ceo/api/breeds/image/random")
		const response = await fetch("http://127.0.0.1:5000/test_with_pyshark");
		const text = await response.text();
		console.log(text);
	}
	
	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension "chatgdp" is now active!');

	// The command has been defined in the package.json file
	// Now provide the implementation of the command with registerCommand
	// The commandId parameter must match the command field in package.json
	let disposable = vscode.commands.registerCommand('chatgdp.helloWorld', () => {
		networkSearch();
		vscode.window.showInformationMessage('Hello World from ChatGDP!');
	});

	context.subscriptions.push(disposable);
}

// This method is called when your extension is deactivated
export function deactivate() {}
