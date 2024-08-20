function toggleSidebar() {
    var sidebar = document.getElementById("sidebar");
    var mainContent = document.querySelector(".main-content");

    if (sidebar.classList.contains("active")) {
        sidebar.classList.remove("active");
        mainContent.classList.remove("shifted");
    } else {
        sidebar.classList.add("active");
        mainContent.classList.add("shifted");
    }
}

