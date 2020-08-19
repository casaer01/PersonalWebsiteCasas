// OpenNav & CloseNav opens and closes the sidebar

function openNav() {
    document.getElementById("sidebutton").style.display = "none";
    document.getElementById("mySidenav").style.width = "250px";
    }

/* Set the width of the side navigation to 0 */
function closeNav() {
    document.getElementById("sidebutton").style.display = "inline-block";
    document.getElementById("mySidenav").style.width = "0";
    }