function CheckLogin() {
    var email = document.getElementById("user").value;
    var password = document.getElementById("password").value;
    if (email === "") {
        alert("Please enter your email");
        return false;
    }
    else if (password === "") {
        alert("Please enter your password");
        return false;
    }
    else {
        acess_login(email, password)
    }
}


async function acess_login (email, password) {
        
    let options = {
        method: 'post',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        },
        body: 'grant_type=&username=' + email + '&password=' + password + '&scope=&client_id=&client_secret='
    };

    let ret = await fetch(`http://127.0.0.1:8000/token`, options);


    if (ret.status === 200)
    {
        let data = await ret.json();
        localStorage.setItem("token", data);
        document.location = "./pages/home.html";
    }
    else
    {
        alert("Invalid email or password");
    }
}