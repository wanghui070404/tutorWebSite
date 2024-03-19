document.addEventListener('DOMContentLoaded', function() {
    function OpenSideNav(){
        document.getElementById("Adminsidenav").style.width = "150px";
        document.getElementById("main").style.marginLeft = "175px";
        document.getElementById("topbar").style.marginLeft = "175px";
    }
    function CloseSideNav(){
        document.getElementById("Adminsidenav").style.width = "25px";
        document.getElementById("main").style.marginLeft = "50px";
        document.getElementById("topbar").style.marginLeft = "50px";
    }
    document.getElementById("switch").addEventListener('click', OpenSideNav);
    document.getElementById("collapse").addEventListener('click', CloseSideNav);
});
