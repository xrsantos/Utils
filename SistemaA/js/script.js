function CheckLogin() {
    var email = document.getElementById("user").value;
    var password = document.getElementById("password").value;
    if (email == "") {
        alert("Please enter your email");
        return false;
    }
    else if (password == "") {
        alert("Please enter your password");
        return false;
    }
    else {
        document.location = "./pages/home.html";
        return true;
    }
}