document.addEventListener("DOMContentLoaded", function () {
    console.log("Django To-Do App JavaScript loaded!");

    const taskItems = document.querySelectorAll(".task-item");

    taskItems.forEach(function (item) {
        item.addEventListener("mouseenter", function () {
            item.style.transform = "translateX(5px)";
        });

        item.addEventListener("mouseleave", function () {
            item.style.transform = "translateX(0)";
        });
    });
});