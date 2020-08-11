function changeImage(event){
document.getElementById("photo").src=URL.createObjectURL(event.target.files[0]);
}

function validateform(){
    var name = document.getElementById("name").value;
    if((!/[a-zA-Z]+/.test(name)) || name == ""){
        alert("Invalid name");
        return false;
    }
    var email_id = document.getElementById("email_id").value;
    if (email_id === ""){
        alert("Email ID cannot be empty");
        return false;
    }
    var number = document.getElementById("number").value;
    if((!/[0-9]+/.test(number)) || number === ""){
        alert("Invalid contact number");
        return false;
    }

    var age = document.getElementById("age").value;
    if((!/[0-9]+/.test(age)) || !(10 <= age <= 100) || age === ""){
        alert("Enter correct age value");
        return false;
    }
    var img = document.getElementById("photo").src;
    if(img === "file:///F:/Demo/html/profile_photo.jpg"){
        alert("Please select profile picture");
        return false;
    }
    commit()
}

function commit() {
    var name = document.getElementById("name").value;
    var email_id = document.getElementById("email_id").value;
    var number = document.getElementById("number").value;
    var age = document.getElementById("age").value;
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "http://127.0.0.1:8000/submit", true);
    xhttp.setRequestHeader('Content-Type', 'text/plain')
    xhttp.onreadystatechange = function(){
        response = JSON.parse(xhttp.responseText)
        if(xhttp.status === 200 && xhttp.readyState === xhttp.DONE){
            alert("Data stored successfully")
        }
        else{
            alert("Data storage failed")
        }

    }
    var cred = localStorage.getItem("credentials").split(',')
    var img = document.getElementById("photo");
    var canvas = document.createElement('CANVAS');
    canvas.height = img.height;
    canvas.width = img.width;
    var ctx = canvas.getContext('2d');
    ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
    var base64 = canvas.toDataURL();
    var data = JSON.stringify({"name": name, "email_id": email_id, "age": age, "number": number, "photo": base64, "uname": cred[0], "passwd": cred[1]});
    xhttp.send(data);
    return true;
}
function logout(){
    window.location.assign("F:/Demo/html/Login.html");
    return false;
}

function load(){
    if(localStorage.getItem("data") !== null){
        data  = JSON.parse(localStorage.getItem("data"));
        document.getElementById("name").value = data['Name'];
            document.getElementById("email_id").value = data['Email'];
            document.getElementById("number").value = data['Contact number'];
            document.getElementById("age").value = data['Age'];
            var img  = new Image();
            img.src = "data:image/png;base64,"+data['photo'];
            document.getElementById("photo").src = "data:image/png;base64,"+data['photo'];
    }
    return false;
}