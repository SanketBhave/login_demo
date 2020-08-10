function validate(){
    var uname = document.getElementById("uname").value;
    var passwd = document.getElementById("passwd").value;

    if(uname == "sanket_bhave" && passwd == "gcp"){
        alert("Successful login");
        window.location.assign("F:/Demo/html/form.html");
        return false;
    }
    else{
        alert("Login failed")
        return true
        }
}
var data = "";
function signin() {
    var uname = document.getElementById("uname").value;
    var passwd = document.getElementById("passwd").value;

    if(uname === "" || passwd === ""){
        alert("Enter username/password");
    }
    
else{
    var cred = [uname, passwd]
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "http://127.0.0.1:8000/getdata/"+uname+"/"+passwd, true);
    xhttp.setRequestHeader('Content-Type', 'text/plain')
    xhttp.responseType = 'text';
    xhttp.onreadystatechange = function(){
        if(xhttp.readyState === xhttp.DONE && xhttp.status ===  200){
            data = JSON.parse(xhttp.responseText)
        if(Object.keys(data).length !== 0){
            localStorage.clear();
            localStorage.setItem("data", JSON.stringify(data))
            window.location.assign("F:/Demo/html/form.html");
        }
        else{
        localStorage.clear();
        localStorage.setItem("credentials", cred);
        window.location.assign("F:/Demo/html/form.html");
        }
    }
    else if ( xhttp.readyState === xhttp.DONE && xhttp.status ===  500){
        alert("Something went wrong. Check password.")
    }
}
    xhttp.send();
    return false;
}
}
