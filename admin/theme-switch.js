document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("theme_switch").addEventListener('click', theme_switch);
    document.getElementById("theme_reset").addEventListener('click', theme_reset);
    function theme_switch(){
            document.body.style.backgroundColor="rgb(100, 100, 100)";
            document.body.style.color="rgb(0, 180, 255)";
            document.getElementById("Adminsidenav").style.backgroundColor="rgb(100, 100, 100)";
            document.getElementById("Adminsidenav").style.backgroundColor="rgb(0, 180, 255)";
            document.getElementById("activetab").style.backgroundColor="rgb(100, 100, 100)";
            document.getElementById("activetab").style.color="rgb(0, 180, 255)";
            document.getElementById("topbar").style.backgroundColor="rgb(100, 100, 100)";
            document.getElementById("topbar").style.color="rgb(0, 180, 255)";
            document.getElementById("switch").style.color="rgb(0, 180, 255)";
            document.getElementById("jump-to-ads").style.backgroundColor="rgb(0, 180, 255)";
            document.getElementById("pfp").style.color="rgb(0, 180, 255)";
            document.getElementById("dropdownlist").style.color="rgb(0, 180, 255)";


    }
    function theme_reset(){
        document.body.style.backgroundColor="rgb(210, 210, 210)";
        document.body.style.color="blueviolet";
        document.getElementById("Adminsidenav").style.backgroundColor="rgb(210, 210, 210)";
        document.getElementById("Adminsidenav").style.backgroundColor="blueviolet";
        document.getElementById("activetab").style.backgroundColor="rgb(210, 210, 210)";
        document.getElementById("activetab").style.color="blueviolet";
        document.getElementById("topbar").style.backgroundColor="white";    
        document.getElementById("topbar").style.color="blueviolet";
        document.getElementById("switch").style.color="blueviolet";
        document.getElementById("jump-to-ads").style.backgroundColor="blueviolet";
        document.getElementById("pfp").style.color="blueviolet";
        document.getElementById("dropdownlist").style.color="blueviolet";
    }

});