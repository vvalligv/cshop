document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('loginForm').addEventListener('submit', function(e) {
        e.preventDefault();
        let key = document.getElementById('key').value;
        let value = document.getElementById('value').value;

        if (key === "" || value === "") {
            alert("Please enter all the fields");
        } else {
            clearAllCookies();
            setCookie(key, value, 365);
            displayNewCookie(key, value);
            window.location.href = '/pay';
            
        }
    });
   
    clearAllCookies(); 
});

function setCookie(key, value, days) {
    let d = new Date();
    d.setTime(d.getTime() + (days * 24 * 60 * 60 * 1000));
    let expires = "expires=" + d.toUTCString();
    document.cookie = key + "=" + value + ";" + expires + ";path=/";
}

function getCookies() {
    let cookies = document.cookie.split(";");
    let res = "";
    for (let i = 0; i < cookies.length; i++) {
        res += (i + 1) + '-' + cookies[i].trim() + "<br>";
    }
    document.getElementById('result').innerHTML = res;
}

function clearAllCookies() {
    let cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i];
        let eqPos = cookie.indexOf("=");
        let name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
        document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/";
    }
}
function displayNewCookie(key, value) {
    let res = `1- ${key}=${value}<br>`;
    document.getElementById('result').innerHTML = res;
}