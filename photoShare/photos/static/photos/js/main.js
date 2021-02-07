function closeNav() {

    document.getElementById('sideNav').style.width = "0";
    document.getElementById('toggle_btn').style.display = "block";
    document.getElementById("main").style.marginLeft = "0";
    document.body.style.backgroundColor = "white";

}

function openNav() {

    document.getElementById('sideNav').style.width = "250px";
    document.getElementById('toggle_btn').style.display = "none";
    document.getElementById("main").style.marginLeft = "250px";
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";



}
