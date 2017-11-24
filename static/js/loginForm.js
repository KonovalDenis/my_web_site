try {	var logButton = document.getElementById("loginButton");
	logButton.addEventListener("click", showLogin);
	var RegButton = document.getElementById("registerButton");
	RegButton.addEventListener("click", showRegister);
	var closeForm = document.getElementById("closeForm");
	closeForm.addEventListener("click", closeAuth);
	document.getElementById("changeForm").addEventListener("click", changeForm)
} catch (err) {};

	function showLogin(){
		debugger;
		document.getElementById("wrapForm").style.display = "block";
		document.getElementById("menuIco").style.display = "none";
		document.getElementById("mainMenu").style.display = "none";
		document.getElementById("registerForm").style.display = "none";
		document.getElementById("loginForm").style.display = "block";
		document.getElementById("changeForm").innerHTML = "Нет аккаунта? РЕГИСТРАЦИЯ";
	}
	function showRegister(){
		debugger;
		document.getElementById("wrapForm").style.display = "block";
		document.getElementById("menuIco").style.display = "none";
		document.getElementById("mainMenu").style.display = "none";
		document.getElementById("registerForm").style.display = "block";
		document.getElementById("loginForm").style.display = "none";
		document.getElementById("changeForm").innerHTML = "Уже есть аккаунт? ВХОД";
	}
	function closeAuth() {
		document.getElementById("wrapForm").style.display = "none";
		document.getElementById("menuIco").style.display = "block";
		document.getElementById("menuIco").innerHTML = "MENU";
	}
	function changeForm() {
		if (this.innerHTML == "Нет аккаунта? РЕГИСТРАЦИЯ") {
			this.innerHTML = "Уже есть аккаунт? ВХОД";
			document.getElementById("registerForm").style.display = "block";
			document.getElementById("loginForm").style.display = "none";
		} else {
			this.innerHTML = "Нет аккаунта? РЕГИСТРАЦИЯ"
			document.getElementById("registerForm").style.display = "none";
			document.getElementById("loginForm").style.display = "block";
		}
	}


	menuButton = document.getElementById("menuIco");
	menuButton.addEventListener("click", showMenu);

	function showMenu() {
		if (menuButton.innerHTML == "MENU") {
			menuButton.innerHTML = "CLOSE";
			document.getElementById("mainMenu").style.display = "flex";
		} else {
			menuButton.innerHTML = "MENU";
			document.getElementById("mainMenu").style.display = "none";
		}
	}